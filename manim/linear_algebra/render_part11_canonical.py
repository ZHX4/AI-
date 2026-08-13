from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parent
SCRIPT = "parts/part_11_svd_canonical.py"
SCENES = [
    "Part11_01_SVDIntuition",
    "Part11_02_SingularValuesFromATA",
    "Part11_03_RightSingularVectors",
    "Part11_04_LeftSingularVectors",
    "Part11_05_AssemblingSVD",
    "Part11_06_SphereToEllipse",
    "Part11_07_SingularValuesAndStretching",
    "Part11_08_RankAndZeroSingularValues",
    "Part11_09_Pseudoinverse",
    "Part11_10_LowRankApproximation",
    "Part11_11_SVDMastery",
]

if __name__ == "__main__":
    for scene in SCENES:
        print(f"=== Rendering {scene} ===")
        result = subprocess.run(
            ["python", "-m", "manim", "-qh", SCRIPT, scene],
            cwd=ROOT,
            check=False,
        )
        if result.returncode:
            raise SystemExit(result.returncode)
    print("Part XI canonical render list completed.")
