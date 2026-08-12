from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parent
SCRIPT = "parts/part_06_determinants_canonical.py"
SCENES = [
    "Part6_01_WhatDeterminantMeasures",
    "Part6_02_TwoByTwoSignedArea",
    "Part6_03_DeterminantAsAreaScale",
    "Part6_04_ThreeByThreeVolume",
    "Part6_05_OrientationAndSign",
    "Part6_06_DeterminantProperties",
    "Part6_07_RowOperationsAndDeterminant",
    "Part6_08_CofactorExpansion",
    "Part6_09_DeterminantAndInvertibility",
    "Part6_10_DeterminantAndProducts",
    "Part6_11_DeterminantMastery",
]


if __name__ == "__main__":
    for scene in SCENES:
        print(f"=== Rendering {scene} ===")
        result = subprocess.run(
            ["uv", "run", "manim", "-qh", SCRIPT, scene],
            cwd=ROOT,
            check=False,
        )
        if result.returncode:
            raise SystemExit(result.returncode)
    print("Part VI render list completed.")
