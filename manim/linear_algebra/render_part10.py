from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parent
SCRIPT = "parts/part_10_decompositions_final.py"
SCENES = [
    "Part10_01_ChangeOfBasisIntuition",
    "Part10_02_CoordinateTransformation",
    "Part10_03_SimilarityTransformations",
    "Part10_04_OrthogonalMatrices",
    "Part10_05_LU_Factorization",
    "Part10_06_LU_SolvingSystems",
    "Part10_07_QR_Factorization",
    "Part10_08_QR_Geometry",
    "Part10_09_LinearOperators",
    "Part10_10_DecompositionComparison",
    "Part10_11_DecompositionsMastery",
]

if __name__ == "__main__":
    for scene in SCENES:
        print(f"=== Rendering {scene} ===")
        result = subprocess.run(["uv", "run", "manim", "-qh", SCRIPT, scene], cwd=ROOT, check=False)
        if result.returncode:
            raise SystemExit(result.returncode)
    print("Part X render list completed.")
