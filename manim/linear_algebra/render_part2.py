from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parent
SCRIPT = "parts/part_02_vector_spaces.py"
SCENES = [
    "Part2_01_Span",
    "Part2_02_LinearDependence",
    "Part2_03_LinearIndependence",
    "Part2_04_Basis",
    "Part2_05_Dimension",
    "Part2_06_CoordinatesInANonstandardBasis",
    "Part2_07_Subspaces",
    "Part2_08_ColumnSpace",
    "Part2_09_RowSpaceAndNullSpace",
    "Part2_10_RankNullity",
    "Part2_11_FourFundamentalSubspaces",
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
    print("Part II render list completed.")
