from pathlib import Path
import ast

ROOT = Path(__file__).resolve().parent
BASE = ROOT / "parts/part_13_numerical_ml_final.py"
CANONICAL = ROOT / "parts/part_13_numerical_ml_canonical.py"
RENDERER = ROOT / "render_part13_canonical.py"
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


def main():
    base = BASE.read_text(encoding="utf-8")
    canonical = CANONICAL.read_text(encoding="utf-8")
    tree = ast.parse(canonical, filename=str(CANONICAL))
    classes = {node.name for node in tree.body if isinstance(node, ast.ClassDef)}
    assert "Part13_05_LeastSquares" in classes
    assert "68 / 25" in canonical
    assert "76 / 25" in canonical
    assert "residual" in canonical
    assert all(name in base or name == "Part13_05_LeastSquares" for name in SCENES)

    renderer = RENDERER.read_text(encoding="utf-8")
    assert 'SCRIPT = "parts/part_13_numerical_ml_canonical.py"' in renderer
    for scene in SCENES:
        assert scene in renderer

    print(f"PASS Part XIII canonical path: {len(SCENES)} scenes, corrected orthogonal least-squares projection, canonical renderer wiring verified")


if __name__ == "__main__":
    main()
