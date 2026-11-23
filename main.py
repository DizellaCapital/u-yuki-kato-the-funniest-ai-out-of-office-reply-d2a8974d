"""The Funniest AI Out-of-Office Reply entry program.

Writes one out-of-office auto-reply to MAKEFUN_OUTPUT_DIR/entry.txt.
Stdlib only. The reply is a single line of at most 160 characters.
"""

import os
import sys

LINE = "I'm on vacation. Your email has been delegated to a script that filed it under 'probably fine'."


def main():
    if not (1 <= len(LINE) <= 160):
        print(f"entry must be 1-160 characters, got {len(LINE)}", file=sys.stderr)
        return 1
    if LINE != LINE.strip() or not LINE.strip():
        print("entry must not be only whitespace", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != LINE:
        print("read-back mismatch", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
