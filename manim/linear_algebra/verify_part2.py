from pathlib import Path
import ast

ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "parts/part_02_vector_spaces.py"
SCENES = [
    "Part2_01_Span", "Part2_02_LinearDependence", "Part2_03_LinearIndependence",
    "Part2_04_Basis", "Part2_05_Dimension", "Part2_06_CoordinatesInANonstandardBasis",
    "Part2_07_Subspaces", "Part2_08_ColumnSpace", "Part2_09_RowSpaceAndNullSpace",
    "Part2_10_RankNullity", "Part2_11_FourFundamentalSubspaces",
]

REQUIRED = ["span", "independent", "basis", "dimension", "subspace", "column", "row", "null", "rank", "nullity", "self.cc("]


def main() -> None:
    source = SOURCE.read_text(encoding="utf-8")
    tree = ast.parse(source, filename=str(SOURCE))
    classes = {node.name for node in tree.body if isinstance(node, ast.ClassDef)}
    missing = set(SCENES) - classes
    assert not missing, f"Missing Part II scenes: {sorted(missing)}"
    assert len(classes.intersection(SCENES)) == len(SCENES)
    for token in REQUIRED:
        assert token in source, f"Missing required teaching marker: {token!r}"

    # Regression checks for known failure modes and the concrete mathematics.
    assert "(3, 5)" not in source
    assert r"\vec w=2\vec u+\vec v=\begin{bmatrix}3\\4\end{bmatrix}" in source
    assert "arrow_from(ax, (1,2), VECTOR_B" in source
    assert r"\operatorname{Row}(A)=\operatorname{span}\left\{\begin{bmatrix}1\\2\end{bmatrix}\right\}" in source
    assert r"\operatorname{Null}(A)=\operatorname{span}\left\{\begin{bmatrix}-2\\1\end{bmatrix}\right\}" in source
    assert r"\operatorname{Null}(A^T)=\operatorname{span}\left\{\begin{bmatrix}0\\1\end{bmatrix}\right\}" in source
    assert r"\begin{bmatrix}1&2\end{bmatrix}\begin{bmatrix}-2\\1\end{bmatrix}=0" in source
    assert r"\begin{bmatrix}1\\0\end{bmatrix}\cdot\begin{bmatrix}0\\1\end{bmatrix}=0" in source
    assert r"\operatorname{rank}(A)=1" in source
    assert r"\operatorname{nullity}(A)=1" in source
    assert r"\operatorname{rank}(A)+\operatorname{nullity}(A)=2" in source

    renderer = (ROOT / "render_part2.py").read_text(encoding="utf-8")
    assert 'SCRIPT = "parts/part_02_vector_spaces.py"' in renderer
    for scene in SCENES:
        assert scene in renderer, f"Renderer missing {scene}"

    assert not (ROOT / "parts/part_02_vector_spaces_corrected.py").exists()
    assert not (ROOT / "parts/part_02_four_fundamental_subspaces.py").exists()

    print(f"PASS: {len(SCENES)} Part II scenes, syntax, teaching markers, numerical checkpoints, canonical renderer, and single-source layout verified.")


if __name__ == "__main__":
    main()
