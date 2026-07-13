#!/usr/bin/env python3
"""Constrain and optimise published raster images without touching originals."""

from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
from pathlib import Path


RASTER_SUFFIXES = {".png", ".jpg", ".jpeg", ".webp"}


def run(*args: str) -> None:
    subprocess.run(args, check=True)


def dimensions(path: Path) -> tuple[int, int]:
    result = subprocess.run(
        ["identify", "-format", "%w %h", f"{path}[0]"],
        check=True,
        capture_output=True,
        text=True,
    )
    width, height = result.stdout.split()
    return int(width), int(height)


def resize(path: Path, maximum: int) -> None:
    temporary = path.with_name(path.stem + ".resized" + path.suffix)
    args = [
        "magick", f"{path}[0]", "-auto-orient", "-resize", f"{maximum}x{maximum}>",
        "-strip",
    ]
    if path.suffix.casefold() in {".jpg", ".jpeg"}:
        args.extend(["-interlace", "Plane", "-quality", "85"])
    args.append(str(temporary))
    run(*args)
    os.replace(temporary, path)


def optimise(path: Path) -> None:
    suffix = path.suffix.casefold()
    if suffix == ".png":
        temporary = path.with_name(path.stem + ".crushed.png")
        run("pngcrush", "-q", "-reduce", "-rem", "alla", str(path), str(temporary))
        os.replace(temporary, path)
        run("optipng", "-quiet", "-o2", str(path))
    elif suffix in {".jpg", ".jpeg"}:
        run("jpegoptim", "--quiet", "--strip-all", "--all-progressive", "--max=85", str(path))
    elif suffix == ".webp":
        # ImageMagick performs the resize. Existing WebP files are otherwise
        # already compressed and should not be transcoded repeatedly.
        pass


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("media", type=Path)
    parser.add_argument("archive", type=Path, nargs="?", help="optional directory in which to preserve originals")
    parser.add_argument("--max-size", type=int, default=800)
    parser.add_argument("--resume", action="store_true", help="skip files already present in the archive")
    parser.add_argument("--report", type=Path)
    args = parser.parse_args()
    if args.archive:
        args.archive.mkdir(parents=True, exist_ok=True)

    results: list[dict[str, object]] = []
    files = sorted(path for path in args.media.iterdir() if path.is_file() and path.suffix.casefold() in RASTER_SUFFIXES)
    for path in files:
        archived = args.archive / path.name if args.archive else None
        if args.resume and archived and archived.exists():
            continue
        if archived and not archived.exists():
            shutil.copy2(path, archived)
        before_bytes = path.stat().st_size
        before_width, before_height = dimensions(path)
        resized = before_width > args.max_size or before_height > args.max_size
        if resized:
            resize(path, args.max_size)
        optimise(path)
        after_width, after_height = dimensions(path)
        results.append(
            {
                "file": path.name,
                "before": {"width": before_width, "height": before_height, "bytes": before_bytes},
                "after": {"width": after_width, "height": after_height, "bytes": path.stat().st_size},
                "resized": resized,
            }
        )

    report = {
        "max_size": args.max_size,
        "files": len(results),
        "resized": sum(bool(item["resized"]) for item in results),
        "before_bytes": sum(int(item["before"]["bytes"]) for item in results),
        "after_bytes": sum(int(item["after"]["bytes"]) for item in results),
        "images": results,
    }
    if args.report:
        args.report.write_text(json.dumps(report, indent=2) + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
