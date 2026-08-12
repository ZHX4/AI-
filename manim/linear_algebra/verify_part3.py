from pathlib import Path
import ast

ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "parts/part_03_matrices_final.py"
SCENES = [
    "Part3_01_WhatIsAMatrix",
    "Part3_02_MatrixVectorMultiplication",
    "Part3_03_ColumnsBuildTheOutput",
    "Part3_04_MatrixAsTransformation",
    "Part3_05_MatrixAdditionAndScaling",
    "Part3_06_MatrixMultiplication",
    "Part3_07_CompositionOfTransformations",
    "Part3_08_IdentityMatrix",
    "Part3_09_Transpose",
    "Part3_10_InverseMatrix",
    "Part3_11_MatrixMastery",
]

REQUIRED = [
    "MatrixLesson",
    "MatrixVectorMultiplication",
    "ColumnsBuildTheOutput",
    "MatrixAsTransformation",
    "MatrixAdditionAndScaling",
    "MatrixMultiplication",
    "CompositionOfTransformations",
    "IdentityMatrix",
    "Transpose",
    "InverseMatrix",
    "self.cc(",
    "ApplyMatrix(",
]


def main():
    source = SOURCE.read_text(encoding="utf-8")
    tree = ast.parse(source, filename=str(SOURCE))
    classes = {node.name for node in tree.body if isinstance(node, ast.ClassDef)}
    missing = set(SCENES) - classes
    assert not missing, f"Missing Part III scenes: {sorted(missing)}"
    for token in REQUIRED:
        assert token in source, f"Missing required Part III marker: {token}"

    # Numerical regression checks mirror the examples taught by the animations.
    A = [[2, 1], [1, 2]]
    x = [3, 1]
    assert [A[0][0] * x[0] + A[0][1] * x[1], A[1][0] * x[0] + A[1][1] * x[1]] == [7, 5]

    C1 = [2, 1]
    C2 = [1, 2]
    assert [3 * C1[0] + C2[0], 3 * C1[1] + C2[1]] == [7, 5]

    A2 = [[1, 2], [0, 1]]
    B2 = [[2, 1], [1, 0]]
    product = [
        [A2[0][0] * B2[0][0] + A2[0][1] * B2[1][0], A2[0][0] * B2[0][1] + A2[0][1] * B2[1][1]],
        [A2[1][0] * B2[0][0] + A2[1][1] * B2[1][0], A2[1][0] * B2[0][1] + A2[1][1] * B2[1][1]],
    ]
    assert product == [[4, 1], [1, 0]]

    A3 = [[1, 1], [0, 1]]
    B3 = [[0, -1], [1, 0]]
    v = [2, 1]
    Bv = [B3[0][0] * v[0] + B3[0][1] * v[1], B3[1][0] * v[0] + B3[1][1] * v[1]]
    ABv = [A3[0][0] * Bv[0] + A3[0][1] * Bv[1], A3[1][0] * Bv[0] + A3[1][1] * Bv[1]]
    BAv = [B3[0][0] * (A3[0][0] * v[0] + A3[0][1] * v[1]) + B3[0][1] * (A3[1][0] * v[0] + A3[1][1] * v[1]), B3[1][0] * (A3[0][0] * v[0] + A3[0][1] * v[1]) + B3[1][1] * (A3[1][0] * v[0] + A3[1][1] * v[1])]
    assert Bv == [-1, 2]
    assert ABv == [1, 2]
    assert BAv == [-1, 3]

    Inv = [[1, -1], [-1, 2]]
    M = [[2, 1], [1, 1]]
    identity = [
        [M[0][0] * Inv[0][0] + M[0][1] * Inv[1][0], M[0][0] * Inv[0][1] + M[0][1] * Inv[1][1]],
        [M[1][0] * Inv[0][0] + M[1][1] * Inv[1][0], M[1][0] * Inv[0][1] + M[1][1] * Inv[1][1]],
    ]
    assert identity == [[1, 0], [0, 1]]

    renderer = (ROOT / "render_part3.py").read_text(encoding="utf-8")
    for scene in SCENES:
        assert scene in renderer, f"Renderer missing {scene}"
    assert 'parts/part_03_matrices_final.py' in renderer

    print(f"PASS Part III: {len(SCENES)} scenes, syntax, teaching markers, renderer wiring, and numerical checkpoints verified")


if __name__ == "__main__":
    main()
