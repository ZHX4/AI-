from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parent
SCRIPT = "parts/part_03_matrices_final.py"
SCENES = [
    "Part3_01_WhatIsAMatrix",
    "Part3_02_MatrixVectorMultiplication",
    "Part3_03_ColumnsBuildTheOutput",
    "Part3_04_MatrixAsTransformation",
    "Part3_05_MatrixAdditionAndScaling",
    "Part3_06_MatrixMultiplication",
    "Part3_07_CompositionOfTransformations",
    "Part3_08_IdentityMatrix",
    "Part3_09_Transpose",
    "Part3_10_InverseMatrix",
    "Part3_11_MatrixMastery",
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
    print("Part III render list completed.")
