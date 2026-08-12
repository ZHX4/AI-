from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parent
SCRIPT = "parts/part_04_systems_final.py"
SCENES = [
    "Part4_01_AxEqualsB",
    "Part4_02_GeometricMeaning",
    "Part4_03_AugmentedMatrix",
    "Part4_04_ElementaryRowOperations",
    "Part4_05_GaussianElimination",
    "Part4_06_BackSubstitution",
    "Part4_07_RREF",
    "Part4_08_ThreeSolutionCases",
    "Part4_09_HomogeneousSystems",
    "Part4_10_ThreeByThreeWorkedSystem",
    "Part4_11_SystemsMastery",
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
    print("Part IV render list completed.")
