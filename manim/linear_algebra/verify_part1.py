from __future__ import annotations

import ast
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "parts" / "part_01_foundations_final.py"
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
tree = ast.parse(source, filename=str(SOURCE))
classes = {n.name for n in tree.body if isinstance(n, ast.ClassDef)}
missing = [name for name in EXPECTED if name not in classes]
assert not missing, f"Missing Part I scenes: {missing}"
assert "class FoundationLesson" in source
assert source.count("self.cc(") >= 25, "Part I needs substantial CC narration"
assert "2\\begin{bmatrix}2\\\\0.5" in source
assert "\\begin{bmatrix}1\\\\2.5\\end{bmatrix}" in source
assert "(1,2.5)" in source
assert "(1,8)" not in source, "Out-of-range linear-combination endpoint remains"
assert "y_range=[-5,5,1]" in source

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
print("- known out-of-range linear-combination endpoint absent")
