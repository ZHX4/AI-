from manim import *
from ..utils import *


class VectorSpaceLesson(LessonScene):
    """Shared visual and caption helpers for Part II."""

    def axes2d(self):
        ax = Axes(
            x_range=[-5, 5, 1],
            y_range=[-5, 5, 1],
            x_length=8.6,
            y_length=6.8,
            axis_config={"include_numbers": True, "stroke_width": 2},
        )
        ax.to_edge(LEFT, buff=0.35)
        return ax

    def eq(self, latex, scale=0.72, y=0):
        return MathTex(latex).scale(scale).to_edge(RIGHT, buff=0.28).shift(UP * y)

    def point(self, ax, coords, color=HIGHLIGHT):
        return Dot(ax.c2p(*coords), radius=0.065, color=color)


class Part2_01_Span(VectorSpaceLesson):
    def construct(self):
        self.title("Part II.1 — Span", "Which vectors can we build from a collection of vectors?")
        ax = self.axes2d(); self.play(Create(ax))
        u = arrow_from(ax, (2, 1), VECTOR_A, r"\vec u"); v = arrow_from(ax, (-1, 2), VECTOR_B, r"\vec v")
        self.play(GrowArrow(u[0]), Write(u[1]), GrowArrow(v[0]), Write(v[1]))
        self.cc("We now ask a broader question: if these are the vectors we are allowed to use, which other vectors can we construct?", 3.2)
        target = arrow_from(ax, (3, 4), HIGHLIGHT, r"\vec w"); self.play(GrowArrow(target[0]), Write(target[1]))
        self.play(Write(self.eq(r"\vec w=2\vec u+\vec v=\begin{bmatrix}3\\4\end{bmatrix}", .70, 1.35)))
        self.cc("Here 2u plus v really is the vector three, four: two times (2,1) plus (-1,2).", 3.3)
        reachable = VGroup()
        for a in range(-4, 5):
            for b in range(-4, 5):
                x, y = 2*a-b, a+2*b
                if -5 <= x <= 5 and -5 <= y <= 5: reachable.add(self.point(ax, (x, y), GREEN_C))
        self.play(LaggedStart(*[FadeIn(p, scale=.5) for p in reachable], lag_ratio=.012), run_time=3)
        self.play(Write(self.eq(r"\operatorname{span}\{\vec u,\vec v\}=\mathbb R^2", .78, .1)))
        self.cc("Because these generators are independent, their linear combinations fill the whole plane. The span is a set of reachable vectors, not one particular vector.", 3.6)
        self.wait(2)


class Part2_02_LinearDependence(VectorSpaceLesson):
    def construct(self):
        self.title("Part II.2 — Linear Dependence", "When one vector is redundant")
        ax = self.axes2d(); self.play(Create(ax))
        u = arrow_from(ax, (2, 1), VECTOR_A, r"\vec u"); v = arrow_from(ax, (4, 2), VECTOR_B, r"\vec v")
        self.play(GrowArrow(u[0]), Write(u[1]), GrowArrow(v[0]), Write(v[1]))
        self.cc("These vectors are different in length, but they point in exactly the same direction.", 2.9)
        self.play(Write(self.eq(r"\vec v=2\vec u", .9, 1.35)))
        self.cc("So v adds no new direction. Anything we can build with v was already reachable using u.", 3.1)
        line = DashedLine(ax.c2p(-5,-2.5), ax.c2p(5,2.5), color=GREY_B, stroke_opacity=.65); self.play(Create(line))
        self.cc("Every linear combination stays on one line because only one independent direction is available.", 3.1)
        self.play(Write(self.eq(r"a\vec u+b\vec v=(a+2b)\vec u", .78, .15)))
        self.cc("Two coefficients collapse into one effective coefficient. That algebraic redundancy is the key idea behind dependence.", 3.2)
        self.play(Write(self.eq(r"\alpha\vec u+\beta\vec v=\vec 0", .82, -1.25)))
        self.cc("For example, alpha equals 2 and beta equals negative 1 gives a nonzero combination that cancels to zero.", 3.1)
        self.wait(2)


class Part2_03_LinearIndependence(VectorSpaceLesson):
    def construct(self):
        self.title("Part II.3 — Linear Independence", "No vector can be rebuilt from the others")
        ax = self.axes2d(); self.play(Create(ax))
        u = arrow_from(ax, (2,1), VECTOR_A, r"\vec u"); v = arrow_from(ax, (1,2), VECTOR_B, r"\vec v")
        self.play(GrowArrow(u[0]), Write(u[1]), GrowArrow(v[0]), Write(v[1]))
        self.cc("Now the vectors point in genuinely different directions. Neither one is a scalar multiple of the other.", 3.0)
        self.play(Write(self.eq(r"c_1\vec u+c_2\vec v=\vec 0", .9, 1.35)))
        self.cc("To test independence, ask whether zero can be produced without setting every coefficient to zero.", 3.0)
        self.play(Write(self.eq(r"\Longrightarrow c_1=0,\quad c_2=0", .90, .2)))
        self.cc("For these vectors, perfect cancellation forces both coefficients to be zero. There is no redundancy.", 3.0)
        self.play(Write(self.eq(r"\det\begin{bmatrix}2&1\\1&2\end{bmatrix}=4-1=3\ne0", .64, -1.2)))
        self.cc("In two dimensions, a nonzero determinant is another reliable test that two vectors contribute two independent directions.", 3.3)
        self.wait(2)


class Part2_04_Basis(VectorSpaceLesson):
    def construct(self):
        self.title("Part II.4 — Basis", "A coordinate system built from independent generators")
        ax = self.axes2d(); self.play(Create(ax))
        e1 = arrow_from(ax, (1,0), VECTOR_A, r"\vec e_1"); e2 = arrow_from(ax, (0,1), VECTOR_B, r"\vec e_2")
        self.play(GrowArrow(e1[0]), Write(e1[1]), GrowArrow(e2[0]), Write(e2[1]))
        self.cc("A basis has two properties: it spans the space, and its vectors are linearly independent.", 3.1)
        self.play(Write(self.eq(r"\text{basis}=\text{span}+\text{independence}", .76, 1.4)))
        self.cc("The standard basis uses one pure horizontal direction and one pure vertical direction.", 2.8)
        p = arrow_from(ax, (3,-2), HIGHLIGHT, r"\vec x"); self.play(GrowArrow(p[0]), Write(p[1]))
        self.play(Write(self.eq(r"\vec x=3\vec e_1-2\vec e_2", .85, .2)))
        self.cc("The coefficients three and negative two become the coordinates of x in this basis.", 2.9)
        self.play(Write(self.eq(r"[\vec x]_{std}=\begin{bmatrix}3\\-2\end{bmatrix}", .82, -1.2)))
        self.cc("Because the basis is independent, every vector gets one unique coordinate pair.", 3.0)
        self.wait(2)


class Part2_05_Dimension(VectorSpaceLesson):
    def construct(self):
        self.title("Part II.5 — Dimension", "How many independent directions does a space need?")
        ax = self.axes2d(); self.play(Create(ax))
        e1 = arrow_from(ax, (1,0), VECTOR_A, r"\vec e_1"); e2 = arrow_from(ax, (0,1), VECTOR_B, r"\vec e_2")
        self.play(GrowArrow(e1[0]), Write(e1[1]), GrowArrow(e2[0]), Write(e2[1]))
        self.cc("Dimension counts independent directions, not the number of points. The plane needs two independent directions.", 3.2)
        self.play(Write(self.eq(r"\dim(\mathbb R^2)=2", 1.0, 1.25)))
        line = Line(ax.c2p(-4,-2), ax.c2p(4,2), color=GREEN_C, stroke_width=7); self.play(Create(line), FadeOut(e2))
        self.cc("A line through the origin needs only one independent direction, even though it contains infinitely many points.", 3.0)
        self.play(Write(self.eq(r"\dim(\text{line through }\vec 0)=1", .74, .10)))
        self.play(FadeOut(line), FadeIn(e2)); self.play(Write(self.eq(r"\dim(\mathbb R^n)=n", .92, -1.2)))
        self.cc("In R to the n, n independent directions are needed to build the whole space. That number is its dimension.", 3.1)
        self.wait(2)


class Part2_06_CoordinatesInANonstandardBasis(VectorSpaceLesson):
    def construct(self):
        self.title("Part II.6 — Coordinates in a Nonstandard Basis", "The same vector can have different coordinates")
        ax = self.axes2d(); self.play(Create(ax))
        b1 = arrow_from(ax, (2,1), VECTOR_A, r"\vec b_1"); b2 = arrow_from(ax, (1,2), VECTOR_B, r"\vec b_2")
        self.play(GrowArrow(b1[0]), Write(b1[1]), GrowArrow(b2[0]), Write(b2[1]))
        self.cc("Coordinates depend on the basis. We can describe the same geometric vector using a tilted pair of basis vectors.", 3.2)
        x = arrow_from(ax, (5,4), HIGHLIGHT, r"\vec x"); self.play(GrowArrow(x[0]), Write(x[1]))
        self.play(Write(self.eq(r"\vec x=2\vec b_1+\vec b_2=\begin{bmatrix}5\\4\end{bmatrix}", .64, 1.25)))
        self.play(Write(self.eq(r"[\vec x]_B=\begin{bmatrix}2\\1\end{bmatrix}", .82, .15)))
        self.cc("Relative to this basis, the coordinate pair is two, one. The geometric vector itself is still five, four in the standard axes.", 3.5)
        self.play(Write(self.eq(r"[\vec x]_{std}=\begin{bmatrix}5\\4\end{bmatrix}", .82, -1.15)))
        self.cc("Same vector, different coordinates. Changing the basis changes the numbers used to describe the object, not the object itself.", 3.4)
        self.wait(2)


class Part2_07_Subspaces(VectorSpaceLesson):
    def construct(self):
        self.title("Part II.7 — Subspaces", "Smaller vector spaces living inside larger ones")
        ax = self.axes2d(); self.play(Create(ax))
        e1 = arrow_from(ax, (1,0), VECTOR_A, r"\vec e_1"); e2 = arrow_from(ax, (0,1), VECTOR_B, r"\vec e_2")
        self.play(GrowArrow(e1[0]), Write(e1[1]), GrowArrow(e2[0]), Write(e2[1]))
        self.cc("A subspace is a subset that is itself closed under addition and scalar multiplication.", 3.1)
        line = Line(ax.c2p(-5,-2), ax.c2p(5,2), color=HIGHLIGHT, stroke_width=8); self.play(Create(line), FadeOut(e1), FadeOut(e2))
        self.cc("This line passes through the origin. Add two points on it and you stay on the line; scale one point and you stay on the line.", 3.4)
        self.play(Write(self.eq(r"S=\operatorname{span}\left\{\begin{bmatrix}1\\0.4\end{bmatrix}\right\}", .66, 1.05)))
        self.cc("That is why spans naturally produce subspaces. Every scalar multiple of the generator remains in the same set.", 3.0)
        self.play(Write(self.eq(r"\vec 0\in S", .9, -.20))); self.cc("Every subspace must contain the zero vector, because zero times any generator equals zero.", 2.8)
        self.wait(2)


class Part2_08_ColumnSpace(VectorSpaceLesson):
    def construct(self):
        self.title("Part II.8 — Column Space", "The set of all outputs a matrix can produce")
        ax = self.axes2d(); self.play(Create(ax))
        c1 = arrow_from(ax, (2,1), VECTOR_A, r"\vec c_1"); c2 = arrow_from(ax, (1,.5), VECTOR_B, r"\vec c_2")
        self.play(GrowArrow(c1[0]), Write(c1[1]), GrowArrow(c2[0]), Write(c2[1])); self.cc("Think of the columns as the output directions that a matrix has available.", 2.8)
        out = arrow_from(ax, (3,1.5), HIGHLIGHT, r"A\vec x"); self.play(GrowArrow(out[0]), Write(out[1]))
        self.play(Write(self.eq(r"A\vec x=x_1\vec c_1+x_2\vec c_2", .76, 1.4)))
        self.cc("Every output is a linear combination of the columns, so every possible output lies in their span.", 3.1)
        self.play(Write(self.eq(r"\operatorname{Col}(A)=\operatorname{span}\{\vec c_1,\vec c_2\}", .62, .10)))
        self.cc("The column space tells us which target vectors in Ax=b are even reachable.", 2.9); self.wait(2)


class Part2_09_RowSpaceAndNullSpace(VectorSpaceLesson):
    def construct(self):
        self.title("Part II.9 — Row Space and Null Space", "What information is measured, and what information disappears?")
        ax = self.axes2d(); self.play(Create(ax))
        self.cc("The row space describes independent directions used to measure inputs. The null space describes input directions that the matrix sends to zero.", 3.6)
        r = MathTex(r"\vec r_1=(1,2),\qquad \vec r_2=(2,4)=2\vec r_1").scale(.82).to_edge(RIGHT).shift(UP*1.35); self.play(Write(r))
        self.play(Write(self.eq(r"\operatorname{Row}(A)=\operatorname{span}\{(1,2)\}", .66, .35))); self.cc("The second row adds no new direction, so the row space has one independent direction.", 2.9)
        null_line = Line(ax.c2p(-4,2), ax.c2p(4,-2), color=HIGHLIGHT, stroke_width=7); z = arrow_from(ax, (2,-1), GREEN_C, r"\vec z")
        self.play(Create(null_line), FadeOut(r), GrowArrow(z[0]), Write(z[1])); self.play(Write(self.eq(r"A\vec z=\vec 0", .95, 1.15)))
        self.cc("The null space consists of exactly those inputs that are completely annihilated by the matrix.", 3.1)
        self.play(Write(self.eq(r"\operatorname{Null}(A)=\{\vec z:A\vec z=\vec 0\}", .66, -.25)))
        self.cc("Row space describes what the matrix can detect; null space describes what it cannot distinguish.", 3.2); self.wait(2)


class Part2_10_RankNullity(VectorSpaceLesson):
    def construct(self):
        self.title("Part II.10 — Rank, Nullity, and Rank–Nullity", "Counting surviving and lost input directions")
        ax = self.axes2d(); self.play(Create(ax))
        A = MathTex(r"A=\begin{bmatrix}1&2\\2&4\end{bmatrix}").scale(.95).to_edge(RIGHT).shift(UP*1.45); self.play(Write(A))
        self.cc("This matrix has two columns, but the second column is twice the first. Only one independent output direction survives.", 3.4)
        self.play(Write(self.eq(r"\operatorname{rank}(A)=1", .92, .35)))
        self.play(Write(self.eq(r"A\begin{bmatrix}x_1\\x_2\end{bmatrix}=\vec0\ \Longleftrightarrow\ x_1+2x_2=0", .58, -.65)))
        self.cc("The equation x1 plus 2x2 equals zero leaves one free input direction that disappears under A. That is the nullity.", 3.6)
        self.play(Write(self.eq(r"\operatorname{nullity}(A)=1", .90, -1.55)))
        self.play(Write(self.eq(r"\boxed{\operatorname{rank}(A)+\operatorname{nullity}(A)=2}", .70, -2.35)))
        self.cc("Rank counts independent directions that survive in the output. Nullity counts independent input directions that are lost. Their sum equals the input dimension.", 3.8); self.wait(2)


class Part2_11_FourFundamentalSubspaces(VectorSpaceLesson):
    def construct(self):
        self.title("Part II.11 — The Four Fundamental Subspaces", "One matrix, four spaces, two orthogonal pairings")
        ax = self.axes2d(); self.play(Create(ax))
        self.cc("We use one concrete matrix so all four fundamental subspaces have a geometric meaning.", 3.3)
        self.play(Write(self.eq(r"A=\begin{bmatrix}1&2\\0&0\end{bmatrix}", .90, 2.0)))
        col = Arrow(ax.c2p(0,0), ax.c2p(1,0), buff=0, color=VECTOR_A, stroke_width=7)
        row = Arrow(ax.c2p(0,0), ax.c2p(1,2), buff=0, color=VECTOR_B, stroke_width=7)
        null = Arrow(ax.c2p(0,0), ax.c2p(-2,1), buff=0, color=HIGHLIGHT, stroke_width=7)
        left = Arrow(ax.c2p(0,0), ax.c2p(0,1), buff=0, color=YELLOW_C, stroke_width=7)
        self.play(GrowArrow(col), GrowArrow(row), GrowArrow(null), GrowArrow(left))
        self.play(Write(self.eq(r"\operatorname{Col}(A)=\operatorname{span}\left\{\begin{bmatrix}1\\0\end{bmatrix}\right\}", .55, .95)))
        self.play(Write(self.eq(r"\operatorname{Row}(A)=\operatorname{span}\left\{\begin{bmatrix}1\\2\end{bmatrix}\right\}", .55, .15)))
        self.play(Write(self.eq(r"\operatorname{Null}(A)=\operatorname{span}\left\{\begin{bmatrix}-2\\1\end{bmatrix}\right\}", .55, -.65)))
        self.play(Write(self.eq(r"\operatorname{Null}(A^T)=\operatorname{span}\left\{\begin{bmatrix}0\\1\end{bmatrix}\right\}", .55, -1.45)))
        self.cc("The column space is the output direction. The row space is the independent input direction measured by the matrix. The null space contains lost inputs. The transpose null space contains output directions perpendicular to the column space.", 4.2)
        self.play(Write(self.eq(r"\begin{bmatrix}1&2\end{bmatrix}\begin{bmatrix}-2\\1\end{bmatrix}=0", .66, -2.25)))
        self.cc("The row vector and the null vector are perpendicular, so Row(A) is orthogonal to Null(A).", 3.0)
        self.play(Write(self.eq(r"\begin{bmatrix}1\\0\end{bmatrix}\cdot\begin{bmatrix}0\\1\end{bmatrix}=0", .66, -2.95)))
        self.cc("The column direction is perpendicular to Null(A transpose). These are the two fundamental orthogonal pairings among the four spaces.", 3.8)
        self.wait(3)


__all__ = [name for name in globals() if name.startswith("Part2_") or name == "VectorSpaceLesson"]
