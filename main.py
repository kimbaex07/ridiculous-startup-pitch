#!/usr/bin/env python3
"""Write the pitch sentence to the make.fun output directory.

Reads entry.txt next to this script, validates it is 1..200 characters
of non-whitespace UTF-8 text, and writes its exact bytes to
$MAKEFUN_OUTPUT_DIR/entry.txt (default "output") with mode 0644.
Writes only to the output directory, never beside the source file.
"""

import os
import sys

MAX_CHARS = 200


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    source_path = os.path.join(here, "entry.txt")
    with open(source_path, "rb") as handle:
        data = handle.read()

    text = data.decode("utf-8")
    if not (1 <= len(text) <= MAX_CHARS):
        sys.exit("entry.txt must be 1..200 characters, got %d" % len(text))
    if not text.strip():
        sys.exit("entry.txt must not be only whitespace")

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "wb") as handle:
        handle.write(data)
    os.chmod(out_path, 0o644)


if __name__ == "__main__":
    main()
