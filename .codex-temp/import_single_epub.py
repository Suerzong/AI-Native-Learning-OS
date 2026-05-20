from __future__ import annotations

import sys
from pathlib import Path

from tools.epub_to_obsidian import convert_epub


def main() -> int:
    if len(sys.argv) != 3:
        print("usage: import_single_epub.py <epub-path> <obsidian-books-dir>")
        return 2
    name, count = convert_epub(Path(sys.argv[1]), Path(sys.argv[2]))
    print(f"{name}: {count} chapters")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
