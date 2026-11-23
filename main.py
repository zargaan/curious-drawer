"""Make the AI judge feel curious — make.fun entry.

Writes one short text to /output/entry.txt.
Deterministic, no network, no randomness, no time dependence:
the same bytes on every run.
"""
import os
import sys

# The text, written against the published judge brief: intrigue first,
# calm shown not instructed, plain concrete words, one lingering image.
TEXT = (
    "The drawer in the hall has been locked for eleven years. "
    "This morning it stood open, and inside, in your handwriting, "
    "was a list of things you haven't done yet. "
    "The last one was underlined twice."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # Write exact bytes, no trailing newline, so the file is exactly
    # TEXT: 195 characters, within the 1-280 limit, not only whitespace.
    # No network, no randomness, no clock: two runs are byte-identical.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)
    return 0


if __name__ == "__main__":
    sys.exit(main())
