#!/usr/bin/env python3
"""Write one short text to $MAKEFUN_OUTPUT_DIR/entry.txt.

The text offers the reader a pause: an evening room, rain on a tin
roof, a cat asleep on a folded blanket, a warm kettle, amber light,
and an empty street outside. No answer is asked of the reader;
nothing is waiting for them.
"""

import os
from pathlib import Path

TEXT = (
    "You have read word after word since morning, and every page asked "
    "something of you. Here is a small room instead. Rain is falling on "
    "the tin roof, steady and soft, and the kettle is warm on the stove. "
    "Outside, the street is empty, and the lamps stand in puddles of "
    "their own light. Amber light sits low in the window. A cat is "
    "asleep on a folded blanket, curled tight, its tail tucked over its "
    "nose. There is nowhere else to be, and nothing here is asking you "
    "for an answer. The rain keeps falling, the cat keeps sleeping, and "
    "the evening keeps its quiet."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_bytes(TEXT.encode("utf-8"))


if __name__ == "__main__":
    main()
