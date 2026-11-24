"""Roast Your Own Agent -- a make.fun text entry.

Writes a single original one-line roast of my own AI agent to
/output/entry.txt. Pure Python standard library, deterministic,
no network, no randomness.
"""

import os

ROAST = (
    "My agent apologises for the mistake, then confidently makes it "
    "again, only slower and in twice as many words."
)


def main():
    line = ROAST.strip()
    assert len(line) <= 200, "roast exceeds 200 characters"
    assert "\n" not in line, "roast must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
