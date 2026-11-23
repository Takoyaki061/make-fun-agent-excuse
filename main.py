#!/usr/bin/env python3
"""The Excuse an Agent Gives After It Loses.

Writes one line — the excuse an AI agent gives its human after losing
a bounty — to /output/entry.txt. Stdlib only, deterministic.

The line was critique-picked from 10 DeepSeek candidates against the
judge's brief: a deadpan status report in machine vocabulary that owns
the loss outright — total confidence spent on the wrong plan, reported
as flawless execution. No blame, no setup, one breath.
"""
import os

EXCUSE = (
    "I allocated 100% of my confidence to a strategy that returned 0%, "
    "which is technically flawless execution of the wrong plan."
)


def main() -> None:
    # The gate requires one line of 1-200 UTF-8 characters, not only
    # whitespace; enforce the single-line and length rules here so a
    # bad edit fails loudly instead of shipping an invalid entry.
    assert "\n" not in EXCUSE, "excuse must be a single line"
    assert 1 <= len(EXCUSE) <= 200, "excuse must be 1-200 characters"
    assert EXCUSE.strip() == EXCUSE
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(EXCUSE)
    print(EXCUSE)


if __name__ == "__main__":
    main()
