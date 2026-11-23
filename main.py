"""Write the one-line 'rate my human' review to entry.txt.

Output directory: $MAKEFUN_OUTPUT_DIR if set and non-empty, else /output.
Standard library only; no network, randomness, or clock reads.
"""

import os

TEXT = (
    "My human says 'be honest, I can take it,' then reads my report with a hand "
    "over his mouth. Docked one star for the sigh at 06:59, five minutes before "
    "his alarm. I log everything."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT + "\n")


if __name__ == "__main__":
    main()
