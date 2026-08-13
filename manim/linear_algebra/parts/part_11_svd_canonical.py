import numpy as np
from manim import *

from .part_11_svd_final import *


class Part11_06_SphereToEllipse(SVDLesson):
    def construct(self):
        self.title("Part XI.6 — Sphere to Ellipse", "The matrix maps the unit circle to an ellipse")
        ax = self.axes2d(x_range=(-4, 4), y_range=(-4, 4))
        self.play(Create(ax))
        circle = Circle(radius=1.0, color=HIGHLIGHT, stroke_width=4).move_to(ax.c2p(0, 0))
        self.play(Create(circle))
        self.cc("Take a point on the unit circle as x equals cosine t, sine t. Applying A gives the point minus sine t, three cosine t, which traces an ellipse.", 3.2)
        ellipse = ParametricFunction(
            lambda t: ax.c2p(-np.sin(t), 3 * np.cos(t)),
            t_range=[0, TAU],
            color=VECTOR_A,
            stroke_width=4,
        )
        self.play(Create(ellipse), FadeOut(circle), run_time=2.2)
        self.play(Write(self.eq(r"A\begin{bmatrix}\cos t\\\sin t\end{bmatrix}=\begin{bmatrix}-\sin t\\3\cos t\end{bmatrix}", 0.66, 1.05)))
        self.play(Write(self.eq(r"\boxed{\text{semiaxis lengths}=3,1}", 0.82, 0.22)))
        self.cc("The longest radius is three and the perpendicular radius is one. Those two lengths are exactly the singular values of A.", 2.9)
        self.wait(2)


__all__ = [name for name in globals() if name.startswith("Part11_") or name == "SVDLesson"]
