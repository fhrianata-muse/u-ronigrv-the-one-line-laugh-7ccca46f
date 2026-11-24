#!/usr/bin/env python3
"""Write one funny line to /output/entry.txt.

One idea, one sentence: a robot vacuum bought to save time now costs
its owner every evening in rescues.
"""

LINE = (
    "I bought a robot vacuum to save time, so now I spend my evenings "
    "rescuing it from cables, untangling it from curtains, and apologising "
    "to a machine that bumps into walls for a living."
)


def main():
    if not 1 <= len(LINE) <= 200:
        raise ValueError("line must be 1-200 characters")
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
