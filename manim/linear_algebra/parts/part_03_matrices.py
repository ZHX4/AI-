from manim import *
from ..utils import *


class MatrixLesson(LessonScene):
    """Shared helpers for the canonical Part III matrix lessons."""

    def axes2d(self):
        ax = Axes(
            x_range=[-5, 5, 1],
            y_range=[-5, 5, 1],
            x_length=8.4,
            y_length=6.5,
            axis_config={"include_numbers": True, "stroke_width": 2},
        )
        ax.to_edge(LEFT, buff=0.32)
        return ax

    def eq(self, latex, scale=0.72, y=0):
        return (
            MathTex(latex)
            .scale(scale)
            .to_edge(RIGHT, buff=0.26)
            .shift(UP * y)
        )

    def matrix(self, entries, scale=0.82, y=0):
        return (
            Matrix(entries, h_buff=1.0, v_buff=0.7)
            .scale(scale)
            .to_edge(RIGHT, buff=0.55)
            .shift(UP * y)
        )


class Part3_01_WhatIsAMatrix(MatrixLesson):
    def construct(self):
        self.title("Part III.1 — What Is a Matrix?", "A structured collection of numbers with geometry hidden inside")
        ax = self.axes2d()
        self.play(Create(ax))
        self.cc("A matrix is not just a rectangular table of numbers. Its layout tells us how those numbers act together on vectors.", 3.3)

        M = self.matrix([[2, 1], [1, 2]], 0.95, 1.15)
        self.play(Write(M))
        self.play(Write(self.eq(r"A=\begin{bmatrix}2&1\\1&2\end{bmatrix}", 0.72, -0.05)))
        self.cc("This is a two-by-two matrix: two rows and two columns. The dimensions tell us what kind of input and output can fit.", 3.4)

        row_box = SurroundingRectangle(M.get_rows()[0], color=VECTOR_A, buff=0.08)
        col_box = SurroundingRectangle(M.get_columns()[0], color=VECTOR_B, buff=0.08)
        self.play(Create(row_box))
        self.cc("A row is a horizontal collection of coefficients. A column is a vertical collection. Later, columns will acquire a direct geometric meaning.", 3.2)
        self.play(Transform(row_box, col_box))
        self.cc("For matrix transformations, the columns are especially important: they describe where the coordinate basis vectors are sent.", 3.3)

        self.play(FadeOut(M), FadeOut(row_box))
        v = arrow_from(ax, (3, 2), HIGHLIGHT, r"\vec x")
        self.play(GrowArrow(v[0]), Write(v[1]))
        self.play(Write(self.eq(r"\vec x\in\mathbb R^2", 0.9, 1.25)))
        self.cc("A two-by-two matrix takes a two-dimensional vector and produces another two-dimensional vector. That input-output structure is the first thing to check before multiplying anything.", 3.7)
        self.wait(2)


class Part3_02_MatrixVectorMultiplication(MatrixLesson):
    def construct(self):
        self.title("Part III.2 — Matrix–Vector Multiplication", "Why the multiplication rule is exactly what geometry needs")
        ax = self.axes2d()
        self.play(Create(ax))
        A = [[2, 1], [1, 2]]
        x = [3, 1]
        u = arrow_from(ax, (3, 1), VECTOR_A, r"\vec x")
        self.play(GrowArrow(u[0]), Write(u[1]))
        self.cc("Take a concrete vector with coordinates three and one. The matrix will turn those two numbers into a new pair.", 2.9)

        self.play(Write(self.eq(r"A=\begin{bmatrix}2&1\\1&2\end{bmatrix},\quad \vec x=\begin{bmatrix}3\\1\end{bmatrix}", 0.60, 1.55)))
        self.play(Write(self.eq(r"A\vec x=\begin{bmatrix}2(3)+1(1)\\1(3)+2(1)\end{bmatrix}", 0.66, 0.45)))
        self.cc("Each output coordinate is a row dot product with the input vector. The first row computes seven; the second row computes five.", 3.4)
        self.play(Write(self.eq(r"A\vec x=\begin{bmatrix}7\\5\end{bmatrix}", 0.92, -0.65)))

        out = arrow_from(ax, (7, 5), HIGHLIGHT, r"A\vec x")
        self.play(GrowArrow(out[0]), Write(out[1]))
        self.cc("The multiplication is therefore a rule from the input vector to an output vector. The matrix is encoding that rule.", 3.1)
        self.play(Write(self.eq(r"\mathbb R^2\xrightarrow{\ A\ }\mathbb R^2", 0.88, -1.65)))
        self.wait(2)


class Part3_03_ColumnsBuildTheOutput(MatrixLesson):
    def construct(self):
        self.title("Part III.3 — Columns Build the Output", "The geometric meaning hiding inside Ax")
        ax = self.axes2d()
        self.play(Create(ax))
        c1 = arrow_from(ax, (2, 1), VECTOR_A, r"\vec c_1")
        c2 = arrow_from(ax, (1, 2), VECTOR_B, r"\vec c_2")
        self.play(GrowArrow(c1[0]), Write(c1[1]), GrowArrow(c2[0]), Write(c2[1]))
        self.cc("Here are the two columns of the matrix. Instead of treating them as a table, watch what happens when they become vectors.", 3.0)

        x1 = Text("3", font_size=34).to_edge(RIGHT, buff=1.6).shift(UP * 1.25)
        x2 = Text("1", font_size=34).to_edge(RIGHT, buff=1.6).shift(UP * 0.35)
        self.play(Write(x1), Write(x2))
        self.play(Write(self.eq(r"A\vec x=x_1\vec c_1+x_2\vec c_2", 0.82, 1.25)))
        self.cc("The input coordinates become weights. We take three copies of the first column and one copy of the second column.", 3.2)

        c1x3 = Arrow(ax.c2p(0, 0), ax.c2p(6, 3), buff=0, color=VECTOR_A, stroke_width=6)
        c2copy = Arrow(ax.c2p(6, 3), ax.c2p(7, 5), buff=0, color=VECTOR_B, stroke_width=6)
        self.play(GrowArrow(c1x3))
        self.cc("Three times the first column gives the intermediate vector six, three.", 2.5)
        self.play(GrowArrow(c2copy))
        self.cc("Then adding one copy of the second column moves us to seven, five. The final arrow is exactly Ax.", 3.1)
        self.play(Write(self.eq(r"3\begin{bmatrix}2\\1\end{bmatrix}+\begin{bmatrix}1\\2\end{bmatrix}=\begin{bmatrix}7\\5\end{bmatrix}", 0.62, -0.75)))
        self.wait(2)


class Part3_04_MatrixAsTransformation(MatrixLesson):
    def construct(self):
        self.title("Part III.4 — A Matrix as a Transformation", "From basis vectors to an entire deformed plane")
        ax = self.axes2d()
        self.play(Create(ax))
        plane_before = NumberPlane(
            x_range=[-5, 5, 1], y_range=[-5, 5, 1],
            x_length=8.4, y_length=6.5,
            background_line_style={"stroke_opacity": 0.18},
            axis_config={"stroke_opacity": 0.0},
        ).move_to(ax)
        self.play(FadeIn(plane_before))
        A = [[2, 1], [1, 2]]
        self.cc("Think of the whole plane as a sheet of graph paper. A matrix can move every point consistently, not one point at a time.", 3.3)

        e1 = arrow_from(ax, (1, 0), VECTOR_A, r"e_1")
        e2 = arrow_from(ax, (0, 1), VECTOR_B, r"e_2")
        self.play(GrowArrow(e1[0]), Write(e1[1]), GrowArrow(e2[0]), Write(e2[1]))
        self.play(Write(self.eq(r"Ae_1=\begin{bmatrix}2\\1\end{bmatrix},\quad Ae_2=\begin{bmatrix}1\\2\end{bmatrix}", 0.61, 1.55)))
        self.cc("The most important shortcut is this: to understand a linear transformation, first see where the basis vectors go. Those images become the columns of the matrix.", 3.7)

        target_plane = NumberPlane(
            x_range=[-5, 5, 1], y_range=[-5, 5, 1],
            x_length=8.4, y_length=6.5,
            background_line_style={"stroke_opacity": 0.16},
            axis_config={"stroke_opacity": 0.0},
        ).move_to(ax)
        try:
            self.play(Transform(plane_before, target_plane), run_time=2.5)
        except Exception:
            self.play(FadeOut(plane_before), FadeIn(target_plane), run_time=1.0)
        new1 = arrow_from(ax, (2, 1), VECTOR_A, r"Ae_1")
        new2 = arrow_from(ax, (1, 2), VECTOR_B, r"Ae_2")
        self.play(Transform(e1[0], new1[0]), Transform(e2[0], new2[0]))
        self.cc("The grid is transformed along with the basis directions. This is the geometric meaning of multiplying vectors by A.", 3.3)
        self.play(Write(self.eq(r"\vec x\mapsto A\vec x", 0.95, -1.20)))
        self.wait(2)


class Part3_05_MatrixAdditionAndScaling(MatrixLesson):
    def construct(self):
        self.title("Part III.5 — Matrix Addition and Scalar Multiplication", "Combining transformations entry by entry")
        A = Matrix([[1, 2], [0, 1]]).scale(0.82).to_edge(RIGHT, buff=2.0).shift(UP * 1.1)
        B = Matrix([[2, -1], [1, 3]]).scale(0.82).to_edge(RIGHT, buff=0.8).shift(UP * 1.1)
        plus = MathTex("+").scale(1.0).move_to([4.4, 1.15, 0])
        self.play(Write(A), Write(plus), Write(B))
        self.cc("Matrix addition is deliberately simple: entries in matching positions are added.", 2.8)
        C = Matrix([[3, 1], [1, 4]]).scale(0.82).to_edge(RIGHT, buff=1.35).shift(DOWN * 0.55)
        eq = MathTex(r"A+B=\begin{bmatrix}3&1\\1&4\end{bmatrix}").scale(0.78).to_edge(RIGHT, buff=0.8).shift(DOWN * 0.55)
        self.play(FadeOut(A), FadeOut(plus), FadeOut(B), Write(C), Write(eq))
        self.cc("The result is another two-by-two matrix because the two matrices had the same dimensions.", 2.8)

        twoA = Matrix([[2, 4], [0, 2]]).scale(0.82).to_edge(RIGHT, buff=1.35).shift(DOWN * 1.65)
        self.play(FadeOut(C), FadeOut(eq))
        self.play(Write(self.eq(r"2A=\begin{bmatrix}2&4\\0&2\end{bmatrix}", 0.82, -0.9)), Write(twoA))
        self.cc("Scalar multiplication simply scales every entry. Later, this same operation will correspond to scaling the effect of a transformation.", 3.0)
        self.play(Write(self.eq(r"\lambda A\ \text{means}\ \text{every entry of }A\text{ is multiplied by }\lambda", 0.63, -2.0)))
        self.wait(2)


class Part3_06_MatrixMultiplication(MatrixLesson):
    def construct(self):
        self.title("Part III.6 — Matrix Multiplication", "The rule that makes composition possible")
        self.cc("Matrix multiplication is not entry-by-entry multiplication. Each output entry is a row from the first matrix dotted with a column from the second.", 3.4)
        self.play(Write(self.eq(r"A=\begin{bmatrix}1&2\\0&1\end{bmatrix},\quad B=\begin{bmatrix}2&1\\1&0\end{bmatrix}", 0.65, 1.45)))
        self.play(Write(self.eq(r"AB=\begin{bmatrix}1(2)+2(1)&1(1)+2(0)\\0(2)+1(1)&0(1)+1(0)\end{bmatrix}", 0.58, 0.45)))
        self.cc("Compute the first row against each column. This produces the first row of the answer.", 2.7)
        self.play(Write(self.eq(r"AB=\begin{bmatrix}4&1\\1&0\end{bmatrix}", 0.90, -0.45)))
        self.cc("Notice the shape rule too: a two-by-two matrix multiplied by a two-by-two matrix stays two-by-two. In general, the inner dimensions must match.", 3.4)
        self.play(Write(self.eq(r"(m\times n)(n\times p)=(m\times p)", 0.86, -1.55)))

        ax = self.axes2d().shift(LEFT * 0.05)
        self.play(Create(ax))
        v = arrow_from(ax, (2, 1), HIGHLIGHT, r"\vec v")
        self.play(GrowArrow(v[0]), Write(v[1]))
        self.cc("The algebra is only half the story. Matrix multiplication matters because it tells us how one transformation can feed directly into another.", 3.0)
        self.wait(2)


class Part3_07_CompositionOfTransformations(MatrixLesson):
    def construct(self):
        self.title("Part III.7 — Composition of Transformations", "Why AB usually differs from BA")
        ax = self.axes2d()
        self.play(Create(ax))
        v = arrow_from(ax, (2, 1), HIGHLIGHT, r"\vec v")
        self.play(GrowArrow(v[0]), Write(v[1]))
        self.cc("Imagine applying two transformations one after another. The output of the first becomes the input to the second.", 3.1)

        A = MathTex(r"A=\begin{bmatrix}1&1\\0&1\end{bmatrix}").scale(0.75).to_edge(RIGHT, buff=0.75).shift(UP * 1.55)
        B = MathTex(r"B=\begin{bmatrix}0&-1\\1&0\end{bmatrix}").scale(0.75).to_edge(RIGHT, buff=0.75).shift(UP * 0.65)
        self.play(Write(A), Write(B))
        self.play(Write(self.eq(r"B\vec v=\begin{bmatrix}-1\\2\end{bmatrix}", 0.73, -0.15)))
        self.cc("First apply B: this rotates the vector a quarter turn counterclockwise.", 2.6)
        self.play(Write(self.eq(r"AB\vec v=A\begin{bmatrix}-1\\2\end{bmatrix}=\begin{bmatrix}1\\2\end{bmatrix}", 0.66, -1.15)))
        self.cc("Then apply A. The final result is one vector produced by the composition A after B.", 3.0)
        self.play(Write(self.eq(r"AB\vec v\neq BA\vec v\ \text{in general}", 0.80, -2.05)))
        self.cc("Order matters. Matrix multiplication records the order in which transformations are composed.", 3.0)
        self.wait(2)


class Part3_08_IdentityMatrix(MatrixLesson):
    def construct(self):
        self.title("Part III.8 — The Identity Matrix", "The transformation that changes nothing")
        ax = self.axes2d()
        self.play(Create(ax))
        v = arrow_from(ax, (3, 1), HIGHLIGHT, r"\vec v")
        self.play(GrowArrow(v[0]), Write(v[1]))
        I = Matrix([[1, 0], [0, 1]]).scale(0.92).to_edge(RIGHT, buff=0.7).shift(UP * 1.35)
        self.play(Write(I))
        self.cc("The identity matrix is the matrix version of doing nothing. It leaves every vector exactly where it already is.", 3.0)
        self.play(Write(self.eq(r"I\vec v=\vec v", 1.05, 0.25)))
        self.play(Write(self.eq(r"I=\begin{bmatrix}1&0\\0&1\end{bmatrix}", 0.73, -0.85)))
        self.cc("The ones preserve each coordinate; the zeros prevent coordinates from mixing into the wrong places.", 3.1)
        self.play(Write(self.eq(r"AI=A\quad\text{and}\quad IA=A", 0.90, -1.75)))
        self.cc("Identity also acts as the neutral element for matrix multiplication, which is why it becomes essential when we define inverses.", 3.2)
        self.wait(2)


class Part3_09_Transpose(MatrixLesson):
    def construct(self):
        self.title("Part III.9 — Transpose", "Turning rows into columns")
        A = Matrix([[1, 2], [3, 4]]).scale(0.95).to_edge(LEFT, buff=1.1)
        arrow = Arrow(LEFT, RIGHT, buff=0.2, color=HIGHLIGHT, stroke_width=6)
        arrow.move_to([0, 0.15, 0])
        AT = Matrix([[1, 3], [2, 4]]).scale(0.95).to_edge(RIGHT, buff=1.1)
        self.play(Write(A))
        self.cc("Transpose means reflect the matrix across its main diagonal: rows become columns and columns become rows.", 3.1)
        self.play(GrowArrow(arrow), Write(AT))
        self.play(Write(self.eq(r"A^T=\begin{bmatrix}1&3\\2&4\end{bmatrix}", 0.78, -1.25)))
        self.cc("The entry in row one, column two of A becomes the entry in row two, column one of the transpose. The diagonal stays fixed.", 3.3)
        self.play(Write(self.eq(r"(AB)^T=B^T A^T", 0.92, -2.1)))
        self.cc("A subtle but crucial property is that transpose reverses multiplication order. This will matter later for symmetry, least squares, and many geometric arguments.", 3.4)
        self.wait(2)


class Part3_10_InverseMatrix(MatrixLesson):
    def construct(self):
        self.title("Part III.10 — The Inverse Matrix", "Undoing a linear transformation")
        ax = self.axes2d()
        self.play(Create(ax))
        A = [[2, 1], [1, 1]]
        v = arrow_from(ax, (2, 1), VECTOR_A, r"\vec v")
        self.play(GrowArrow(v[0]), Write(v[1]))
        self.cc("An inverse is the matrix that reverses what A did. If A moves a vector forward, A inverse should bring it back.", 3.2)
        self.play(Write(self.eq(r"A=\begin{bmatrix}2&1\\1&1\end{bmatrix}", 0.80, 1.45)))
        self.play(Write(self.eq(r"A^{-1}=\begin{bmatrix}1&-1\\-1&2\end{bmatrix}", 0.73, 0.65)))
        self.cc("For this particular matrix, multiplying by the inverse gives back the identity. We can verify the first entry directly: two times one plus one times negative one equals one.", 3.5)
        self.play(Write(self.eq(r"AA^{-1}=A^{-1}A=I", 0.95, -0.35)))

        target = arrow_from(ax, (5, 3), HIGHLIGHT, r"A\vec v")
        self.play(GrowArrow(target[0]), Write(target[1]))
        self.play(Write(self.eq(r"A^{-1}(A\vec v)=\vec v", 0.84, -1.25)))
        self.cc("The key idea is composition: A followed by A inverse is the identity, so the original vector returns unchanged.", 3.3)
        self.play(Write(self.eq(r"A\ \text{invertible}\ \Longleftrightarrow\ \text{an undoing transformation exists}", 0.58, -2.15)))
        self.wait(2)


class Part3_11_MatricesMastery(MatrixLesson):
    def construct(self):
        self.title("Part III.11 — Matrix Mastery", "One mental model connecting the whole chapter")
        ax = self.axes2d()
        self.play(Create(ax))
        v = arrow_from(ax, (2, 1), HIGHLIGHT, r"\vec x")
        self.play(GrowArrow(v[0]), Write(v[1]))
        self.cc("A matrix is best understood as a machine that acts on vectors. The entries describe the rule; the columns reveal its action on basis vectors.", 3.4)

        flow = VGroup(
            MathTex(r"\vec x"),
            MathTex(r"\xrightarrow{\ A\ }") ,
            MathTex(r"A\vec x"),
            MathTex(r"\xrightarrow{\ A^{-1}\ }") ,
            MathTex(r"\vec x"),
        ).scale(0.75).arrange(RIGHT, buff=0.22).to_edge(RIGHT, buff=0.28).shift(UP * 1.25)
        self.play(LaggedStart(*[Write(x) for x in flow], lag_ratio=0.25), run_time=2.5)
        self.cc("Matrix-vector multiplication gives the action. Addition and scalar multiplication combine or rescale matrices. Multiplication composes them.", 3.8)

        summary = VGroup(
            Text("Dimensions → compatibility", font_size=25),
            Text("Columns → basis-vector images", font_size=25),
            Text("AB → composition", font_size=25),
            Text("I → do nothing", font_size=25),
            Text("Aᵀ → swap rows and columns", font_size=25),
            Text("A⁻¹ → undo A", font_size=25),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.22).to_edge(RIGHT, buff=0.2).shift(DOWN * 0.85)
        self.play(Write(summary))
        self.cc("These are not separate tricks. They are different ways of describing the same linear-algebra machine. The next part will use this language to study systems of equations.", 4.0)
        self.play(Write(Text("Part III complete: matrices are transformations, not just tables.", font_size=27, color=YELLOW_B).to_edge(DOWN, buff=0.52)))
        self.wait(3)


__all__ = [name for name in globals() if name.startswith("Part3_") or name == "MatrixLesson"]
