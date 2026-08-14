from manim import *
import numpy as np

from ..utils import HIGHLIGHT, LessonScene, VECTOR_A, VECTOR_B


class NumericalMLLesson(LessonScene):
    """Canonical Part XIII: numerical linear algebra and ML connections."""

    def axes2d(self, x_range=(-5, 5), y_range=(-5, 5)):
        return Axes(x_range=[x_range[0], x_range[1], 1], y_range=[y_range[0], y_range[1], 1], x_length=7.2, y_length=5.8, axis_config={"include_numbers": True, "stroke_width": 2}).to_edge(LEFT, buff=0.22)

    def eq(self, latex, scale=0.68, y=0):
        return MathTex(latex).scale(scale).to_edge(RIGHT, buff=0.14).shift(UP * y)


class Part13_01_NumericalLinearAlgebra(NumericalMLLesson):
    def construct(self):
        self.title("Part XIII.1 — Numerical Linear Algebra", "Exact mathematics meets finite computation")
        self.play(Write(self.eq(r"\text{mathematics}\rightarrow\text{algorithm}\rightarrow\text{floating-point numbers}", 0.68, 1.05)))
        self.play(Write(self.eq(r"\boxed{\text{stable algorithm}\neq\text{merely correct formula}}", 0.72, 0.25)))
        self.cc("A mathematical formula can be exact while a computer implementation is inaccurate. Numerical linear algebra asks how errors enter, how they grow, and how algorithms control them.", 3.2)
        self.play(Write(self.eq(r"\text{data}\rightarrow\text{matrix operations}\rightarrow\text{model output}", 0.70, -0.75)))
        self.play(Write(self.eq(r"\text{PCA, regression, neural nets, embeddings}", 0.72, -1.50)))
        self.wait(2)


class Part13_02_Conditioning(NumericalMLLesson):
    def construct(self):
        self.title("Part XIII.2 — Conditioning", "How sensitive is the problem itself?")
        self.play(Write(self.eq(r"\kappa(A)=\|A\|\,\|A^{-1}\|", 0.90, 1.05)))
        self.play(Write(self.eq(r"\kappa(I)=1", 0.86, 0.30)))
        self.play(Write(self.eq(r"A=\begin{bmatrix}1&0\\0&\varepsilon\end{bmatrix}\Rightarrow\kappa_2(A)=\frac1\varepsilon", 0.64, -0.48)))
        self.play(Write(self.eq(r"\varepsilon=10^{-3}\Rightarrow\kappa_2=10^3", 0.72, -1.28)))
        self.cc("Conditioning describes the sensitivity of the problem, not the quality of the algorithm. A large condition number means small input errors can produce much larger output changes.", 3.1)
        self.wait(2)


class Part13_03_FloatingPointAndCancellation(NumericalMLLesson):
    def construct(self):
        self.title("Part XIII.3 — Floating-Point Error", "Small representation errors can change arithmetic")
        self.play(Write(self.eq(r"x\mapsto\operatorname{fl}(x)=x(1+\delta),\qquad|\delta|\lesssim u", 0.70, 1.00)))
        self.play(Write(self.eq(r"(1+10^{-16})-1\approx0\text{ numerically}", 0.72, 0.22)))
        self.cc("Computers represent real numbers with finite precision. Subtracting nearly equal numbers can destroy significant digits; this is called catastrophic cancellation.", 3.0)
        self.play(Write(self.eq(r"\boxed{\text{avoid subtracting nearly equal quantities when possible}}", 0.65, -0.72)))
        self.wait(2)


class Part13_04_StableAlgorithms(NumericalMLLesson):
    def construct(self):
        self.title("Part XIII.4 — Stable Algorithms", "Algebraically equivalent does not mean numerically equivalent")
        self.play(Write(self.eq(r"Ax=b\quad\text{via Gaussian elimination with pivoting}", 0.76, 1.05)))
        self.play(Write(self.eq(r"\text{QR}\;\text{avoids forming}\;A^TA\;\text{when stability matters}", 0.60, 0.18)))
        self.play(Write(self.eq(r"\text{SVD}\;\text{reveals rank and small singular directions}", 0.63, -0.60)))
        self.cc("A stable algorithm keeps rounding errors controlled. Pivoting, orthogonal transformations, and SVD are important because they reduce unnecessary error amplification.", 3.1)
        self.play(Write(self.eq(r"\boxed{\text{algorithm design is part of the mathematics}}", 0.70, -1.45)))
        self.wait(2)


class Part13_05_LeastSquares(NumericalMLLesson):
    def construct(self):
        self.title("Part XIII.5 — Least Squares", "Fit the closest vector when Ax=b has no exact solution")
        ax = self.axes2d(x_range=(-1, 5), y_range=(-1, 5))
        self.play(Create(ax))
        line = Line(ax.c2p(0, 1), ax.c2p(4, 4), color=VECTOR_A, stroke_width=4)
        point = Dot(ax.c2p(2, 4), radius=0.08, color=HIGHLIGHT)
        foot = Dot(ax.c2p(2.4, 2.8), radius=0.07, color=VECTOR_B)
        residual = Line(point.get_center(), foot.get_center(), color=VECTOR_B, stroke_width=3)
        self.play(Create(line), FadeIn(point), FadeIn(foot), Create(residual))
        self.play(Write(self.eq(r"\min_x\|Ax-b\|_2", 0.96, 1.05)))
        self.play(Write(self.eq(r"A^T(Ax-b)=0", 0.84, 0.28)))
        self.cc("The residual is orthogonal to the column space at the least-squares solution. The fitted vector is therefore the closest point that A can produce.", 3.0)
        self.play(Write(self.eq(r"\hat b=A\hat x\in\operatorname{Col}(A)", 0.76, -0.62)))
        self.wait(2)


class Part13_06_NormalEquationsVsQR(NumericalMLLesson):
    def construct(self):
        self.title("Part XIII.6 — Normal Equations vs QR", "Same least-squares goal, different numerical paths")
        self.play(Write(self.eq(r"A^TAx=A^Tb", 0.92, 1.05)))
        self.play(Write(self.eq(r"A=QR\Rightarrow Rx=Q^Tb", 0.92, 0.28)))
        self.play(Write(self.eq(r"\kappa(A^TA)=\kappa(A)^2", 0.76, -0.52)))
        self.cc("Forming A transpose A squares the condition number. QR avoids that squaring and uses orthogonal transformations, which are numerically safer.", 3.0)
        self.play(Write(self.eq(r"\boxed{\text{prefer QR when numerical stability matters}}", 0.72, -1.35)))
        self.wait(2)


class Part13_07_LinearRegression(NumericalMLLesson):
    def construct(self):
        self.title("Part XIII.7 — Linear Regression", "Least squares becomes an ML training problem")
        self.play(Write(self.eq(r"y\approx X\beta", 1.00, 1.02)))
        self.play(Write(self.eq(r"\hat\beta=\arg\min_\beta\|X\beta-y\|_2^2", 0.78, 0.28)))
        self.play(Write(self.eq(r"\nabla L(\beta)=2X^T(X\beta-y)", 0.74, -0.52)))
        self.play(Write(self.eq(r"X^T(X\hat\beta-y)=0", 0.86, -1.30)))
        self.cc("Linear regression is linear algebra applied to data. The design matrix contains features, beta contains parameters, and least squares chooses the parameter vector with the smallest residual norm.", 3.15)
        self.wait(2)


class Part13_08_GradientDescent(NumericalMLLesson):
    def construct(self):
        self.title("Part XIII.8 — Gradient Descent", "Move parameters opposite the gradient")
        ax = self.axes2d(x_range=(-2, 2), y_range=(-1, 5))
        self.play(Create(ax))
        curve = FunctionGraph(lambda x: (x - 0.5) ** 2 + 0.5, x_range=[-1.5, 1.5], color=VECTOR_A)
        x0, x1, x2 = -1.2, -0.2, 0.36
        p0 = Dot(ax.c2p(x0, (x0 - 0.5) ** 2 + 0.5), color=HIGHLIGHT)
        p1 = Dot(ax.c2p(x1, (x1 - 0.5) ** 2 + 0.5), color=HIGHLIGHT)
        p2 = Dot(ax.c2p(x2, (x2 - 0.5) ** 2 + 0.5), color=HIGHLIGHT)
        self.play(Create(curve), FadeIn(p0))
        self.play(Transform(p0, p1), run_time=0.9)
        self.play(Transform(p0, p2), run_time=0.9)
        self.play(Write(self.eq(r"\theta_{k+1}=\theta_k-\eta\nabla J(\theta_k)", 0.82, 1.02)))
        self.play(Write(self.eq(r"\eta>0\quad\text{= learning rate}", 0.72, 0.26)))
        self.cc("Gradient descent is an iterative numerical method. The learning rate controls the step size; too large can overshoot, too small can converge slowly.", 3.0)
        self.wait(2)


class Part13_09_NeuralNetworkLinearAlgebra(NumericalMLLesson):
    def construct(self):
        self.title("Part XIII.9 — Neural Networks", "Every dense layer is linear algebra plus a nonlinearity")
        self.play(Write(self.eq(r"z=Wx+b", 1.12, 1.00)))
        self.play(Write(self.eq(r"a=\phi(z)", 1.02, 0.30)))
        self.play(Write(self.eq(r"x\rightarrow W_1x+b_1\rightarrow\phi\rightarrow W_2a+b_2", 0.62, -0.50)))
        self.play(Write(self.eq(r"W\in\mathbb{R}^{m\times n}", 0.82, -1.28)))
        self.cc("A fully connected neural network is a sequence of matrix-vector products, bias additions, and nonlinear functions. The linear algebra you learned is the computational backbone of the layer.", 3.2)
        self.wait(2)


class Part13_10_EmbeddingsAndSimilarity(NumericalMLLesson):
    def construct(self):
        self.title("Part XIII.10 — Embeddings and Similarity", "Represent objects as vectors in a learned space")
        ax = self.axes2d(x_range=(-2, 4), y_range=(-2, 4))
        self.play(Create(ax))
        dog = Dot(ax.c2p(2, 1), color=VECTOR_A, radius=0.09)
        cat = Dot(ax.c2p(2.5, 1.3), color=VECTOR_B, radius=0.09)
        car = Dot(ax.c2p(-1, 2), color=HIGHLIGHT, radius=0.09)
        self.play(FadeIn(dog), FadeIn(cat), FadeIn(car))
        self.play(Write(self.eq(r"\cos\theta=\frac{x^Ty}{\|x\|\|y\|}", 0.82, 1.02)))
        self.play(Write(self.eq(r"\text{small angle}\Rightarrow\text{high cosine similarity}", 0.70, 0.24)))
        self.cc("Embedding models map discrete objects into vectors. Linear algebra then supplies distance, angle, projection, nearest-neighbor search, and matrix transformations for comparing those representations.", 3.05)
        self.play(Write(self.eq(r"\boxed{\text{representation}+\text{geometry}=\text{similarity search}}", 0.64, -0.82)))
        self.wait(2)


class Part13_11_NumericalMLMastery(NumericalMLLesson):
    def construct(self):
        self.title("Part XIII.11 — Numerical + ML Mastery", "The linear algebra pipeline behind modern ML")
        summary = VGroup(
            Text("Conditioning → understand sensitivity", font_size=20),
            Text("Floating point → understand representation error", font_size=20),
            Text("Stable algorithms → control numerical error", font_size=20),
            Text("Least squares → fit data", font_size=20),
            Text("Regression → linear algebra becomes an ML objective", font_size=20),
            Text("Gradient descent → optimize parameters iteratively", font_size=20),
            Text("Neural layers → repeated matrix operations + nonlinearities", font_size=20),
            Text("Embeddings → geometry of learned representations", font_size=20),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.13).to_edge(RIGHT, buff=0.03).shift(DOWN * 0.02)
        self.play(LaggedStart(*[Write(x) for x in summary], lag_ratio=0.10), run_time=3.0)
        self.cc("The course now closes the loop: vectors become matrices, matrices become transformations, decompositions reveal structure, and numerical linear algebra turns those ideas into reliable machine-learning computation.", 3.5)
        self.play(Write(self.eq(r"\boxed{\text{linear algebra}\rightarrow\text{numerics}\rightarrow\text{machine learning}}", 0.72, -2.28)))
        self.wait(3)


__all__ = [name for name in globals() if name.startswith("Part13_") or name == "NumericalMLLesson"]
