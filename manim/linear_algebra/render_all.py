from pathlib import Path
import subprocess
import sys

LESSONS = [
    "Lesson01Vectors",
    "Lesson02VectorOperations",
    "Lesson03SpanBasisDimension",
    "Lesson04MatricesTransformations",
    "Lesson05MatrixMultiplication",
    "Lesson06DeterminantInverse",
    "Lesson07DotProduct",
    "Lesson08ProjectionLeastSquares",
    "Lesson09Rank",
    "Lesson10Eigen",
    "Lesson11QuadraticForms",
    "Lesson12SVD",
    "Lesson13PCA",
    "Lesson14Conditioning",
    "Lesson15LinearAlgebraForML",
]

ROOT = Path(__file__).parent

if __name__ == "__main__":
    for scene in LESSONS:
        print(f"=== Rendering {scene} ===")
        result = subprocess.run(
            ["uv", "run", "manim", "-qh", "course.py", scene],
            cwd=ROOT,
            check=False,
        )
        if result.returncode:
            raise SystemExit(result.returncode)
