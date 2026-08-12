from pathlib import Path
import sys

# Allow `manim render_part1.py SceneName` from this directory while
# preserving package-relative imports inside parts/.
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from linear_algebra.parts.part_01_foundations import *  # noqa: F401,F403
