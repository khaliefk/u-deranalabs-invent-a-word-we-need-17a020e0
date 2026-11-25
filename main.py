#!/usr/bin/env python3
"""Invent a Word We Need.

Writes the coined word and its one-line definition to /output/entry.txt.
Standard library only. The entry is a single line, 140 characters at most.
"""

from pathlib import Path

ENTRY = (
    "Goodbyeloop (n.): the five goodbyes after the first "
    "goodbye on a phone call."
)
OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    # Gate self-check: one line, 1 to 140 characters, no trailing newline.
    assert ENTRY and len(ENTRY) <= 140 and "\n" not in ENTRY
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(ENTRY, encoding="utf-8")
    print(f"wrote {len(ENTRY)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
