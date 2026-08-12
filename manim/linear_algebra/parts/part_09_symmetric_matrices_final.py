from math import sqrt

from manim import *

from ..utils import HIGHLIGHT, LessonScene, VECTOR_A, VECTOR_B


class SymmetricMatrixLesson(LessonScene):
    """Part IX: symmetric matrices, spectral theorem, and quadratic forms."""

    A = [[3, 1], [1, 3]]
    eigvals = (4, 2)

    def axes2d(self, x_range=(-4, 5), y_range=(-4, 5)):
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

    def eigendirection(self, ax, direction, color, length=3.0):
        dx, dy = direction
        n = sqrt(dx * dx + dy * dy)
        dx, dy = dx / n * length, dy / n * length
        return Line(ax.c2p(-dx, -dy), ax.c2p(dx, dy), color=color, stroke_width=4)


class Part9_01_SymmetryIntuition(SymmetricMatrixLesson):
    def construct(self):
        self.title("Part IX.1 — Symmetry Intuition", "The matrix equals its transpose")
        self.play(Write(self.matrix(r"A=\begin{bmatrix}3&1\\1&3\end{bmatrix}")))
        self.cc("A real matrix is symmetric when reflecting it across the main diagonal leaves it unchanged. Algebraically, A equals A transpose.", 3.0)
        self.play(Write(self.eq(r"A^T=A", 1.00, 0.75)))
        self.play(Write(self.eq(r"a_{ij}=a_{ji}", 0.90, 0.05)))
        self.cc("This symmetry has a major consequence: real symmetric matrices have real eigenvalues and an orthonormal eigenbasis.", 3.0)
        self.play(Write(self.eq(r"A=A^T\Rightarrow\text{real eigenvalues + orthonormal eigenbasis}", 0.58, -1.00)))
        self.wait(2)


class Part9_02_OrthogonalEigenvectors(SymmetricMatrixLesson):
    def construct(self):
        self.title("Part IX.2 — Orthogonal Eigenvectors", "Distinct eigenvalues give perpendicular directions")
        ax = self.axes2d()
        self.play(Create(ax))
        self.play(Create(self.eigendirection(ax, (1, 1), VECTOR_A)), Create(self.eigendirection(ax, (1, -1), VECTOR_B)))
        self.play(Write(self.matrix(r"A=\begin{bmatrix}3&1\\1&3\end{bmatrix}")))
        self.play(Write(self.eq(r"A\begin{bmatrix}1\\1\end{bmatrix}=4\begin{bmatrix}1\\1\end{bmatrix}", 0.72, 0.72)))
        self.play(Write(self.eq(r"A\begin{bmatrix}1\\-1\end{bmatrix}=2\begin{bmatrix}1\\-1\end{bmatrix}", 0.72, -0.05)))
        self.play(Write(self.eq(r"\begin{bmatrix}1\\1\end{bmatrix}\cdot\begin{bmatrix}1\\-1\end{bmatrix}=0", 0.72, -0.92)))
        self.cc("For a real symmetric matrix, eigenvectors belonging to distinct eigenvalues are orthogonal.", 3.0)
        self.play(Write(self.eq(r"\lambda_1\neq\lambda_2\Rightarrow v_1\perp v_2", 0.78, -1.80)))
        self.wait(2)


class Part9_03_SpectralTheorem(SymmetricMatrixLesson):
    def construct(self):
        self.title("Part IX.3 — The Spectral Theorem", "Symmetric matrices can be diagonalized orthogonally")
        self.play(Write(self.matrix(r"A=\begin{bmatrix}3&1\\1&3\end{bmatrix}")))
        self.cc("Every real symmetric matrix can be diagonalized using an orthonormal eigenbasis. Therefore the change-of-basis matrix can be chosen orthogonal.", 3.1)
        self.play(Write(self.eq(r"Q^TQ=I", 1.00, 0.72)))
        self.play(Write(self.eq(r"A=Q\Lambda Q^T", 0.96, -0.02)))
        self.play(Write(self.eq(r"\Lambda=\begin{bmatrix}4&0\\0&2\end{bmatrix}", 0.72, -0.82)))
        self.play(Write(self.eq(r"Q^{-1}=Q^T", 0.92, -1.70)))
        self.wait(2)


class Part9_04_BuildingQAndLambda(SymmetricMatrixLesson):
    def construct(self):
        self.title("Part IX.4 — Building Q and Λ", "Normalize the eigenvectors and put them into columns")
        self.play(Write(self.eq(r"q_1=\frac1{\sqrt2}\begin{bmatrix}1\\1\end{bmatrix}", 0.82, 1.30)))
        self.play(Write(self.eq(r"q_2=\frac1{\sqrt2}\begin{bmatrix}1\\-1\end{bmatrix}", 0.82, 0.45)))
        self.play(Write(self.eq(r"Q=\frac1{\sqrt2}\begin{bmatrix}1&1\\1&-1\end{bmatrix}", 0.76, -0.40)))
        self.play(Write(self.eq(r"\Lambda=\begin{bmatrix}4&0\\0&2\end{bmatrix}", 0.76, -1.25)))
        self.cc("The normalized eigenvectors are perpendicular, so Q is orthogonal and its columns form an orthonormal basis.", 3.0)
        self.play(Write(self.eq(r"Q^TQ=I", 0.92, -2.10)))
        self.wait(2)


class Part9_05_QuadraticForms(SymmetricMatrixLesson):
    def construct(self):
        self.title("Part IX.5 — Quadratic Forms", "A symmetric matrix defines a scalar function of a vector")
        self.play(Write(self.matrix(r"A=\begin{bmatrix}3&1\\1&3\end{bmatrix}")))
        self.cc("Given a symmetric matrix A and a vector x, the quadratic form x transpose A x produces one scalar number.", 3.0)
        self.play(Write(self.eq(r"q(x)=x^TAx", 1.02, 0.82)))
        self.play(Write(self.eq(r"q(x,y)=3x^2+2xy+3y^2", 0.82, 0.05)))
        self.cc("The symmetric off-diagonal entries create the cross-term. Eigenvector coordinates will remove that cross-term.", 2.8)
        self.wait(2)


class Part9_06_PrincipalAxes(SymmetricMatrixLesson):
    def construct(self):
        self.title("Part IX.6 — Principal Axes", "Rotate into the eigenvector coordinate system")
        ax = self.axes2d(x_range=(-3, 3), y_range=(-3, 3))
        self.play(Create(ax))
        self.play(Create(self.eigendirection(ax, (1, 1), VECTOR_A)), Create(self.eigendirection(ax, (1, -1), VECTOR_B)))
        ellipse = Ellipse(width=sqrt(2), height=1.0, color=HIGHLIGHT, stroke_width=4)
        self.play(Create(ellipse.rotate(PI / 4)))
        self.play(Write(self.eq(r"q=4u^2+2v^2", 1.00, 0.95)))
        self.play(Write(self.eq(r"4u^2+2v^2=1", 0.90, 0.15)))
        self.cc("The eigenvectors are the principal axes. In those coordinates there is no cross-term, and the ellipse full axis lengths are 1 and sqrt(2), determined by the eigenvalues.", 3.1)
        self.play(Write(self.eq(r"\text{full axis lengths}=1,\ \sqrt2", 0.72, -0.85)))
        self.wait(2)


class Part9_07_RayleighQuotient(SymmetricMatrixLesson):
    def construct(self):
        self.title("Part IX.7 — Rayleigh Quotient", "Eigenvalues are the extreme quadratic-form values")
        self.play(Write(self.matrix(r"A=\begin{bmatrix}3&1\\1&3\end{bmatrix}")))
        self.cc("For nonzero x, the Rayleigh quotient compares x transpose A x with the squared length of x.", 2.9)
        self.play(Write(self.eq(r"R(x)=\frac{x^TAx}{x^Tx}", 1.00, 0.80)))
        self.play(Write(self.eq(r"2\le R(x)\le4", 0.90, -0.02)))
        self.play(Write(self.eq(r"R(q_1)=4,\qquad R(q_2)=2", 0.84, -0.90)))
        self.cc("For a real symmetric matrix, the smallest and largest eigenvalues are the minimum and maximum of the Rayleigh quotient.", 3.1)
        self.wait(2)


class Part9_08_PositiveDefinite(SymmetricMatrixLesson):
    def construct(self):
        self.title("Part IX.8 — Positive Definite Matrices", "Quadratic forms that are always positive")
        self.play(Write(self.matrix(r"A=\begin{bmatrix}3&1\\1&3\end{bmatrix}")))
        self.play(Write(self.eq(r"x\neq0\Rightarrow x^TAx>0", 0.96, 0.85)))
        self.play(Write(self.eq(r"\lambda_1=4>0,\qquad\lambda_2=2>0", 0.80, 0.10)))
        self.cc("For real symmetric matrices, positive definiteness is equivalent to every eigenvalue being positive.", 3.0)
        self.play(Write(self.eq(r"\boxed{A\succ0\iff\lambda_i>0\text{ for all }i}", 0.70, -0.85)))
        self.wait(2)


class Part9_09_NegativeAndIndefinite(SymmetricMatrixLesson):
    def construct(self):
        self.title("Part IX.9 — Negative Definite and Indefinite", "Eigenvalue signs classify the quadratic form")
        self.play(Write(self.eq(r"A_- =\begin{bmatrix}-2&0\\0&-1\end{bmatrix}", 0.82, 1.20)))
        self.play(Write(self.eq(r"\lambda_1=-2,\quad\lambda_2=-1\Rightarrow x^TA_-x<0\ (x\neq0)", 0.64, 0.25)))
        self.play(Write(self.eq(r"A_{\pm}=\begin{bmatrix}1&0\\0&-2\end{bmatrix}", 0.82, -0.65)))
        self.play(Write(self.eq(r"q(x,y)=x^2-2y^2\quad\text{takes both signs}", 0.67, -1.50)))
        self.cc("All negative eigenvalues give negative definiteness. Mixed signs give an indefinite quadratic form.", 3.0)
        self.play(Write(self.eq(r"\text{negative definite}\iff\lambda_i<0", 0.72, -2.15)))
        self.play(Write(self.eq(r"\text{indefinite}\iff\text{eigenvalues have mixed signs}", 0.67, -2.75)))
        self.wait(2)


class Part9_10_SemidefiniteAndTests(SymmetricMatrixLesson):
    def construct(self):
        self.title("Part IX.10 — Semidefinite Matrices and Tests", "Zero eigenvalues create flat directions")
        self.play(Write(self.eq(r"A_0=\begin{bmatrix}1&0\\0&0\end{bmatrix}", 0.88, 1.15)))
        self.play(Write(self.eq(r"x^TA_0x=x^2\ge0", 0.88, 0.25)))
        self.play(Write(self.eq(r"\lambda_1=1,\quad\lambda_2=0\Rightarrow\text{positive semidefinite}", 0.65, -0.65)))
        self.cc("Positive semidefinite allows zero values for nonzero vectors. A zero eigenvalue marks a flat direction.", 3.0)
        self.play(Write(self.eq(r"\text{PSD}\iff\lambda_i\ge0", 0.82, -1.45)))
        self.play(Write(self.eq(r"\text{NSD}\iff\lambda_i\le0", 0.82, -2.10)))
        self.wait(2)


class Part9_11_SymmetricMatrixMastery(SymmetricMatrixLesson):
    def construct(self):
        self.title("Part IX.11 — Symmetric Matrix Mastery", "One chain connects symmetry, eigenvectors, and geometry")
        summary = VGroup(
            Text("Symmetric → A = Aᵀ", font_size=21),
            Text("Distinct eigenvalues → orthogonal eigenvectors", font_size=21),
            Text("Spectral theorem → A = QΛQᵀ", font_size=21),
            Text("Quadratic form → q(x) = xᵀAx", font_size=21),
            Text("Eigenvectors → principal axes", font_size=21),
            Text("Eigenvalues → extremal Rayleigh values", font_size=21),
            Text("All λ > 0 → positive definite", font_size=21),
            Text("All λ < 0 → negative definite", font_size=21),
            Text("Mixed signs → indefinite", font_size=21),
            Text("Zeros → semidefinite / flat directions", font_size=21),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.12).to_edge(RIGHT, buff=0.04).shift(DOWN * 0.02)
        self.play(LaggedStart(*[Write(s) for s in summary], lag_ratio=0.10), run_time=3.0)
        self.cc("Symmetry gives orthogonal eigen-directions; those directions diagonalize the quadratic form; eigenvalue signs then classify its geometry.", 3.6)
        self.play(Write(self.eq(r"\boxed{A=A^T\Rightarrow A=Q\Lambda Q^T}", 0.72, -2.35)))
        self.play(Write(Text("Part IX complete: symmetry turns a coupled quadratic form into independent principal directions.", font_size=22, color=YELLOW_B).to_edge(DOWN, buff=0.38)))
        self.wait(3)


__all__ = [name for name in globals() if name.startswith("Part9_") or name == "SymmetricMatrixLesson"]
