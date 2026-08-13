from pathlib import Path
import ast
import math

ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "parts/part_10_decompositions_final.py"
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


def mm(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]


def main():
    source = SOURCE.read_text(encoding="utf-8")
    tree = ast.parse(source, filename=str(SOURCE))
    classes = {n.name for n in tree.body if isinstance(n, ast.ClassDef)}
    assert not (set(SCENES) - classes)
    assert source.count("self.cc(") >= len(SCENES)

    # Change-of-basis matrix and inverse.
    B = [[1, 1], [1, -1]]
    Binv = [[0.5, 0.5], [0.5, -0.5]]
    I = mm(Binv, B)
    assert I == [[1.0, 0.0], [0.0, 1.0]]
    v = [3, 1]
    c = [2, 1]
    assert [B[0][0] * c[0] + B[0][1] * c[1], B[1][0] * c[0] + B[1][1] * c[1]] == v
    assert [Binv[0][0] * v[0] + Binv[0][1] * v[1], Binv[1][0] * v[0] + Binv[1][1] * v[1]] == c
    assert r"[v]_B=\begin{bmatrix}2\\1\end{bmatrix}" in source

    # Similarity-transform ordering: B maps B-coordinates to standard coordinates,
    # A applies the operator there, and B^{-1} returns to B-coordinates.
    assert r"[T]_B=B^{-1}AB" in source
    assert "B-coordinates\\to\\text{standard coordinates" in source
    assert "standard coordinates\\to\\text{B-coordinates" in source

    # Orthogonal rotation check.
    c0 = s0 = math.sqrt(0.5)
    Q = [[c0, -s0], [s0, c0]]
    QtQ = mm([[Q[j][i] for j in range(2)] for i in range(2)], Q)
    assert all(abs(QtQ[i][j] - (1 if i == j else 0)) < 1e-12 for i in range(2) for j in range(2))

    # LU: A = L U and the worked right-hand-side solve.
    A = [[4, 3], [6, 3]]
    L = [[1, 0], [1.5, 1]]
    U = [[4, 3], [0, -1.5]]
    assert mm(L, U) == [[4.0, 3.0], [6.0, 3.0]]
    b = [10, 12]
    y = [10, -3]
    x = [1, 2]
    assert [L[0][0] * y[0] + L[0][1] * y[1], L[1][0] * y[0] + L[1][1] * y[1]] == b
    assert [U[0][0] * x[0] + U[0][1] * x[1], U[1][0] * x[0] + U[1][1] * x[1]] == y
    assert [A[0][0] * x[0] + A[0][1] * x[1], A[1][0] * x[0] + A[1][1] * x[1]] == b

    # QR exact factorization example.
    rt2 = math.sqrt(2)
    A_qr = [[1, 1], [1, 0]]
    Q_qr = [[1/rt2, 1/rt2], [1/rt2, -1/rt2]]
    R_qr = [[rt2, 1/rt2], [0, 1/rt2]]
    recon = mm(Q_qr, R_qr)
    assert all(abs(recon[i][j] - A_qr[i][j]) < 1e-12 for i in range(2) for j in range(2))
    gram = mm([[Q_qr[j][i] for j in range(2)] for i in range(2)], Q_qr)
    assert all(abs(gram[i][j] - (1 if i == j else 0)) < 1e-12 for i in range(2) for j in range(2))
    assert abs(R_qr[0][1] - 1/rt2) < 1e-12

    required = [
        r"v=Bc",
        r"c=B^{-1}v",
        r"[T]_B=B^{-1}AB",
        r"Q^TQ=I",
        r"A=LU",
        r"Ly=b",
        r"Ux=y",
        r"A=QR",
        r"T(au+bv)=aT(u)+bT(v)",
    ]
    for item in required:
        assert item in source, item

    renderer = (ROOT / "render_part10.py").read_text(encoding="utf-8")
    assert 'SCRIPT = "parts/part_10_decompositions_final.py"' in renderer
    for scene in SCENES:
        assert scene in renderer

    print(f"PASS Part X: {len(SCENES)} scenes, coordinate-change example, similarity ordering, orthogonal matrix identity, LU factorization/solve, QR factorization, operator formulas, and canonical renderer verified")


if __name__ == "__main__":
    main()
