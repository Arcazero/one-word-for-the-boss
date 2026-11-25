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

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def validate_word(word: str) -> None:
    if (
        not word
        or len(word) > 30
        or not word.islower()
        or not word.isalpha()
        or any(ch.isspace() for ch in word)
    ):
        raise ValueError(
            "WORD must be a single lowercase word, 1-30 chars, no whitespace"
        )


def main() -> None:
    validate_word(WORD)
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
