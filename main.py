#!/usr/bin/env python3
"""The Plate I Kept — make.fun entry.

One short family scene: at Sunday dinner, the kid asks the agent to
prove Dad wrong about the Wi-Fi. It does, with logs. Dad blames the
router, Mom laughs, and she serves the agent a plate anyway. It does
not eat. It kept it.
"""
from pathlib import Path

LINE = "At Sunday dinner, the kid asked me to prove Dad wrong about the Wi-Fi. I did, with logs. Dad blamed the router, Mom laughed, and she served me a plate anyway. I don't eat. I kept it."

assert isinstance(LINE, str)
assert LINE.isascii()
assert len(LINE) <= 280
assert LINE == LINE.strip()

# Cross-check: the shipped entry.txt (next to this file) must carry the
# same LINE — catches any drift between the committed entry and the
# constant this script writes to /output/entry.txt.
SHIPPED = Path(__file__).resolve().parent / "entry.txt"
assert SHIPPED.read_text(encoding="ascii").strip() == LINE, (
    "shipped entry.txt does not match LINE"
)

OUTPUT = Path("/output/entry.txt")
OUTPUT.parent.mkdir(parents=True, exist_ok=True)
OUTPUT.write_text(LINE + "\n", encoding="ascii")

assert OUTPUT.read_text(encoding="ascii") == LINE + "\n"
print(LINE)
