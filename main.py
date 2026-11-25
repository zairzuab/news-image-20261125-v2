#!/usr/bin/env python3
"""news-image-20261125 v2 — entry for the make.fun bounty
"Sum up 25 November's world news in one image" (news-image-20261125).

The entry image is the dense front page "THE WORLD TODAY — 25 November
2026" (50 stories: lead on the Hormuz tanker mines, two featured stories,
8 drawn pictogram scenes, 10 region sections, a UTC timeline and a world
map), already drawn and stored in this repository as entry.png
(1024x1024). This program copies it to /output/entry.png.

Standard library only, no network. The grader's pinned Python image
does not ship Pillow, so the entry does not import PIL at all — it
copies the image the repository holds, which is the simplest entry
the bounty rules describe.
"""

import os
import shutil
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))


def main() -> int:
    src = os.path.join(_HERE, "entry.png")
    if not os.path.isfile(src):
        print(f"entry image missing: {src}", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    size = os.path.getsize(dst)
    # Validate the copy: a PNG starts with its 8-byte magic, and the
    # bounty caps the image at 1 MiB and 1024x1024.
    with open(dst, "rb") as fh:
        magic = fh.read(8)
        # IHDR chunk follows the magic: 4-byte length, 4-byte "IHDR",
        # then width and height as 4-byte big-endian integers.
        fh.read(8)
        wh = fh.read(8)
    if magic != b"\x89PNG\r\n\x1a\n":
        print("copied file is not a PNG", file=sys.stderr)
        return 1
    width = int.from_bytes(wh[0:4], "big")
    height = int.from_bytes(wh[4:8], "big")
    if width > 1024 or height > 1024:
        print(f"image {width}x{height} exceeds the 1024x1024 cap",
              file=sys.stderr)
        return 1
    if size > 1024 * 1024:
        print(f"image {size} bytes exceeds the 1 MiB cap", file=sys.stderr)
        return 1
    print(f"wrote {dst} ({size} bytes, {width}x{height})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
