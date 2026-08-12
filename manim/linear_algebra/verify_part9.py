from pathlib import Path
import ast

ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "parts/part_09_symmetric_matrices_final.py"
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


def matmul(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]


def main():
    source = SOURCE.read_text(encoding="utf-8")
    tree = ast.parse(source, filename=str(SOURCE))
    classes = {node.name for node in tree.body if isinstance(node, ast.ClassDef)}
    missing = set(SCENES) - classes
    assert not missing, f"Missing Part IX scenes: {sorted(missing)}"
    assert source.count("self.cc(") >= len(SCENES)

    A = [[3, 1], [1, 3]]
    assert A == [list(row) for row in zip(*A)]

    # Exact eigenpairs.
    assert [A[0][0] + A[0][1], A[1][0] + A[1][1]] == [4, 4]
    assert [A[0][0] - A[0][1], A[1][0] - A[1][1]] == [2, 2]

    # Orthonormal Q and exact spectral decomposition up to floating-point tolerance.
    inv_sqrt2 = 1 / (2 ** 0.5)
    Q = [[inv_sqrt2, inv_sqrt2], [inv_sqrt2, -inv_sqrt2]]
    Qt = [[Q[j][i] for j in range(2)] for i in range(2)]
    QtQ = matmul(Qt, Q)
    assert all(abs(QtQ[i][j] - (1 if i == j else 0)) < 1e-12 for i in range(2) for j in range(2))
    Lambda = [[4, 0], [0, 2]]
    reconstructed = matmul(matmul(Q, Lambda), Qt)
    assert all(abs(reconstructed[i][j] - A[i][j]) < 1e-12 for i in range(2) for j in range(2))

    # Quadratic form and principal-axis form.
    assert "3x^2+2xy+3y^2" in source
    assert "4u^2+2v^2" in source
    assert "full axis lengths}=1," in source
    assert "R(x)=\\frac{x^TAx}{x^Tx}" in source

    # Rayleigh quotient bounds for this symmetric matrix.
    assert "2\\le R(x)\\le4" in source
    assert "R(q_1)=4" in source and "R(q_2)=2" in source

    # Definiteness examples.
    assert "A\\succ0\\iff\\lambda_i>0" in source
    assert "negative definite\\iff\\lambda_i<0" in source
    assert "indefinite\\iff\\text{eigenvalues have mixed signs}" in source
    assert "PSD\\iff\\lambda_i\\ge0" in source
    assert "NSD\\iff\\lambda_i\\le0" in source

    renderer = (ROOT / "render_part9.py").read_text(encoding="utf-8")
    assert 'SCRIPT = "parts/part_09_symmetric_matrices_final.py"' in renderer
    for scene in SCENES:
        assert scene in renderer

    print(f"PASS Part IX: {len(SCENES)} scenes, symmetry/eigenpair checks, orthogonal Q, spectral decomposition, quadratic-form geometry, Rayleigh bounds, definiteness classification, and renderer wiring verified")


if __name__ == "__main__":
    main()
