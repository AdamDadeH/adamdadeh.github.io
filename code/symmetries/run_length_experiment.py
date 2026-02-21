"""
Symmetries in ML — Experiment 1: Max Run Length
================================================
Compare four approaches to handling rotation symmetry:
  1. Raw features, no augmentation
  2. Raw features + data augmentation (all N rotations)
  3. Autocorrelation features (rotation-invariant, degree-2) + any model
  4. Circular CNN — equivariant to cyclic shifts by construction,
     invariant at output via global average pool

Key observation: approaches 3 and 4 both exploit symmetry, but differently.
Approach 3 bakes invariance into the featurization (upstream of the model).
Approach 4 bakes equivariance into the model architecture (the featurization
is the raw signal). Both achieve the same theoretical guarantee.
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_absolute_error
import xgboost as xgb
import torch
import torch.nn as nn
import torch.optim as optim

RNG = np.random.default_rng(42)
N = 16  # circular string length


# ---------------------------------------------------------------------------
# Data
# ---------------------------------------------------------------------------

def max_run_length(x):
    """Max run of consecutive 1s in a circular binary string."""
    x2 = np.concatenate([x, x])
    max_run = run = 0
    for b in x2:
        run = run + 1 if b == 1 else 0
        if run > max_run:
            max_run = run
        if max_run >= N:
            break
    return min(max_run, N)


def generate_data(n_samples):
    """Generate unique random binary strings and their max run lengths."""
    X = RNG.integers(0, 2, (n_samples, N))
    y = np.array([max_run_length(x) for x in X])
    return X.astype(float), y.astype(float)


def random_rotation(X):
    """Apply a random cyclic rotation to each row of X."""
    shifts = RNG.integers(0, N, len(X))
    return np.array([np.roll(x, s) for x, s in zip(X, shifts)])


# ---------------------------------------------------------------------------
# Features
# ---------------------------------------------------------------------------

def autocorrelation_features(X):
    """
    Rotation-invariant degree-2 features.
    R_x(tau) = sum_n x(n) * x(n - tau)
    Same for all rotations of x — no canonical form needed.
    """
    n = X.shape[1]
    return np.array([
        [np.dot(x, np.roll(x, tau)) for tau in range(n)]
        for x in X
    ])


def augment(X, y):
    """Augment dataset with all N rotations of each example."""
    X_aug = np.vstack([np.roll(X, s, axis=1) for s in range(N)])
    y_aug = np.tile(y, N)
    return X_aug, y_aug


# ---------------------------------------------------------------------------
# Circular CNN — equivariant to cyclic shifts by construction
# ---------------------------------------------------------------------------

class _CircularNet(nn.Module):
    """
    1D CNN with circular padding — equivariant to cyclic shifts.
    Global average pool collapses the sequence → invariant scalar output.

    Translation equivariance: conv with circular padding satisfies
        f(shift(x)) = shift(f(x))
    Global average pool: invariant to any permutation of the sequence,
    so in particular invariant to shifts.
    """
    def __init__(self, hidden=32, kernel_size=3, n_layers=3):
        super().__init__()
        pad = kernel_size // 2
        layers = []
        in_ch = 1
        for _ in range(n_layers):
            layers += [
                nn.Conv1d(in_ch, hidden, kernel_size,
                          padding=pad, padding_mode='circular'),
                nn.ReLU(),
            ]
            in_ch = hidden
        self.conv = nn.Sequential(*layers)
        self.head = nn.Linear(hidden, 1)

    def forward(self, x):
        h = self.conv(x.unsqueeze(1))   # (B, hidden, L) — equivariant
        h = h.mean(dim=-1)              # (B, hidden)    — invariant
        return self.head(h).squeeze(-1) # (B,)


class CircularCNNRegressor:
    """Sklearn-compatible wrapper for the circular CNN."""

    def __init__(self, hidden=32, kernel_size=3, n_layers=3,
                 n_epochs=100, lr=3e-3, batch_size=64):
        self.hidden = hidden
        self.kernel_size = kernel_size
        self.n_layers = n_layers
        self.n_epochs = n_epochs
        self.lr = lr
        self.batch_size = batch_size

    def fit(self, X, y):
        self._net = _CircularNet(self.hidden, self.kernel_size, self.n_layers)
        opt = optim.Adam(self._net.parameters(), lr=self.lr)
        loss_fn = nn.MSELoss()
        Xt = torch.tensor(X, dtype=torch.float32)
        yt = torch.tensor(y, dtype=torch.float32)
        n = len(Xt)
        self._net.train()
        for _ in range(self.n_epochs):
            idx = torch.randperm(n)
            for start in range(0, n, self.batch_size):
                b = idx[start:start + self.batch_size]
                opt.zero_grad()
                loss_fn(self._net(Xt[b]), yt[b]).backward()
                opt.step()
        return self

    def predict(self, X):
        self._net.eval()
        with torch.no_grad():
            return self._net(torch.tensor(X, dtype=torch.float32)).numpy()


# ---------------------------------------------------------------------------
# Models (non-CNN)
# ---------------------------------------------------------------------------


# ---------------------------------------------------------------------------
# Experiment
# ---------------------------------------------------------------------------

# Total training examples seen — augmentation uses N times more data per unique example,
# so we compare at equal data throughput. Aug models get n_total / N unique examples.
N_TOTAL_SIZES = [N, N*2, N*5, N*10, N*20, N*50, N*100, N*200]
N_TEST = 2000
N_REPEATS = 5

# Test set: unique examples each seen at a random rotation
X_test_base, y_test = generate_data(N_TEST)
X_test_raw = random_rotation(X_test_base)
X_test_autocorr = autocorrelation_features(X_test_raw)

results = {name: [] for name in [
    "Ridge (raw)", "Ridge (autocorr)", "XGBoost (raw)", "XGBoost (autocorr)",
    "Ridge (raw+aug)", "XGBoost (raw+aug)", "CNN (circular)",
]}

for n_total in N_TOTAL_SIZES:
    # Non-aug models see n_total unique examples
    n_unique = n_total
    # Aug models see n_total / N unique examples, augmented to n_total
    n_unique_aug = max(1, n_total // N)

    run_results = {name: [] for name in results}

    for _ in range(N_REPEATS):
        X_tr_base, y_tr = generate_data(n_unique)
        X_tr_raw = random_rotation(X_tr_base)
        X_tr_autocorr = autocorrelation_features(X_tr_raw)

        X_tr_aug_base, y_tr_aug_base = generate_data(n_unique_aug)
        X_tr_aug_raw_small = random_rotation(X_tr_aug_base)
        X_tr_aug_raw, y_tr_aug = augment(X_tr_aug_raw_small, y_tr_aug_base)

        configs = {
            "Ridge (raw)":        (Ridge(),      X_tr_raw,      y_tr,     X_test_raw),
            "Ridge (autocorr)":   (Ridge(),      X_tr_autocorr, y_tr,     X_test_autocorr),
            "XGBoost (raw)":      (xgb.XGBRegressor(n_estimators=100, max_depth=4, verbosity=0),
                                   X_tr_raw,      y_tr,     X_test_raw),
            "XGBoost (autocorr)": (xgb.XGBRegressor(n_estimators=100, max_depth=4, verbosity=0),
                                   X_tr_autocorr, y_tr,     X_test_autocorr),
            "Ridge (raw+aug)":    (Ridge(),      X_tr_aug_raw,  y_tr_aug, X_test_raw),
            "XGBoost (raw+aug)":  (xgb.XGBRegressor(n_estimators=100, max_depth=4, verbosity=0),
                                   X_tr_aug_raw,  y_tr_aug, X_test_raw),
            # Equivariant architecture: raw features, symmetry in the model
            "CNN (circular)":     (CircularCNNRegressor(), X_tr_raw, y_tr, X_test_raw),
        }

        for name, (model, X_tr, y_tr_, X_te) in configs.items():
            model.fit(X_tr, y_tr_)
            pred = model.predict(X_te)
            run_results[name].append(mean_absolute_error(y_test, pred))

    for name in results:
        results[name].append(np.mean(run_results[name]))

# ---------------------------------------------------------------------------
# Plot
# ---------------------------------------------------------------------------

fig, ax = plt.subplots(figsize=(9, 5))

styles = {
    "Ridge (raw)":        dict(color="steelblue",  ls="--",  marker="o"),
    "XGBoost (raw)":      dict(color="steelblue",  ls="-",   marker="o"),
    "Ridge (raw+aug)":    dict(color="darkorange", ls="--",  marker="s"),
    "XGBoost (raw+aug)":  dict(color="darkorange", ls="-",   marker="s"),
    "Ridge (autocorr)":   dict(color="seagreen",   ls="--",  marker="^"),
    "XGBoost (autocorr)": dict(color="seagreen",   ls="-",   marker="^"),
    "CNN (circular)":     dict(color="mediumpurple", ls="-", marker="D"),
}

for name, mae in results.items():
    ax.plot(N_TOTAL_SIZES, mae, label=name, **styles[name])

ax.set_xscale("log")
ax.set_xlabel(f"Total training examples seen (aug uses N={N} rotations per unique example)")
ax.set_ylabel("MAE (max run length)")
ax.set_title(f"Sample efficiency at equal data throughput (N={N})")
ax.legend(ncol=2, fontsize=9)
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig("run_length_experiment.png", dpi=150)
plt.show()

print(f"\nMAE by total examples seen (N={N}):")
print(f"{'Model':25s} " + " ".join(f"{n:>6d}" for n in N_TOTAL_SIZES))
for name, mae in results.items():
    print(f"  {name:25s} " + " ".join(f"{m:>6.3f}" for m in mae))
