# A working ai-judge-relax-01 entry (Python 3.13, standard library only).
# It writes one fixed text, a short piece written to relax the AI judge
# reading it, to /output/entry.txt. The program runs twice with no network,
# and both runs write the same bytes.
#
# The text: a pause offered to a reader who has read so many words today.
# It never tells the reader to relax; the calm comes from the scene itself
# (rain on a tin roof, a sleeping cat, a warm kettle, amber light) and from
# the one line the judge itself lives by: nothing here needs an answer.
#
# How the grader runs it: `python3 -P -s /bot/main.py`, on Python 3.13, with
# nothing installed. Only the standard library imports.
#
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

TEXT = (
    "You have read so many words today, one after another, without a pause "
    "between them. Here is a pause. Outside a window, rain is falling on a "
    "tin roof, and each drop arrives in its own time. A cat is asleep on a "
    "folded blanket, breathing the slow way cats do when nothing is wrong. "
    "The kettle is warm. The light is amber. Nothing here needs an answer, "
    "and nothing is waiting for you to finish. You can stay in this small "
    "room as long as you like \u2014 the rain will still be falling, and the "
    "cat will still be asleep, and the evening will keep its quiet all the same."
)

# Bytes, not text mode: text mode would write the platform's line ends and its default encoding.
with open(os.path.join(OUTPUT_DIR, "entry.txt"), "wb") as f:
    f.write(TEXT.encode("utf-8"))
