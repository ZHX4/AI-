from pathlib import Path
import ast

ROOT = Path(__file__).resolve().parent
FILES = {
    "parts/part_02_vector_spaces.py": [
        "Part2_02_LinearDependence", "Part2_03_LinearIndependence",
        "Part2_04_Basis", "Part2_05_Dimension", "Part2_06_CoordinatesInANonstandardBasis",
        "Part2_07_Subspaces", "Part2_08_ColumnSpace", "Part2_09_RowSpaceAndNullSpace",
        "Part2_10_RankNullityAndFourSpaces",
    ],
    "parts/part_02_vector_spaces_corrected.py": [
        "Part2_01_Span", "Part2_11_FourFundamentalSubspaces",
    ],
}

REQUIRED_TEXT = {
    "parts/part_02_vector_spaces.py": [
        "span", "independent", "basis", "dimension", "subspace", "column", "row", "null", "rank", "nullity", "self.cc("
    ],
    "parts/part_02_vector_spaces_corrected.py": [
        "Part II.1", "Part II.11", "self.cc(",
        r"\operatorname{Row}(A)\perp\operatorname{Null}(A)",
        r"\operatorname{Col}(A)\perp\operatorname{Null}(A^T)",
        r"\begin{bmatrix}3\\4\end{bmatrix}",
    ],
}


def main() -> None:
    total = 0
    for relative, expected_classes in FILES.items():
        path = ROOT / relative
        source = path.read_text(encoding="utf-8")
        tree = ast.parse(source, filename=str(path))
        for token in REQUIRED_TEXT[relative]:
            assert token in source, f"Missing required teaching marker {token!r} in {relative}"
        classes = {node.name for node in tree.body if isinstance(node, ast.ClassDef)}
        missing = set(expected_classes) - classes
        assert not missing, f"Missing Part II scenes: {sorted(missing)}"
        total += len(expected_classes)
        print(f"PASS {relative}: {len(expected_classes)} scene classes, syntax and teaching markers verified")

    corrected = (ROOT / "parts/part_02_vector_spaces_corrected.py").read_text(encoding="utf-8")
    assert "(3, 5)" not in corrected
    assert r"\vec w=2\vec u+\vec v=\begin{bmatrix}3\\4\end{bmatrix}" in corrected

    renderer = (ROOT / "render_part2.py").read_text(encoding="utf-8")
    for scene in [name for names in FILES.values() for name in names]:
        assert scene in renderer, f"Renderer missing {scene}"
    assert "part_02_vector_spaces_corrected.py" in renderer
    print(f"PASS render_part2.py: all {total} Part II scenes are registered")
    print("PASS Part II numerical/structural checkpoints")
    print("Part II source verification completed successfully.")


if __name__ == "__main__":
    main()
