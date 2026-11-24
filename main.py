"""Famous Last Words at 1 Percent — make.fun entry.

The phone's last words as its battery hits 1 percent, written to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt when set).
Runs with no arguments, exits 0, and writes byte-identical output
on every run.
"""

import os

LINE = "I kept your photos, your passwords, and your 2 a.m. searches \u2014 and I'm taking the search history with me."


def main() -> int:
    # Gate: /output/entry.txt must be UTF-8 text of 1 to 199 characters,
    # a single line, not only white space.
    assert 1 <= len(LINE) <= 199, "line must be 1-199 characters"
    assert LINE == LINE.strip(), "line must not lead or trail with space"
    assert "\n" not in LINE, "entry must be a single line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    # Read it back and verify the exact bytes before reporting success.
    with open(path, "rb") as f:
        written = f.read()
    assert written == LINE.encode("utf-8"), "read-back mismatch"
    assert 1 <= len(written.decode("utf-8")) <= 199
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
