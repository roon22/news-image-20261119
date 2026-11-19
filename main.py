#!/usr/bin/env python3
"""Copy the bundled front page to /output/entry.png."""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "entry.png")
TARGET = "/output/entry.png"
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"
JPEG_MAGIC = b"\xff\xd8\xff"


def main():
    with open(SOURCE, "rb") as fh:
        head = fh.read(8)
    if not (head.startswith(PNG_MAGIC) or head.startswith(JPEG_MAGIC)):
        raise SystemExit("entry.png is not a PNG or JPEG image")
    try:
        os.makedirs(os.path.dirname(TARGET), exist_ok=True)
        target = TARGET
    except OSError:
        target = os.path.join(HERE, "output", "entry.png")
        os.makedirs(os.path.dirname(target), exist_ok=True)
    shutil.copyfile(SOURCE, target)
    print("wrote", target, os.path.getsize(target), "bytes")


if __name__ == "__main__":
    main()
