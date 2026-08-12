from pathlib import Path
from math import isclose
import ast

ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "parts/part_06_determinants_canonical.py"
SCENES = [
    "Part6_01_WhatDeterminantMeasures",
    "Part6_02_TwoByTwoSignedArea",
    "Part6_03_DeterminantAsAreaScale",
    "Part6_04_ThreeByThreeVolume",
    "Part6_05_OrientationAndSign",
    "Part6_06_DeterminantProperties",
    "Part6_07_RowOperationsAndDeterminant",
    "Part6_08_CofactorExpansion",
    "Part6_09_DeterminantAndInvertibility",
    "Part6_10_DeterminantAndProducts",
    "Part6_11_DeterminantMastery",
]


def det2(a, b, c, d):
    return a * d - b * c


def det3(A):
    return (
        A[0][0] * (A[1][1] * A[2][2] - A[1][2] * A[2][1])
        - A[0][1] * (A[1][0] * A[2][2] - A[1][2] * A[2][0])
        + A[0][2] * (A[1][0] * A[2][1] - A[1][1] * A[2][0])
    )


def matmul(A, B):
    return [
        [sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))]
        for i in range(len(A))
    ]


def main():
    source = SOURCE.read_text(encoding="utf-8")
    tree = ast.parse(source, filename=str(SOURCE))
    classes = {node.name for node in tree.body if isinstance(node, ast.ClassDef)}
    assert not (set(SCENES) - classes)
    for scene in SCENES:
        assert scene in source
    assert source.count("self.cc(") >= 11

    assert det2(2, 1, 1, 2) == 3
    assert det2(1, 0, 0, -2) == -2

    A3 = [[1, 2, 0], [0, 1, 3], [2, 0, 1]]
    assert det3(A3) == 13

    C = [[1, 2, 3], [0, 1, 4], [5, 6, 0]]
    assert det3(C) == 1

    S = [[1, 2], [2, 4]]
    assert det2(S[0][0], S[0][1], S[1][0], S[1][1]) == 0

    P = [[2, 0], [0, 3]]
    Q = [[1, 1], [0, 2]]
    PQ = matmul(P, Q)
    assert PQ == [[2, 2], [0, 6]]
    assert det2(2, 2, 0, 6) == 12
    assert det2(2, 0, 0, 3) * det2(1, 1, 0, 2) == 12

    # The actual 3D animation example is D = [[1,1,0],[0,2,0],[0,0,1]], det(D)=2.
    D = [[1, 1, 0], [0, 2, 0], [0, 0, 1]]
    assert det3(D) == 2

    for identity in [
        r"\det(AB)=\det(A)\det(B)",
        r"\det(cA)=c^n\det(A)",
        r"\det(A^T)=\det(A)",
        r"\det(A^{-1})=\frac{1}{\det(A)}",
        r"R_i\leftrightarrow R_j",
        r"R_i\leftarrow cR_i",
        r"R_i\leftarrow R_i+cR_j",
    ]:
        assert identity in source, identity

    assert "\"\det(D)=2\\\\Rightarrow\\\\text{volume doubles}\"" in source
    assert r"\boxed{\operatorname{volume}=|\det(A)|=13}" not in source
    assert r"\boxed{\text{volume scale}=|\det(A)|=13}" in source
    assert r"\boxed{\text{area}=|\det(A)|=3}" in source
    assert r"\boxed{\det(A)=1}" in source
    assert r"\det(A)=0\iff A\text{ is singular}\iff A^{-1}\text{ does not exist}" in source

    renderer = (ROOT / "render_part6.py").read_text(encoding="utf-8")
    assert 'SCRIPT = "parts/part_06_determinants_canonical.py"' in renderer
    for scene in SCENES:
        assert scene in renderer

    assert not (ROOT / "parts/part_06_determinants_final.py").exists()
    assert not (ROOT / "parts/part_06_determinants.py").exists()

    print(f"PASS Part VI: {len(SCENES)} scenes, syntax structure, exact determinant arithmetic, 3D determinant animation check, canonical renderer, and single-source layout verified")


if __name__ == "__main__":
    main()
