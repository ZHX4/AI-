from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parent
SCRIPT = "parts/part_07_fundamental_subspaces_canonical.py"
SCENES = [
    "Part7_01_RankIntuition",
    "Part7_02_ColumnSpace",
    "Part7_03_RowSpace",
    "Part7_04_NullSpace",
    "Part7_05_LeftNullSpace",
    "Part7_06_FourFundamentalSubspaces",
    "Part7_07_RankPivotsAndIndependentDirections",
    "Part7_08_RankNullity",
    "Part7_09_OrthogonalityPairs",
    "Part7_10_DimensionsAndStructure",
    "Part7_11_FundamentalSubspacesMastery",
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
    print("Part VII render list completed.")
