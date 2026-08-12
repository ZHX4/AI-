from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parent
PARENT = ROOT.parent
sys.path.insert(0, str(PARENT))

LESSONS = [
    "Part1_01_ScalarsAndVectors",
    "Part1_02_CoordinatesAndComponents",
    "Part1_03_VectorAddition",
    "Part1_04_VectorSubtraction",
    "Part1_05_ScalingAndUnitVectors",
    "Part1_06_MagnitudeAndDistance",
    "Part1_07_LinearCombinations",
    "Part1_08_VectorAlgebraAndMastery",
]


if __name__ == "__main__":
    for scene in LESSONS:
        print(f"=== Rendering {scene} ===")
        result = subprocess.run(
            ["uv", "run", "manim", "-pqh", "parts/part_01_foundations.py", scene],
            cwd=ROOT,
            check=False,
        )
        if result.returncode != 0:
            raise SystemExit(result.returncode)

    print("Part I rendering completed successfully.")
