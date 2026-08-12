from manim import *
from ..utils import *


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

    def vector_point(self, ax, xy, color):
        return ax.c2p(*xy)


class Part6_01_WhatDeterminantMeasures(DeterminantLesson):
    def construct(self):
        self.title("Part VI.1 — What Does a Determinant Measure?", "A single number tells us how a linear map scales oriented volume")
        ax = self.axes2d(x_range=(-1, 5), y_range=(-1, 5))
        self.play(Create(ax))
        square = Polygon(
            ax.c2p(0, 0), ax.c2p(1, 0), ax.c2p(1, 1), ax.c2p(0, 1),
            stroke_width=4,
        )
        self.play(Create(square))
        self.cc("A determinant is not just a formula. Geometrically, it measures how a linear transformation changes signed area in two dimensions and signed volume in three dimensions.", 3.4)
        self.play(Write(self.eq(r"\det(A)=\text{oriented area/volume scale factor}", 0.70, 1.30)))
        self.cc("The word signed matters. A transformation can preserve size while reversing orientation, which makes the determinant negative.", 3.0)
        self.play(Write(self.eq(r"|\det(A)|=\text{size scale},\qquad \operatorname{sign}(\det A)=\text{orientation}", 0.58, 0.20)))
        self.cc("The rest of this chapter explains exactly why this one number encodes all of that geometry.", 2.8)
        self.wait(2)


class Part6_02_TwoByTwoSignedArea(DeterminantLesson):
    def construct(self):
        self.title("Part VI.2 — The 2×2 Determinant", "The parallelogram area formula")
        ax = self.axes2d(x_range=(-1, 4), y_range=(-1, 4))
        self.play(Create(ax))
        a = Arrow(ax.c2p(0, 0), ax.c2p(2, 1), buff=0, color=VECTOR_A, stroke_width=6)
        b = Arrow(ax.c2p(0, 0), ax.c2p(1, 2), buff=0, color=VECTOR_B, stroke_width=6)
        self.play(GrowArrow(a), GrowArrow(b))
        p = Polygon(ax.c2p(0,0), ax.c2p(2,1), ax.c2p(3,3), ax.c2p(1,2), stroke_width=4)
        self.play(Create(p))
        self.cc("Two vectors form a parallelogram. Its area is the absolute value of the determinant of the matrix whose columns are those vectors.", 3.0)
        self.play(Write(self.eq(r"A=\begin{bmatrix}2&1\\1&2\end{bmatrix}", 0.82, 1.45)))
        self.play(Write(self.eq(r"\det(A)=ad-bc=2(2)-1(1)=3", 0.78, 0.45)))
        self.play(Write(self.eq(r"\boxed{\operatorname{area}=|\det(A)|=3}", 0.86, -0.55)))
        self.cc("The determinant is three, so this transformation multiplies oriented area by three.", 2.8)
        self.play(Write(self.eq(r"\text{area of parallelogram}=|ad-bc|", 0.74, -1.45)))
        self.wait(2)


class Part6_03_DeterminantAsAreaScale(DeterminantLesson):
    def construct(self):
        self.title("Part VI.3 — Determinant as an Area Scale Factor", "Watch a unit square become three times as large")
        plane_obj = plane(x_range=(-1, 5), y_range=(-1, 5), x_length=7.3, y_length=6.2).to_edge(LEFT, buff=0.25)
        self.play(Create(plane_obj))
        square = Polygon(
            plane_obj.c2p(0, 0), plane_obj.c2p(1, 0), plane_obj.c2p(1, 1), plane_obj.c2p(0, 1),
            stroke_width=4,
        )
        self.play(Create(square))
        self.cc("Start with a unit square. Its area is one. Apply the matrix that sends the basis vectors to (2,1) and (1,2).", 3.0)
        self.play(Write(self.eq(r"A=\begin{bmatrix}2&1\\1&2\end{bmatrix}", 0.80, 1.55)))
        self.play(Write(self.eq(r"\det(A)=3", 0.95, 0.75)))
        target = Polygon(
            plane_obj.c2p(0, 0), plane_obj.c2p(2, 1), plane_obj.c2p(3, 3), plane_obj.c2p(1, 2),
            stroke_width=4,
        )
        self.play(Transform(square, target))
        self.cc("The square became a parallelogram with area three. The determinant predicted that scale factor before we measured the new area.", 3.2)
        self.play(Write(self.eq(r"\boxed{\text{new area}=|\det(A)|\times\text{old area}=3}", 0.67, -0.10)))
        self.cc("This is why determinants are useful: they turn a complicated geometric deformation into one scalar measurement.", 2.8)
        self.wait(2)


class Part6_04_ThreeByThreeVolume(DeterminantLesson):
    def construct(self):
        self.title("Part VI.4 — The 3×3 Determinant", "Now the determinant measures signed volume")
        self.play(Write(self.eq(r"A=\begin{bmatrix}1&2&0\\0&1&3\\2&0&1\end{bmatrix}", 0.72, 1.65)))
        self.cc("In three dimensions, three column vectors form a parallelepiped. Its volume is the absolute value of the determinant.", 3.0)
        self.play(Write(self.eq(r"\det(A)=1(1-0)-2(0-6)+0=13", 0.78, 0.65)))
        self.play(Write(self.eq(r"\boxed{\operatorname{volume}=|\det(A)|=13}", 0.84, -0.30)))
        cube = Cube(side_length=2, fill_opacity=0.25, stroke_width=3).shift(LEFT * 2.3)
        self.play(Create(cube))
        self.cc("The identity transformation gives volume scale one. A general 3×3 matrix changes that volume by the absolute value of its determinant.", 3.0)
        self.play(Write(self.eq(r"|\det(A)|=\text{3D volume scale factor}", 0.72, -1.25)))
        self.wait(2)


class Part6_05_OrientationAndSign(DeterminantLesson):
    def construct(self):
        self.title("Part VI.5 — Orientation and the Sign", "Negative determinant means a flip")
        ax = self.axes2d(x_range=(-3, 4), y_range=(-3, 4))
        self.play(Create(ax))
        tri = Polygon(ax.c2p(0,0), ax.c2p(2,0), ax.c2p(0,1), stroke_width=4)
        self.play(Create(tri))
        self.play(Write(self.eq(r"A=\begin{bmatrix}1&0\\0&-2\end{bmatrix}", 0.78, 1.45)))
        self.play(Write(self.eq(r"\det(A)=1(-2)-0=-2", 0.82, 0.55)))
        reflected = Polygon(ax.c2p(0,0), ax.c2p(2,0), ax.c2p(0,-2), stroke_width=4)
        self.play(Transform(tri, reflected))
        self.cc("The magnitude of the determinant is two, so area is doubled. The negative sign tells us that the orientation was reversed by a reflection.", 3.2)
        self.play(Write(self.eq(r"|\det(A)|=2,\qquad \det(A)<0\Rightarrow\text{orientation reversal}", 0.62, -0.35)))
        self.cc("A positive determinant preserves orientation. A negative determinant reverses it. A zero determinant collapses dimension, which we will connect to invertibility.", 3.1)
        self.wait(2)


class Part6_06_DeterminantProperties(DeterminantLesson):
    def construct(self):
        self.title("Part VI.6 — Determinant Properties", "The determinant behaves predictably under matrix operations")
        self.play(Write(self.eq(r"\det(AB)=\det(A)\det(B)", 0.92, 1.55)))
        self.cc("Composition multiplies area or volume scale factors. If A scales area by two and B scales it by three, doing both scales by six.", 2.9)
        self.play(Write(self.eq(r"\det(2A)=2^n\det(A)\quad\text{for an }n\times n\text{ matrix}", 0.65, 0.55)))
        self.cc("Scalar multiplication affects every column, so in n dimensions the determinant receives n copies of that scale factor.", 2.8)
        self.play(Write(self.eq(r"\det(A^T)=\det(A)", 0.88, -0.35)))
        self.play(Write(self.eq(r"\det(A^{-1})=\frac1{\det(A)}\quad\text{when }\det(A)\neq0", 0.66, -1.15)))
        self.cc("These identities are not isolated tricks. They are the algebraic shadow of how geometric scale factors behave under composition and reversal.", 3.1)
        self.wait(2)


class Part6_07_RowOperationsAndDeterminant(DeterminantLesson):
    def construct(self):
        self.title("Part VI.7 — Row Operations and Determinant", "Three operations, three determinant rules")
        self.play(Write(self.eq(r"R_i\leftrightarrow R_j\Rightarrow\det\text{ changes sign}", 0.74, 1.45)))
        self.play(Write(self.eq(r"R_i\leftarrow cR_i\Rightarrow\det\text{ is multiplied by }c", 0.68, 0.65)))
        self.play(Write(self.eq(r"R_i\leftarrow R_i+cR_j\Rightarrow\det\text{ is unchanged}", 0.68, -0.15)))
        self.cc("Swapping rows reverses orientation. Scaling one row scales the volume factor. Adding one row to another is a shear, which changes shape but not oriented volume.", 3.6)
        self.play(Write(self.eq(r"\text{row replacement is a volume-preserving shear}", 0.72, -1.10)))
        self.cc("These rules are the reason Gaussian elimination can compute determinants efficiently without repeatedly expanding large formulas.", 2.9)
        self.wait(2)


class Part6_08_CofactorExpansion(DeterminantLesson):
    def construct(self):
        self.title("Part VI.8 — Cofactor Expansion", "Break a 3×3 determinant into smaller 2×2 determinants")
        self.play(Write(self.eq(r"A=\begin{bmatrix}1&2&3\\0&1&4\\5&6&0\end{bmatrix}", 0.78, 1.55)))
        self.cc("A 3×3 determinant can be expanded along any row or column. Each entry is multiplied by a signed minor.", 3.0)
        self.play(Write(self.eq(r"\det(A)=1\begin{vmatrix}1&4\\6&0\end{vmatrix}-2\begin{vmatrix}0&4\\5&0\end{vmatrix}+3\begin{vmatrix}0&1\\5&6\end{vmatrix}", 0.60, 0.45)))
        self.play(Write(self.eq(r"=1(-24)-2(-20)+3(-5)", 0.80, -0.45)))
        self.play(Write(self.eq(r"\boxed{\det(A)=1}", 0.96, -1.30)))
        self.cc("The alternating signs are essential: plus, minus, plus along the first row. A cofactor expansion is just a systematic way of reducing the determinant to smaller ones.", 3.2)
        self.play(Write(self.eq(r"C_{ij}=(-1)^{i+j}M_{ij}", 0.78, -2.10)))
        self.wait(2)


class Part6_09_DeterminantAndInvertibility(DeterminantLesson):
    def construct(self):
        self.title("Part VI.9 — Determinant and Invertibility", "Zero determinant means the transformation collapses dimension")
        ax = self.axes2d(x_range=(-2, 4), y_range=(-2, 4))
        self.play(Create(ax))
        square = Polygon(ax.c2p(0,0), ax.c2p(1,0), ax.c2p(1,1), ax.c2p(0,1), stroke_width=4)
        self.play(Create(square))
        self.play(Write(self.eq(r"A=\begin{bmatrix}1&2\\2&4\end{bmatrix}", 0.80, 1.45)))
        self.play(Write(self.eq(r"\det(A)=1(4)-2(2)=0", 0.86, 0.55)))
        collapsed = Polygon(ax.c2p(0,0), ax.c2p(1,2), ax.c2p(2,4), stroke_width=5)
        self.play(Transform(square, collapsed))
        self.cc("The determinant is zero, so the area scale factor is zero. A two-dimensional region collapses onto a line. Once dimension is lost, the map cannot be inverted.", 3.3)
        self.play(Write(self.eq(r"\boxed{\det(A)=0\iff A\text{ is singular}\iff A\text{ is not invertible}}", 0.58, -0.30)))
        self.cc("When the determinant is nonzero, the transformation preserves dimension and an inverse exists.", 2.8)
        self.play(Write(self.eq(r"\det(A)\neq0\iff A^{-1}\text{ exists}", 0.78, -1.35)))
        self.wait(2)


class Part6_10_DeterminantAndProducts(DeterminantLesson):
    def construct(self):
        self.title("Part VI.10 — Determinants of Products", "Composition becomes multiplication of scale factors")
        A = [[2, 0], [0, 3]]
        B = [[1, 1], [0, 2]]
        self.play(Write(self.eq(r"A=\begin{bmatrix}2&0\\0&3\end{bmatrix},\quad B=\begin{bmatrix}1&1\\0&2\end{bmatrix}", 0.68, 1.50)))
        self.play(Write(self.eq(r"\det(A)=6,\qquad\det(B)=2", 0.84, 0.65)))
        self.play(Write(self.eq(r"AB=\begin{bmatrix}2&2\\0&6\end{bmatrix}", 0.78, -0.15)))
        self.play(Write(self.eq(r"\det(AB)=12=6\cdot2", 0.88, -1.05)))
        self.cc("The algebra matches the geometry perfectly. Apply B, then A: the total area scale is the product of the two individual scale factors.", 3.0)
        self.play(Write(self.eq(r"\boxed{\det(AB)=\det(A)\det(B)}", 0.92, -1.95)))
        self.cc("This property is one of the most useful determinant identities in matrix theory, and it will later connect naturally to eigenvalues and decompositions.", 2.8)
        self.wait(2)


class Part6_11_DeterminantMastery(DeterminantLesson):
    def construct(self):
        self.title("Part VI.11 — Determinant Mastery", "One number connecting geometry, algebra, and invertibility")
        self.play(Write(self.eq(r"\det(A)=\text{oriented volume scale factor}", 0.78, 1.55)))
        self.cc("The determinant has three views that should never be separated: geometry, algebra, and invertibility.", 3.0)
        summary = VGroup(
            Text("2×2 determinant → signed area", font_size=22),
            Text("3×3 determinant → signed volume", font_size=22),
            Text("absolute value → size scale", font_size=22),
            Text("sign → orientation", font_size=22),
            Text("row operations → predictable updates", font_size=22),
            Text("cofactor expansion → computable formula", font_size=22),
            Text("det = 0 → dimension collapse", font_size=22),
            Text("det ≠ 0 → invertible transformation", font_size=22),
            Text("det(AB) = det(A)det(B)", font_size=22),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.12).to_edge(RIGHT, buff=0.08).shift(DOWN * 0.25)
        self.play(LaggedStart(*[Write(item) for item in summary], lag_ratio=0.14), run_time=3.0)
        self.cc("The best way to remember the determinant is not the expansion formula. Remember what it measures: how a linear map changes oriented volume, and whether it destroys dimension.", 3.7)
        self.play(Write(Text("Part VI complete: determinants are geometry encoded as a scalar.", font_size=26, color=YELLOW_B).to_edge(DOWN, buff=0.45)))
        self.wait(3)


__all__ = [name for name in globals() if name.startswith("Part6_") or name == "DeterminantLesson"]
