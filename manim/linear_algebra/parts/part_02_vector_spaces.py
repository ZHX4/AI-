from manim import *
from ..utils import *


class VectorSpaceLesson(LessonScene):
    def axes2d(self):
        ax = Axes(
            x_range=[-5, 5, 1],
            y_range=[-5, 5, 1],
            x_length=8.6,
            y_length=7.0,
            axis_config={"include_numbers": True, "stroke_width": 2},
        )
        ax.to_edge(LEFT, buff=0.35)
        return ax

    def eq(self, latex, scale=0.72, y=0):
        return MathTex(latex).scale(scale).to_edge(RIGHT, buff=0.28).shift(UP * y)

    def span_point(self, ax, coords, color=HIGHLIGHT):
        return Dot(ax.c2p(*coords), radius=0.065, color=color)


class Part2_01_Span(VectorSpaceLesson):
    def construct(self):
        self.title("Part II.1 — Span", "Which vectors can we build from a collection of vectors?")
        ax = self.axes2d()
        self.play(Create(ax))
        u = arrow_from(ax, (2, 1), VECTOR_A, r"\vec u")
        v = arrow_from(ax, (-1, 2), VECTOR_B, r"\vec v")
        self.play(GrowArrow(u[0]), Write(u[1]), GrowArrow(v[0]), Write(v[1]))
        self.cc("We now ask a broader question: if these are the vectors we are allowed to use, what other vectors can we create?", 3.2)

        target = arrow_from(ax, (3, 5), HIGHLIGHT, r"\vec w")
        self.play(GrowArrow(target[0]), Write(target[1]))
        self.play(Write(self.eq(r"\vec w=2\vec u+1\vec v", 0.86, 1.5)))
        self.cc("This particular vector is reachable because it is a linear combination of u and v.", 2.9)

        grid = VGroup()
        for a in range(-4, 5):
            for b in range(-4, 5):
                x = 2 * a - b
                y = a + 2 * b
                if -5 <= x <= 5 and -5 <= y <= 5:
                    grid.add(self.span_point(ax, (x, y), GREEN_C))
        self.play(LaggedStart(*[FadeIn(p, scale=0.5) for p in grid], lag_ratio=0.015), run_time=3)
        self.cc("Because u and v point in independent directions, their combinations spread across the whole plane.", 3.1)
        self.play(Write(self.eq(r"\operatorname{span}\{\vec u,\vec v\}=\mathbb R^2", 0.8, 0.2)))
        self.cc("The span is the set of every vector reachable by all allowed linear combinations.", 3.1)
        self.play(FadeOut(grid), FadeOut(target))
        self.cc("Span is therefore not one vector. It is a whole set of attainable vectors.", 2.8)
        self.wait(2)


class Part2_02_LinearDependence(VectorSpaceLesson):
    def construct(self):
        self.title("Part II.2 — Linear Dependence", "When one vector is redundant")
        ax = self.axes2d()
        self.play(Create(ax))
        u = arrow_from(ax, (2, 1), VECTOR_A, r"\vec u")
        v = arrow_from(ax, (4, 2), VECTOR_B, r"\vec v")
        self.play(GrowArrow(u[0]), Write(u[1]), GrowArrow(v[0]), Write(v[1]))
        self.cc("These two vectors look different, but one is just a scaled copy of the other.", 3)
        self.play(Write(self.eq(r"\vec v=2\vec u", 0.9, 1.4)))
        self.cc("So v contributes no genuinely new direction. Anything made with v could already be made with u.", 3.2)

        line = DashedLine(ax.c2p(-5, -2.5), ax.c2p(5, 2.5), color=GREY_B, stroke_opacity=0.6)
        self.play(Create(line))
        self.cc("All linear combinations stay on one line because the two vectors contain only one direction of information.", 3)
        self.play(Write(self.eq(r"a\vec u+b\vec v=(a+2b)\vec u", 0.78, -0.1)))
        self.cc("Two coefficients collapse into one effective coefficient. That is the algebraic fingerprint of redundancy.", 3.2)
        self.play(Write(self.eq(r"\alpha\vec u+\beta\vec v=\vec 0", 0.82, -1.5)))
        self.cc("For example, choosing alpha = 2 and beta = -1 gives a nontrivial combination equal to zero.", 3)
        self.wait(2)


class Part2_03_LinearIndependence(VectorSpaceLesson):
    def construct(self):
        self.title("Part II.3 — Linear Independence", "No vector can be rebuilt from the others")
        ax = self.axes2d()
        self.play(Create(ax))
        u = arrow_from(ax, (2, 1), VECTOR_A, r"\vec u")
        v = arrow_from(ax, (1, 2), VECTOR_B, r"\vec v")
        self.play(GrowArrow(u[0]), Write(u[1]), GrowArrow(v[0]), Write(v[1]))
        self.cc("Here the two vectors point in genuinely different directions. Neither is a scalar multiple of the other.", 3)
        self.play(Write(self.eq(r"c_1\vec u+c_2\vec v=\vec 0", 0.9, 1.4)))
        self.cc("To test independence, ask whether a combination can produce zero without all coefficients being zero.", 3.1)
        self.play(Write(self.eq(r"\Longrightarrow c_1=0,\ c_2=0", 0.92, 0.2)))
        self.cc("For these two vectors, the only way to cancel perfectly is to use zero of each.", 2.8)

        det_box = SurroundingRectangle(MathTex(r"\det\begin{bmatrix}2&1\\1&2\end{bmatrix}=3"), color=YELLOW_C, buff=0.25)
        det_formula = MathTex(r"\det\begin{bmatrix}2&1\\1&2\end{bmatrix}=3").scale(0.78).to_edge(RIGHT).shift(DOWN * 1.2)
        self.play(Write(det_formula))
        self.cc("In two dimensions, a nonzero determinant is another way to detect that two vectors provide two independent directions.", 3.1)
        self.wait(2)


class Part2_04_Basis(VectorSpaceLesson):
    def construct(self):
        self.title("Part II.4 — Basis", "A minimal coordinate system built from vectors")
        ax = self.axes2d()
        self.play(Create(ax))
        e1 = arrow_from(ax, (1, 0), VECTOR_A, r"\vec e_1")
        e2 = arrow_from(ax, (0, 1), VECTOR_B, r"\vec e_2")
        self.play(GrowArrow(e1[0]), Write(e1[1]), GrowArrow(e2[0]), Write(e2[1]))
        self.cc("A basis is a collection that does two jobs: it spans the space and its vectors are linearly independent.", 3.4)
        self.play(Write(self.eq(r"\text{basis}=\text{span}+\text{independence}", 0.77, 1.45)))
        self.cc("The standard basis of the plane uses one pure horizontal direction and one pure vertical direction.", 3)

        p = self.span_point(ax, (3, -2), HIGHLIGHT)
        self.play(FadeIn(p))
        self.play(Write(self.eq(r"\begin{bmatrix}3\\-2\end{bmatrix}=3\vec e_1-2\vec e_2", 0.76, 0.1)))
        self.cc("The coefficients become the coordinates of the point in that basis.", 3)

        self.play(Write(self.eq(r"\text{every vector}\ \longleftrightarrow\ \text{one coordinate pair}", 0.66, -1.35)))
        self.cc("That uniqueness is exactly why bases are so useful: they remove ambiguity from representation.", 3.1)
        self.wait(2)


class Part2_05_Dimension(VectorSpaceLesson):
    def construct(self):
        self.title("Part II.5 — Dimension", "How many independent directions does a space really have?")
        ax = self.axes2d()
        self.play(Create(ax))
        e1 = arrow_from(ax, (1, 0), VECTOR_A, r"\vec e_1")
        e2 = arrow_from(ax, (0, 1), VECTOR_B, r"\vec e_2")
        self.play(GrowArrow(e1[0]), Write(e1[1]), GrowArrow(e2[0]), Write(e2[1]))
        self.cc("The plane needs exactly two independent directions. Two coordinates are enough to reach every point.", 3.1)
        self.play(Write(self.eq(r"\dim(\mathbb R^2)=2", 1.0, 1.2)))
        self.cc("Dimension counts independent directions, not the number of points in a space.", 2.9)

        line = Line(ax.c2p(-4, -2), ax.c2p(4, 2), color=GREEN_C, stroke_width=7)
        self.play(Create(line), FadeOut(e2))
        self.cc("A line through the origin needs only one independent direction.", 2.7)
        self.play(Write(self.eq(r"\dim(\text{a line through }0)=1", 0.78, 0.1)))
        self.cc("The line contains infinitely many points, but its dimension is still one.", 2.8)

        self.play(FadeOut(line), FadeIn(e2))
        self.play(Write(self.eq(r"\dim(\mathbb R^n)=n", 0.9, -1.15)))
        self.cc("In n-dimensional Euclidean space, the dimension is the number of independent directions needed to build the whole space.", 3.2)
        self.wait(2)


class Part2_06_CoordinatesInANonstandardBasis(VectorSpaceLesson):
    def construct(self):
        self.title("Part II.6 — Coordinates in a Nonstandard Basis", "The same vector can have different coordinates")
        ax = self.axes2d()
        self.play(Create(ax))
        b1 = arrow_from(ax, (2, 1), VECTOR_A, r"\vec b_1")
        b2 = arrow_from(ax, (1, 2), VECTOR_B, r"\vec b_2")
        self.play(GrowArrow(b1[0]), Write(b1[1]), GrowArrow(b2[0]), Write(b2[1]))
        self.cc("Coordinates depend on the basis. We are about to describe the same geometric vector using a tilted coordinate system.", 3.2)

        p = arrow_from(ax, (5, 4), HIGHLIGHT, r"\vec x")
        self.play(GrowArrow(p[0]), Write(p[1]))
        self.play(Write(self.eq(r"\vec x=2\vec b_1+1\vec b_2", 0.9, 1.4)))
        self.cc("The vector at five, four has coordinates (2,1) relative to this basis.", 2.9)
        self.play(Write(self.eq(r"[\vec x]_B=\begin{bmatrix}2\\1\end{bmatrix}", 0.9, 0.2)))

        self.play(FadeOut(b1), FadeOut(b2), FadeOut(p))
        e1 = arrow_from(ax, (1, 0), VECTOR_A, r"\vec e_1")
        e2 = arrow_from(ax, (0, 1), VECTOR_B, r"\vec e_2")
        p2 = arrow_from(ax, (5, 4), HIGHLIGHT, r"\vec x")
        self.play(GrowArrow(e1[0]), Write(e1[1]), GrowArrow(e2[0]), Write(e2[1]), GrowArrow(p2[0]), Write(p2[1]))
        self.play(Write(self.eq(r"[\vec x]_{std}=\begin{bmatrix}5\\4\end{bmatrix}", 0.86, -1.1)))
        self.cc("Same vector, different coordinates. The geometric object did not change; only the coordinate language changed.", 3.3)
        self.wait(2)


class Part2_07_Subspaces(VectorSpaceLesson):
    def construct(self):
        self.title("Part II.7 — Subspaces", "Smaller vector spaces living inside larger ones")
        ax = self.axes2d()
        self.play(Create(ax))
        e1 = arrow_from(ax, (1, 0), VECTOR_A, r"\vec e_1")
        e2 = arrow_from(ax, (0, 1), VECTOR_B, r"\vec e_2")
        self.play(GrowArrow(e1[0]), Write(e1[1]), GrowArrow(e2[0]), Write(e2[1]))
        self.cc("A subspace is a subset that is itself closed under the vector operations: addition and scalar multiplication.", 3.4)

        line = Line(ax.c2p(-5, -2), ax.c2p(5, 2), color=HIGHLIGHT, stroke_width=8)
        self.play(Create(line), FadeOut(e1), FadeOut(e2))
        self.cc("This line is a subspace because adding two points on it keeps us on the line, and scaling a point keeps us on the line.", 3.3)
        self.play(Write(self.eq(r"S=\{t\begin{bmatrix}1\\0.4\end{bmatrix}:t\in\mathbb R\}", 0.72, 1.1)))
        self.cc("A subspace can therefore be described as the span of some vectors.", 2.8)

        origin = Dot(ax.c2p(0, 0), color=YELLOW_C)
        self.play(FadeIn(origin))
        self.cc("A subspace must always contain the zero vector, because multiplying every generating vector by zero gives zero.", 3.1)
        self.play(Write(self.eq(r"\vec 0\in S", 0.9, -0.3)))
        self.wait(2)


class Part2_08_ColumnSpace(VectorSpaceLesson):
    def construct(self):
        self.title("Part II.8 — Column Space", "The set of all outputs a matrix can produce")
        ax = self.axes2d()
        self.play(Create(ax))
        c1 = arrow_from(ax, (2, 1), VECTOR_A, r"\vec c_1")
        c2 = arrow_from(ax, (1, 0.5), VECTOR_B, r"\vec c_2")
        self.play(GrowArrow(c1[0]), Write(c1[1]), GrowArrow(c2[0]), Write(c2[1]))
        self.cc("Think of the columns of a matrix as the directions available to the transformation.", 3)

        out = arrow_from(ax, (3, 1.5), HIGHLIGHT, r"A\vec x")
        self.play(GrowArrow(out[0]), Write(out[1]))
        self.play(Write(self.eq(r"A\vec x=x_1\vec c_1+x_2\vec c_2", 0.76, 1.45)))
        self.cc("Every output is a linear combination of the columns. So every possible output lies in the column space.", 3.1)
        self.play(Write(self.eq(r"\operatorname{Col}(A)=\operatorname{span}\{\vec c_1,\vec c_2\}", 0.64, 0.1)))
        self.cc("The column space tells us exactly which target vectors Ax=b can possibly reach.", 3)
        self.wait(2)


class Part2_09_RowSpaceAndNullSpace(VectorSpaceLesson):
    def construct(self):
        self.title("Part II.9 — Row Space and Null Space", "Two complementary questions about Ax")
        ax = self.axes2d()
        self.play(Create(ax))
        self.cc("For a matrix, we can ask two different questions: what outputs can it make, and which inputs disappear completely?", 3.4)

        row1 = MathTex(r"\vec r_1=(1,2)").scale(0.95).to_edge(RIGHT).shift(UP*1.55)
        row2 = MathTex(r"\vec r_2=(2,4)=2\vec r_1").scale(0.85).to_edge(RIGHT).shift(UP*0.65)
        self.play(Write(row1), Write(row2))
        self.cc("The row space is generated by the rows. Here the second row is redundant, so the row space has one independent direction.", 3.3)
        self.play(Write(self.eq(r"\operatorname{Row}(A)=\operatorname{span}\{\vec r_1\}", 0.72, -0.35)))

        null_line = Line(ax.c2p(-4, 2), ax.c2p(4, -2), color=HIGHLIGHT, stroke_width=7)
        self.play(Create(null_line), FadeOut(row1), FadeOut(row2))
        z = arrow_from(ax, (2, -1), GREEN_C, r"\vec z")
        self.play(GrowArrow(z[0]), Write(z[1]))
        self.cc("The null space consists of inputs that the matrix sends exactly to zero.", 3)
        self.play(Write(self.eq(r"A\vec z=\vec 0", 0.95, 1.2)))
        self.cc("The line shown is a geometric picture of all such null-space vectors for this example.", 2.8)
        self.play(Write(self.eq(r"\operatorname{Null}(A)=\{\vec z:A\vec z=\vec 0\}", 0.68, -0.25)))
        self.wait(2)


class Part2_10_RankNullityAndFourSpaces(VectorSpaceLesson):
    def construct(self):
        self.title("Part II.10 — Rank, Nullity, and the Four Fundamental Subspaces", "Putting the pieces together")
        ax = self.axes2d()
        self.play(Create(ax))
        self.cc("We now have enough language to talk about how much independent information a matrix contains.", 2.9)

        matrix = MathTex(r"A=\begin{bmatrix}1&2\\2&4\end{bmatrix}").scale(1.0).to_edge(RIGHT).shift(UP*1.55)
        self.play(Write(matrix))
        self.play(Write(self.eq(r"\operatorname{rank}(A)=1", 0.9, 0.45)))
        self.cc("The two columns are dependent, so only one independent output direction survives. That number is the rank.", 3.1)
        self.play(Write(self.eq(r"\operatorname{nullity}(A)=1", 0.9, -0.65)))
        self.cc("There is also one independent input direction that gets sent to zero. That number is the nullity.", 3.1)
        self.play(Write(self.eq(r"\boxed{\operatorname{rank}(A)+\operatorname{nullity}(A)=2}", 0.76, -1.65)))
        self.cc("For a matrix with two columns, rank plus nullity equals the number of input dimensions. This is the rank-nullity theorem.", 3.3)

        summary = VGroup(
            MathTex(r"\operatorname{Col}(A)"),
            MathTex(r"\operatorname{Row}(A)"),
            MathTex(r"\operatorname{Null}(A)"),
            MathTex(r"\operatorname{Null}(A^T)"),
        ).scale(0.68).arrange(DOWN, aligned_edge=LEFT, buff=0.34).to_edge(RIGHT, buff=0.2).shift(DOWN*0.2)
        self.play(FadeOut(matrix), FadeOut(*[m for m in self.mobjects if m is not ax and m is not summary]), run_time=0.8)
        self.play(Write(summary))
        self.cc("A matrix is associated with four fundamental subspaces: column space, row space, null space, and the null space of the transpose.", 3.5)
        self.play(Write(Text("Part II complete: vectors now have a space, coordinates, and structure.", font_size=26, color=YELLOW_B).to_edge(DOWN, buff=0.55)))
        self.wait(3)
