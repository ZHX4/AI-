from pathlib import Path
import ast
from math import isclose

ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "parts/part_06_determinants_final.py"
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
REQUIRED = [
    "TwoByTwoSignedArea", "DeterminantAsAreaScale", "ThreeByThreeVolume",
    "OrientationAndSign", "DeterminantProperties", "RowOperationsAndDeterminant",
    "CofactorExpansion", "DeterminantAndInvertibility", "DeterminantAndProducts",
    "self.cc(",
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
    classes = {n.name for n in tree.body if isinstance(n, ast.ClassDef)}
    missing = set(SCENES) - classes
    assert not missing, f"Missing Part VI scenes: {sorted(missing)}"
    for token in REQUIRED:
        assert token in source, f"Missing Part VI marker: {token}"

    # 2x2 signed area.
    assert det2(2, 1, 1, 2) == 3

    # Orientation example.
    assert det2(1, 0, 0, -2) == -2

    # 3x3 volume example.
    A3 = [[1, 2, 0], [0, 1, 3], [2, 0, 1]]
    assert det3(A3) == 13

    # Cofactor example.
    C = [[1, 2, 3], [0, 1, 4], [5, 6, 0]]
    assert det3(C) == 1
    assert "1(-24)-2(-20)+3(-5)" in source

    # Singular/invertibility example.
    S = [[1, 2], [2, 4]]
    assert det2(*[S[0][0], S[0][1], S[1][0], S[1][1]]) == 0
    assert "det(A)=0\\\\iff A" in source or "det(A)=0\\iff A" in source

    # Product property example.
    A = [[2, 0], [0, 3]]
    B = [[1, 1], [0, 2]]
    AB = matmul(A, B)
    assert AB == [[2, 2], [0, 6]]
    assert det2(2, 2, 0, 6) == 12
    assert det2(2, 0, 0, 3) * det2(1, 1, 0, 2) == 12

    # Determinant identities represented in the lesson.
    assert "\\det(AB)=\\det(A)\\det(B)" in source
    assert "\\det(A^T)=\\det(A)" in source
    assert "\\det(A^{-1})=\\frac1{\\det(A)}" in source
    assert "\\det(2A)=2^n\\det(A)" in source

    # Row-operation rules are explicitly present.
    assert "R_i\\leftrightarrow R_j" in source
    assert "R_i\\leftarrow cR_i" in source
    assert "R_i\\leftarrow R_i+cR_j" in source

    # Canonical renderer and single-source layout.
    renderer = (ROOT / "render_part6.py").read_text(encoding="utf-8")
    assert 'SCRIPT = "parts/part_06_determinants_final.py"' in renderer
    for scene in SCENES:
        assert scene in renderer, f"Renderer missing {scene}"
    assert not (ROOT / "parts/part_06_determinants.py").exists()

    # Ensure exact teaching examples are present.
    assert "\\boxed{\\operatorname{area}=|\\det(A)|=3}" in source
    assert "\\boxed{\\operatorname{volume}=|\\det(A)|=13}" in source
    assert "\\boxed{\\det(A)=1}" in source
    assert "\\boxed{\\det(A)=0\\iff A" in source or "\\boxed{\\det(A)=0\\iff A" in source

    print(
        f"PASS Part VI: {len(SCENES)} scenes, syntax, CC coverage, determinant arithmetic, "+
        "geometric examples, algebraic identities, canonical renderer, and single-source layout verified"
    )


if __name__ == "__main__":
    main()
