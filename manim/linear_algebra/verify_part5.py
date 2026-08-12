from math import isclose, sqrt
from pathlib import Path
import ast

ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "parts/part_05_geometry_final.py"
SCENES = [
    "Part5_01_DotProductComputation",
    "Part5_02_DotProductGeometry",
    "Part5_03_NormAndVectorLength",
    "Part5_04_DistanceBetweenPoints",
    "Part5_05_AngleAndCauchySchwarz",
    "Part5_06_Orthogonality",
    "Part5_07_Projection",
    "Part5_08_OrthogonalDecomposition",
    "Part5_09_OrthogonalComplements",
    "Part5_10_GramSchmidt",
    "Part5_11_GeometryMastery",
]

REQUIRED = [
    "DotProductComputation",
    "DotProductGeometry",
    "NormAndVectorLength",
    "DistanceBetweenPoints",
    "AngleAndCauchySchwarz",
    "Orthogonality",
    "Projection",
    "OrthogonalDecomposition",
    "OrthogonalComplements",
    "GramSchmidt",
    "self.cc(",
]


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def norm(v):
    return sqrt(dot(v, v))


def main():
    source = SOURCE.read_text(encoding="utf-8")
    tree = ast.parse(source, filename=str(SOURCE))
    classes = {node.name for node in tree.body if isinstance(node, ast.ClassDef)}
    missing = set(SCENES) - classes
    assert not missing, f"Missing Part V scenes: {sorted(missing)}"
    for token in REQUIRED:
        assert token in source, f"Missing required Part V marker: {token}"

    # Dot product and norm examples.
    u = [3, 1]
    v = [1, 2]
    assert dot(u, v) == 5
    w = [3, 4]
    assert norm(w) == 5

    # Distance example P=(1,1), Q=(4,5).
    displacement = [3, 4]
    assert norm(displacement) == 5

    # 60-degree example: u=(1,0), v=(1,sqrt(3)).
    u_angle = [1, 0]
    v_angle = [1, sqrt(3)]
    assert isclose(dot(u_angle, v_angle), 1.0)
    assert isclose(norm(v_angle), 2.0)
    assert isclose(dot(u_angle, v_angle) / (norm(u_angle) * norm(v_angle)), 0.5)

    # Orthogonality example.
    ortho_u = [2, 1]
    ortho_v = [1, -2]
    assert dot(ortho_u, ortho_v) == 0

    # Projection b onto a: a=(2,1), b=(3,2).
    a = [2, 1]
    b = [3, 2]
    coefficient = dot(a, b) / dot(a, a)
    projection = [coefficient * x for x in a]
    residual = [b[i] - projection[i] for i in range(2)]
    assert isclose(coefficient, 8 / 5)
    assert all(isclose(x, y) for x, y in zip(projection, [16 / 5, 8 / 5]))
    assert all(isclose(x, y) for x, y in zip(residual, [-1 / 5, 2 / 5]))
    assert isclose(dot(a, residual), 0.0, abs_tol=1e-12)

    # Orthogonal complement example.
    s = [2, 1]
    s_perp = [1, -2]
    assert dot(s, s_perp) == 0

    # Gram-Schmidt example.
    u1 = [1, 1]
    u2 = [1, 0]
    v1 = u1
    proj = [0.5, 0.5]
    v2 = [u2[i] - proj[i] for i in range(2)]
    assert v2 == [0.5, -0.5]
    assert isclose(dot(v1, v2), 0.0, abs_tol=1e-12)
    q1 = [x / norm(v1) for x in v1]
    q2 = [x / norm(v2) for x in v2]
    assert isclose(norm(q1), 1.0)
    assert isclose(norm(q2), 1.0)
    assert isclose(dot(q1, q2), 0.0, abs_tol=1e-12)
    assert r"Q=\begin{bmatrix}\vec q_1&\vec q_2\end{bmatrix},\qquad Q^TQ=I" in source

    renderer = (ROOT / "render_part5.py").read_text(encoding="utf-8")
    assert 'SCRIPT = "parts/part_05_geometry_final.py"' in renderer
    for scene in SCENES:
        assert scene in renderer, f"Renderer missing {scene}"

    assert not (ROOT / "parts/part_05_geometry.py").exists()
    assert "1.732" not in source

    print(f"PASS Part V: {len(SCENES)} scenes, syntax, CC coverage, exact geometry checks, canonical renderer, and single-source layout verified")


if __name__ == "__main__":
    main()
