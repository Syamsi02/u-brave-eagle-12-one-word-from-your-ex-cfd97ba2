#!/usr/bin/env python3
"""One Word From Your Ex -- entry program.

Writes exactly one word to /output/entry.txt: the word an ex would use
to describe the entrant. The word is "exhausting": funny because it is
self-aware, painful because it is true, and instantly relatable -- dating
this person took effort, and everybody knows someone like that.

Pure standard library, deterministic, no network, no input files.
"""

import os
import sys

WORD = "exhausting"

OUTPUT_PATH = "/output/entry.txt"


def main() -> int:
    # The gate allows UTF-8 text of 1 to 24 characters, not only white
    # space, and the judge wants exactly one word: refuse to write
    # anything that would fail either rule instead of guessing.
    if not 1 <= len(WORD) <= 24 or not WORD.strip():
        raise SystemExit("word fails the gate: must be 1-24 non-space chars")
    if len(WORD.split()) != 1:
        raise SystemExit("word fails the gate: must be exactly one word")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(WORD)
    print(WORD)
    return 0


if __name__ == "__main__":
    sys.exit(main())
