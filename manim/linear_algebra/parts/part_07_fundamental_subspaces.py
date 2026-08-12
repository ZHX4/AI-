from manim import *
from ..utils import LessonScene, VECTOR_A, VECTOR_B, HIGHLIGHT


class FundamentalSubspacesLesson(LessonScene):
    """Shared helpers for the canonical Part VII lessons."""

    A = [[1, 2, 3], [0, 1, 1], [1, 3, 4]]
    null_vec = [-1, -1, 1]

    def axes2d(self, x_range=(-4, 5), y_range=(-4, 5)):
        return Axes(
            x_range=[x_range[0], x_range[1], 1],
            y_range=[y_range[0], y_range[1], 1],
            x_length=7.4,
            y_length=6.2,
            axis_config={"include_numbers": True, "stroke_width": 2},
        ).to_edge(LEFT, buff=0.25)

    def eq(self, latex, scale=0.66, y=0):
        return MathTex(latex).scale(scale).to_edge(RIGHT, buff=0.18).shift(UP * y)

    def matrix_tex(self):
        return MathTex(
            r"A=\begin{bmatrix}1&2&3\\0&1&1\\1&3&4\end{bmatrix}"
        ).scale(0.73).to_edge(RIGHT, buff=0.22).shift(UP * 1.55)

    def row_matrix_tex(self):
        return MathTex(
            r"r_1=\begin{bmatrix}1\\2\\3\end{bmatrix},\quad"
            r"r_2=\begin{bmatrix}0\\1\\1\end{bmatrix},\quad"
            r"r_3=r_1+r_2"
        ).scale(0.58).to_edge(RIGHT, buff=0.12).shift(UP * 0.45)

    def column_matrix_tex(self):
        return MathTex(
            r"c_1=\begin{bmatrix}1\\0\\1\end{bmatrix},\quad"
            r"c_2=\begin{bmatrix}2\\1\\3\end{bmatrix},\quad"
            r"c_3=c_1+c_2"
        ).scale(0.56).to_edge(RIGHT, buff=0.10).shift(UP * 0.35)


class Part7_01_RankIntuition(FundamentalSubspacesLesson):
    def construct(self):
        self.title("Part VII.1 — Rank Intuition", "Rank counts independent directions produced by a matrix")
        self.play(Write(self.matrix_tex()))
        self.cc(
            "Rank is not simply the number of rows or columns. Rank counts how many independent directions remain after we remove redundancy.",
            3.0,
        )
        self.play(Write(self.row_matrix_tex()))
        self.cc(
            "Here the third row is exactly the sum of the first two rows. So the three rows contain only two independent directions.",
            2.9,
        )
        self.play(Write(self.eq(r"r_3=r_1+r_2\quad\Rightarrow\quad\operatorname{rank}(A)=2", 0.72, -0.35)))
        self.cc(
            "The same rank will appear from the columns. Rank is a structural property of the linear map, not a property of one particular row or column description.",
            3.0,
        )
        self.play(Write(self.eq(r"\boxed{\operatorname{rank}(A)=2}", 0.92, -1.40)))
        self.wait(2)


class Part7_02_ColumnSpace(FundamentalSubspacesLesson):
    def construct(self):
        self.title("Part VII.2 — Column Space", "The output directions a matrix can actually produce")
        ax = self.axes2d(x_range=(-1, 4), y_range=(-1, 5))
        self.play(Create(ax))
        c1 = Arrow(ax.c2p(0, 0), ax.c2p(1, 2), buff=0, color=VECTOR_A, stroke_width=6)
        c2 = Arrow(ax.c2p(0, 0), ax.c2p(1, 0.5), buff=0, color=VECTOR_B, stroke_width=6)
        self.play(GrowArrow(c1), GrowArrow(c2))
        self.play(Write(self.column_matrix_tex()))
        self.cc(
            "The column space is the span of the columns. It is exactly the set of output vectors A can produce when the input vector varies.",
            3.1,
        )
        self.play(Write(self.eq(r"\operatorname{Col}(A)=\operatorname{span}\{c_1,c_2,c_3\}", 0.67, -0.80)))
        self.play(Write(self.eq(r"c_3=c_1+c_2\quad\Rightarrow\quad\operatorname{Col}(A)=\operatorname{span}\{c_1,c_2\}", 0.55, -1.70)))
        self.cc(
            "There are two independent column directions, so the column space has dimension two. In a larger-dimensional problem, this same idea describes the reachable output subspace.",
            3.2,
        )
        self.play(Write(self.eq(r"\boxed{\dim\operatorname{Col}(A)=2}", 0.80, -2.55)))
        self.wait(2)


class Part7_03_RowSpace(FundamentalSubspacesLesson):
    def construct(self):
        self.title("Part VII.3 — Row Space", "The independent directions encoded by the rows")
        self.play(Write(self.matrix_tex()))
        self.play(Write(self.row_matrix_tex()))
        self.cc(
            "The row space is the span of all rows. Because the third row is redundant, the first two rows already generate the entire row space.",
            3.0,
        )
        self.play(Write(self.eq(r"\operatorname{Row}(A)=\operatorname{span}\{r_1,r_2,r_3\}=\operatorname{span}\{r_1,r_2\}", 0.57, -0.75)))
        self.cc(
            "Row operations change the appearance of the rows, but they preserve the row space. This is why elimination can reveal the same structural information in a simpler form.",
            3.1,
        )
        self.play(Write(self.eq(r"\boxed{\dim\operatorname{Row}(A)=\operatorname{rank}(A)=2}", 0.68, -1.75)))
        self.play(Write(self.eq(r"\operatorname{Row}(A)=\operatorname{Col}(A^T)", 0.78, -2.55)))
        self.wait(2)


class Part7_04_NullSpace(FundamentalSubspacesLesson):
    def construct(self):
        self.title("Part VII.4 — Null Space", "Inputs that produce the zero output")
        ax = self.axes2d(x_range=(-4, 4), y_range=(-4, 4))
        self.play(Create(ax))
        null_line = ax.plot(lambda x: x, color=HIGHLIGHT, x_range=[-3.3, 3.3])
        self.play(Create(null_line))
        self.play(Write(self.matrix_tex()))
        self.cc(
            "The null space contains every input x for which Ax equals zero. We find it by solving a homogeneous system.",
            3.0,
        )
        self.play(Write(self.eq(r"A\begin{bmatrix}x_1\\x_2\\x_3\end{bmatrix}=0", 0.78, 0.70)))
        self.play(Write(self.eq(r"x_2+x_3=0\Rightarrow x_2=-x_3", 0.76, -0.05)))
        self.play(Write(self.eq(r"x_1+2x_2+3x_3=0\Rightarrow x_1=-x_3", 0.68, -0.75)))
        self.play(Write(self.eq(r"x=t\begin{bmatrix}-1\\-1\\1\end{bmatrix}", 0.78, -1.60)))
        self.cc(
            "There is one free parameter t, so the null space has one independent direction. It is a line through the origin inside the three-dimensional input space.",
            3.0,
        )
        self.play(Write(self.eq(r"\boxed{\operatorname{Null}(A)=\operatorname{span}\left\{\begin{bmatrix}-1\\-1\\1\end{bmatrix}\right\}}", 0.55, -2.55)))
        self.wait(2)


class Part7_05_LeftNullSpace(FundamentalSubspacesLesson):
    def construct(self):
        self.title("Part VII.5 — Left Null Space", "The null space of the transpose")
        self.play(Write(self.matrix_tex()))
        self.cc(
            "The left null space is the null space of A transpose. It lives in output-space coordinates and consists of every vector y satisfying A transpose y equals zero.",
            3.2,
        )
        self.play(Write(self.eq(r"A^Ty=0", 0.95, 0.85)))
        self.play(Write(self.eq(r"y=t\begin{bmatrix}-1\\-1\\1\end{bmatrix}", 0.78, -0.05)))
        self.play(Write(self.eq(r"\boxed{\operatorname{Null}(A^T)=\operatorname{span}\left\{\begin{bmatrix}-1\\-1\\1\end{bmatrix}\right\}}", 0.53, -0.95)))
        self.cc(
            "This space records dependencies among the rows. Here the dependency is exactly minus row one minus row two plus row three equals zero.",
            3.1,
        )
        self.play(Write(self.eq(r"-r_1-r_2+r_3=0", 0.88, -1.90)))
        self.play(Write(self.eq(r"\boxed{\dim\operatorname{Null}(A^T)=1}", 0.80, -2.65)))
        self.wait(2)


class Part7_06_FourFundamentalSubspaces(FundamentalSubspacesLesson):
    def construct(self):
        self.title("Part VII.6 — The Four Fundamental Subspaces", "One matrix produces four linked spaces")
        self.play(Write(self.matrix_tex()))
        spaces = VGroup(
            Text("Column space: outputs reachable by Ax", font_size=22),
            Text("Row space: independent row directions", font_size=22),
            Text("Null space: inputs sent to zero", font_size=22),
            Text("Left null space: row dependencies", font_size=22),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.22).to_edge(RIGHT, buff=0.12).shift(DOWN * 0.35)
        self.play(LaggedStart(*[Write(s) for s in spaces], lag_ratio=0.18), run_time=2.2)
        self.cc(
            "These four spaces are not four unrelated definitions. They form the structural skeleton of every matrix: two spaces live in the input side and two in the output side.",
            3.3,
        )
        self.play(Write(self.eq(r"\operatorname{Col}(A),\ \operatorname{Null}(A)\subseteq\mathbb{R}^3", 0.68, -1.25)))
        self.play(Write(self.eq(r"\operatorname{Row}(A),\ \operatorname{Null}(A^T)\subseteq\mathbb{R}^3", 0.68, -2.05)))
        self.wait(2)


class Part7_07_RankPivotsAndIndependentDirections(FundamentalSubspacesLesson):
    def construct(self):
        self.title("Part VII.7 — Rank, Pivots, and Independent Directions", "Pivot columns reveal independent output directions")
        self.play(Write(self.matrix_tex()))
        self.cc(
            "Row reduction exposes pivot positions. Each pivot represents a new independent direction; non-pivot information is redundant.",
            3.0,
        )
        rref = MathTex(r"\operatorname{RREF}(A)=\begin{bmatrix}1&0&1\\0&1&1\\0&0&0\end{bmatrix}").scale(0.62).to_edge(RIGHT, buff=0.12).shift(UP * 0.65)
        self.play(Write(rref))
        self.play(Write(self.eq(r"\text{pivot columns}=1,2\quad\Rightarrow\quad\operatorname{rank}(A)=2", 0.67, -0.25)))
        self.cc(
            "The pivot columns of the original matrix—not necessarily the pivot columns of the reduced matrix—form a basis for the column space. Here the first two original columns are independent.",
            3.1,
        )
        self.play(Write(self.eq(r"\{c_1,c_2\}\text{ is a basis of }\operatorname{Col}(A)", 0.67, -1.20)))
        self.play(Write(self.eq(r"\#\text{pivots}=\operatorname{rank}(A)=2", 0.82, -2.05)))
        self.wait(2)


class Part7_08_RankNullity(FundamentalSubspacesLesson):
    def construct(self):
        self.title("Part VII.8 — Rank–Nullity Theorem", "Every input dimension is split into visible and invisible directions")
        self.play(Write(self.matrix_tex()))
        self.cc(
            "The domain is three-dimensional. Rank counts the independent directions that survive into the output; nullity counts the independent directions that disappear into zero.",
            3.1,
        )
        self.play(Write(self.eq(r"\operatorname{rank}(A)=2", 0.90, 0.85)))
        self.play(Write(self.eq(r"\operatorname{nullity}(A)=1", 0.90, 0.10)))
        self.play(Write(self.eq(r"\boxed{\operatorname{rank}(A)+\operatorname{nullity}(A)=3}", 0.74, -0.70)))
        self.cc(
            "The theorem says nothing is missing: every dimension in the input space belongs either to an independent direction that affects the output or to a null direction that gets collapsed.",
            3.2,
        )
        self.play(Write(self.eq(r"2+1=3=\dim(\text{domain})", 0.84, -1.65)))
        self.wait(2)


class Part7_09_OrthogonalityPairs(FundamentalSubspacesLesson):
    def construct(self):
        self.title("Part VII.9 — The Orthogonality Pairs", "Null space is perpendicular to row space")
        row1 = np.array([1, 2, 3]) if False else None
        self.play(Write(self.matrix_tex()))
        self.cc(
            "Every vector in the null space is orthogonal to every row of the matrix. Therefore the null space is the orthogonal complement of the row space.",
            3.2,
        )
        self.play(Write(self.eq(r"\begin{bmatrix}1\\2\\3\end{bmatrix}\cdot\begin{bmatrix}-1\\-1\\1\end{bmatrix}=0", 0.70, 0.80)))
        self.play(Write(self.eq(r"\begin{bmatrix}0\\1\\1\end{bmatrix}\cdot\begin{bmatrix}-1\\-1\\1\end{bmatrix}=0", 0.70, 0.10)))
        self.play(Write(self.eq(r"\boxed{\operatorname{Null}(A)=\operatorname{Row}(A)^\perp}", 0.76, -0.75)))
        self.cc(
            "The same phenomenon occurs on the output side: every vector in the left null space is perpendicular to every column of A.",
            3.0,
        )
        self.play(Write(self.eq(r"\boxed{\operatorname{Null}(A^T)=\operatorname{Col}(A)^\perp}", 0.70, -1.65)))
        self.wait(2)


class Part7_10_DimensionsAndStructure(FundamentalSubspacesLesson):
    def construct(self):
        self.title("Part VII.10 — Dimensions and Structure", "The dimensions of all four spaces fit together")
        self.play(Write(self.matrix_tex()))
        self.cc(
            "For an m by n matrix of rank r, the four spaces have dimensions r, n-r, r, and m-r in a fixed order.",
            3.2,
        )
        self.play(Write(self.eq(r"\dim\operatorname{Col}(A)=r", 0.80, 1.15)))
        self.play(Write(self.eq(r"\dim\operatorname{Null}(A)=n-r", 0.80, 0.50)))
        self.play(Write(self.eq(r"\dim\operatorname{Row}(A)=r", 0.80, -0.15)))
        self.play(Write(self.eq(r"\dim\operatorname{Null}(A^T)=m-r", 0.80, -0.80)))
        self.cc(
            "Here m=n=3 and r=2, so the dimensions are 2, 1, 2, and 1. The two orthogonal decompositions therefore account for the whole input and output spaces.",
            3.3,
        )
        self.play(Write(self.eq(r"(2,1,2,1)\quad\text{for our }3\times3\text{ rank-2 matrix}", 0.66, -1.70)))
        self.play(Write(self.eq(r"\mathbb{R}^3=\operatorname{Row}(A)\oplus\operatorname{Null}(A)", 0.66, -2.45)))
        self.wait(2)


class Part7_11_FundamentalSubspacesMastery(FundamentalSubspacesLesson):
    def construct(self):
        self.title("Part VII.11 — Fundamental Subspaces Mastery", "A single matrix, four spaces, one coherent structure")
        self.play(Write(self.eq(r"A:\mathbb{R}^3\to\mathbb{R}^3", 0.90, 1.55)))
        summary = VGroup(
            Text("Column space → reachable outputs", font_size=21),
            Text("Row space → independent row directions", font_size=21),
            Text("Null space → inputs erased by A", font_size=21),
            Text("Left null space → dependencies among rows", font_size=21),
            Text("Rank → number of independent directions", font_size=21),
            Text("Nullity → number of invisible directions", font_size=21),
            Text("Rank + nullity = domain dimension", font_size=21),
            Text("Null ⟂ Row,  Left-null ⟂ Column", font_size=21),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.13).to_edge(RIGHT, buff=0.08).shift(DOWN * 0.25)
        self.play(LaggedStart(*[Write(item) for item in summary], lag_ratio=0.15), run_time=2.8)
        self.cc(
            "The goal is not to memorize four names. Given a matrix, you should be able to ask: what outputs are reachable, what inputs vanish, what dependencies exist, and how many independent directions remain?",
            3.6,
        )
        self.play(Write(self.eq(r"\boxed{\text{four spaces}\;\longleftrightarrow\;\text{one matrix structure}}", 0.70, -2.05)))
        self.play(Write(Text("Part VII complete: the matrix now has a full structural map.", font_size=25, color=YELLOW_B).to_edge(DOWN, buff=0.42)))
        self.wait(3)


__all__ = [
    name for name in globals()
    if name.startswith("Part7_") or name == "FundamentalSubspacesLesson"
]
