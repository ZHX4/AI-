import numpy as np
from manim import *

from .part_13_numerical_ml_final import *


class Part13_05_LeastSquares(NumericalMLLesson):
    def construct(self):
        self.title("Part XIII.5 — Least Squares", "The residual is orthogonal to the fitted subspace")
        ax = self.axes2d(x_range=(-1, 5), y_range=(-1, 5))
        self.play(Create(ax))

        # Line: y = 3x/4 + 1. Point: (2,4). Exact orthogonal projection:
        # foot = (68/25, 76/25) = (2.72, 3.04).
        line = Line(ax.c2p(0, 1), ax.c2p(4, 4), color=VECTOR_A, stroke_width=4)
        point = Dot(ax.c2p(2, 4), radius=0.08, color=HIGHLIGHT)
        foot = Dot(ax.c2p(68 / 25, 76 / 25), radius=0.07, color=VECTOR_B)
        residual = Line(point.get_center(), foot.get_center(), color=VECTOR_B, stroke_width=3)
        self.play(Create(line), FadeIn(point), FadeIn(foot), Create(residual))
        self.play(Write(self.eq(r"\min_x\|Ax-b\|_2", 0.96, 1.05)))
        self.play(Write(self.eq(r"A^T(Ax-b)=0", 0.84, 0.28)))
        self.play(Write(self.eq(r"\hat b=\operatorname{proj}_{\operatorname{Col}(A)}(b)", 0.70, -0.55)))
        self.play(Write(self.eq(r"\boxed{\text{residual}\perp\operatorname{Col}(A)}", 0.72, -1.25)))
        self.cc("At the least-squares solution, the residual is exactly perpendicular to the column space. The fitted vector is the closest vector that A can produce.", 3.0)
        self.wait(2)


__all__ = [name for name in globals() if name.startswith("Part13_") or name == "NumericalMLLesson"]
