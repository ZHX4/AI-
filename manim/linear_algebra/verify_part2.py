from pathlib import Path
import ast

ROOT = Path(__file__).resolve().parent
FILES = {
    "parts/part_02_vector_spaces.py": [
        "Part2_01_Span", "Part2_02_LinearDependence", "Part2_03_LinearIndependence",
        "Part2_04_Basis", "Part2_05_Dimension", "Part2_06_CoordinatesInANonstandardBasis",
        "Part2_07_Subspaces", "Part2_08_ColumnSpace", "Part2_09_RowSpaceAndNullSpace",
        "Part2_10_RankNullityAndFourSpaces",
    ],
    "parts/part_02_four_fundamental_subspaces.py": ["Part2_11_FourFundamentalSubspaces"],
}

REQUIRED_TEXT = {
    "parts/part_02_vector_spaces.py": [
        "span", "independent", "basis", "dimension", "subspace",
        "column", "row", "null", "rank", "nullity", "rank-nullity",
        "self.cc(", "\n        self.wait(2)",
    ],
    "parts/part_02_four_fundamental_subspaces.py": [
        "Col(A)", "Row(A)", "Null(A)", "Null(A^T)",
        "self.cc(", "\n        self.wait(3)",
    ],
}


def main() -> None:
    total = 0
    for relative, expected_classes in FILES.items():
        path = ROOT / relative
        source = path.read_text(encoding="utf-8")
        ast.parse(source, filename=str(path))
        for token in REQUIRED_TEXT[relative]:
            assert token in source, f"Missing required teaching marker {token!r} in {relative}"
        tree = ast.parse(source)
        classes = {n.name for n in tree.body if isinstance(n, ast.ClassDef)}
        missing = set(expected_classes) - classes
        assert not missing, f"Missing Part II scenes: {sorted(missing)}"
        total += len(expected_classes)
        print(f"PASS {relative}: {len(expected_classes)} scene classes, syntax and teaching markers verified")

    renderer = (ROOT / "render_part2.py").read_text(encoding="utf-8")
    for scene in [name for names in FILES.values() for name in names]:
        assert scene in renderer, f"Renderer missing {scene}"
    assert "Part2_11_FourFundamentalSubspaces" in renderer
    print(f"PASS render_part2.py: all {total} Part II scenes are registered")

    source = (ROOT / "parts/part_02_vector_spaces.py").read_text(encoding="utf-8")
    assert "(3, 5)" not in source
    assert "(1, 8)" not in source
    assert "2\\begin{bmatrix}2\\\\0.5\\end{bmatrix}+3\\begin{bmatrix}-1\\\\0.5\\end{bmatrix}=\\begin{bmatrix}1\\\\2.5\\end{bmatrix}" in source
    print("PASS Part II numerical checkpoint: linear-combination example is bounded and consistent")

    print("Part II source verification completed successfully.")


if __name__ == "__main__":
    main()
