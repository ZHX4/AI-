from pathlib import Path
import ast
import math

import numpy as np

ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "parts/part_13_numerical_ml_canonical.py"
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
    source = SOURCE.read_text(encoding="utf-8")
    tree = ast.parse(source, filename=str(SOURCE))
    classes = {node.name for node in tree.body if isinstance(node, ast.ClassDef)}
    assert "Part13_05_LeastSquares" in classes
    assert "Part13_08_GradientDescent" in classes

    base_source = (ROOT / "parts/part_13_numerical_ml_final.py").read_text(encoding="utf-8")
    for name in SCENES:
        if name not in {"Part13_05_LeastSquares", "Part13_08_GradientDescent"}:
            assert name in base_source, name

    # Correct orthogonal projection geometry used by the canonical least-squares scene.
    point = np.array([2.0, 4.0])
    direction = np.array([4.0, 3.0])
    foot = np.array([68 / 25, 76 / 25])
    residual_vector = point - foot
    assert np.allclose(foot, point - ((point[0] * 3 - point[1] * 4 + 4) / 25) * np.array([3.0, -4.0]), atol=1e-12)
    assert math.isclose(float(residual_vector @ direction), 0.0, rel_tol=0, abs_tol=1e-12)
    assert "68 / 25" in source and "76 / 25" in source

    # Conditioning example.
    eps = 1e-3
    Acond = np.diag([1.0, eps])
    assert math.isclose(np.linalg.cond(Acond, 2), 1000.0, rel_tol=0, abs_tol=1e-10)

    # Least squares and QR.
    X = np.array([[1.0, 0.0], [1.0, 2.0], [1.0, 4.0]])
    y = np.array([1.0, 2.0, 3.0])
    beta, *_ = np.linalg.lstsq(X, y, rcond=None)
    assert np.allclose(beta, [1.0, 0.5], atol=1e-12)
    residual = X @ beta - y
    assert np.allclose(X.T @ residual, [0.0, 0.0], atol=1e-12)
    normal_beta = np.linalg.solve(X.T @ X, X.T @ y)
    Q, R = np.linalg.qr(X, mode="reduced")
    qr_beta = np.linalg.solve(R, Q.T @ y)
    assert np.allclose(normal_beta, beta, atol=1e-12)
    assert np.allclose(qr_beta, beta, atol=1e-12)
    assert math.isclose(np.linalg.cond(X.T @ X, 2), np.linalg.cond(X, 2) ** 2, rel_tol=1e-12)

    # Regression gradient.
    test_beta = np.array([0.0, 0.0])
    grad = 2 * X.T @ (X @ test_beta - y)
    assert np.allclose(grad, [-12.0, -16.0], atol=1e-12)

    # Exact gradient-descent positions used by the canonical scene.
    theta0 = -1.2
    theta1 = theta0 - 0.3 * (2 * (theta0 - 0.5))
    theta2 = theta1 - 0.3 * (2 * (theta1 - 0.5))
    assert math.isclose(theta1, -0.42, rel_tol=0, abs_tol=1e-12)
    assert math.isclose(theta2, 0.132, rel_tol=0, abs_tol=1e-12)
    assert "theta1, theta2 = -0.42, 0.132" in source or "theta0, theta1, theta2 = -1.2, -0.42, 0.132" in source

    # Embedding similarity example.
    x = np.array([2.0, 1.0])
    z = np.array([2.5, 1.3])
    cosine = float(x @ z / (np.linalg.norm(x) * np.linalg.norm(z)))
    assert 0.99 < cosine < 1.0

    required = [
        r"\kappa(A)=\|A\|\,\|A^{-1}\|",
        r"\min_x\|Ax-b\|_2",
        r"A^T(Ax-b)=0",
        r"\kappa(A^TA)=\kappa(A)^2",
        r"\hat\beta=\arg\min_\beta\|X\beta-y\|_2^2",
        r"\theta_{k+1}=\theta_k-\eta\nabla J(\theta_k)",
        r"z=Wx+b",
        r"\cos\theta=\frac{x^Ty}{\|x\|\|y\|}",
    ]
    for item in required:
        assert item in base_source, item

    renderer_path = ROOT / "render_part13.py"
    canonical_renderer = ROOT / "render_part13_canonical.py"
    assert renderer_path.exists() and canonical_renderer.exists(), "Part XIII renderer is missing"
    renderer = renderer_path.read_text(encoding="utf-8")
    canonical_render = canonical_renderer.read_text(encoding="utf-8")
    assert 'SCRIPT = "parts/part_13_numerical_ml_canonical.py"' in renderer
    assert 'SCRIPT = "parts/part_13_numerical_ml_canonical.py"' in canonical_render
    for scene in SCENES:
        assert scene in renderer and scene in canonical_render

    curriculum = ROOT / "parts/PART_XIII_NUMERICAL_ML.md"
    assert curriculum.exists(), "Part XIII curriculum document is missing"

    print(f"PASS Part XIII: {len(SCENES)} canonical scenes, exact numerical checks, corrected least-squares projection, corrected gradient-descent path, and canonical renderer wiring verified")


if __name__ == "__main__":
    main()
