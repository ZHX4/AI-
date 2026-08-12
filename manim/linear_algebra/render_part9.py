from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parent
SCRIPT = "parts/part_09_symmetric_matrices_canonical.py"
SCENES = [
    "Part9_01_SymmetryIntuition",
    "Part9_02_OrthogonalEigenvectors",
    "Part9_03_SpectralTheorem",
    "Part9_04_BuildingQAndLambda",
    "Part9_05_QuadraticForms",
    "Part9_06_PrincipalAxes",
    "Part9_07_RayleighQuotient",
    "Part9_08_PositiveDefinite",
    "Part9_09_NegativeAndIndefinite",
    "Part9_10_SemidefiniteAndTests",
    "Part9_11_SymmetricMatrixMastery",
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
    print("Part IX render list completed.")
