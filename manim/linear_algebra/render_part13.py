from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parent
SCRIPT = "parts/part_13_numerical_ml_canonical.py"
SCENES = [
    "Part13_01_NumericalLinearAlgebra",
    "Part13_02_Conditioning",
    "Part13_03_FloatingPointAndCancellation",
    "Part13_04_StableAlgorithms",
    "Part13_05_LeastSquares",
    "Part13_06_NormalEquationsVsQR",
    "Part13_07_LinearRegression",
    "Part13_08_GradientDescent",
    "Part13_09_NeuralNetworkLinearAlgebra",
    "Part13_10_EmbeddingsAndSimilarity",
    "Part13_11_NumericalMLMastery",
]

if __name__ == "__main__":
    for scene in SCENES:
        print(f"=== Rendering canonical {scene} ===")
        result = subprocess.run(["python", "-m", "manim", "-qh", SCRIPT, scene], cwd=ROOT, check=False)
        if result.returncode:
            raise SystemExit(result.returncode)
    print("Part XIII canonical render list completed.")
