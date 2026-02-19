#!/usr/bin/env python3
"""
Migrate Jekyll posts (_posts/, draft/) to Quarto posts/ directory.
Creates posts/YYYY-MM-DD-slug/index.qmd for each post.
"""

import re
import shutil
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).parent.parent
POSTS_DIR = ROOT / "posts"
JEKYLL_POSTS = ROOT / "_posts"
JEKYLL_DRAFTS = ROOT / "draft"

# Keys to remove from frontmatter
REMOVE_KEYS = {
    "layout", "author", "use_math", "share", "related", "comments",
    "read_time", "author_profile", "started", "published",
}

# Skip this file (space in name, duplicate draft)
SKIP_FILES = {"2020-03-03-identity-binary copy.md"}

# Draft posts by filename stem (from plan's draft classification)
DRAFT_STEMS = {
    "2016-01-01-confidence-intervals",
    "2019-12-02-manifold_stats",
    "2020-02-22-symmetries-in-ml-2",
    "2021-05-02-structures",
    "2021-05-10-symmetries-in-ml-4",
    "2021-05-22-symmetries-3",
    "2022-06-04-topology-as-category",
    "2024-04-26-iverson-notation",
    "2024-05-02-categories-and-programming",
}

# Map of slug → replacement for Liquid tags
LIQUID_REPLACEMENTS = {
    "2020-02-22-symmetries-in-ml-2": [
        (
            r"\{%\s*post_url\s+2020-02-22-symmetries-in-ml-1\s*%\}",
            "/posts/2020-02-22-symmetries-in-ml-1/",
        )
    ]
}


def parse_frontmatter(text):
    """Return (frontmatter_dict, body_str) from a file's text content."""
    if not text.startswith("---"):
        return {}, text
    # Find closing ---
    end = text.find("\n---", 3)
    if end == -1:
        return {}, text
    fm_text = text[3:end].strip()
    body = text[end + 4:].lstrip("\n")
    try:
        fm = yaml.safe_load(fm_text) or {}
    except yaml.YAMLError as e:
        print(f"  WARNING: YAML parse error: {e}", file=sys.stderr)
        fm = {}
    return fm, body


def normalize_list(val):
    """Turn a scalar or space-separated string into a list."""
    if val is None:
        return []
    if isinstance(val, list):
        return [str(v).strip() for v in val if v]
    # space-separated string like "Math Analysis"
    return [v.strip() for v in str(val).split() if v.strip()]


def build_new_frontmatter(fm, slug, is_draft_file):
    """Return a clean frontmatter dict for Quarto."""
    new_fm = {}

    # Title — clean [Draft] prefix
    title = str(fm.get("title", slug)).strip()
    if title.startswith("[Draft]"):
        title = title[len("[Draft]"):].strip()
    new_fm["title"] = title

    # Date
    # Try to extract from slug YYYY-MM-DD-...
    date_match = re.match(r"^(\d{4}-\d{2}-\d{2})", slug)
    if "date" in fm:
        new_fm["date"] = fm["date"]
    elif date_match:
        new_fm["date"] = date_match.group(1)

    # Categories — merge category + categories + tags (space-sep strings)
    cats = []
    for key in ("category", "categories"):
        cats.extend(normalize_list(fm.get(key)))
    cats.extend(normalize_list(fm.get("tags")))
    # Deduplicate preserving order
    seen = set()
    unique_cats = []
    for c in cats:
        if c not in seen:
            seen.add(c)
            unique_cats.append(c)
    if unique_cats:
        new_fm["categories"] = unique_cats

    # Description placeholder
    new_fm["description"] = ""

    # Draft status
    draft = (
        is_draft_file
        or slug in DRAFT_STEMS
        or "[Draft]" in str(fm.get("title", ""))
        or fm.get("published") is False
    )
    if draft:
        new_fm["draft"] = True

    return new_fm


def fm_to_yaml(fm):
    """Serialize frontmatter dict to YAML string."""
    return yaml.dump(fm, default_flow_style=False, allow_unicode=True, sort_keys=False)


def migrate_file(src_path, is_draft_file=False):
    name = src_path.name

    if name in SKIP_FILES:
        print(f"  SKIP: {name}")
        return

    text = src_path.read_text(encoding="utf-8")
    fm, body = parse_frontmatter(text)

    # Determine slug from filename
    stem = src_path.stem  # e.g. "2016-02-21-statespace"
    # For draft/coordinates-part2.md — no date prefix, use a placeholder date
    date_match = re.match(r"^(\d{4}-\d{2}-\d{2})-(.+)$", stem)
    if date_match:
        slug = stem
    else:
        slug = f"2021-07-12-{stem}"  # fallback date for undated drafts

    dest_dir = POSTS_DIR / slug
    dest_dir.mkdir(parents=True, exist_ok=True)
    dest_file = dest_dir / "index.qmd"

    new_fm = build_new_frontmatter(fm, slug, is_draft_file)

    # Apply Liquid tag replacements in body
    if slug in LIQUID_REPLACEMENTS:
        for pattern, replacement in LIQUID_REPLACEMENTS[slug]:
            body = re.sub(pattern, replacement, body)

    output = f"---\n{fm_to_yaml(new_fm)}---\n\n{body}"
    dest_file.write_text(output, encoding="utf-8")
    draft_flag = " [DRAFT]" if new_fm.get("draft") else ""
    print(f"  OK{draft_flag}: {name} → posts/{slug}/index.qmd")


def main():
    POSTS_DIR.mkdir(exist_ok=True)

    print("=== Migrating _posts/ ===")
    for src in sorted(JEKYLL_POSTS.glob("*.md")):
        migrate_file(src, is_draft_file=False)

    print("\n=== Migrating draft/ ===")
    for src in sorted(JEKYLL_DRAFTS.glob("*.md")):
        migrate_file(src, is_draft_file=True)

    print("\nDone.")


if __name__ == "__main__":
    main()
