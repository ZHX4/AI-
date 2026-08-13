from pathlib import Path
import ast

ROOT = Path(__file__).resolve().parent
BASE = ROOT / "parts/part_11_svd_final.py"
CANONICAL = ROOT / "parts/part_11_svd_canonical.py"
SCENES = [
    "Part11_01_SVDIntuition",
    "Part11_02_SingularValuesFromATA",
    "Part11_03_RightSingularVectors",
    "Part11_04_LeftSingularVectors",
    "Part11_05_AssemblingSVD",
    "Part11_06_SphereToEllipse",
    "Part11_07_SingularValuesAndStretching",
    "Part11_08_RankAndZeroSingularValues",
    "Part11_09_Pseudoinverse",
    "Part11_10_LowRankApproximation",
    "Part11_11_SVDMastery",
]


def main():
    base = BASE.read_text(encoding="utf-8")
    canonical = CANONICAL.read_text(encoding="utf-8")
    base_tree = ast.parse(base, filename=str(BASE))
    canonical_tree = ast.parse(canonical, filename=str(CANONICAL))
    base_classes = {node.name for node in base_tree.body if isinstance(node, ast.ClassDef)}
    canonical_classes = {node.name for node in canonical_tree.body if isinstance(node, ast.ClassDef)}
    assert set(SCENES) - base_classes == set()
    assert "Part11_06_SphereToEllipse" in canonical_classes
    assert canonical.count("cos t") >= 1
    assert "3 * np.cos(t)" in canonical
    assert "-np.sin(t)" in canonical

    renderer = (ROOT / "render_part11_canonical.py").read_text(encoding="utf-8")
    assert 'SCRIPT = "parts/part_11_svd_canonical.py"' in renderer
    for scene in SCENES:
        assert scene in renderer

    verify = (ROOT / "verify_part11.py").read_text(encoding="utf-8")
    assert 'SOURCE = ROOT / "parts/part_11_svd_final.py"' in verify

    print(f"PASS Part XI canonical path: {len(SCENES)} scenes, corrected sphere-to-ellipse mapping, renderer and verifier paths verified")


if __name__ == "__main__":
    main()
