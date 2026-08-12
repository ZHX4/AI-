from manim import *
from ..utils import *


class MatrixLesson(LessonScene):
    """Shared helpers for the canonical Part III matrix lessons."""

    def axes2d(self):
        ax = Axes(
            x_range=[-8, 8, 1],
            y_range=[-6, 6, 1],
            x_length=8.4,
            y_length=6.3,
            axis_config={"include_numbers": True, "stroke_width": 2},
        )
        ax.to_edge(LEFT, buff=0.28)
        return ax

    def eq(self, latex, scale=0.70, y=0):
        return MathTex(latex).scale(scale).to_edge(RIGHT, buff=0.28).shift(UP * y)


class Part3_01_WhatIsAMatrix(MatrixLesson):
    def construct(self):
        self.title("Part III.1 — What Is a Matrix?", "A structured rule, not merely a rectangle of numbers")
        ax = self.axes2d(); self.play(Create(ax))
        self.cc("A matrix is a rectangular arrangement of numbers, but its purpose is to encode how coordinates are combined or transformed.", 3.2)
        M = Matrix([[2, 1], [1, 2]]).scale(0.95).to_edge(RIGHT, buff=0.65).shift(UP * 1.1)
        self.play(Write(M))
        self.play(Write(self.eq(r"A=\begin{bmatrix}2&1\\1&2\end{bmatrix}", 0.72, -0.05)))
        self.cc("This is a two-by-two matrix: two rows and two columns. Its shape tells us what kind of vector can be multiplied by it and what dimension comes out.", 3.2)
        self.play(Write(self.eq(r"2\times2\;\text{matrix}:\quad\mathbb R^2\to\mathbb R^2", 0.72, -1.0)))
        self.cc("Rows tell us how output coordinates are calculated. Columns will soon reveal the geometry of the transformation.", 3.0)
        self.play(Write(self.eq(r"\text{rows}\to\text{coordinate formulas},\qquad\text{columns}\to\text{basis images}", 0.55, -1.85)))
        self.wait(2)


class Part3_02_MatrixVectorMultiplication(MatrixLesson):
    def construct(self):
        self.title("Part III.2 — Matrix–Vector Multiplication", "Rows compute the output coordinates")
        ax = self.axes2d(); self.play(Create(ax))
        x = arrow_from(ax, (3, 1), VECTOR_A, r"\vec x")
        self.play(GrowArrow(x[0]), Write(x[1]))
        self.cc("Let the input vector be three, one. The matrix turns those two input coordinates into a new pair.", 2.8)
        self.play(Write(self.eq(r"A=\begin{bmatrix}2&1\\1&2\end{bmatrix},\quad\vec x=\begin{bmatrix}3\\1\end{bmatrix}", 0.58, 1.55)))
        self.play(Write(self.eq(r"A\vec x=\begin{bmatrix}2(3)+1(1)\\1(3)+2(1)\end{bmatrix}", 0.63, 0.65)))
        self.cc("The first row produces seven. The second row produces five. Each output coordinate is a dot product between one row and the input vector.", 3.3)
        self.play(Write(self.eq(r"A\vec x=\begin{bmatrix}7\\5\end{bmatrix}", 0.92, -0.35)))
        out = arrow_from(ax, (7, 5), HIGHLIGHT, r"A\vec x")
        self.play(GrowArrow(out[0]), Write(out[1]))
        self.cc("The arrow has moved from the input vector to its output. Matrix multiplication is therefore a function from vectors to vectors.", 3.2)
        self.play(Write(self.eq(r"\vec x\longmapsto A\vec x", 0.92, -1.55)))
        self.wait(2)


class Part3_03_ColumnsBuildTheOutput(MatrixLesson):
    def construct(self):
        self.title("Part III.3 — Columns Build the Output", "The column picture of Ax")
        ax = self.axes2d(); self.play(Create(ax))
        c1 = arrow_from(ax, (2, 1), VECTOR_A, r"\vec c_1"); c2 = arrow_from(ax, (1, 2), VECTOR_B, r"\vec c_2")
        self.play(GrowArrow(c1[0]), Write(c1[1]), GrowArrow(c2[0]), Write(c2[1]))
        self.cc("The same multiplication can be understood column by column. The input coordinates become weights on the matrix columns.", 3.1)
        self.play(Write(self.eq(r"A\vec x=x_1\vec c_1+x_2\vec c_2", 0.82, 1.45)))
        first = Arrow(ax.c2p(0, 0), ax.c2p(6, 3), buff=0, color=VECTOR_A, stroke_width=6)
        second = Arrow(ax.c2p(6, 3), ax.c2p(7, 5), buff=0, color=VECTOR_B, stroke_width=6)
        self.play(GrowArrow(first)); self.cc("Three times the first column gives six, three.", 2.3)
        self.play(GrowArrow(second)); self.cc("Adding one copy of the second column moves to seven, five. This is the same Ax we calculated from rows.", 3.0)
        self.play(Write(self.eq(r"3\begin{bmatrix}2\\1\end{bmatrix}+\begin{bmatrix}1\\2\end{bmatrix}=\begin{bmatrix}7\\5\end{bmatrix}", 0.60, -0.75)))
        self.play(Write(self.eq(r"\text{columns}=\text{images of basis directions}", 0.66, -1.85)))
        self.wait(2)


class Part3_04_MatrixAsTransformation(MatrixLesson):
    def construct(self):
        self.title("Part III.4 — Matrix as a Transformation", "The whole plane deforms from the motion of two basis directions")
        grid = NumberPlane(
            x_range=[-5, 5, 1], y_range=[-5, 5, 1], x_length=8.5, y_length=6.3,
            background_line_style={"stroke_opacity": 0.18}, axis_config={"stroke_opacity": 0.75, "stroke_width": 2},
        )
        self.play(Create(grid))
        self.cc("Treat the plane as a sheet of graph paper. A matrix moves every point according to one consistent linear rule.", 3.0)
        e1 = Arrow(ORIGIN, RIGHT, buff=0, color=VECTOR_A, stroke_width=7)
        e2 = Arrow(ORIGIN, UP, buff=0, color=VECTOR_B, stroke_width=7)
        l1 = MathTex(r"e_1", color=VECTOR_A).next_to(e1.get_end(), UR, buff=0.10)
        l2 = MathTex(r"e_2", color=VECTOR_B).next_to(e2.get_end(), UR, buff=0.10)
        self.play(GrowArrow(e1), GrowArrow(e2), Write(l1), Write(l2))
        A = [[2, 1], [1, 2]]
        self.play(Write(self.eq(r"A=\begin{bmatrix}2&1\\1&2\end{bmatrix}", 0.75, 1.55)))
        self.cc("The first column tells us where e1 goes. The second column tells us where e2 goes.", 2.8)
        self.play(ApplyMatrix(A, grid), ApplyMatrix(A, e1), ApplyMatrix(A, e2), run_time=3.0)
        l1_target = MathTex(r"Ae_1", color=VECTOR_A).next_to(e1.get_end(), UR, buff=0.10)
        l2_target = MathTex(r"Ae_2", color=VECTOR_B).next_to(e2.get_end(), UR, buff=0.10)
        self.play(Transform(l1, l1_target), Transform(l2, l2_target), run_time=0.8)
        self.cc("The grid and both basis arrows deform together. That is what it means for A to act as a linear transformation.", 3.2)
        self.play(Write(self.eq(r"\vec x\mapsto A\vec x", 0.92, -1.15)))
        self.play(Write(self.eq(r"Ae_1=\begin{bmatrix}2\\1\end{bmatrix},\quad Ae_2=\begin{bmatrix}1\\2\end{bmatrix}", 0.59, -2.0)))
        self.wait(2)


class Part3_05_MatrixAdditionAndScaling(MatrixLesson):
    def construct(self):
        self.title("Part III.5 — Matrix Addition and Scalar Multiplication", "Combining or rescaling linear rules")
        self.play(Write(self.eq(r"A=\begin{bmatrix}1&2\\0&1\end{bmatrix},\quad B=\begin{bmatrix}2&-1\\1&3\end{bmatrix}", 0.68, 1.55)))
        self.cc("Matrix addition is position by position: entries in matching locations are added.", 2.7)
        self.play(Write(self.eq(r"A+B=\begin{bmatrix}1+2&2-1\\0+1&1+3\end{bmatrix}", 0.68, 0.55)))
        self.play(Write(self.eq(r"A+B=\begin{bmatrix}3&1\\1&4\end{bmatrix}", 0.88, -0.35)))
        self.cc("The result has the same dimensions because both inputs had the same shape.", 2.4)
        self.play(Write(self.eq(r"2A=\begin{bmatrix}2&4\\0&2\end{bmatrix}", 0.86, -1.25)))
        self.cc("Scalar multiplication multiplies every entry by the same scalar, rescaling the whole linear rule.", 2.8)
        self.play(Write(self.eq(r"\lambda A=[\lambda a_{ij}]", 0.82, -2.05)))
        self.wait(2)


class Part3_06_MatrixMultiplication(MatrixLesson):
    def construct(self):
        self.title("Part III.6 — Matrix Multiplication", "Rows meet columns")
        self.play(Write(self.eq(r"A=\begin{bmatrix}1&2\\0&1\end{bmatrix},\quad B=\begin{bmatrix}2&1\\1&0\end{bmatrix}", 0.66, 1.55)))
        self.cc("Matrix multiplication is not entry-by-entry multiplication. Each output entry is a row of A dotted with a column of B.", 3.1)
        self.play(Write(self.eq(r"AB=\begin{bmatrix}1(2)+2(1)&1(1)+2(0)\\0(2)+1(1)&0(1)+1(0)\end{bmatrix}", 0.56, 0.55)))
        self.play(Write(self.eq(r"AB=\begin{bmatrix}4&1\\1&0\end{bmatrix}", 0.92, -0.35)))
        self.cc("There is also a shape rule: the inner dimensions must agree, and the outer dimensions become the shape of the result.", 3.0)
        self.play(Write(self.eq(r"(m\times n)(n\times p)=(m\times p)", 0.88, -1.35)))
        self.cc("This is the algebraic rule that makes composition of transformations possible.", 2.5)
        self.wait(2)


class Part3_07_CompositionOfTransformations(MatrixLesson):
    def construct(self):
        self.title("Part III.7 — Composition of Transformations", "Why AB usually differs from BA")
        ax = self.axes2d(); self.play(Create(ax))
        v = Arrow(ax.c2p(0, 0), ax.c2p(2, 1), buff=0, color=HIGHLIGHT, stroke_width=7)
        lab = MathTex(r"\vec v", color=HIGHLIGHT).next_to(v.get_end(), UR, buff=0.10)
        self.play(GrowArrow(v), Write(lab))
        self.cc("When two transformations are applied in sequence, the output of the first becomes the input to the second.", 3.0)
        A = [[1, 1], [0, 1]]; B = [[0, -1], [1, 0]]
        self.play(Write(self.eq(r"A=\begin{bmatrix}1&1\\0&1\end{bmatrix},\quad B=\begin{bmatrix}0&-1\\1&0\end{bmatrix}", 0.57, 1.55)))
        self.play(ApplyMatrix(B, v), ApplyMatrix(B, lab), run_time=1.8)
        self.play(Write(self.eq(r"B\vec v=\begin{bmatrix}-1\\2\end{bmatrix}", 0.76, 0.35)))
        self.cc("B rotates the vector a quarter-turn counterclockwise.", 2.2)
        self.play(ApplyMatrix(A, v), ApplyMatrix(A, lab), run_time=1.8)
        self.play(Write(self.eq(r"AB\vec v=\begin{bmatrix}1\\2\end{bmatrix}", 0.76, -0.65)))
        self.cc("Then A shears that result. In the reverse order, BA sends the original vector to negative one, three.", 3.0)
        self.play(Write(self.eq(r"BA\vec v=\begin{bmatrix}-1\\3\end{bmatrix}\neq AB\vec v", 0.73, -1.65)))
        self.cc("Order matters. Matrix multiplication is generally not commutative because transformations generally do not commute.", 3.0)
        self.wait(2)


class Part3_08_IdentityMatrix(MatrixLesson):
    def construct(self):
        self.title("Part III.8 — Identity Matrix", "The neutral transformation")
        ax = self.axes2d(); self.play(Create(ax))
        v = arrow_from(ax, (3, 2), HIGHLIGHT, r"\vec v")
        self.play(GrowArrow(v[0]), Write(v[1]))
        self.play(Write(self.eq(r"I=\begin{bmatrix}1&0\\0&1\end{bmatrix}", 0.82, 1.45)))
        self.cc("The identity matrix does nothing to a vector. It preserves every coordinate exactly.", 2.8)
        self.play(Write(self.eq(r"I\vec v=\vec v", 1.0, 0.45)))
        self.cc("The diagonal ones preserve coordinates. The zeros keep one coordinate from mixing into the other.", 2.8)
        self.play(Write(self.eq(r"AI=A\quad\text{and}\quad IA=A", 0.90, -0.55)))
        self.cc("Identity is the neutral element for matrix multiplication. It will be the target produced by multiplying a matrix by its inverse.", 3.0)
        self.wait(2)


class Part3_09_Transpose(MatrixLesson):
    def construct(self):
        self.title("Part III.9 — Transpose", "Reflecting rows into columns")
        A = Matrix([[1, 2], [3, 4]]).scale(0.92).to_edge(LEFT, buff=1.0)
        AT = Matrix([[1, 3], [2, 4]]).scale(0.92).to_edge(RIGHT, buff=1.0)
        arrow = Arrow(LEFT, RIGHT, buff=0.2, color=HIGHLIGHT, stroke_width=6).move_to([0, 0.2, 0])
        self.play(Write(A)); self.cc("Transpose swaps rows and columns. The main diagonal stays fixed.", 2.7)
        self.play(GrowArrow(arrow), Write(AT))
        self.play(Write(self.eq(r"A^T=\begin{bmatrix}1&3\\2&4\end{bmatrix}", 0.78, -1.15)))
        self.cc("Every off-diagonal entry crosses the diagonal to a new location. Transpose is therefore a very controlled reorganization of the same numbers.", 3.0)
        self.play(Write(self.eq(r"(A^T)^T=A", 0.88, -1.85)))
        self.play(Write(self.eq(r"(AB)^T=B^TA^T", 0.82, -2.45)))
        self.cc("Notice the reversed order in the second identity. Transpose of a product reverses the multiplication order.", 3.0)
        self.wait(2)


class Part3_10_InverseMatrix(MatrixLesson):
    def construct(self):
        self.title("Part III.10 — Inverse Matrix", "The transformation that undoes another transformation")
        ax = self.axes2d(); self.play(Create(ax))
        v = Arrow(ax.c2p(0, 0), ax.c2p(2, 1), buff=0, color=VECTOR_A, stroke_width=7)
        lab = MathTex(r"\vec v", color=VECTOR_A).next_to(v.get_end(), UR, buff=0.10)
        self.play(GrowArrow(v), Write(lab))
        self.play(Write(self.eq(r"A=\begin{bmatrix}2&1\\1&1\end{bmatrix}", 0.80, 1.55)))
        self.cc("An inverse is the matrix that reverses an invertible transformation.", 2.5)
        self.play(ApplyMatrix([[2, 1], [1, 1]], v), ApplyMatrix([[2, 1], [1, 1]], lab), run_time=1.7)
        self.play(Write(self.eq(r"A\vec v=\begin{bmatrix}5\\3\end{bmatrix}", 0.78, 0.45)))
        self.cc("A sends two, one to five, three. Now apply the inverse transformation.", 2.5)
        self.play(Write(self.eq(r"A^{-1}=\begin{bmatrix}1&-1\\-1&2\end{bmatrix}", 0.72, -0.35)))
        self.play(ApplyMatrix([[1, -1], [-1, 2]], v), ApplyMatrix([[1, -1], [-1, 2]], lab), run_time=1.7)
        self.play(Write(self.eq(r"A^{-1}A\vec v=\vec v", 0.84, -1.15)))
        self.cc("The original vector returns. That is the defining geometric idea: A inverse undoes A.", 2.8)
        self.play(Write(self.eq(r"AA^{-1}=A^{-1}A=I", 0.92, -2.0)))
        self.wait(2)


class Part3_11_MatrixMastery(MatrixLesson):
    def construct(self):
        self.title("Part III.11 — Matrix Mastery", "One mental model connecting the whole chapter")
        ax = self.axes2d(); self.play(Create(ax))
        v = arrow_from(ax, (2, 1), HIGHLIGHT, r"\vec x")
        self.play(GrowArrow(v[0]), Write(v[1]))
        self.cc("Think of a matrix as a linear machine acting on vectors. The entries define the rule; the columns reveal what happens to basis directions.", 3.5)
        summary = VGroup(
            Text("Dimensions → multiplication compatibility", font_size=23),
            Text("Ax → rows compute outputs", font_size=23),
            Text("Columns → weighted building blocks", font_size=23),
            Text("AB → composition in order", font_size=23),
            Text("I → do nothing", font_size=23),
            Text("Aᵀ → rows ↔ columns", font_size=23),
            Text("A⁻¹ → undo A", font_size=23),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.17).to_edge(RIGHT, buff=0.12).shift(DOWN * 0.55)
        self.play(LaggedStart(*[Write(item) for item in summary], lag_ratio=0.18), run_time=2.6)
        self.cc("These are not isolated rules. They are different views of the same mathematical object: a linear transformation with algebraic structure.", 3.5)
        self.play(Write(Text("Part III complete: matrices are transformations with structure.", font_size=26, color=YELLOW_B).to_edge(DOWN, buff=0.48)))
        self.wait(3)


__all__ = [name for name in globals() if name.startswith("Part3_") or name == "MatrixLesson"]
