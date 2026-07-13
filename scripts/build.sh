#!/bin/sh
set -eu

root=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)
pagefind=${PAGEFIND:-"$root/.tools/pagefind"}

python3 "$root/scripts/update_lastmod.py" "$root/content/wiki"

if [ ! -x "$pagefind" ]; then
  echo "Pagefind is not installed. Run scripts/install_pagefind.sh first." >&2
  exit 1
fi

hugo --source "$root" --cleanDestinationDir "$@"
"$pagefind" --site "$root/public"
