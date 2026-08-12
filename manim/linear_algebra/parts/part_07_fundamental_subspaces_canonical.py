from manim import *
from ..utils import LessonScene, VECTOR_A, VECTOR_B, HIGHLIGHT


class FundamentalSubspacesLesson(LessonScene):
    """Canonical Part VII: Fundamental Subspaces."""

    A = [[1, 2, 3], [0, 1, 1], [1, 3, 4]]
    null_vec = [-1, -1, 1]
    left_null_vec = [-1, -1, 1]

    def axes2d(self, x_range=(-4, 5), y_range=(-4, 5)):
        return Axes(
            x_range=[x_range[0], x_range[1], 1],
            y_range=[y_range[0], y_range[1], 1],
            x_length=7.3,
            y_length=6.0,
            axis_config={"include_numbers": True, "stroke_width": 2},
        ).to_edge(LEFT, buff=0.22)

    def axes3d(self):
        axes = ThreeDAxes(
            x_range=[-4, 4, 1],
            y_range=[-4, 4, 1],
            z_range=[-4, 4, 1],
            x_length=6.2,
            y_length=6.2,
            z_length=5.8,
        )
        self.set_camera_orientation(phi=68 * DEGREES, theta=32 * DEGREES)
        return axes.to_edge(LEFT, buff=0.15)

    def eq(self, latex, scale=0.66, y=0):
        return MathTex(latex).scale(scale).to_edge(RIGHT, buff=0.16).shift(UP * y)

    def matrix_tex(self):
        return MathTex(
            r"A=\begin{bmatrix}1&2&3\\0&1&1\\1&3&4\end{bmatrix}"
        ).scale(0.72).to_edge(RIGHT, buff=0.18).shift(UP * 1.55)

    def rows_tex(self):
        return MathTex(
            r"r_1=\begin{bmatrix}1\\2\\3\end{bmatrix},\quad"
            r"r_2=\begin{bmatrix}0\\1\\1\end{bmatrix},\quad"
            r"r_3=r_1+r_2"
        ).scale(0.57).to_edge(RIGHT, buff=0.08).shift(UP * 0.40)

    def cols_tex(self):
        return MathTex(
            r"c_1=\begin{bmatrix}1\\0\\1\end{bmatrix},\quad"
            r"c_2=\begin{bmatrix}2\\1\\3\end{bmatrix},\quad"
            r"c_3=c_1+c_2"
        ).scale(0.55).to_edge(RIGHT, buff=0.06).shift(UP * 0.32)


class Part7_01_RankIntuition(FundamentalSubspacesLesson):
    def construct(self):
        self.title("Part VII.1 — Rank Intuition", "Rank counts independent directions after redundancy is removed")
        self.play(Write(self.matrix_tex()), Write(self.rows_tex()))
        self.cc("Rank is the number of independent directions represented by the matrix. Redundant rows do not increase rank.", 2.9)
        self.play(Write(self.eq(r"r_3=r_1+r_2", 0.88, -0.45)))
        self.play(Write(self.eq(r"\boxed{\operatorname{rank}(A)=2}", 0.92, -1.35)))
        self.cc("There are three rows, but only two are independent. The same rank will emerge from the columns and from the number of pivots.", 3.0)
        self.play(Write(self.eq(r"\text{independent directions}=\text{rank}", 0.76, -2.30)))
        self.wait(2)


class Part7_02_ColumnSpace(FundamentalSubspacesLesson):
    def construct(self):
        self.title("Part VII.2 — Column Space", "All outputs the matrix can reach")
        axes = self.axes3d()
        self.play(Create(axes))
        c1 = Arrow3D(ORIGIN, axes.c2p(1, 0, 1), color=VECTOR_A, thickness=0.025)
        c2 = Arrow3D(ORIGIN, axes.c2p(2, 1, 3), color=VECTOR_B, thickness=0.025)
        c3 = Arrow3D(ORIGIN, axes.c2p(3, 1, 4), color=HIGHLIGHT, thickness=0.025)
        self.play(Create(c1), Create(c2), Create(c3))
        self.play(Write(self.cols_tex()))
        self.cc("The column space is the span of the columns. It is the set of every output vector Ax can produce.", 3.0)
        self.play(Write(self.eq(r"c_3=c_1+c_2", 0.84, -0.75)))
        self.play(Write(self.eq(r"\operatorname{Col}(A)=\operatorname{span}\{c_1,c_2\}", 0.68, -1.50)))
        self.play(Write(self.eq(r"\boxed{\dim\operatorname{Col}(A)=2}", 0.80, -2.25)))
        self.cc("Three columns collapse to two independent directions. The third column adds no new output direction.", 2.8)
        self.wait(2)


class Part7_03_RowSpace(FundamentalSubspacesLesson):
    def construct(self):
        self.title("Part VII.3 — Row Space", "All independent directions encoded by the rows")
        self.play(Write(self.matrix_tex()), Write(self.rows_tex()))
        self.cc("The row space is the span of all rows. Because the third row is their sum, the first two rows form a basis.", 3.0)
        self.play(Write(self.eq(r"\operatorname{Row}(A)=\operatorname{span}\{r_1,r_2\}", 0.75, -0.65)))
        self.play(Write(self.eq(r"\boxed{\dim\operatorname{Row}(A)=2}", 0.82, -1.40)))
        self.cc("Row operations change individual row vectors but preserve the row space. That is why row reduction can reveal the same subspace in simpler form.", 3.1)
        self.play(Write(self.eq(r"\operatorname{Row}(A)=\operatorname{Col}(A^T)", 0.78, -2.20)))
        self.wait(2)


class Part7_04_NullSpace(FundamentalSubspacesLesson):
    def construct(self):
        self.title("Part VII.4 — Null Space", "Inputs that disappear into zero")
        axes = self.axes3d()
        self.play(Create(axes))
        null_arrow = Arrow3D(ORIGIN, axes.c2p(-2, -2, 2), color=HIGHLIGHT, thickness=0.03)
        neg_arrow = Arrow3D(ORIGIN, axes.c2p(2, 2, -2), color=VECTOR_B, thickness=0.03)
        self.play(Create(null_arrow), Create(neg_arrow))
        self.play(Write(self.matrix_tex()))
        self.cc("The null space contains every input x satisfying Ax equals zero. Solve the homogeneous system to find all such directions.", 3.0)
        self.play(Write(self.eq(r"x_2+x_3=0", 0.82, 0.80)))
        self.play(Write(self.eq(r"x_1+2x_2+3x_3=0", 0.74, 0.15)))
        self.play(Write(self.eq(r"x=t\begin{bmatrix}-1\\-1\\1\end{bmatrix}", 0.78, -0.60)))
        self.play(Write(self.eq(r"\boxed{\operatorname{Null}(A)=\operatorname{span}\left\{\begin{bmatrix}-1\\-1\\1\end{bmatrix}\right\}}", 0.53, -1.45)))
        self.cc("There is one free parameter, so the null space has dimension one: a line through the origin in the three-dimensional input space.", 3.0)
        self.play(Write(self.eq(r"\boxed{\dim\operatorname{Null}(A)=1}", 0.80, -2.35)))
        self.wait(2)


class Part7_05_LeftNullSpace(FundamentalSubspacesLesson):
    def construct(self):
        self.title("Part VII.5 — Left Null Space", "Dependencies among rows, expressed as Null(A^T)")
        self.play(Write(self.matrix_tex()))
        self.cc("The left null space is the null space of A transpose. A vector y belongs to it when A transpose y equals zero.", 3.0)
        self.play(Write(self.eq(r"A^Ty=0", 0.94, 0.90)))
        self.play(Write(self.eq(r"y=t\begin{bmatrix}-1\\-1\\1\end{bmatrix}", 0.78, 0.20)))
        self.play(Write(self.eq(r"-r_1-r_2+r_3=0", 0.86, -0.55)))
        self.play(Write(self.eq(r"\boxed{\operatorname{Null}(A^T)=\operatorname{span}\left\{\begin{bmatrix}-1\\-1\\1\end{bmatrix}\right\}}", 0.51, -1.35)))
        self.cc("The left-null direction records the exact row dependency. One independent dependency means one dimension in the left null space.", 3.0)
        self.play(Write(self.eq(r"\boxed{\dim\operatorname{Null}(A^T)=1}", 0.80, -2.30)))
        self.wait(2)


class Part7_06_FourFundamentalSubspaces(FundamentalSubspacesLesson):
    def construct(self):
        self.title("Part VII.6 — The Four Fundamental Subspaces", "Four spaces, two sides of one matrix")
        self.play(Write(self.matrix_tex()))
        spaces = VGroup(
            Text("Column space — reachable outputs", font_size=21),
            Text("Row space — independent row directions", font_size=21),
            Text("Null space — inputs sent to zero", font_size=21),
            Text("Left null space — row dependencies", font_size=21),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.18).to_edge(RIGHT, buff=0.06).shift(DOWN * 0.35)
        self.play(LaggedStart(*[Write(s) for s in spaces], lag_ratio=0.18), run_time=2.3)
        self.cc("For an m by n matrix, column and left-null spaces live in the output space R^m, while row and null spaces live in the input space R^n.", 3.3)
        self.play(Write(self.eq(r"\operatorname{Col}(A),\operatorname{Null}(A^T)\subseteq\mathbb{R}^m", 0.62, -1.45)))
        self.play(Write(self.eq(r"\operatorname{Row}(A),\operatorname{Null}(A)\subseteq\mathbb{R}^n", 0.62, -2.15)))
        self.wait(2)


class Part7_07_RankPivotsAndIndependentDirections(FundamentalSubspacesLesson):
    def construct(self):
        self.title("Part VII.7 — Rank, Pivots, and Independent Directions", "Pivot positions expose rank")
        self.play(Write(self.matrix_tex()))
        rref = MathTex(r"\operatorname{RREF}(A)=\begin{bmatrix}1&0&1\\0&1&1\\0&0&0\end{bmatrix}").scale(0.60).to_edge(RIGHT, buff=0.08).shift(UP * 0.55)
        self.play(Write(rref))
        self.cc("A pivot is a position where a genuinely new independent direction appears. The number of pivots equals the rank.", 3.0)
        self.play(Write(self.eq(r"\#\text{pivots}=2\quad\Rightarrow\quad\operatorname{rank}(A)=2", 0.72, -0.20)))
        self.cc("For the column space, take the corresponding columns from the original matrix. Here c1 and c2 are independent, while c3 equals their sum.", 3.0)
        self.play(Write(self.eq(r"\{c_1,c_2\}\text{ is a basis of }\operatorname{Col}(A)", 0.66, -1.15)))
        self.play(Write(self.eq(r"\operatorname{rank}(A)=\dim\operatorname{Col}(A)=\dim\operatorname{Row}(A)=2", 0.58, -2.05)))
        self.wait(2)


class Part7_08_RankNullity(FundamentalSubspacesLesson):
    def construct(self):
        self.title("Part VII.8 — Rank–Nullity Theorem", "Every input dimension is either visible or invisible")
        self.play(Write(self.matrix_tex()))
        self.cc("The input space is R^3. Two independent directions survive into the output, while one independent direction is erased into zero.", 3.0)
        self.play(Write(self.eq(r"\operatorname{rank}(A)=2", 0.92, 0.90)))
        self.play(Write(self.eq(r"\operatorname{nullity}(A)=1", 0.92, 0.20)))
        self.play(Write(self.eq(r"\boxed{\operatorname{rank}(A)+\operatorname{nullity}(A)=3}", 0.72, -0.55)))
        self.cc("This is the rank–nullity theorem. More generally, for an m by n matrix, rank plus nullity equals n, the dimension of the domain.", 3.1)
        self.play(Write(self.eq(r"\operatorname{rank}(A)+\operatorname{nullity}(A)=n", 0.72, -1.55)))
        self.play(Write(self.eq(r"2+1=3", 0.90, -2.25)))
        self.wait(2)


class Part7_09_OrthogonalityPairs(FundamentalSubspacesLesson):
    def construct(self):
        self.title("Part VII.9 — The Orthogonality Pairs", "Two fundamental perpendicularities")
        self.play(Write(self.matrix_tex()))
        self.cc("Every null-space vector is perpendicular to every row of A because Ax equals zero means every row has zero dot product with x.", 3.2)
        self.play(Write(self.eq(r"\begin{bmatrix}1\\2\\3\end{bmatrix}\cdot\begin{bmatrix}-1\\-1\\1\end{bmatrix}=0", 0.67, 0.85)))
        self.play(Write(self.eq(r"\begin{bmatrix}0\\1\\1\end{bmatrix}\cdot\begin{bmatrix}-1\\-1\\1\end{bmatrix}=0", 0.67, 0.15)))
        self.play(Write(self.eq(r"\boxed{\operatorname{Null}(A)=\operatorname{Row}(A)^\perp}", 0.74, -0.65)))
        self.cc("On the output side, every left-null vector is perpendicular to every column of A. This is the transpose version of the same idea.", 3.0)
        self.play(Write(self.eq(r"\begin{bmatrix}-1\\-1\\1\end{bmatrix}\cdot\begin{bmatrix}1\\0\\1\end{bmatrix}=0", 0.63, -1.35)))
        self.play(Write(self.eq(r"\boxed{\operatorname{Null}(A^T)=\operatorname{Col}(A)^\perp}", 0.67, -2.10)))
        self.wait(2)


class Part7_10_DimensionsAndStructure(FundamentalSubspacesLesson):
    def construct(self):
        self.title("Part VII.10 — Dimensions and Structure", "The four dimensions are determined by m, n, and rank")
        self.play(Write(self.matrix_tex()))
        self.cc("For an m by n matrix of rank r, the four fundamental spaces have dimensions r, n-r, r, and m-r.", 3.0)
        self.play(Write(self.eq(r"\dim\operatorname{Col}(A)=r", 0.82, 1.05)))
        self.play(Write(self.eq(r"\dim\operatorname{Null}(A)=n-r", 0.82, 0.40)))
        self.play(Write(self.eq(r"\dim\operatorname{Row}(A)=r", 0.82, -0.25)))
        self.play(Write(self.eq(r"\dim\operatorname{Null}(A^T)=m-r", 0.82, -0.90)))
        self.cc("For our 3 by 3 rank-2 matrix, these dimensions are 2, 1, 2, and 1. The two orthogonal decompositions therefore account for all of R^3 on each side.", 3.2)
        self.play(Write(self.eq(r"(\dim\operatorname{Col},\dim\operatorname{Null},\dim\operatorname{Row},\dim\operatorname{Null}(A^T))=(2,1,2,1)", 0.49, -1.75)))
        self.play(Write(self.eq(r"\mathbb{R}^3=\operatorname{Row}(A)\oplus\operatorname{Null}(A)", 0.63, -2.35)))
        self.wait(2)


class Part7_11_FundamentalSubspacesMastery(FundamentalSubspacesLesson):
    def construct(self):
        self.title("Part VII.11 — Fundamental Subspaces Mastery", "One matrix, four spaces, one structural map")
        self.play(Write(self.eq(r"A:\mathbb{R}^3\to\mathbb{R}^3", 0.90, 1.55)))
        summary = VGroup(
            Text("Column space → reachable outputs", font_size=20),
            Text("Row space → independent row directions", font_size=20),
            Text("Null space → inputs erased by A", font_size=20),
            Text("Left null → row dependencies", font_size=20),
            Text("Rank → number of independent directions", font_size=20),
            Text("Nullity → number of invisible directions", font_size=20),
            Text("Rank + nullity = domain dimension", font_size=20),
            Text("Null ⟂ Row; Left-null ⟂ Column", font_size=20),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.12).to_edge(RIGHT, buff=0.05).shift(DOWN * 0.30)
        self.play(LaggedStart(*[Write(item) for item in summary], lag_ratio=0.15), run_time=2.7)
        self.cc("Given a matrix, you should now be able to identify its reachable outputs, erased inputs, row dependencies, rank, nullity, and the two orthogonal pairs.", 3.6)
        self.play(Write(self.eq(r"\boxed{\text{four spaces}\;\longleftrightarrow\;\text{one matrix structure}}", 0.69, -2.05)))
        self.play(Write(Text("Part VII complete: the four fundamental subspaces now fit together.", font_size=24, color=YELLOW_B).to_edge(DOWN, buff=0.42)))
        self.wait(3)


__all__ = [name for name in globals() if name.startswith("Part7_") or name == "FundamentalSubspacesLesson"]
