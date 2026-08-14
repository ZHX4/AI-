from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT.parent))
from linear_algebra.parts.part_01_foundations_canonical import *  # noqa: F401,F403

SCENES = [
    "Part1_01_ScalarsAndVectors",
    "Part1_02_CoordinatesAndComponents",
    "Part1_03_VectorAddition",
    "Part1_04_VectorSubtraction",
    "Part1_05_ScalingAndUnitVectors",
    "Part1_06_MagnitudeAndDistance",
    "Part1_07_LinearCombinations",
    "Part1_08_FoundationsRecap",
]

if __name__ == "__main__":
    for scene in SCENES:
        print(f"=== Rendering {scene} ===")
        result = subprocess.run(
            ["uv", "run", "manim", "-qh", "parts/part_01_foundations_canonical.py", scene],
            cwd=ROOT,
            check=False,
        )
        if result.returncode != 0:
            raise SystemExit(result.returncode)
