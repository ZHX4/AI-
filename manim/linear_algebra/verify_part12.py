from pathlib import Path
import ast
import math

import numpy as np

ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "parts/part_12_pca_final.py"
SCENES = [
    "Part12_01_PCAIntuition", "Part12_02_CenteringData", "Part12_03_CovarianceMatrix",
    "Part12_04_PrincipalDirections", "Part12_05_MaximumVariance", "Part12_06_ProjectionOntoPCs",
    "Part12_07_Reconstruction", "Part12_08_ExplainedVariance", "Part12_09_PCAFromSVD",
    "Part12_10_HigherDimensionalPCA", "Part12_11_PCAMastery",
]


def main():
    source = SOURCE.read_text(encoding="utf-8")
    tree = ast.parse(source, filename=str(SOURCE))
    classes = {n.name for n in tree.body if isinstance(n, ast.ClassDef)}
    assert not (set(SCENES) - classes)
    assert source.count("self.cc(") >= len(SCENES)

    s2 = math.sqrt(2)
    s3 = math.sqrt(3)
    q1 = np.array([1 / s2, 1 / s2])
    q2 = np.array([1 / s2, -1 / s2])
    X = np.array([s3 * q1, -s3 * q1, q2, -q2])

    # Centering: the chosen observations already have mean zero.
    assert np.allclose(X.mean(axis=0), [0.0, 0.0], atol=1e-12)

    # Population-style covariance used throughout this lesson: C=(1/n)X^T X.
    C = (X.T @ X) / len(X)
    assert np.allclose(C, [[1.0, 0.5], [0.5, 1.0]], atol=1e-12)

    # Exact PCA directions/eigenvalues.
    assert np.allclose(C @ q1, 1.5 * q1, atol=1e-12)
    assert np.allclose(C @ q2, 0.5 * q2, atol=1e-12)
    assert abs(np.dot(q1, q2)) < 1e-12

    # Projection onto PC1.
    scores = X @ q1
    assert np.allclose(scores, [s3, -s3, 0.0, 0.0], atol=1e-12)
    X1 = np.outer(scores, q1)
    assert np.allclose(X1[:2], X[:2], atol=1e-12)
    assert np.allclose(X1[2:], 0.0, atol=1e-12)

    # Explained variance and reconstruction error.
    total = 1.5 + 0.5
    assert math.isclose(1.5 / total, 0.75, rel_tol=0, abs_tol=1e-12)
    mse = np.mean(np.sum((X - X1) ** 2, axis=1))
    assert math.isclose(mse, 0.5, rel_tol=0, abs_tol=1e-12)

    # SVD relationship: C=(1/n)X^T X, so lambda_i=sigma_i^2/n.
    singular_values = np.linalg.svd(X, full_matrices=False, compute_uv=False)
    assert np.allclose(np.sort(singular_values)[::-1], [math.sqrt(6), math.sqrt(2)], atol=1e-12)

    required = [
        r"C=\frac1nX_c^TX_c",
        r"Cq_1=\frac32q_1",
        r"Cq_2=\frac12q_2",
        r"z=Q^Tx",
        r"\lambda_i=\frac{\sigma_i^2}{n}",
    ]
    for item in required:
        assert item in source, item

    renderer = (ROOT / "render_part12.py").read_text(encoding="utf-8") if (ROOT / "render_part12.py").exists() else ""
    if renderer:
        assert 'SCRIPT = "parts/part_12_pca_final.py"' in renderer
        for scene in SCENES:
            assert scene in renderer

    print(f"PASS Part XII: {len(SCENES)} scenes, exact centering/covariance, PCA eigenpairs, projection/reconstruction, explained variance, SVD relationship, and scene structure verified")


if __name__ == "__main__":
    main()
