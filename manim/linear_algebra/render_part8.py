from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parent
SCRIPT = "parts/part_08_eigenvalues_canonical.py"
SCENES = [
    "Part8_01_EigenvectorIntuition",
    "Part8_02_EigenEquation",
    "Part8_03_CharacteristicPolynomial",
    "Part8_04_FindingEigenvectors",
    "Part8_05_GeometricEigenspaces",
    "Part8_06_AlgebraicVsGeometricMultiplicity",
    "Part8_07_Diagonalization",
    "Part8_08_MatrixPowers",
    "Part8_09_DynamicsAndEigenDirections",
    "Part8_10_EigenvaluesBeyond2D",
    "Part8_11_EigenvalueMastery",
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
    print("Part VIII render list completed.")
