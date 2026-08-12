from manim import *
from ..utils import *


class MatrixLesson(LessonScene):
    """Canonical shared helpers for Part III."""

    def axes2d(self):
        ax = Axes(
            x_range=[-8, 8, 1],
            y_range=[-6, 6, 1],
            x_length=8.5,
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
        ax = self.axes2d()
        self.play(Create(ax))
        self.cc("A matrix is a rectangular arrangement of numbers, but its real purpose is to encode how coordinates are combined or transformed.", 3.2)
        M = Matrix([[2, 1], [1, 2]]).scale(0.95).to_edge(RIGHT, buff=0.65).shift(UP * 1.1)
        self.play(Write(M))
        self.play(Write(self.eq(r"A=\begin{bmatrix}2&1\\1&2\end{bmatrix}", 0.72, -0.05)))
        self.cc("This is a two-by-two matrix: two rows and two columns. Its shape already tells us that it works naturally with two-dimensional vectors.", 3.2)
        self.play(Write(self.eq(r"2\times2\;\text{matrix}:\quad\mathbb R^2\to\mathbb R^2", 0.72, -1.0)))
        self.cc("The rows tell us how output coordinates are calculated. The columns will give us an even more geometric interpretation in the next lessons.", 3.2)
        self.wait(2)


class Part3_02_MatrixVectorMultiplication(MatrixLesson):
    def construct(self):
        self.title("Part III.2 — Matrix–Vector Multiplication", "Rows compute the output coordinates")
        ax = self.axes2d()
        self.play(Create(ax))
        x = arrow_from(ax, (3, 1), VECTOR_A, r"\vec x")
        self.play(GrowArrow(x[0]), Write(x[1]))
        self.cc("Let the input vector be three, one. We now let the matrix turn those two input coordinates into a new vector.", 2.8)
        self.play(Write(self.eq(r"A=\begin{bmatrix}2&1\\1&2\end{bmatrix},\quad \vec x=\begin{bmatrix}3\\1\end{bmatrix}", 0.58, 1.55)))
        self.play(Write(self.eq(r"A\vec x=\begin{bmatrix}2(3)+1(1)\\1(3)+2(1)\end{bmatrix}", 0.63, 0.65)))
        self.cc("The first row produces seven. The second row produces five. Each output coordinate is a dot product between one row and the input vector.", 3.4)
        self.play(Write(self.eq(r"A\vec x=\begin{bmatrix}7\\5\end{bmatrix}", 0.92, -0.35)))
        out = arrow_from(ax, (7, 5), HIGHLIGHT, r"A\vec x")
        self.play(GrowArrow(out[0]), Write(out[1]))
        self.cc("The arrow has moved from the input vector to its output. Matrix multiplication is therefore a function from vectors to vectors.", 3.2)
        self.play(Write(self.eq(r"\vec x\longmapsto A\vec x", 0.92, -1.55)))
        self.wait(2)


class Part3_03_ColumnsBuildTheOutput(MatrixLesson):
    def construct(self):
        self.title("Part III.3 — Columns Build the Output", "The column picture of matrix–vector multiplication")
        ax = self.axes2d()
        self.play(Create(ax))
        c1 = arrow_from(ax, (2, 1), VECTOR_A, r"\vec c_1")
        c2 = arrow_from(ax, (1, 2), VECTOR_B, r"\vec c_2")
        self.play(GrowArrow(c1[0]), Write(c1[1]), GrowArrow(c2[0]), Write(c2[1]))
        self.cc("The same multiplication can be understood column by column. The input coordinates become weights placed on the matrix columns.", 3.2)
        self.play(Write(self.eq(r"A\vec x=x_1\vec c_1+x_2\vec c_2", 0.82, 1.45)))
        first = Arrow(ax.c2p(0, 0), ax.c2p(6, 3), buff=0, color=VECTOR_A, stroke_width=6)
        second = Arrow(ax.c2p(6, 3), ax.c2p(7, 5), buff=0, color=VECTOR_B, stroke_width=6)
        self.play(GrowArrow(first))
        self.cc("Three times the first column gives six, three.", 2.3)
        self.play(GrowArrow(second))
        self.cc("Adding one copy of the second column moves to seven, five. This is the same Ax we calculated using rows.", 3.1)
        self.play(Write(self.eq(r"3\begin{bmatrix}2\\1\end{bmatrix}+\begin{bmatrix}1\\2\end{bmatrix}=\begin{bmatrix}7\\5\end{bmatrix}", 0.60, -0.75)))
        self.play(Write(self.eq(r"\text{columns}=\text{images of basis directions}", 0.66, -1.85)))
        self.wait(2)


class Part3_04_MatrixAsTransformation(MatrixLesson):
    def construct(self):
        self.title("Part III.4 — Matrix as a Transformation", "A whole plane can move according to two basis directions")
        plane_grid = NumberPlane(
            x_range=[-5, 5, 1], y_range=[-5, 5, 1],
            x_length=8.5, y_length=6.3,
            background_line_style={"stroke_opacity": 0.18},
            axis_config={"stroke_opacity": 0.75, "stroke_width": 2},
        )
        plane_grid.to_edge(LEFT, buff=0.28)
        self.play(Create(plane_grid))
        self.cc("Imagine the plane as a rubber sheet. A matrix moves every point according to the same linear rule.", 2.9)
        e1 = arrow_from(plane_grid, (1, 0), VECTOR_A, r"e_1")
        e2 = arrow_from(plane_grid, (0, 1), VECTOR_B, r"e_2")
        self.play(GrowArrow(e1[0]), Write(e1[1]), GrowArrow(e2[0]), Write(e2[1]))
        self.play(Write(self.eq(r"A=\begin{bmatrix}2&1\\1&2\end{bmatrix}", 0.75, 1.55)))
        self.cc("A sends the first basis vector to the first column, and the second basis vector to the second column.", 3.0)
        self.play(ApplyMatrix([[2, 1], [1, 2]], plane_grid), ApplyMatrix([[2, 1], [1, 2]], e1[0]), ApplyMatrix([[2, 1], [1, 2]], e2[0]), run_time=3.0)
        self.cc("The grid and the basis arrows deform together. That is the geometric meaning of a matrix acting on the plane.", 3.4)
        self.play(Write(self.eq(r"\vec x\mapsto A\vec x", 0.92, -1.15)))
        self.play(Write(self.eq(r"Ae_1=\begin{bmatrix}2\\1\end{bmatrix},\quad Ae_2=\begin{bmatrix}1\\2\end{bmatrix}", 0.59, -2.0)))
        self.wait(2)


class Part3_05_MatrixAdditionAndScaling(MatrixLesson):
    def construct(self):
        self.title("Part III.5 — Matrix Addition and Scaling", "Combining or rescaling linear rules")
        self.play(Write(self.eq(r"A=\begin{bmatrix}1&2\\0&1\end{bmatrix},\quad B=\begin{bmatrix}2&-1\\1&3\end{bmatrix}", 0.68, 1.55)))
        self.cc("Matrix addition works position by position. We add entries that occupy the same row and column.", 2.8)
        self.play(Write(self.eq(r"A+B=\begin{bmatrix}1+2&2-1\\0+1&1+3\end{bmatrix}", 0.70, 0.55)))
        self.play(Write(self.eq(r"A+B=\begin{bmatrix}3&1\\1&4\end{bmatrix}", 0.88, -0.35)))
        self.cc("The result has the same shape because both inputs had the same dimensions.", 2.5)
        self.play(Write(self.eq(r"2A=\begin{bmatrix}2&4\\0&2\end{bmatrix}", 0.86, -1.25)))
        self.cc("Scalar multiplication is equally direct: multiply every entry by the scalar. Conceptually, this rescales the strength of the entire linear rule.", 3.0)
        self.play(Write(self.eq(r"\lambda A=[\lambda a_{ij}]", 0.82, -2.05)))
        self.wait(2)


class Part3_06_MatrixMultiplication(MatrixLesson):
    def construct(self):
        self.title("Part III.6 — Matrix Multiplication", "Rows meet columns")
        self.play(Write(self.eq(r"A=\begin{bmatrix}1&2\\0&1\end{bmatrix},\quad B=\begin{bmatrix}2&1\\1&0\end{bmatrix}", 0.66, 1.55)))
        self.cc("Matrix multiplication is not entry-by-entry multiplication. Each answer entry is a row of A dotted with a column of B.", 3.2)
        self.play(Write(self.eq(r"AB=\begin{bmatrix}1(2)+2(1)&1(1)+2(0)\\0(2)+1(1)&0(1)+1(0)\end{bmatrix}", 0.56, 0.55)))
        self.play(Write(self.eq(r"AB=\begin{bmatrix}4&1\\1&0\end{bmatrix}", 0.92, -0.35)))
        self.cc("There is also a dimension rule. The inner dimensions must agree, and the outer dimensions determine the shape of the result.", 3.1)
        self.play(Write(self.eq(r"(m\times n)(n\times p)=(m\times p)", 0.88, -1.35)))
        self.cc("This rule is exactly what allows one matrix transformation to feed into another.", 2.6)
        self.wait(2)


class Part3_07_CompositionAndOrder(MatrixLesson):
    def construct(self):
        self.title("Part III.7 — Composition and Order", "Why AB and BA are generally different")
        ax = self.axes2d()
        self.play(Create(ax))
        v = arrow_from(ax, (2, 1), HIGHLIGHT, r"\vec v")
        self.play(GrowArrow(v[0]), Write(v[1]))
        A = [[1, 1], [0, 1]]
        B = [[0, -1], [1, 0]]
        self.play(Write(self.eq(r"A=\begin{bmatrix}1&1\\0&1\end{bmatrix},\quad B=\begin{bmatrix}0&-1\\1&0\end{bmatrix}", 0.58, 1.55)))
        self.cc("B is a quarter-turn rotation. A is a shear. We will apply them in a specific order and watch the difference.", 3.0)
        self.play(ApplyMatrix(B, v[0]), run_time=1.8)
        self.play(Write(self.eq(r"B\vec v=\begin{bmatrix}-1\\2\end{bmatrix}", 0.78, 0.35)))
        self.cc("First B rotates the vector from two, one to negative one, two.", 2.5)
        self.play(ApplyMatrix(A, v[0]), run_time=1.8)
        self.play(Write(self.eq(r"AB\vec v=\begin{bmatrix}1\\2\end{bmatrix}", 0.78, -0.65)))
        self.cc("Now A shears that result to one, two. In reverse order, BA sends the original vector to negative one, three.", 3.2)
        self.play(Write(self.eq(r"BA\vec v=\begin{bmatrix}-1\\3\end{bmatrix}\neq AB\vec v", 0.73, -1.65)))
        self.cc("So matrix multiplication is generally not commutative. The order of the transformations is part of the mathematics.", 3.2)
        self.wait(2)


class Part3_08_IdentityMatrix(MatrixLesson):
    def construct(self):
        self.title("Part III.8 — Identity Matrix", "The neutral transformation")
        ax = self.axes2d()
        self.play(Create(ax))
        v = arrow_from(ax, (3, 2), HIGHLIGHT, r"\vec v")
        self.play(GrowArrow(v[0]), Write(v[1]))
        self.play(Write(self.eq(r"I=\begin{bmatrix}1&0\\0&1\end{bmatrix}", 0.82, 1.45)))
        self.cc("The identity matrix does nothing to a vector. It preserves each coordinate exactly.", 2.8)
        self.play(Write(self.eq(r"I\vec v=\vec v", 1.0, 0.45)))
        self.cc("The diagonal ones preserve the coordinates. The zeros prevent one coordinate from leaking into the other.", 3.0)
        self.play(Write(self.eq(r"AI=A\quad\text{and}\quad IA=A", 0.90, -0.55)))
        self.cc("Identity is therefore the multiplicative neutral element for matrices, just as the number one is for ordinary multiplication.", 3.1)
        self.wait(2)


class Part3_09_Transpose(MatrixLesson):
    def construct(self):
        self.title("Part III.9 — Transpose", "Reflecting the matrix across its main diagonal")
        A = Matrix([[1, 2], [3, 4]]).scale(0.92).to_edge(LEFT, buff=1.0)
        AT = Matrix([[1, 3], [2, 4]]).scale(0.92).to_edge(RIGHT, buff=1.0)
        arrow = Arrow(LEFT, RIGHT, buff=0.2, color=HIGHLIGHT, stroke_width=6).move_to([0, 0.2, 0])
        self.play(Write(A))
        self.cc("Transpose swaps rows and columns. Geometrically, it is like reflecting the entries across the main diagonal.", 2.9)
        self.play(GrowArrow(arrow), Write(AT))
        self.play(Write(self.eq(r"A^T=\begin{bmatrix}1&3\\2&4\end{bmatrix}", 0.78, -1.15)))
        self.cc("The diagonal entries stay in place. Every off-diagonal entry crosses the diagonal to a new position.", 2.8)
        self.play(Write(self.eq(r"(A^T)^T=A", 0.88, -1.85)))
        self.play(Write(self.eq(r"(AB)^T=B^TA^T", 0.82, -2.45)))
        self.cc("Transpose also reverses multiplication order. That reversal is a recurring structural fact throughout linear algebra.", 3.1)
        self.wait(2)


class Part3_10_InverseMatrix(MatrixLesson):
    def construct(self):
        self.title("Part III.10 — Inverse Matrix", "The transformation that undoes another transformation")
        ax = self.axes2d()
        self.play(Create(ax))
        v = arrow_from(ax, (2, 1), VECTOR_A, r"\vec v")
        self.play(GrowArrow(v[0]), Write(v[1]))
        self.play(Write(self.eq(r"A=\begin{bmatrix}2&1\\1&1\end{bmatrix}", 0.80, 1.55)))
        self.cc("For an invertible matrix, there is another matrix that reverses its action. We call it the inverse.", 2.9)
        self.play(ApplyMatrix([[2, 1], [1, 1]], v[0]), run_time=1.7)
        self.play(Write(self.eq(r"A\vec v=\begin{bmatrix}5\\3\end{bmatrix}", 0.78, 0.45)))
        self.cc("A sends our vector two, one to five, three. Now we apply the inverse transformation.", 2.8)
        self.play(Write(self.eq(r"A^{-1}=\begin{bmatrix}1&-1\\-1&2\end{bmatrix}", 0.72, -0.35)))
        self.play(ApplyMatrix([[1, -1], [-1, 2]], v[0]), run_time=1.7)
        self.play(Write(self.eq(r"A^{-1}A\vec v=\vec v", 0.84, -1.15)))
        self.cc("The vector returns to its original position. Algebraically, an inverse satisfies A inverse times A equals the identity.", 3.1)
        self.play(Write(self.eq(r"AA^{-1}=A^{-1}A=I", 0.92, -2.0)))
        self.wait(2)


class Part3_11_MatrixMastery(MatrixLesson):
    def construct(self):
        self.title("Part III.11 — Matrix Mastery", "One mental model for the whole matrix chapter")
        ax = self.axes2d()
        self.play(Create(ax))
        v = arrow_from(ax, (2, 1), HIGHLIGHT, r"\vec x")
        self.play(GrowArrow(v[0]), Write(v[1]))
        self.cc("The safest way to think about matrices is as linear machines acting on vectors. The entries define the machine; the columns reveal what it does to basis directions.", 3.6)
        summary = VGroup(
            Text("Dimensions → what can multiply what", font_size=24),
            Text("Ax → rows compute outputs", font_size=24),
            Text("Columns → weighted building blocks", font_size=24),
            Text("AB → composition in order", font_size=24),
            Text("I → do nothing", font_size=24),
            Text("Aᵀ → rows ↔ columns", font_size=24),
            Text("A⁻¹ → undo A", font_size=24),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.18).to_edge(RIGHT, buff=0.15).shift(DOWN * 0.55)
        self.play(LaggedStart(*[Write(item) for item in summary], lag_ratio=0.18), run_time=2.6)
        self.cc("These are not isolated rules. They are different views of the same object: a linear transformation. Part IV will use matrices to describe and solve systems of equations.", 4.0)
        self.play(Write(Text("Part III complete: matrices are transformations with algebraic structure.", font_size=26, color=YELLOW_B).to_edge(DOWN, buff=0.48)))
        self.wait(3)


__all__ = [name for name in globals() if name.startswith("Part3_") or name == "MatrixLesson"]
