from manim import *

from .part_01_foundations_final import *


# Part I uses a dedicated visual layout while reusing the already-verified
# lesson mathematics and scene classes from part_01_foundations_final.py.
def _safe_axes(self):
    ax = Axes(
        x_range=[-5, 5, 1],
        y_range=[-4, 4, 1],
        x_length=7.25,
        y_length=5.35,
        axis_config={"include_numbers": True, "stroke_width": 2},
    )
    ax.to_edge(LEFT, buff=0.28).shift(DOWN * 0.28)
    return ax


def _safe_eq(self, s, scale=0.7, y=0):
    mob = MathTex(s).scale(scale)
    mob.set_max_width(3.25)
    mob.to_edge(RIGHT, buff=0.22).shift(UP * y + DOWN * 0.05)
    return mob


FoundationLesson.axes = _safe_axes
FoundationLesson.eq = _safe_eq


__all__ = [name for name in globals() if name.startswith("Part1_") or name == "FoundationLesson"]
