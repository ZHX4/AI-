from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parent
SCRIPT = "parts/part_05_geometry_final.py"
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


if __name__ == "__main__":
    for scene in SCENES:
        print(f"=== Rendering {scene} ===")
        result = subprocess.run(
            ["uv", "run", "manim", "-qh", SCRIPT, scene],
            cwd=ROOT,
            check=False,
        )
        if result.returncode:
            raise SystemExit(result.returncode)
    print("Part V render list completed.")
