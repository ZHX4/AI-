from pathlib import Path
import ast

ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "parts/part_08_eigenvalues_canonical.py"
SCENES = [
    "Part8_01_EigenvectorIntuition",
    "Part8_02_EigenEquation",
    "Part8_03_CharacteristicPolynomial",
    "Part8_04_FindingEigenvectors",
    "Part8_05_GeometricEigenspaces",
    "Part8_06_AlgebraicVsGeometricMultiplicity",
    "Part8_07_Diagonalization",
    "Part8_08_MatrixPowers",
    "Part8_09_DynamicsAndEigenDirections",
    "Part8_10_EigenvaluesBeyond2D",
    "Part8_11_EigenvalueMastery",
]


def matmul(A, B):
    return [
        [sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))]
        for i in range(len(A))
    ]


def matvec(A, v):
    return [sum(A[i][j] * v[j] for j in range(len(v))) for i in range(len(A))]


def matrix_power(A, n):
    out = [[1 if i == j else 0 for j in range(len(A))] for i in range(len(A))]
    for _ in range(n):
        out = matmul(out, A)
    return out


def main():
    source = SOURCE.read_text(encoding="utf-8")
    tree = ast.parse(source, filename=str(SOURCE))
    classes = {node.name for node in tree.body if isinstance(node, ast.ClassDef)}
    missing = set(SCENES) - classes
    assert not missing, f"Missing Part VIII scenes: {sorted(missing)}"
    assert source.count("self.cc(") >= len(SCENES)

    A = [[3, 1], [0, 2]]
    v3 = [1, 0]
    v2 = [1, -1]
    assert matvec(A, v3) == [3, 0]
    assert matvec(A, v2) == [2, -2]

    # Characteristic polynomial: lambda^2 - 5 lambda + 6.
    assert "\\lambda^2-5\\lambda+6" in source
    assert "(\\lambda-3)(\\lambda-2)" in source

    # Eigenspaces for lambda=3 and lambda=2.
    assert "E_{3}=\\operatorname{span}" in source
    assert "E_{2}=\\operatorname{span}" in source

    # Multiplicity examples: diagonal matrix has two independent eigenvectors;
    # Jordan block has only one-dimensional eigenspace.
    assert "m_a(2)=2,\\qquad m_g(2)=2" in source
    assert "m_a(2)=2,\\quad m_g(2)=1" in source

    # Diagonalization identity A = P D P^{-1} for the canonical example.
    P = [[1, 1], [0, -1]]
    D = [[3, 0], [0, 2]]
    P_inv = [[1, 1], [0, -1]]  # P^2 = I
    assert matmul(matmul(P, D), P_inv) == A

    # Matrix powers for the canonical example.
    assert matrix_power(A, 2) == [[9, 5], [0, 4]]
    assert matrix_power(A, 3) == [[27, 19], [0, 8]]
    assert "3^k" in source and "2^k" in source

    # 3D diagonal example.
    D3 = [[4, 0, 0], [0, 2, 0], [0, 0, 1]]
    assert matvec(D3, [1, 0, 0]) == [4, 0, 0]
    assert matvec(D3, [0, 1, 0]) == [0, 2, 0]
    assert matvec(D3, [0, 0, 1]) == [0, 0, 1]

    renderer = (ROOT / "render_part8.py").read_text(encoding="utf-8")
    assert 'SCRIPT = "parts/part_08_eigenvalues_canonical.py"' in renderer
    for scene in SCENES:
        assert scene in renderer

    print(
        f"PASS Part VIII: {len(SCENES)} scenes, CC coverage, eigenvector arithmetic, characteristic polynomial, "
        "multiplicity cases, diagonalization, matrix powers, 3D eigen-directions, and canonical renderer verified"
    )


if __name__ == "__main__":
    main()
