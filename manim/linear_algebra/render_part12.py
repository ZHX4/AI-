from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parent
SCRIPT = "parts/part_12_pca_final.py"
SCENES = [
    "Part12_01_PCAIntuition", "Part12_02_CenteringData", "Part12_03_CovarianceMatrix",
    "Part12_04_PrincipalDirections", "Part12_05_MaximumVariance", "Part12_06_ProjectionOntoPCs",
    "Part12_07_Reconstruction", "Part12_08_ExplainedVariance", "Part12_09_PCAFromSVD",
    "Part12_10_HigherDimensionalPCA", "Part12_11_PCAMastery",
]

def render_all():
    for scene in SCENES:
        print(f"=== Rendering {scene} ===")
        result = subprocess.run(["python", "-m", "manim", "-qh", SCRIPT, scene], cwd=ROOT, check=False)
        if result.returncode:
            raise SystemExit(result.returncode)

if __name__ == "__main__":
    render_all()
