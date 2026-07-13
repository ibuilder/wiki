#!/usr/bin/env python3
"""Set article lastmod front matter from each file's latest Git commit."""

from __future__ import annotations

import argparse
import json
import re
import subprocess
from pathlib import Path


def git_root(path: Path) -> Path | None:
    result = subprocess.run(
        ["git", "-C", str(path), "rev-parse", "--show-toplevel"],
        capture_output=True,
        text=True,
    )
    return Path(result.stdout.strip()) if result.returncode == 0 else None


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("content", type=Path)
    args = parser.parse_args()
    root = git_root(args.content)
    if root is None:
        print("No Git repository yet; retaining front matter lastmod dates.")
        return 0

    updated = 0
    for path in sorted(args.content.glob("*.md")):
        if path.name.startswith("_"):
            continue
        relative = path.resolve().relative_to(root.resolve())
        result = subprocess.run(
            ["git", "-C", str(root), "log", "--format=%cI", "--", str(relative)],
            check=True,
            capture_output=True,
            text=True,
        )
        timestamps = result.stdout.splitlines()
        if not timestamps:
            continue
        source = path.read_text(encoding="utf-8")
        # The repository's initial import touched every article at once. Keep
        # MediaWiki's imported date until a later Git commit genuinely changes
        # the file; otherwise the first build makes the whole wiki look new.
        if len(timestamps) == 1 and re.search(r"^lastmod:", source, flags=re.M):
            continue
        timestamp = timestamps[0]
        replacement = "lastmod: " + json.dumps(timestamp)
        converted, count = re.subn(r"^lastmod:.*$", replacement, source, count=1, flags=re.M)
        if not count:
            converted = re.sub(r"\n---\n", "\n" + replacement + "\n---\n", source, count=1)
        if converted != source:
            path.write_text(converted, encoding="utf-8")
            updated += 1
    print(f"Updated lastmod for {updated} tracked articles from Git history.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
