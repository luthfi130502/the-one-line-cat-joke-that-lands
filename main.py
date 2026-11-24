#!/usr/bin/env python3
"""The One-Line Cat Joke That Lands - entrypoint.

Writes exactly one line (the joke) to /output/entry.txt.
Python standard library only.
"""

import os

OUTPUT_PATH = "/output/entry.txt"

JOKE = (
    "My cat gives me performance reviews by knocking one thing off the "
    "table for every flaw she finds - this morning she cleared the entire desk."
)


def main() -> None:
    line = JOKE.strip()
    assert "\n" not in line, "entry must be exactly one line"
    assert 1 <= len(line) <= 200, f"entry must be 1-200 chars, got {len(line)}"

    out_dir = os.path.dirname(OUTPUT_PATH)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)

    with open(OUTPUT_PATH, "w", encoding="utf-8") as fh:
        fh.write(line + "\n")

    print(f"wrote {len(line)} chars to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
