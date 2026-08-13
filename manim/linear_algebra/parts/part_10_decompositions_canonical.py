from math import sqrt

from manim import *

from ..utils import HIGHLIGHT, LessonScene, VECTOR_A, VECTOR_B


class DecompositionLesson(LessonScene):
    """Canonical Part X: change of basis, orthogonal matrices, LU, QR, operators."""

    def axes2d(self, x_range=(-5, 5), y_range=(-5, 5)):
        return Axes(
            x_range=[x_range[0], x_range[1], 1],
            y_range=[y_range[0], y_range[1], 1],
            x_length=7.2,
            y_length=6.0,
            axis_config={"include_numbers": True, "stroke_width": 2},
        ).to_edge(LEFT, buff=0.22)

    def eq(self, latex, scale=0.67, y=0):
        return MathTex(latex).scale(scale).to_edge(RIGHT, buff=0.14).shift(UP * y)

    def matrix(self, latex, scale=0.70, y=1.55):
        return MathTex(latex).scale(scale).to_edge(RIGHT, buff=0.14).shift(UP * y)

    def line(self, ax, direction, color, length=3.0):
        dx, dy = direction
        n = sqrt(dx * dx + dy * dy)
        dx, dy = dx / n * length, dy / n * length
        return Line(ax.c2p(-dx, -dy), ax.c2p(dx, dy), color=color, stroke_width=4)


class Part10_01_ChangeOfBasisIntuition(DecompositionLesson):
    def construct(self):
        self.title("Part X.1 — Change of Basis Intuition", "The vector stays the same; the coordinates change")
        ax = self.axes2d()
        self.play(Create(ax))
        v = Arrow(ax.c2p(0, 0), ax.c2p(3, 1), buff=0, color=HIGHLIGHT, stroke_width=6)
        e1 = Arrow(ax.c2p(0, 0), ax.c2p(1, 0), buff=0, color=VECTOR_A, stroke_width=5)
        e2 = Arrow(ax.c2p(0, 0), ax.c2p(0, 1), buff=0, color=VECTOR_B, stroke_width=5)
        self.play(GrowArrow(e1), GrowArrow(e2), GrowArrow(v))
        self.cc("A basis is a coordinate language. Changing the basis does not move the geometric vector; it changes the numbers used to describe that vector.", 3.2)
        self.play(Write(self.eq(r"v=3e_1+e_2", 0.92, 0.95)))
        self.play(Write(self.eq(r"[v]_E=\begin{bmatrix}3\\1\end{bmatrix}", 0.80, 0.20)))
        self.play(Write(self.eq(r"B=\begin{bmatrix}1&1\\1&-1\end{bmatrix}", 0.70, -0.60)))
        self.play(Write(self.eq(r"v=B[v]_B", 0.88, -1.45)))
        self.cc("The matrix B converts coordinates in the B-basis into ordinary coordinates. Its columns are the new basis vectors.", 3.1)
        self.wait(2)


class Part10_02_CoordinateTransformation(DecompositionLesson):
    def construct(self):
        self.title("Part X.2 — Coordinate Transformations", "Convert between coordinate systems with inverse matrices")
        self.play(Write(self.matrix(r"B=\begin{bmatrix}1&1\\1&-1\end{bmatrix}")))
        self.cc("Suppose the same geometric vector has coordinates c in the B-basis and standard coordinates v. Then v equals B times c.", 3.0)
        self.play(Write(self.eq(r"v=Bc", 0.95, 0.82)))
        self.play(Write(self.eq(r"c=B^{-1}v", 0.95, 0.10)))
        self.play(Write(self.eq(r"B^{-1}=\frac12\begin{bmatrix}1&1\\1&-1\end{bmatrix}", 0.66, -0.68)))
        self.cc("The forward matrix changes coordinates into the standard frame; the inverse recovers coordinates in the original basis.", 3.0)
        self.play(Write(self.eq(r"B^{-1}B=I", 0.92, -1.45)))
        self.wait(2)


class Part10_03_ChangeOfBasisForOperators(DecompositionLesson):
    def construct(self):
        self.title("Part X.3 — Changing the Matrix of an Operator", "The same linear map gets a different matrix in a new basis")
        self.play(Write(self.matrix(r"[T]_E=A", 0.86, 1.45)))
        self.cc("A linear operator is a geometric rule. Its matrix depends on the coordinate basis used to describe that rule.", 3.0)
        self.play(Write(self.eq(r"[T]_B=B^{-1}AB", 0.95, 0.55)))
        self.play(Write(self.eq(r"\text{old coordinates}\;\xrightarrow{B}\;\text{standard}\;\xrightarrow{A}\;\text{standard}\;\xrightarrow{B^{-1}}\;\text{new coordinates}", 0.55, -0.35)))
        self.cc("This similarity transformation does not change the underlying operator. It changes only its coordinate representation.", 3.0)
        self.play(Write(self.eq(r"A\sim B^{-1}AB", 0.92, -1.30)))
        self.play(Write(self.eq(r"\boxed{\text{same transformation, different coordinates}}", 0.68, -2.05)))
        self.wait(2)


class Part10_04_OrthogonalMatrices(DecompositionLesson):
    def construct(self):
        self.title("Part X.4 — Orthogonal Matrices", "Rotations and reflections preserve lengths and angles")
        ax = self.axes2d()
        self.play(Create(ax))
        e1 = Arrow(ax.c2p(0, 0), ax.c2p(2, 0), buff=0, color=VECTOR_A, stroke_width=6)
        e2 = Arrow(ax.c2p(0, 0), ax.c2p(0, 2), buff=0, color=VECTOR_B, stroke_width=6)
        self.play(GrowArrow(e1), GrowArrow(e2))
        theta = PI / 4
        R = np.array([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]])
        self.play(ApplyMatrix(R, e1), ApplyMatrix(R, e2), run_time=2.0)
        self.play(Write(self.matrix(r"Q=\begin{bmatrix}\cos\theta&-\sin\theta\\\sin\theta&\cos\theta\end{bmatrix}")))
        self.play(Write(self.eq(r"Q^TQ=I", 0.95, 0.78)))
        self.play(Write(self.eq(r"\|Qv\|=\|v\|,\qquad(Qu)\cdot(Qv)=u\cdot v", 0.62, -0.05)))
        self.cc("An orthogonal matrix preserves Euclidean geometry. Rotations and reflections change orientation or direction without changing lengths or angles.", 3.2)
        self.play(Write(self.eq(r"Q^{-1}=Q^T", 0.92, -0.90)))
        self.wait(2)


class Part10_05_LU_Factorization(DecompositionLesson):
    def construct(self):
        self.title("Part X.5 — LU Factorization", "Gaussian elimination can be stored as L times U")
        self.play(Write(self.matrix(r"A=\begin{bmatrix}4&3\\6&3\end{bmatrix}")))
        self.cc("Gaussian elimination turns a matrix into an upper-triangular matrix. LU factorization remembers the elimination multipliers so the process becomes a product.", 3.1)
        self.play(Write(self.eq(r"R_2\leftarrow R_2-\frac32R_1", 0.78, 0.78)))
        self.play(Write(self.eq(r"U=\begin{bmatrix}4&3\\0&-\frac32\end{bmatrix}", 0.72, 0.02)))
        self.play(Write(self.eq(r"L=\begin{bmatrix}1&0\\\frac32&1\end{bmatrix}", 0.72, -0.78)))
        self.play(Write(self.eq(r"\boxed{A=LU}", 1.02, -1.62)))
        self.cc("L stores the elimination multipliers below the diagonal; U stores the resulting triangular system. This is why LU lets many right-hand sides reuse one factorization.", 3.1)
        self.wait(2)


class Part10_06_LU_SolvingSystems(DecompositionLesson):
    def construct(self):
        self.title("Part X.6 — Solving with LU", "Factor once, solve two simpler triangular systems")
        self.play(Write(self.eq(r"A=LU,\qquad Ax=b", 0.98, 1.35)))
        self.play(Write(self.eq(r"LUx=b", 0.98, 0.65)))
        self.play(Write(self.eq(r"Ly=b\quad\text{then}\quad Ux=y", 0.90, -0.05)))
        self.play(Write(self.eq(r"b=\begin{bmatrix}10\\12\end{bmatrix}", 0.72, -0.75)))
        self.play(Write(self.eq(r"y=\begin{bmatrix}10\\-3\end{bmatrix}", 0.72, -1.40)))
        self.play(Write(self.eq(r"x=\begin{bmatrix}-\frac14\\\frac43\end{bmatrix}", 0.72, -2.05)))
        self.cc("The factorization is reused; only the forward and backward substitutions change with b. This separation is one of the main computational reasons LU is useful.", 3.1)
        self.wait(2)


class Part10_07_QR_Factorization(DecompositionLesson):
    def construct(self):
        self.title("Part X.7 — QR Factorization", "Turn independent columns into an orthonormal basis")
        self.play(Write(self.matrix(r"A=\begin{bmatrix}1&1\\1&0\end{bmatrix}")))
        self.cc("QR factorization writes a matrix as Q times R, where Q has orthonormal columns and R is upper triangular.", 3.0)
        self.play(Write(self.eq(r"a_1=\begin{bmatrix}1\\1\end{bmatrix},\qquad\|a_1\|=\sqrt2", 0.70, 0.80)))
        self.play(Write(self.eq(r"q_1=\frac1{\sqrt2}\begin{bmatrix}1\\1\end{bmatrix}", 0.72, 0.05)))
        self.play(Write(self.eq(r"r_{12}=q_1^Ta_2=\frac1{\sqrt2}", 0.70, -0.70)))
        self.play(Write(self.eq(r"q_2=\frac1{\sqrt2}\begin{bmatrix}1\\-1\end{bmatrix}", 0.72, -1.35)))
        self.play(Write(self.eq(r"R=\begin{bmatrix}\sqrt2&\frac1{\sqrt2}\\0&\frac1{\sqrt2}\end{bmatrix}", 0.60, -2.05)))
        self.cc("The columns of Q are orthonormal directions; R records how the original columns are rebuilt from them.", 2.9)
        self.wait(2)


class Part10_08_QR_Geometry(DecompositionLesson):
    def construct(self):
        self.title("Part X.8 — QR Geometry", "Orthogonalize first, then store coordinates")
        ax = self.axes2d(x_range=(-3, 4), y_range=(-3, 4))
        self.play(Create(ax))
        a1 = Arrow(ax.c2p(0, 0), ax.c2p(1, 1), buff=0, color=VECTOR_A, stroke_width=6)
        a2 = Arrow(ax.c2p(0, 0), ax.c2p(1, 0), buff=0, color=VECTOR_B, stroke_width=6)
        self.play(GrowArrow(a1), GrowArrow(a2))
        self.cc("QR separates two ideas: Q captures the geometry of orthogonal directions, while R captures the coordinates needed to reconstruct the original columns.", 3.1)
        self.play(Write(self.eq(r"A=QR", 1.05, 1.10)))
        self.play(Write(self.eq(r"Q^TQ=I", 0.96, 0.35)))
        self.play(Write(self.eq(r"R\text{ upper triangular}", 0.76, -0.35)))
        self.cc("This makes QR a natural bridge from geometry to numerical computation, especially for least-squares problems.", 2.9)
        self.play(Write(self.eq(r"\boxed{\text{orthogonal directions + triangular coordinates}}", 0.64, -1.25)))
        self.wait(2)


class Part10_09_LinearOperators(DecompositionLesson):
    def construct(self):
        self.title("Part X.9 — Linear Operators", "A matrix is a coordinate representation of a linear rule")
        ax = self.axes2d()
        self.play(Create(ax))
        v = Arrow(ax.c2p(0, 0), ax.c2p(2, 1), buff=0, color=HIGHLIGHT, stroke_width=6)
        self.play(GrowArrow(v))
        self.play(Write(self.eq(r"T(au+bv)=aT(u)+bT(v)", 0.82, 1.25)))
        self.play(Write(self.eq(r"T:\mathbb{R}^n\to\mathbb{R}^m", 0.84, 0.60)))
        self.cc("A linear operator respects vector addition and scalar multiplication. Its matrix is the coordinate description of that rule after choosing bases.", 3.2)
        self.play(Write(self.eq(r"[T]_B=B^{-1}[T]_E B", 0.72, -0.35)))
        self.play(Write(self.eq(r"\text{operator}\neq\text{one particular matrix representation}", 0.62, -1.20)))
        self.cc("This distinction becomes essential when moving between coordinates, diagonal forms, decompositions, and numerical implementations.", 2.9)
        self.wait(2)


class Part10_10_DecompositionComparison(DecompositionLesson):
    def construct(self):
        self.title("Part X.10 — Decomposition Comparison", "Different factorizations expose different structure")
        table = VGroup(
            Text("Change of basis → coordinate structure", font_size=22),
            Text("Orthogonal Q → geometry without distortion", font_size=22),
            Text("LU → elimination and fast solves", font_size=22),
            Text("QR → orthonormal directions + triangular coordinates", font_size=22),
            Text("Spectral form → invariant eigen-directions", font_size=22),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.20).to_edge(RIGHT, buff=0.06).shift(DOWN * 0.10)
        self.play(LaggedStart(*[Write(t) for t in table], lag_ratio=0.12), run_time=2.8)
        self.cc("A decomposition is useful because it exposes hidden structure. The best factorization depends on the question you want to answer.", 3.2)
        self.play(Write(self.eq(r"\boxed{\text{factorization} = \text{structure made visible}}", 0.72, -2.25)))
        self.wait(2)


class Part10_11_DecompositionsMastery(DecompositionLesson):
    def construct(self):
        self.title("Part X.11 — Decompositions Mastery", "One language for changing, solving, and understanding linear maps")
        summary = VGroup(
            Text("Basis change → coordinates are transformed, not the vector", font_size=20),
            Text("Similarity → the same operator in a new basis", font_size=20),
            Text("Orthogonal matrices → preserve lengths and angles", font_size=20),
            Text("LU → elimination stored as factors", font_size=20),
            Text("QR → orthonormal basis + triangular coordinates", font_size=20),
            Text("Linear operator → abstract rule behind a matrix", font_size=20),
            Text("Different decompositions answer different questions", font_size=20),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.14).to_edge(RIGHT, buff=0.03).shift(DOWN * 0.08)
        self.play(LaggedStart(*[Write(s) for s in summary], lag_ratio=0.11), run_time=2.8)
        self.cc("The central idea is structural: instead of treating a matrix as a single block of numbers, factor it into pieces whose jobs you can understand.", 3.5)
        self.play(Write(self.eq(r"\boxed{\text{matrix}=\text{composition of understandable structure}}", 0.68, -2.25)))
        self.play(Write(Text("Part X complete: decompositions connect coordinate systems, geometry, and computation.", font_size=22, color=YELLOW_B).to_edge(DOWN, buff=0.38)))
        self.wait(3)


__all__ = [name for name in globals() if name.startswith("Part10_") or name == "DecompositionLesson"]
