import numpy as np
from manim import *
from ..utils import LessonScene, VECTOR_A, VECTOR_B, HIGHLIGHT


class EigenvalueLesson(LessonScene):
    """Canonical Part VIII: Eigenvalues and eigenvectors."""

    A = [[3, 1], [0, 2]]
    eigvals = (3, 2)
    v3 = [1, 0]
    v2 = [1, -1]

    def axes2d(self, x_range=(-4, 5), y_range=(-4, 5)):
        return Axes(
            x_range=[x_range[0], x_range[1], 1],
            y_range=[y_range[0], y_range[1], 1],
            x_length=7.2,
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
            z_length=5.6,
        )
        self.set_camera_orientation(phi=68 * DEGREES, theta=32 * DEGREES)
        return axes.to_edge(LEFT, buff=0.15)

    def eq(self, latex, scale=0.68, y=0):
        return MathTex(latex).scale(scale).to_edge(RIGHT, buff=0.15).shift(UP * y)

    def matrix(self, latex, scale=0.70, y=1.55):
        return MathTex(latex).scale(scale).to_edge(RIGHT, buff=0.15).shift(UP * y)

    def line2d(self, ax, direction, color, length=3.2):
        dx, dy = direction
        norm = np.hypot(dx, dy)
        dx, dy = dx / norm * length, dy / norm * length
        return Line(ax.c2p(-dx, -dy), ax.c2p(dx, dy), color=color, stroke_width=4)


class Part8_01_EigenvectorIntuition(EigenvalueLesson):
    def construct(self):
        self.title("Part VIII.1 — Eigenvector Intuition", "Special directions that a matrix only stretches or flips")
        ax = self.axes2d()
        self.play(Create(ax))
        v1 = Arrow(ax.c2p(0, 0), ax.c2p(2, 0), buff=0, color=VECTOR_A, stroke_width=6)
        v2 = Arrow(ax.c2p(0, 0), ax.c2p(1, -1), buff=0, color=VECTOR_B, stroke_width=6)
        self.play(GrowArrow(v1), GrowArrow(v2))
        self.cc("Most vectors change both length and direction when a matrix acts on them. An eigenvector is special: the direction survives the transformation.", 3.1)
        self.play(Write(self.matrix(r"A=\begin{bmatrix}3&1\\0&2\end{bmatrix}")))
        self.play(Write(self.eq(r"A\begin{bmatrix}1\\0\end{bmatrix}=3\begin{bmatrix}1\\0\end{bmatrix}", 0.78, 0.75)))
        self.play(Write(self.eq(r"A\begin{bmatrix}1\\-1\end{bmatrix}=2\begin{bmatrix}1\\-1\end{bmatrix}", 0.78, -0.10)))
        self.cc("These two directions are invariant lines. The matrix stretches the first by three and the second by two, without rotating either direction away from its line.", 3.2)
        self.play(Write(self.eq(r"\boxed{Av=\lambda v}", 0.98, -1.20)))
        self.cc("The number lambda is the eigenvalue: it tells us the exact scale factor along that special direction.", 2.7)
        self.wait(2)


class Part8_02_EigenEquation(EigenvalueLesson):
    def construct(self):
        self.title("Part VIII.2 — The Eigenvalue Equation", "Turn geometry into one algebraic condition")
        self.play(Write(self.matrix(r"A=\begin{bmatrix}3&1\\0&2\end{bmatrix}")))
        self.cc("Start from the definition: A times v must equal lambda times v. Move everything to one side so the unknown vector is multiplied by one matrix.", 3.0)
        self.play(Write(self.eq(r"Av=\lambda v", 0.95, 0.85)))
        self.play(Write(self.eq(r"(A-\lambda I)v=0", 0.92, 0.15)))
        self.cc("A nonzero eigenvector exists only when A minus lambda I has a nontrivial null space. That means the matrix must be singular.", 3.0)
        self.play(Write(self.eq(r"\det(A-\lambda I)=0", 0.95, -0.70)))
        self.play(Write(self.eq(r"\boxed{\text{eigenvalues come from a singular }A-\lambda I}", 0.65, -1.55)))
        self.wait(2)


class Part8_03_CharacteristicPolynomial(EigenvalueLesson):
    def construct(self):
        self.title("Part VIII.3 — Characteristic Polynomial", "Find the eigenvalues systematically")
        self.play(Write(self.matrix(r"A=\begin{bmatrix}3&1\\0&2\end{bmatrix}")))
        self.cc("Subtract lambda from the diagonal and take the determinant. This produces a polynomial whose roots are exactly the eigenvalues.", 3.0)
        self.play(Write(self.eq(r"A-\lambda I=\begin{bmatrix}3-\lambda&1\\0&2-\lambda\end{bmatrix}", 0.64, 0.75)))
        self.play(Write(self.eq(r"p(\lambda)=\det(A-\lambda I)=(3-\lambda)(2-\lambda)", 0.67, -0.05)))
        self.play(Write(self.eq(r"=\lambda^2-5\lambda+6=(\lambda-3)(\lambda-2)", 0.64, -0.85)))
        self.play(Write(self.eq(r"\boxed{\lambda_1=3,\qquad \lambda_2=2}", 0.84, -1.70)))
        self.cc("The characteristic polynomial packages the search for special directions into an ordinary root-finding problem.", 2.8)
        self.wait(2)


class Part8_04_FindingEigenvectors(EigenvalueLesson):
    def construct(self):
        self.title("Part VIII.4 — Finding Eigenvectors", "Each eigenvalue gives a null-space problem")
        self.play(Write(self.matrix(r"A=\begin{bmatrix}3&1\\0&2\end{bmatrix}")))
        self.cc("Once an eigenvalue is known, return to the equation (A minus lambda I)v equals zero and solve for the corresponding direction.", 3.0)
        self.play(Write(self.eq(r"\lambda=3:\quad(A-3I)v=0\Rightarrow v=t\begin{bmatrix}1\\0\end{bmatrix}", 0.65, 0.85)))
        self.play(Write(self.eq(r"\lambda=2:\quad(A-2I)v=0\Rightarrow v=t\begin{bmatrix}1\\-1\end{bmatrix}", 0.65, -0.05)))
        self.cc("Notice the pattern: eigenvalues are scalar values, while eigenvectors form directions or, more precisely, eigenspaces.", 2.9)
        self.play(Write(self.eq(r"E_{3}=\operatorname{span}\left\{\begin{bmatrix}1\\0\end{bmatrix}\right\}", 0.67, -0.85)))
        self.play(Write(self.eq(r"E_{2}=\operatorname{span}\left\{\begin{bmatrix}1\\-1\end{bmatrix}\right\}", 0.67, -1.70)))
        self.wait(2)


class Part8_05_GeometricEigenspaces(EigenvalueLesson):
    def construct(self):
        self.title("Part VIII.5 — Geometric Eigenspaces", "Eigenvectors form entire invariant subspaces")
        ax = self.axes2d(x_range=(-4, 4), y_range=(-4, 4))
        self.play(Create(ax))
        line1 = self.line2d(ax, (1, 0), VECTOR_A)
        line2 = self.line2d(ax, (1, -1), VECTOR_B)
        self.play(Create(line1), Create(line2))
        self.play(Write(self.matrix(r"A=\begin{bmatrix}3&1\\0&2\end{bmatrix}")))
        self.cc("An eigenspace is not one vector. It is the entire set of eigenvectors associated with an eigenvalue, including every scalar multiple and the zero vector.", 3.2)
        self.play(Write(self.eq(r"E_3=\operatorname{span}\{(1,0)\}", 0.82, 0.80)))
        self.play(Write(self.eq(r"E_2=\operatorname{span}\{(1,-1)\}", 0.82, 0.10)))
        self.cc("The key geometric property is invariance: applying A to any vector in an eigenspace leaves it inside the same line.", 2.8)
        self.play(Write(self.eq(r"v\in E_\lambda\Rightarrow Av\in E_\lambda", 0.80, -0.80)))
        self.wait(2)


class Part8_06_AlgebraicVsGeometricMultiplicity(EigenvalueLesson):
    def construct(self):
        self.title("Part VIII.6 — Algebraic vs Geometric Multiplicity", "Repeated eigenvalues can have one or several directions")
        self.cc("A repeated root of the characteristic polynomial is algebraic multiplicity. The dimension of its eigenspace is geometric multiplicity.", 3.1)
        self.play(Write(self.matrix(r"D=\begin{bmatrix}2&0\\0&2\end{bmatrix}")))
        self.play(Write(self.eq(r"p(\lambda)=(\lambda-2)^2", 0.90, 0.80)))
        self.play(Write(self.eq(r"m_a(2)=2,\qquad m_g(2)=2", 0.84, 0.05)))
        self.cc("This matrix has one repeated eigenvalue, but its eigenspace is the whole plane. Two independent eigenvectors are available.", 2.8)
        self.play(Write(self.eq(r"E_2=\mathbb{R}^2", 0.90, -0.75)))
        self.play(Write(self.eq(r"J=\begin{bmatrix}2&1\\0&2\end{bmatrix}:\quad m_a(2)=2,\quad m_g(2)=1", 0.66, -1.60)))
        self.cc("The Jordan block has the same algebraic multiplicity, but only one independent eigenvector. This is exactly the obstruction to diagonalization.", 3.0)
        self.wait(2)


class Part8_07_Diagonalization(EigenvalueLesson):
    def construct(self):
        self.title("Part VIII.7 — Diagonalization", "Replace a complicated transformation with independent eigen-directions")
        self.play(Write(self.matrix(r"A=\begin{bmatrix}3&1\\0&2\end{bmatrix}")))
        self.cc("If we can find enough independent eigenvectors to form a basis, we can place them into a matrix P and the eigenvalues into a diagonal matrix D.", 3.0)
        self.play(Write(self.eq(r"P=\begin{bmatrix}1&1\\0&-1\end{bmatrix},\qquad D=\begin{bmatrix}3&0\\0&2\end{bmatrix}", 0.64, 0.70)))
        self.play(Write(self.eq(r"A=PDP^{-1}", 1.02, -0.15)))
        self.cc("In the eigenvector coordinate system, the transformation becomes diagonal: each coordinate direction is simply scaled by its eigenvalue.", 3.0)
        self.play(Write(self.eq(r"A^k=PD^kP^{-1}", 0.94, -1.05)))
        self.play(Write(self.eq(r"\boxed{\text{diagonalization = change basis to eigenvectors}}", 0.65, -1.90)))
        self.wait(2)


class Part8_08_MatrixPowers(EigenvalueLesson):
    def construct(self):
        self.title("Part VIII.8 — Matrix Powers", "Repeated transformations become scalar powers")
        self.play(Write(self.eq(r"A=PDP^{-1}", 1.00, 1.35)))
        self.play(Write(self.eq(r"A^k=PD^kP^{-1}", 1.00, 0.55)))
        self.play(Write(self.eq(r"D^k=\begin{bmatrix}3^k&0\\0&2^k\end{bmatrix}", 0.78, -0.25)))
        self.cc("Instead of multiplying A by itself again and again, diagonalization turns the hard part into scalar exponentiation.", 3.0)
        self.play(Write(self.eq(r"A^2=\begin{bmatrix}9&5\\0&4\end{bmatrix}", 0.84, -1.10)))
        self.play(Write(self.eq(r"A^3=\begin{bmatrix}27&19\\0&8\end{bmatrix}", 0.84, -1.90)))
        self.cc("The diagonal entries reveal the long-term behavior immediately: the eigenvalue with largest magnitude eventually dominates repeated applications.", 3.0)
        self.wait(2)


class Part8_09_DynamicsAndEigenDirections(EigenvalueLesson):
    def construct(self):
        self.title("Part VIII.9 — Eigenvectors in Dynamical Systems", "The dominant eigenvalue controls long-term behavior")
        ax = self.axes2d(x_range=(-4, 4), y_range=(-4, 4))
        self.play(Create(ax))
        v = Arrow(ax.c2p(0, 0), ax.c2p(1, 1), buff=0, color=HIGHLIGHT, stroke_width=6)
        self.play(GrowArrow(v))
        self.play(Write(self.eq(r"x_{k+1}=Ax_k", 0.92, 1.40)))
        self.play(Write(self.eq(r"x_k=A^k x_0", 0.92, 0.70)))
        self.play(Write(self.eq(r"A^k\sim P\begin{bmatrix}3^k&0\\0&2^k\end{bmatrix}P^{-1}", 0.63, -0.15)))
        self.cc("Because 3 grows faster than 2, components aligned with the eigenvalue-three direction dominate as k becomes large, provided that component is present.", 3.2)
        self.play(Write(self.eq(r"3^k\gg2^k\quad\text{as }k\to\infty", 0.82, -1.05)))
        self.cc("This is why eigenvalues appear throughout dynamical systems, recurrence relations, stability analysis, and machine learning optimization.", 3.0)
        self.play(Write(self.eq(r"\boxed{\text{eigenvalues reveal growth, decay, or oscillation rates}}", 0.63, -1.85)))
        self.wait(2)


class Part8_10_EigenvaluesBeyond2D(EigenvalueLesson):
    def construct(self):
        self.title("Part VIII.10 — Eigenvalues Beyond 2D", "The same ideas survive in higher dimensions")
        axes = self.axes3d()
        self.play(Create(axes))
        self.play(Write(self.matrix(r"A=\begin{bmatrix}4&0&0\\0&2&0\\0&0&1\end{bmatrix}", 0.60, 1.55)))
        e1 = Arrow3D(ORIGIN, axes.c2p(2, 0, 0), color=VECTOR_A, thickness=0.025)
        e2 = Arrow3D(ORIGIN, axes.c2p(0, 1.2, 0), color=VECTOR_B, thickness=0.025)
        e3 = Arrow3D(ORIGIN, axes.c2p(0, 0, 0.7), color=HIGHLIGHT, thickness=0.025)
        self.play(Create(e1), Create(e2), Create(e3))
        self.cc("In three dimensions a matrix can have three independent invariant directions. For a diagonal matrix, the coordinate axes are already eigen-directions.", 3.1)
        self.play(Write(self.eq(r"\lambda_1=4,\quad\lambda_2=2,\quad\lambda_3=1", 0.78, -0.35)))
        self.play(Write(self.eq(r"Ae_i=\lambda_i e_i", 0.92, -1.10)))
        self.cc("Nothing essential changed from two dimensions. We still search for invariant directions, solve a characteristic equation, and study the corresponding eigenspaces.", 3.0)
        self.wait(2)


class Part8_11_EigenvalueMastery(EigenvalueLesson):
    def construct(self):
        self.title("Part VIII.11 — Eigenvalue Mastery", "One concept connecting geometry, algebra, and dynamics")
        summary = VGroup(
            Text("Eigenvector → invariant direction", font_size=21),
            Text("Eigenvalue → scale factor on that direction", font_size=21),
            Text("A − λI → search for invariant directions", font_size=21),
            Text("det(A − λI)=0 → characteristic equation", font_size=21),
            Text("Eigenspace → all eigenvectors for λ", font_size=21),
            Text("Multiplicity → repeated eigenvalues and eigenspace size", font_size=21),
            Text("Diagonalization → eigenvector coordinate system", font_size=21),
            Text("Powers → scalar powers in diagonal form", font_size=21),
            Text("Dynamics → dominant eigenvalues control growth", font_size=21),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.14).to_edge(RIGHT, buff=0.05).shift(DOWN * 0.10)
        self.play(LaggedStart(*[Write(s) for s in summary], lag_ratio=0.12), run_time=3.0)
        self.cc("The goal is not to memorize a recipe. See the same story from three angles: invariant geometry, null-space algebra, and long-term dynamics.", 3.5)
        self.play(Write(self.eq(r"\boxed{Av=\lambda v\quad\Longleftrightarrow\quad\text{special directions of }A}", 0.62, -2.55)))
        self.play(Write(Text("Part VIII complete: eigenvalues turn repeated matrix behavior into understandable scalar behavior.", font_size=23, color=YELLOW_B).to_edge(DOWN, buff=0.42)))
        self.wait(3)


__all__ = [name for name in globals() if name.startswith("Part8_") or name == "EigenvalueLesson"]
