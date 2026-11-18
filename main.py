"""Entry program for make.fun news-image-20261118.

Copies the pre-built cover image (entry.png) to the output directory
named by the MAKEFUN_OUTPUT_DIR environment variable. Deterministic:
the same bytes are written on every run.
"""

import os
import shutil
import sys


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(out_dir, exist_ok=True)
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    if not os.path.isfile(src):
        print("entry.png not found next to main.py", file=sys.stderr)
        return 1
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    # Confirm the copy landed byte-identical before reporting success.
    if os.path.getsize(src) != os.path.getsize(dst):
        print("copy size mismatch", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
