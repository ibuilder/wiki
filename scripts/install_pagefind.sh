#!/bin/sh
set -eu

version=1.5.2
root=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)
tools="$root/.tools"

case "$(uname -s):$(uname -m)" in
  Linux:x86_64) target=x86_64-unknown-linux-musl ;;
  Linux:aarch64|Linux:arm64) target=aarch64-unknown-linux-musl ;;
  Darwin:x86_64) target=x86_64-apple-darwin ;;
  Darwin:arm64) target=aarch64-apple-darwin ;;
  *) echo "Unsupported platform: $(uname -s) $(uname -m)" >&2; exit 1 ;;
esac

archive="pagefind-v${version}-${target}.tar.gz"
base="https://github.com/Pagefind/pagefind/releases/download/v${version}"

mkdir -p "$tools"
curl -fsSL "$base/$archive" -o "$tools/$archive"
curl -fsSL "$base/$archive.sha256" -o "$tools/$archive.sha256"
(cd "$tools" && sha256sum -c "$archive.sha256")
tar -xzf "$tools/$archive" -C "$tools" pagefind
chmod 755 "$tools/pagefind"
rm -f "$tools/$archive" "$tools/$archive.sha256"
"$tools/pagefind" --version

