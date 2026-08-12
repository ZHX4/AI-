from pathlib import Path
import ast
from math import isclose

ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "parts/part_07_fundamental_subspaces_canonical.py"
SCENES = [
    "Part7_01_RankIntuition",
    "Part7_02_ColumnSpace",
    "Part7_03_RowSpace",
    "Part7_04_NullSpace",
    "Part7_05_LeftNullSpace",
    "Part7_06_FourFundamentalSubspaces",
    "Part7_07_RankPivotsAndIndependentDirections",
    "Part7_08_RankNullity",
    "Part7_09_OrthogonalityPairs",
    "Part7_10_DimensionsAndStructure",
    "Part7_11_FundamentalSubspacesMastery",
]

A = [[1, 2, 3], [0, 1, 1], [1, 3, 4]]
NULL = [-1, -1, 1]
LEFT_NULL = [-1, -1, 1]
ROWS = [[1, 2, 3], [0, 1, 1], [1, 3, 4]]
COLS = [[1, 0, 1], [2, 1, 3], [3, 1, 4]]


def mat_vec(M, v):
    return [sum(M[i][j] * v[j] for j in range(len(v))) for i in range(len(M))]


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def rank_3x3(M):
    a = [row[:] for row in M]
    rank = 0
    for col in range(3):
        pivot = next((r for r in range(rank, 3) if a[r][col] != 0), None)
        if pivot is None:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        p = a[rank][col]
        a[rank] = [x / p for x in a[rank]]
        for r in range(3):
            if r != rank and a[r][col] != 0:
                f = a[r][col]
                a[r] = [a[r][j] - f * a[rank][j] for j in range(3)]
        rank += 1
    return rank


def main():
    source = SOURCE.read_text(encoding="utf-8")
    tree = ast.parse(source, filename=str(SOURCE))
    classes = {node.name for node in tree.body if isinstance(node, ast.ClassDef)}
    missing = set(SCENES) - classes
    assert not missing, f"Missing Part VII scenes: {sorted(missing)}"
    assert source.count("self.cc(") >= len(SCENES)

    # Structural facts for the canonical matrix.
    assert rank_3x3(A) == 2
    assert ROWS[2] == [ROWS[0][j] + ROWS[1][j] for j in range(3)]
    assert COLS[2] == [COLS[0][j] + COLS[1][j] for j in range(3)]

    # Null-space vector: A * NULL = 0.
    assert mat_vec(A, NULL) == [0, 0, 0]
    assert NULL != [0, 0, 0]

    # Left-null vector: A^T * LEFT_NULL = 0, equivalently y dot each column = 0.
    assert all(dot(LEFT_NULL, c) == 0 for c in COLS)

    # Null vector is orthogonal to every row.
    assert all(dot(r, NULL) == 0 for r in ROWS)

    # Rank-nullity for a 3-column matrix.
    assert rank_3x3(A) + 1 == 3

    # Expected RREF and pivot structure for this matrix.
    expected_rref = [[1, 0, 1], [0, 1, 1], [0, 0, 0]]
    assert r"\operatorname{RREF}(A)=\begin{bmatrix}1&0&1\\0&1&1\\0&0&0\end{bmatrix}" in source
    assert "pivot columns=1,2" in source

    # Dimension formulas for an m x n rank-r matrix.
    assert "dim\\operatorname{Col}(A)=r" in source
    assert "dim\\operatorname{Null}(A)=n-r" in source
    assert "dim\\operatorname{Row}(A)=r" in source
    assert "dim\\operatorname{Null}(A^T)=m-r" in source

    # Canonical renderer wiring.
    renderer = (ROOT / "render_part7.py").read_text(encoding="utf-8")
    assert 'SCRIPT = "parts/part_07_fundamental_subspaces_canonical.py"' in renderer
    for scene in SCENES:
        assert scene in renderer

    print(
        f"PASS Part VII: {len(SCENES)} scenes, syntax structure, CC coverage, rank/space arithmetic, "
        "null and left-null checks, orthogonality checks, rank-nullity, RREF/pivot structure, and canonical renderer verified"
    )


if __name__ == "__main__":
    main()
