from math import isclose

import numpy as np
from manim import *

from ..utils import LessonScene, VECTOR_A, VECTOR_B, plane


class DeterminantLesson(LessonScene):
    def axes2d(self, x_range=(-1, 5), y_range=(-1, 5)):
        return Axes(
            x_range=[x_range[0], x_range[1], 1],
            y_range=[y_range[0], y_range[1], 1],
            x_length=8.0,
            y_length=6.2,
            axis_config={"include_numbers": True, "stroke_width": 2},
        ).to_edge(LEFT, buff=0.28)

    def eq(self, latex, scale=0.70, y=0):
        return MathTex(latex).scale(scale).to_edge(RIGHT, buff=0.25).shift(UP * y)


class Part6_01_WhatDeterminantMeasures(DeterminantLesson):
    def construct(self):
        self.title(
            "Part VI.1 — What Does a Determinant Measure?",
            "A single number measures oriented area or volume scaling",
        )
        ax = self.axes2d()
        self.play(Create(ax))
        square = Polygon(
            ax.c2p(0, 0), ax.c2p(1, 0), ax.c2p(1, 1), ax.c2p(0, 1),
            stroke_width=4,
        )
        self.play(Create(square))
        self.cc(
            "A determinant is not merely a formula. It tells us how a square area or a three-dimensional volume is scaled by a linear transformation.",
            3.2,
        )
        self.play(Write(self.eq(r"\det(A)=\text{oriented area/volume scale factor}", 0.70, 1.25)))
        self.cc(
            "The word oriented matters. The absolute value measures size scaling; the sign records whether orientation is preserved or reversed.",
            3.1,
        )
        self.play(Write(self.eq(r"|\det(A)|=\text{size scale},\qquad \operatorname{sign}(\det A)=\text{orientation}", 0.57, 0.10)))
        self.play(Write(self.eq(r"\det(A)=0\Rightarrow\text{dimension collapse}", 0.76, -0.95)))
        self.cc("Those three ideas—scale, orientation, and dimension collapse—will organize the whole chapter.", 2.8)
        self.wait(2)


class Part6_02_TwoByTwoSignedArea(DeterminantLesson):
    def construct(self):
        self.title("Part VI.2 — The 2×2 Determinant", "The determinant is the signed parallelogram area")
        ax = self.axes2d(x_range=(-1, 4), y_range=(-1, 4))
        self.play(Create(ax))
        a = Arrow(ax.c2p(0, 0), ax.c2p(2, 1), buff=0, color=VECTOR_A, stroke_width=6)
        b = Arrow(ax.c2p(0, 0), ax.c2p(1, 2), buff=0, color=VECTOR_B, stroke_width=6)
        p = Polygon(ax.c2p(0, 0), ax.c2p(2, 1), ax.c2p(3, 3), ax.c2p(1, 2), stroke_width=4)
        self.play(GrowArrow(a), GrowArrow(b), Create(p))
        self.cc("The two column vectors form a parallelogram. Its unsigned area is the absolute value of the determinant.", 3.0)
        self.play(Write(self.eq(r"A=\begin{bmatrix}2&1\\1&2\end{bmatrix}", 0.82, 1.40)))
        self.play(Write(self.eq(r"\det(A)=ad-bc=2(2)-1(1)=3", 0.78, 0.45)))
        self.play(Write(self.eq(r"\boxed{\text{area}=|\det(A)|=3}", 0.90, -0.55)))
        self.cc("The determinant is signed, but ordinary geometric area is never negative, so we use its absolute value for size.", 2.7)
        self.play(Write(self.eq(r"\text{signed area}=\det(A),\qquad \text{area}=|\det(A)|", 0.70, -1.45)))
        self.wait(2)


class Part6_03_DeterminantAsAreaScale(DeterminantLesson):
    def construct(self):
        self.title("Part VI.3 — Determinant as an Area Scale Factor", "Watch a unit square become three times as large")
        plane_obj = plane(x_range=(-1, 5), y_range=(-1, 5), x_length=7.2, y_length=6.2).to_edge(LEFT, buff=0.25)
        self.play(Create(plane_obj))
        square = Polygon(
            plane_obj.c2p(0, 0), plane_obj.c2p(1, 0), plane_obj.c2p(1, 1), plane_obj.c2p(0, 1),
            stroke_width=4,
        )
        self.play(Create(square))
        self.cc("Start with a unit square, whose area is one. Now transform its basis vectors to (2,1) and (1,2).", 3.0)
        self.play(Write(self.eq(r"A=\begin{bmatrix}2&1\\1&2\end{bmatrix}", 0.80, 1.50)))
        self.play(Write(self.eq(r"\det(A)=3", 0.95, 0.70)))
        target = Polygon(
            plane_obj.c2p(0, 0), plane_obj.c2p(2, 1), plane_obj.c2p(3, 3), plane_obj.c2p(1, 2),
            stroke_width=4,
        )
        self.play(Transform(square, target))
        self.cc("The transformed parallelogram has area three. The determinant predicted that exact area scale factor.", 3.0)
        self.play(Write(self.eq(r"\boxed{\text{new area}=|\det(A)|\times\text{old area}=3}", 0.67, -0.10)))
        self.play(Write(self.eq(r"\frac{\text{new area}}{\text{old area}}=|\det(A)|", 0.75, -1.20)))
        self.wait(2)


class Part6_04_ThreeByThreeVolume(DeterminantLesson):
    def construct(self):
        self.title("Part VI.4 — The 3×3 Determinant", "In three dimensions, determinant becomes volume scale")
        self.play(Write(self.eq(r"A=\begin{bmatrix}1&2&0\\0&1&3\\2&0&1\end{bmatrix}", 0.70, 1.65)))
        self.cc("Three independent column vectors form a parallelepiped. Its volume is the absolute value of the determinant.", 3.0)
        self.play(Write(self.eq(r"\det(A)=1(1-0)-2(0-6)+0=13", 0.78, 0.65)))
        self.play(Write(self.eq(r"\boxed{\text{volume scale}=|\det(A)|=13}", 0.78, -0.30)))

        self.cc("For a visible 3D deformation, use a smaller example whose determinant is two, so the transformed solid remains on screen.", 3.0)
        cube = Cube(side_length=2, fill_opacity=0.22, stroke_width=3).shift(LEFT * 2.0)
        self.play(Create(cube))
        D = np.array([[1, 1, 0], [0, 2, 0], [0, 0, 1]], dtype=float)
        self.play(ApplyMatrix(D, cube), run_time=2.5)
        self.play(Write(self.eq(r"D=\begin{bmatrix}1&1&0\\0&2&0\\0&0&1\end{bmatrix}", 0.66, -1.10)))
        self.play(Write(self.eq(r"\det(D)=2\Rightarrow\text{volume doubles}", 0.72, -2.00)))
        self.cc("The cube has been sheared and stretched, but its volume changed by exactly a factor of two. That is the 3D meaning of the determinant.", 3.1)
        self.wait(2)


class Part6_05_OrientationAndSign(DeterminantLesson):
    def construct(self):
        self.title("Part VI.5 — Orientation and the Sign", "Negative determinant means orientation reversal")
        ax = self.axes2d(x_range=(-3, 4), y_range=(-3, 4))
        self.play(Create(ax))
        tri = Polygon(ax.c2p(0, 0), ax.c2p(2, 0), ax.c2p(0, 1), stroke_width=4)
        self.play(Create(tri))
        self.play(Write(self.eq(r"A=\begin{bmatrix}1&0\\0&-2\end{bmatrix}", 0.78, 1.45)))
        self.play(Write(self.eq(r"\det(A)=1(-2)-0=-2", 0.82, 0.55)))
        reflected = Polygon(ax.c2p(0, 0), ax.c2p(2, 0), ax.c2p(0, -2), stroke_width=4)
        self.play(Transform(tri, reflected))
        self.cc("The absolute value is two, so area doubles. The negative sign tells us that orientation was reversed.", 3.1)
        self.play(Write(self.eq(r"|\det(A)|=2,\qquad \det(A)<0\Rightarrow\text{orientation reversal}", 0.60, -0.35)))
        self.cc("Positive determinant preserves orientation; negative determinant reverses it; zero determinant collapses dimension.", 3.0)
        self.wait(2)


class Part6_06_DeterminantProperties(DeterminantLesson):
    def construct(self):
        self.title("Part VI.6 — Determinant Properties", "The main identities and what they mean")
        self.play(Write(self.eq(r"\det(AB)=\det(A)\det(B)", 0.92, 1.55)))
        self.cc("Composition multiplies scale factors. Applying one transformation and then another multiplies their area or volume effects.", 2.8)
        self.play(Write(self.eq(r"\det(cA)=c^n\det(A)\quad\text{for an }n\times n\text{ matrix}", 0.67, 0.55)))
        self.cc("Every one of the n columns is scaled by c, so the determinant receives n copies of that factor.", 2.7)
        self.play(Write(self.eq(r"\det(A^T)=\det(A)", 0.88, -0.35)))
        self.play(Write(self.eq(r"\det(A^{-1})=\frac{1}{\det(A)}\quad\text{when }\det(A)\neq0", 0.66, -1.15)))
        self.cc("These identities are the algebraic version of how geometric scale behaves under composition, transpose, and reversal of an invertible map.", 3.0)
        self.wait(2)


class Part6_07_RowOperationsAndDeterminant(DeterminantLesson):
    def construct(self):
        self.title("Part VI.7 — Row Operations and Determinant", "Three operations, three determinant rules")
        self.play(Write(self.eq(r"R_i\leftrightarrow R_j\Rightarrow\det\text{ changes sign}", 0.74, 1.45)))
        self.play(Write(self.eq(r"R_i\leftarrow cR_i\Rightarrow\det\text{ is multiplied by }c", 0.68, 0.65)))
        self.play(Write(self.eq(r"R_i\leftarrow R_i+cR_j\Rightarrow\det\text{ is unchanged}", 0.68, -0.15)))
        self.cc("Swapping rows reverses orientation. Scaling one row scales volume. Adding a multiple of one row to another is a shear, which preserves oriented volume.", 3.5)
        self.play(Write(self.eq(r"\text{row replacement is a volume-preserving shear}", 0.72, -1.10)))
        self.cc("These rules make determinant computation by elimination efficient and predictable.", 2.6)
        self.wait(2)


class Part6_08_CofactorExpansion(DeterminantLesson):
    def construct(self):
        self.title("Part VI.8 — Cofactor Expansion", "Reduce a 3×3 determinant to 2×2 determinants")
        self.play(Write(self.eq(r"A=\begin{bmatrix}1&2&3\\0&1&4\\5&6&0\end{bmatrix}", 0.78, 1.55)))
        self.cc("Expand along the first row. Each entry is multiplied by its signed minor.", 2.8)
        self.play(Write(self.eq(r"\det(A)=1\begin{vmatrix}1&4\\6&0\end{vmatrix}-2\begin{vmatrix}0&4\\5&0\end{vmatrix}+3\begin{vmatrix}0&1\\5&6\end{vmatrix}", 0.58, 0.45)))
        self.play(Write(self.eq(r"=1(-24)-2(-20)+3(-5)", 0.80, -0.45)))
        self.play(Write(self.eq(r"\boxed{\det(A)=1}", 0.96, -1.30)))
        self.cc("The alternating plus-minus-plus signs come from the cofactor rule, not from memory alone.", 2.7)
        self.play(Write(self.eq(r"C_{ij}=(-1)^{i+j}M_{ij}", 0.78, -2.10)))
        self.wait(2)


class Part6_09_DeterminantAndInvertibility(DeterminantLesson):
    def construct(self):
        self.title("Part VI.9 — Determinant and Invertibility", "Zero determinant means dimension has been lost")
        ax = self.axes2d(x_range=(-2, 4), y_range=(-2, 4))
        self.play(Create(ax))
        square = Polygon(ax.c2p(0, 0), ax.c2p(1, 0), ax.c2p(1, 1), ax.c2p(0, 1), stroke_width=4)
        self.play(Create(square))
        self.play(Write(self.eq(r"A=\begin{bmatrix}1&2\\2&4\end{bmatrix}", 0.80, 1.45)))
        self.play(Write(self.eq(r"\det(A)=1(4)-2(2)=0", 0.86, 0.55)))
        collapsed = Line(ax.c2p(-1, -2), ax.c2p(2, 4), stroke_width=5)
        self.play(Transform(square, collapsed))
        self.cc("A determinant of zero means the area scale factor is zero. A two-dimensional region collapses onto a line, so the transformation cannot be inverted.", 3.3)
        self.play(Write(self.eq(r"\boxed{\det(A)=0\iff A\text{ is singular}\iff A^{-1}\text{ does not exist}}", 0.55, -0.30)))
        self.cc("When the determinant is nonzero, no dimension is lost and the square matrix has an inverse.", 2.8)
        self.play(Write(self.eq(r"\det(A)\neq0\iff A^{-1}\text{ exists}", 0.78, -1.35)))
        self.wait(2)


class Part6_10_DeterminantAndProducts(DeterminantLesson):
    def construct(self):
        self.title("Part VI.10 — Determinants of Products", "Composition becomes multiplication of scale factors")
        self.play(Write(self.eq(r"A=\begin{bmatrix}2&0\\0&3\end{bmatrix},\quad B=\begin{bmatrix}1&1\\0&2\end{bmatrix}", 0.68, 1.50)))
        self.play(Write(self.eq(r"\det(A)=6,\qquad\det(B)=2", 0.84, 0.65)))
        self.play(Write(self.eq(r"AB=\begin{bmatrix}2&2\\0&6\end{bmatrix}", 0.78, -0.15)))
        self.play(Write(self.eq(r"\det(AB)=12=6\cdot2", 0.88, -1.05)))
        self.cc("Apply B and then A. The total area scale is the product of the individual scale factors.", 2.8)
        self.play(Write(self.eq(r"\boxed{\det(AB)=\det(A)\det(B)}", 0.92, -1.95)))
        self.wait(2)


class Part6_11_DeterminantMastery(DeterminantLesson):
    def construct(self):
        self.title("Part VI.11 — Determinant Mastery", "Geometry, algebra, and invertibility in one picture")
        self.play(Write(self.eq(r"\det(A)=\text{oriented volume scale factor}", 0.78, 1.55)))
        self.cc("The determinant has three views that should stay connected: geometry, algebra, and invertibility.", 3.0)
        summary = VGroup(
            Text("2×2 → signed area", font_size=22),
            Text("3×3 → signed volume", font_size=22),
            Text("absolute value → size scale", font_size=22),
            Text("sign → orientation", font_size=22),
            Text("row operations → predictable updates", font_size=22),
            Text("cofactor expansion → computable formula", font_size=22),
            Text("det = 0 → dimension collapse", font_size=22),
            Text("det ≠ 0 → invertible", font_size=22),
            Text("det(AB) = det(A)det(B)", font_size=22),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.12).to_edge(RIGHT, buff=0.08).shift(DOWN * 0.25)
        self.play(LaggedStart(*[Write(item) for item in summary], lag_ratio=0.14), run_time=3.0)
        self.cc("Remember the determinant by what it measures: oriented volume scaling, together with whether the transformation destroys a dimension.", 3.5)
        self.play(Write(Text("Part VI complete: determinants are geometry encoded as a scalar.", font_size=26, color=YELLOW_B).to_edge(DOWN, buff=0.45)))
        self.wait(3)


__all__ = [name for name in globals() if name.startswith("Part6_") or name == "DeterminantLesson"]
