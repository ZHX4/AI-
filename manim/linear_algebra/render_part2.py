from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parent
SCENES = [
    ("parts/part_02_vector_spaces_corrected.py", "Part2_01_Span"),
    ("parts/part_02_vector_spaces.py", "Part2_02_LinearDependence"),
    ("parts/part_02_vector_spaces.py", "Part2_03_LinearIndependence"),
    ("parts/part_02_vector_spaces.py", "Part2_04_Basis"),
    ("parts/part_02_vector_spaces.py", "Part2_05_Dimension"),
    ("parts/part_02_vector_spaces.py", "Part2_06_CoordinatesInANonstandardBasis"),
    ("parts/part_02_vector_spaces.py", "Part2_07_Subspaces"),
    ("parts/part_02_vector_spaces.py", "Part2_08_ColumnSpace"),
    ("parts/part_02_vector_spaces.py", "Part2_09_RowSpaceAndNullSpace"),
    ("parts/part_02_vector_spaces.py", "Part2_10_RankNullityAndFourSpaces"),
    ("parts/part_02_vector_spaces_corrected.py", "Part2_11_FourFundamentalSubspaces"),
]

if __name__ == "__main__":
    for script, scene in SCENES:
        print(f"=== Rendering {scene} ===")
        result = subprocess.run(["uv", "run", "manim", "-qh", script, scene], cwd=ROOT, check=False)
        if result.returncode:
            raise SystemExit(result.returncode)
    print("Part II render list completed.")
