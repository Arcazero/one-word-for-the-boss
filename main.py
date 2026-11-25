#!/usr/bin/env python3
"""One Word for the Boss — a make.fun program/v1 entry.

The entry is a single word describing the boss, written to
/output/entry.txt. The word is:

    nanomanager

A micromanager manages every little thing you do. A nanomanager manages
at an even smaller scale: every keystroke, every minute, every breath
between the keystrokes. One level down from micro, one level more
suffocating — the boss who has to approve the font before you type the
sentence, and then re-approves it while you are still typing.
"""

import os

WORD = "nanomanager"

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
