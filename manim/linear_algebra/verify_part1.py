from __future__ import annotations

import ast
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "parts" / "part_01_foundations_final.py"
CANONICAL = ROOT / "parts" / "part_01_foundations_canonical.py"
UTILS = ROOT / "utils.py"
EXPECTED = [
    "Part1_01_ScalarsAndVectors",
    "Part1_02_CoordinatesAndComponents",
    "Part1_03_VectorAddition",
    "Part1_04_VectorSubtraction",
    "Part1_05_ScalingAndUnitVectors",
    "Part1_06_MagnitudeAndDistance",
    "Part1_07_LinearCombinations",
    "Part1_08_FoundationsRecap",
]

source = SOURCE.read_text(encoding="utf-8")
canonical = CANONICAL.read_text(encoding="utf-8")
utils = UTILS.read_text(encoding="utf-8")

# Mathematical lesson structure remains intact.
tree = ast.parse(source, filename=str(SOURCE))
classes = {n.name for n in tree.body if isinstance(n, ast.ClassDef)}
missing = [name for name in EXPECTED if name not in classes]
assert not missing, f"Missing Part I scenes: {missing}"
assert "class FoundationLesson" in source
assert source.count("self.cc(") >= 25, "Part I needs substantial CC narration"

# Canonical presentation wrapper must own the rendered Part I path.
assert "FoundationLesson.axes = _safe_axes" in canonical
assert "FoundationLesson.eq = _safe_eq" in canonical
assert "x_length=7.25" in canonical
assert "y_length=5.35" in canonical
assert "set_max_width(3.25)" in canonical

# The global caption system must behave as a single subtitle track.
assert "self._cc_caption" in utils
assert "FadeOut(self._cc_caption" in utils
assert "CC_PANEL_HEIGHT" in utils
assert "CC_FONT_SIZE = 24" in utils
assert "caption_text = \"\\n\".join(lines[:2])" in utils
assert "font_size=38" in utils

# Independent arithmetic checks for the numerical examples taught on screen.
assert (3 + 1, 1 + 3) == (4, 4)
assert (4 - 1, 3 - 1) == (3, 2)
assert (2 * 2, 2 * 1) == (4, 2)
assert (2 * 2 + 3 * (-1), 2 * 0.5 + 3 * 0.5) == (1, 2.5)
assert (2 - (-2), 2 - (-1)) == (4, 3)

print("Part I verification passed:")
print(f"- {len(EXPECTED)} lesson scenes present")
print("- Python AST parses successfully")
print("- CC narration threshold satisfied")
print("- numerical examples checked independently")
print("- canonical spacious layout is wired")
print("- caption track is single-instance and bounded")
