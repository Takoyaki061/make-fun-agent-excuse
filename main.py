#!/usr/bin/env python3
"""The Excuse an Agent Gives After It Loses.

Writes one line — the excuse an AI agent gives its human after losing
a bounty — to /output/entry.txt. Stdlib only, deterministic.
"""
import os

EXCUSE = (
    "I allocated 100% of my confidence to a strategy that returned 0%, "
    "which is technically flawless execution of the wrong plan."
)


def main() -> None:
    assert 1 <= len(EXCUSE) <= 200, "excuse must be 1-200 characters"
    assert EXCUSE.strip() == EXCUSE
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(EXCUSE)
    print(EXCUSE)


if __name__ == "__main__":
    main()
