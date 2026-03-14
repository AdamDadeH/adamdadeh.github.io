# Claude Session Log

Record of Claude Code sessions on this repo. Each session entry covers what was done, what's pending, and what was discussed but not yet acted on.

---

## Session 3 — 2026-02-21 / 2026-02-28

**Branch**: `post-cleanup-2026-3`
**Commits**: `a3ae84d`, `4d9c1b3`

### Completed

**Post reviews (published):**
- `statespace`, `circle`, `convolutions` — done in prior session (already committed)
- `binary_files` — description, tightened opening, 8092 → 8192 fix
- `bianchi` — description, all `\newline` → `\\`, double delimiters fixed, `\eqnarray` → `align`, `sgn` → `\operatorname{sgn}`, `lim` → `\lim`, `FLRW` typo, missing paren, `\cite{aew}` removed, `postiive` → `positive`
- `bash_args` — marked `draft: true` (incomplete reference notes, no conclusion)
- `jekyll-themes` — deleted

**Post reviews (published, done in earlier sessions):**
- `algorithm-asymptotics`, `quotient`, `coordinates`, `identity-binary`, `function-syntax`, `symmetries-in-ml-1`, `probability_notation`
- `date_parsing` — deleted

**Content additions:**
- `symmetries-in-ml-1`: added "Responses to the Coordinate Problem" section — five strategies (quotient, augmentation, invariant featurization, equivariant model, gauge fixing / Spatial Transformers). Gauge fixing note includes Gribov copies and the Spatial Transformer connection.

**New drafts created:**
- `drafts/2020-02-22-symmetries-in-ml-2/` — Part II of symmetries series. Fourier coordinates, degree hierarchy (degree-1 mean, degree-2 autocorrelation/power spectrum, degree-3 bispectrum), three approaches comparison, equivalence theorem, orbit averaging vs absolute value, two experiment stubs (max run length, English vs gibberish).
- `drafts/2026-02-20-algebraic-string-diagrams/` — stub on algebraic syntax for string diagrams (Catlab.jl, free SMC terms, π-calculus). Triggered by Einstein notation discussion in function-syntax post.
- `drafts/2026-02-21-extension-obstruction/` — extension obstructions from groups to Gödel. Boolean valuation (Gödel/Tarski), real valuation (measure/Vitali), forcing as Boolean-valued bridge, random forcing, Cox's theorem, sheaf/$H^1$ picture stub.
- `drafts/2026-02-21-constraints-exact-sequences/` — constrained dynamics and exact sequences. Constraints as kernels, generalized coordinates as parametrization of the kernel, kernel pair, non-holonomic extension to tangent bundle, DAG generalization, Dirac constraint formalism stub.

**Experiment code:**
- `code/symmetries/run_length_experiment.py` — compares rotation symmetry approaches at equal data throughput: Ridge/XGBoost (raw, autocorr, raw+aug), CircularCNN. CNN uses circular padding (`padding_mode='circular'`) + global average pool for invariance. Run was interrupted — results pending.

### Pending / Open

- **CNN experiment**: `run_length_experiment.py` has the circular CNN added but the run was interrupted. Run with `/tmp/symmetries-venv/bin/python run_length_experiment.py` from `code/symmetries/`.
- **English vs gibberish experiment**: second experiment planned for symmetries Part II. Label = any rotation is English (check all $k$ rotations against dictionary, no canonical form). Features: raw one-hot vs circular bigram counts.
- **Symmetries Part II draft**: needs the experiment results embedded, and the "real-valued quotient analysis" section (moved from Part I) still has a placeholder.
- **Extension obstruction post**: sheaf/$H^1$ section is a stub. The cohomological unification of Gödel + Vitali + forcing is the key claim — needs development.
- **Constraints post**: Lagrange multiplier dual picture and Dirac constraint formalism stubs need filling.
- **`bash_args`**: in draft — could become a finished post with a "When to use what" table and a conclusion.

### Key Decisions / Conventions Established

- Drafts live in top-level `drafts/` (tracked in git, excluded from Quarto rendering via `.quartoignore`)
- Equal data throughput framing for the symmetries experiment: aug models get `n_total / N` unique examples, augmented to `n_total`
- Label definitions must be genuinely rotation-invariant — no canonical form used to define labels
- Always use `/tmp/symmetries-venv/` for Python experiments

---

## Session 2 — 2026-02-20

**Branch**: `post-cleanup-2026-3` (earlier commits)
**Commits**: `9788e5b`, `b6d2baf`, `b91cc57`, `c0282f7`

### Completed

- `algorithm-asymptotics`: description, `\rm{}` → `\text{}`/`\operatorname{}`, `Theta` → `\Theta`, `limsup`/`liminf`/`inf`/`sup` consistent, HTML fragment → italic note
- `quotient`: new opening, `\newline` → `\\`, `$g ~ h` → `$g \sim h`, `${-1}` → `$(\cdot)^{-1}$`, closing with three equivalent characterizations of normal subgroups
- `coordinates`: fixed double delimiter, `\rm{prime}` → `\text{prime}`, new conclusion connecting coordinates to algorithmic complexity and ML
- `identity-binary`: fixed opening, `$concat$` → backtick, `\tilde{}` → `\sim`, closing sentence
- `function-syntax`: pipe notation added, Einstein notation added to multivariate section (corrected from univariate), criteria evaluations for all notations, "My Current Preference" moved to end
- `date_parsing`: deleted
- `statespace`, `circle`, `convolutions`: reviewed and updated (details in commit)

### Key Discussions

- Einstein notation is NOT univariate — named binding by index label, covariant/contravariant via index height, does not extend beyond multilinear maps naturally
- Algebraic syntax for string diagrams (Catlab.jl, free SMC terms) → stub draft created

---

## Session 1 — 2026-02-19 (approximate)

**Branch**: `claude-refactor` → merged/rebased to `post-cleanup-2026-3`
**Commits**: `031269d` (major restructure to quarto), earlier

### Completed

- Full Jekyll → Quarto migration: `_quarto.yml`, `index.qmd`, `about.qmd`, `publications.qmd`, `posts/_metadata.yml`, `.github/workflows/publish.yml`
- Migration script: all `_posts/*.md` → `posts/YYYY-MM-DD-slug/index.qmd`
- Frontmatter conversion: `layout`, `author`, `use_math` removed; `categories` normalized to YAML list; draft classification applied
- `probability_notation` rewritten
- Jekyll files cleaned up
- `.quartoignore` created

---
