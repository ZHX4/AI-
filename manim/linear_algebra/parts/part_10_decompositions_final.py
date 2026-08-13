from math import sqrt

import numpy as np
from manim import *

from ..utils import HIGHLIGHT, LessonScene, VECTOR_A, VECTOR_B


class DecompositionLesson(LessonScene):
    def axes2d(self, x_range=(-5, 5), y_range=(-5, 5)):
        return Axes(x_range=[x_range[0], x_range[1], 1], y_range=[y_range[0], y_range[1], 1], x_length=7.2, y_length=6.0, axis_config={"include_numbers": True, "stroke_width": 2}).to_edge(LEFT, buff=0.22)

    def eq(self, latex, scale=0.67, y=0):
        return MathTex(latex).scale(scale).to_edge(RIGHT, buff=0.14).shift(UP * y)

    def matrix(self, latex, scale=0.70, y=1.55):
        return MathTex(latex).scale(scale).to_edge(RIGHT, buff=0.14).shift(UP * y)

    def direction_line(self, ax, direction, color, length=3.0):
        dx, dy = direction
        n = sqrt(dx * dx + dy * dy)
        dx, dy = dx / n * length, dy / n * length
        return Line(ax.c2p(-dx, -dy), ax.c2p(dx, dy), color=color, stroke_width=4)


class Part10_01_ChangeOfBasisIntuition(DecompositionLesson):
    def construct(self):
        self.title("Part X.1 — Change of Basis Intuition", "The vector stays fixed; its coordinates change")
        ax = self.axes2d(); self.play(Create(ax))
        self.play(GrowArrow(Arrow(ax.c2p(0,0), ax.c2p(3,1), buff=0, color=HIGHLIGHT, stroke_width=6)))
        self.cc("A basis is a coordinate language. Changing the basis does not move the geometric vector; it changes the numbers used to describe it.", 3.1)
        self.play(Write(self.eq(r"v=3e_1+e_2", 0.90, 0.95)))
        self.play(Write(self.eq(r"[v]_E=\begin{bmatrix}3\\1\end{bmatrix}", 0.80, 0.18)))
        self.play(Write(self.eq(r"B=\begin{bmatrix}1&1\\1&-1\end{bmatrix}", 0.70, -0.60)))
        self.play(Write(self.eq(r"[v]_B=\begin{bmatrix}2\\1\end{bmatrix}", 0.80, -1.18)))
        self.play(Write(self.eq(r"v=B[v]_B", 0.88, -1.82)))
        self.cc("The columns of B are the new basis vectors. Here 2(1,1)+1(1,-1)=(3,1), so the same vector has B-coordinates (2,1).", 3.0)
        self.wait(2)


class Part10_02_CoordinateTransformation(DecompositionLesson):
    def construct(self):
        self.title("Part X.2 — Coordinate Transformations", "Forward and inverse coordinate maps")
        self.play(Write(self.matrix(r"B=\begin{bmatrix}1&1\\1&-1\end{bmatrix}")))
        self.cc("If c contains coordinates in the B-basis, then Bc gives the standard-coordinate vector. To go back, apply the inverse.", 3.0)
        self.play(Write(self.eq(r"v=Bc", 0.96, 0.82)))
        self.play(Write(self.eq(r"c=B^{-1}v", 0.96, 0.10)))
        self.play(Write(self.eq(r"B^{-1}=\frac12\begin{bmatrix}1&1\\1&-1\end{bmatrix}", 0.66, -0.68)))
        self.play(Write(self.eq(r"B^{-1}B=I", 0.92, -1.48)))
        self.cc("The vector is unchanged geometrically; only the coordinate description changes.", 2.7)
        self.wait(2)


class Part10_03_SimilarityTransformations(DecompositionLesson):
    def construct(self):
        self.title("Part X.3 — Similarity Transformations", "The same operator in a different basis")
        self.play(Write(self.eq(r"[T]_E=A", 0.90, 1.30)))
        self.play(Write(self.eq(r"[T]_B=B^{-1}AB", 0.96, 0.48)))
        self.cc("A linear operator is the underlying rule. Its matrix depends on the basis used to represent that rule.", 3.0)
        self.play(Write(self.eq(r"\text{B}:\ \text{B-coordinates}\to\text{standard coordinates}", 0.58, -0.28)))
        self.play(Write(self.eq(r"\text{A}:\ \text{apply the operator in standard coordinates}", 0.60, -0.88)))
        self.play(Write(self.eq(r"\text{B}^{-1}:\ \text{standard coordinates}\to\text{B-coordinates}", 0.56, -1.48)))
        self.play(Write(self.eq(r"\boxed{[T]_B=B^{-1}AB}", 0.82, -2.20)))
        self.wait(2)


class Part10_04_OrthogonalMatrices(DecompositionLesson):
    def construct(self):
        self.title("Part X.4 — Orthogonal Matrices", "Rotations and reflections preserve Euclidean geometry")
        ax = self.axes2d(); self.play(Create(ax))
        a = Arrow(ax.c2p(0,0), ax.c2p(2,0), buff=0, color=VECTOR_A, stroke_width=6)
        b = Arrow(ax.c2p(0,0), ax.c2p(0,2), buff=0, color=VECTOR_B, stroke_width=6)
        self.play(GrowArrow(a), GrowArrow(b))
        R = np.array([[np.cos(PI/4), -np.sin(PI/4)], [np.sin(PI/4), np.cos(PI/4)]])
        self.play(ApplyMatrix(R, a), ApplyMatrix(R, b), run_time=2)
        self.play(Write(self.matrix(r"Q=\begin{bmatrix}\cos\theta&-\sin\theta\\\sin\theta&\cos\theta\end{bmatrix}")))
        self.play(Write(self.eq(r"Q^TQ=I", 0.95, 0.78)))
        self.play(Write(self.eq(r"Q^{-1}=Q^T", 0.92, 0.00)))
        self.play(Write(self.eq(r"\|Qv\|=\|v\|,\qquad(Qu)\cdot(Qv)=u\cdot v", 0.58, -0.88)))
        self.cc("Orthogonal matrices preserve lengths and angles. They change coordinates by rotations or reflections without distortion of Euclidean geometry.", 3.1)
        self.wait(2)


class Part10_05_LU_Factorization(DecompositionLesson):
    def construct(self):
        self.title("Part X.5 — LU Factorization", "Store elimination as L times U")
        self.play(Write(self.matrix(r"A=\begin{bmatrix}4&3\\6&3\end{bmatrix}")))
        self.cc("Eliminate the entry below the first pivot. The multiplier becomes an entry of L, while the resulting triangular matrix is U.", 3.0)
        self.play(Write(self.eq(r"R_2\leftarrow R_2-\frac32R_1", 0.78, 0.78)))
        self.play(Write(self.eq(r"U=\begin{bmatrix}4&3\\0&-\frac32\end{bmatrix}", 0.72, 0.02)))
        self.play(Write(self.eq(r"L=\begin{bmatrix}1&0\\\frac32&1\end{bmatrix}", 0.72, -0.78)))
        self.play(Write(self.eq(r"\boxed{A=LU}", 1.02, -1.62)))
        self.cc("LU stores the elimination process in reusable factors. That makes repeated linear-system solves much cheaper after one factorization.", 3.0)
        self.wait(2)


class Part10_06_LU_SolvingSystems(DecompositionLesson):
    def construct(self):
        self.title("Part X.6 — Solving with LU", "Two triangular solves replace one full solve")
        self.play(Write(self.eq(r"A=LU,\qquad Ax=b", 0.98, 1.35)))
        self.play(Write(self.eq(r"Ly=b\quad\text{then}\quad Ux=y", 0.90, 0.65)))
        self.play(Write(self.eq(r"b=\begin{bmatrix}10\\12\end{bmatrix}", 0.72, -0.05)))
        self.play(Write(self.eq(r"y=\begin{bmatrix}10\\-3\end{bmatrix}", 0.72, -0.72)))
        self.play(Write(self.eq(r"x=\begin{bmatrix}1\\2\end{bmatrix}", 0.72, -1.40)))
        self.play(Write(self.eq(r"A\begin{bmatrix}1\\2\end{bmatrix}=\begin{bmatrix}10\\12\end{bmatrix}", 0.72, -2.08)))
        self.cc("For this system, forward substitution gives y=(10,-3), and back substitution gives x=(1,2). The factorization can now be reused for another right-hand side.", 3.2)
        self.wait(2)


class Part10_07_QR_Factorization(DecompositionLesson):
    def construct(self):
        self.title("Part X.7 — QR Factorization", "Build an orthonormal basis from the columns")
        self.play(Write(self.matrix(r"A=\begin{bmatrix}1&1\\1&0\end{bmatrix}")))
        self.cc("Start with the first column and normalize it. Then remove its component from the second column and normalize what remains.", 3.0)
        self.play(Write(self.eq(r"q_1=\frac1{\sqrt2}\begin{bmatrix}1\\1\end{bmatrix}", 0.72, 0.82)))
        self.play(Write(self.eq(r"r_{12}=q_1^Ta_2=\frac1{\sqrt2}", 0.70, 0.15)))
        self.play(Write(self.eq(r"q_2=\frac1{\sqrt2}\begin{bmatrix}1\\-1\end{bmatrix}", 0.72, -0.52)))
        self.play(Write(self.eq(r"R=\begin{bmatrix}\sqrt2&\frac1{\sqrt2}\\0&\frac1{\sqrt2}\end{bmatrix}", 0.60, -1.22)))
        self.play(Write(self.eq(r"\boxed{A=QR,\qquad Q^TQ=I}", 0.82, -2.00)))
        self.wait(2)


class Part10_08_QR_Geometry(DecompositionLesson):
    def construct(self):
        self.title("Part X.8 — QR Geometry", "Q stores pure geometry; R stores coordinates")
        ax = self.axes2d(x_range=(-3, 4), y_range=(-3, 4)); self.play(Create(ax))
        self.play(GrowArrow(Arrow(ax.c2p(0,0), ax.c2p(1,1), buff=0, color=VECTOR_A, stroke_width=6)))
        self.play(GrowArrow(Arrow(ax.c2p(0,0), ax.c2p(1,0), buff=0, color=VECTOR_B, stroke_width=6)))
        self.cc("QR separates the geometry of orthogonal directions from the coordinates needed to rebuild the original columns.", 3.0)
        self.play(Write(self.eq(r"A=QR", 1.05, 1.00)))
        self.play(Write(self.eq(r"Q^TQ=I", 0.96, 0.25)))
        self.play(Write(self.eq(r"R\text{ upper triangular}", 0.76, -0.50)))
        self.play(Write(self.eq(r"\boxed{\text{orthogonal geometry + triangular coordinates}}", 0.62, -1.35)))
        self.cc("That structure is especially valuable in numerical linear algebra and least-squares computation.", 2.8)
        self.wait(2)


class Part10_09_LinearOperators(DecompositionLesson):
    def construct(self):
        self.title("Part X.9 — Linear Operators", "The abstract rule behind a matrix")
        ax = self.axes2d(); self.play(Create(ax))
        self.play(GrowArrow(Arrow(ax.c2p(0,0), ax.c2p(2,1), buff=0, color=HIGHLIGHT, stroke_width=6)))
        self.play(Write(self.eq(r"T(au+bv)=aT(u)+bT(v)", 0.82, 1.25)))
        self.play(Write(self.eq(r"T:\mathbb{R}^n\to\mathbb{R}^m", 0.84, 0.60)))
        self.cc("A linear operator is the rule itself. A matrix is the coordinate representation of that rule after bases have been chosen.", 3.0)
        self.play(Write(self.eq(r"[T]_B=B^{-1}[T]_E B", 0.72, -0.30)))
        self.play(Write(self.eq(r"\text{same operator}\neq\text{same matrix in every basis}", 0.62, -1.12)))
        self.wait(2)


class Part10_10_DecompositionComparison(DecompositionLesson):
    def construct(self):
        self.title("Part X.10 — Decomposition Comparison", "Different factorizations expose different structure")
        items = VGroup(
            Text("Basis change → coordinate structure", font_size=22),
            Text("Orthogonal Q → geometry without distortion", font_size=22),
            Text("LU → elimination and repeated solves", font_size=22),
            Text("QR → orthonormal directions + triangular coordinates", font_size=22),
            Text("Spectral form → invariant eigen-directions", font_size=22),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.20).to_edge(RIGHT, buff=0.04).shift(DOWN * 0.05)
        self.play(LaggedStart(*[Write(x) for x in items], lag_ratio=0.12), run_time=2.8)
        self.cc("A useful decomposition makes hidden structure visible. The best factorization depends on the mathematical or computational question.", 3.1)
        self.play(Write(self.eq(r"\boxed{\text{factorization}=\text{structure made visible}}", 0.72, -2.25)))
        self.wait(2)


class Part10_11_DecompositionsMastery(DecompositionLesson):
    def construct(self):
        self.title("Part X.11 — Decompositions Mastery", "Changing, solving, and understanding linear maps")
        summary = VGroup(
            Text("Basis change → coordinates change, vector does not", font_size=20),
            Text("Similarity → same operator in a new basis", font_size=20),
            Text("Orthogonal matrices → preserve lengths and angles", font_size=20),
            Text("LU → elimination stored as factors", font_size=20),
            Text("QR → orthonormal basis + triangular coordinates", font_size=20),
            Text("Operators → abstract rules behind matrix representations", font_size=20),
            Text("Decompositions → simpler pieces with understandable jobs", font_size=20),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.14).to_edge(RIGHT, buff=0.03).shift(DOWN * 0.08)
        self.play(LaggedStart(*[Write(x) for x in summary], lag_ratio=0.11), run_time=2.8)
        self.cc("The central idea is structural: replace one opaque matrix with pieces whose individual roles are easy to understand.", 3.4)
        self.play(Write(self.eq(r"\boxed{\text{matrix}=\text{composition of understandable structure}}", 0.68, -2.30)))
        self.play(Write(Text("Part X complete: decompositions connect coordinates, geometry, and computation.", font_size=22, color=YELLOW_B).to_edge(DOWN, buff=0.38)))
        self.wait(3)


__all__ = [name for name in globals() if name.startswith("Part10_") or name == "DecompositionLesson"]