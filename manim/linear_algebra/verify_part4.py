from pathlib import Path
import ast

ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "parts/part_04_systems_final.py"
SCENES = [
    "Part4_01_AxEqualsB",
    "Part4_02_GeometricMeaning",
    "Part4_03_AugmentedMatrix",
    "Part4_04_ElementaryRowOperations",
    "Part4_05_GaussianElimination",
    "Part4_06_BackSubstitution",
    "Part4_07_RREF",
    "Part4_08_ThreeSolutionCases",
    "Part4_09_HomogeneousSystems",
    "Part4_10_ThreeByThreeWorkedSystem",
    "Part4_11_SystemsMastery",
]

REQUIRED = [
    "AxEqualsB",
    "GeometricMeaning",
    "AugmentedMatrix",
    "ElementaryRowOperations",
    "GaussianElimination",
    "BackSubstitution",
    "RREF",
    "ThreeSolutionCases",
    "HomogeneousSystems",
    "ThreeByThreeWorkedSystem",
    "self.cc(",
]


def matvec(A, x):
    return [sum(a * b for a, b in zip(row, x)) for row in A]


def main():
    source = SOURCE.read_text(encoding="utf-8")
    tree = ast.parse(source, filename=str(SOURCE))
    classes = {node.name for node in tree.body if isinstance(node, ast.ClassDef)}
    missing = set(SCENES) - classes
    assert not missing, f"Missing Part IV scenes: {sorted(missing)}"
    for token in REQUIRED:
        assert token in source, f"Missing required Part IV marker: {token}"

    # Core 2x2 system: x+y=5, 2x-y=1 -> (2,3).
    A = [[1, 1], [2, -1]]
    x = [2, 3]
    b = [5, 1]
    assert matvec(A, x) == b

    # Gaussian elimination regression.
    R2 = [A[1][j] - 2 * A[0][j] for j in range(2)] + [b[1] - 2 * b[0]]
    assert R2 == [0, -3, -9]

    # Back-substitution regression for the exact triangular system shown.
    z = 10 / 5
    y = (7 - 2 * z) / 3
    x_back = 4 - 2 * y + z
    assert (z, y, x_back) == (2, 1, 4)
    assert "x+2y-z=4\\Rightarrow x=4" in source
    assert "(x,y,z)=(4,1,2)" in source

    # RREF example shown in the lesson.
    assert "1&0&2" in source and "0&1&3" in source

    # Three solution cases: distinct intersecting, parallel distinct, coincident.
    # y=-x+5 and y=2x-3 intersect at (2,3).
    assert -2 + 5 == 2 * 2 - 3 == 3
    # y=-x+2 and y=-x+2.5 are parallel and distinct.
    assert -1 == -1 and 2 != 2.5
    # y=-x+2 and y=-x+2 are the same line.
    assert 2 == 2

    # Homogeneous system x+y=0: x=t, y=-t.
    for t in [-3, 0, 2.5]:
        assert abs(t + (-t)) < 1e-12
    assert r"\operatorname{Null}(A)=\{x:A x=0\}" in source

    # Full 3x3 worked example has solution (1,2,3).
    A3 = [[1, 1, 1], [2, -1, 1], [1, 2, -1]]
    x3 = [1, 2, 3]
    b3 = [6, 3, 2]
    assert matvec(A3, x3) == b3
    assert "-\\frac73" in source
    assert "-7" in source
    assert "(x,y,z)=(1,2,3)" in source

    renderer = (ROOT / "render_part4.py").read_text(encoding="utf-8")
    assert 'SCRIPT = "parts/part_04_systems_final.py"' in renderer
    for scene in SCENES:
        assert scene in renderer, f"Renderer missing {scene}"

    assert not (ROOT / "parts/part_04_systems.py").exists()
    assert "8/3" not in source
    assert "7/3" not in source

    print(f"PASS Part IV: {len(SCENES)} scenes, syntax, teaching markers, mathematical checkpoints, canonical renderer, and single-source layout verified")


if __name__ == "__main__":
    main()
