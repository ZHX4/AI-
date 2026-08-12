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


def matmul(A, B):
    rows, inner, cols = len(A), len(B), len(B[0])
    assert len(A[0]) == inner
    return [
        [sum(A[i][k] * B[k][j] for k in range(inner)) for j in range(cols)]
        for i in range(rows)
    ]


def matvec(A, v):
    return [sum(a * x for a, x in zip(row, v)) for row in A]


def main():
    source = SOURCE.read_text(encoding="utf-8")
    tree = ast.parse(source, filename=str(SOURCE))
    classes = {node.name for node in tree.body if isinstance(node, ast.ClassDef)}
    missing = set(SCENES) - classes
    assert not missing, f"Missing Part III scenes: {sorted(missing)}"
    assert len(classes.intersection(SCENES)) == len(SCENES)
    for token in REQUIRED:
        assert token in source, f"Missing required Part III marker: {token}"

    # Geometry regression: the transformation lesson uses matching world and grid units.
    assert "x_range=[-4, 4, 1], y_range=[-3, 3, 1], x_length=8.0, y_length=6.0" in source
    assert "x_length=8.5, y_length=6.3" not in source

    # Numerical regression checks mirror the examples taught by the animations.
    A = [[2, 1], [1, 2]]
    x = [3, 1]
    assert matvec(A, x) == [7, 5]

    C1 = [2, 1]
    C2 = [1, 2]
    assert [3 * C1[0] + C2[0], 3 * C1[1] + C2[1]] == [7, 5]

    A2 = [[1, 2], [0, 1]]
    B2 = [[2, 1], [1, 0]]
    assert matmul(A2, B2) == [[4, 1], [1, 0]]

    A3 = [[1, 1], [0, 1]]
    B3 = [[0, -1], [1, 0]]
    v = [2, 1]
    assert matvec(B3, v) == [-1, 2]
    assert matvec(A3, matvec(B3, v)) == [1, 2]
    assert matvec(B3, matvec(A3, v)) == [-1, 3]

    Inv = [[1, -1], [-1, 2]]
    M = [[2, 1], [1, 1]]
    assert matmul(M, Inv) == [[1, 0], [0, 1]]
    assert matmul(Inv, M) == [[1, 0], [0, 1]]
    assert matvec(Inv, matvec(M, [2, 1])) == [2, 1]

    # Transpose regression.
    T = [[1, 2], [3, 4]]
    assert [list(row) for row in zip(*T)] == [[1, 3], [2, 4]]
    assert [list(row) for row in zip(*zip(*T))] == T

    renderer = (ROOT / "render_part3.py").read_text(encoding="utf-8")
    assert 'SCRIPT = "parts/part_03_matrices_final.py"' in renderer
    for scene in SCENES:
        assert scene in renderer, f"Renderer missing {scene}"

    # No duplicate Part III implementation should exist.
    part_files = [p.name for p in (ROOT / "parts").glob("part_03_*.py")]
    assert part_files == ["part_03_matrices_final.py"], f"Unexpected Part III sources: {part_files}"

    print(f"PASS Part III: {len(SCENES)} scenes, syntax, teaching markers, geometry regression, numerical checkpoints, canonical renderer, and single-source layout verified")


if __name__ == "__main__":
    main()
