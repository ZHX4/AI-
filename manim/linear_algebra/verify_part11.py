from pathlib import Path
import ast
import math

ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "parts/part_11_svd_final.py"
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


def mm(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]


def mv(A, v):
    return [sum(A[i][j] * v[j] for j in range(len(v))) for i in range(len(A))]


def main():
    source = SOURCE.read_text(encoding="utf-8")
    tree = ast.parse(source, filename=str(SOURCE))
    classes = {node.name for node in tree.body if isinstance(node, ast.ClassDef)}
    missing = set(SCENES) - classes
    assert not missing, f"Missing Part XI scenes: {sorted(missing)}"
    assert source.count("self.cc(") >= len(SCENES)

    A = [[0, -1], [3, 0]]
    U = [[0, -1], [1, 0]]
    Sigma = [[3, 0], [0, 1]]
    V = [[1, 0], [0, 1]]

    # A^T A and singular values.
    At = [[A[j][i] for j in range(2)] for i in range(2)]
    AtA = mm(At, A)
    assert AtA == [[9, 0], [0, 1]]
    assert math.isclose(math.sqrt(9), 3.0)
    assert math.isclose(math.sqrt(1), 1.0)

    # Right singular vectors.
    assert mv(AtA, [1, 0]) == [9, 0]
    assert mv(AtA, [0, 1]) == [0, 1]

    # Left singular vectors.
    assert mv(A, [1, 0]) == [0, 3]
    assert mv(A, [0, 1]) == [-1, 0]

    # Orthonormal U and V.
    UtU = mm([[U[j][i] for j in range(2)] for i in range(2)], U)
    VtV = mm([[V[j][i] for j in range(2)] for i in range(2)], V)
    assert UtU == [[1, 0], [0, 1]]
    assert VtV == [[1, 0], [0, 1]]

    # Exact SVD reconstruction.
    reconstructed = mm(mm(U, Sigma), [[V[j][i] for j in range(2)] for i in range(2)])
    assert reconstructed == A

    # Pseudoinverse.
    Sigma_plus = [[1 / 3, 0], [0, 1]]
    A_plus = mm(mm(V, Sigma_plus), [[U[j][i] for j in range(2)] for i in range(2)])
    assert A_plus == [[0, 1 / 3], [-1, 0]]
    assert mm(A, A_plus) == [[1, 0], [0, 1]]
    assert mm(A_plus, A) == [[1, 0], [0, 1]]

    # Rank-one approximation and spectral-norm error.
    A1 = [[0, 0], [3, 0]]
    residual = [[A[i][j] - A1[i][j] for j in range(2)] for i in range(2)]
    assert A1 == [[3 * U[i][0] * V[j][0] for j in range(2)] for i in range(2)]
    assert residual == [[0, -1], [0, 0]]
    assert "\\|A-A_1\\|_2=\\sigma_2=1" in source

    # Required conceptual statements.
    required = [
        r"\boxed{A=U\Sigma V^T}",
        r"\sigma_i=\sqrt{\lambda_i}",
        r"\operatorname{rank}(A)=\#\{\sigma_i>0\}",
        r"A^+=V\Sigma^+U^T",
        r"A_1=\sigma_1u_1v_1^T",
    ]
    for item in required:
        assert item in source, item

    renderer = (ROOT / "render_part11.py").read_text(encoding="utf-8")
    assert 'SCRIPT = "parts/part_11_svd_final.py"' in renderer
    for scene in SCENES:
        assert scene in renderer

    print(f"PASS Part XI: {len(SCENES)} scenes, A^T A, singular values/vectors, exact SVD reconstruction, pseudoinverse, rank-one approximation, and canonical renderer verified")


if __name__ == "__main__":
    main()
