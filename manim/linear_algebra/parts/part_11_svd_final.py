from math import sqrt

import numpy as np
from manim import *

from ..utils import HIGHLIGHT, LessonScene, VECTOR_A, VECTOR_B


class SVDLesson(LessonScene):
    """Part XI: singular value decomposition, geometry, pseudoinverse, low rank."""

    # A = U Sigma V^T with U a 90-degree rotation and V = I.
    A = [[0, -1], [3, 0]]
    U = [[0, -1], [1, 0]]
    Sigma = [[3, 0], [0, 1]]
    V = [[1, 0], [0, 1]]
    singular_values = (3, 1)

    def axes2d(self, x_range=(-4, 4), y_range=(-4, 4)):
        return Axes(
            x_range=[x_range[0], x_range[1], 1],
            y_range=[y_range[0], y_range[1], 1],
            x_length=7.2,
            y_length=6.0,
            axis_config={"include_numbers": True, "stroke_width": 2},
        ).to_edge(LEFT, buff=0.22)

    def axes3d(self):
        axes = ThreeDAxes(
            x_range=[-3, 3, 1],
            y_range=[-3, 3, 1],
            z_range=[-3, 3, 1],
            x_length=6.0,
            y_length=6.0,
            z_length=5.6,
        )
        self.set_camera_orientation(phi=68 * DEGREES, theta=32 * DEGREES)
        return axes.to_edge(LEFT, buff=0.15)

    def eq(self, latex, scale=0.68, y=0):
        return MathTex(latex).scale(scale).to_edge(RIGHT, buff=0.14).shift(UP * y)

    def matrix(self, latex, scale=0.70, y=1.55):
        return MathTex(latex).scale(scale).to_edge(RIGHT, buff=0.14).shift(UP * y)


class Part11_01_SVDIntuition(SVDLesson):
    def construct(self):
        self.title("Part XI.1 — SVD Intuition", "Break one linear map into three simple stages")
        self.play(Write(self.matrix(r"A=\begin{bmatrix}0&-1\\3&0\end{bmatrix}")))
        self.cc("The singular value decomposition separates a matrix into three understandable actions: a rotation or reflection, a stretch along perpendicular directions, and another rotation or reflection.", 3.2)
        self.play(Write(self.eq(r"\boxed{A=U\Sigma V^T}", 1.05, 0.78)))
        self.play(Write(self.eq(r"\text{change directions}\;\to\;\text{stretch}\;\to\;\text{change directions again}", 0.58, -0.05)))
        self.play(Write(self.eq(r"\Sigma=\begin{bmatrix}3&0\\0&1\end{bmatrix}", 0.76, -0.88)))
        self.cc("The diagonal entries of Sigma are the singular values. They tell us exactly how strongly the transformation stretches each singular direction.", 2.9)
        self.wait(2)


class Part11_02_SingularValuesFromATA(SVDLesson):
    def construct(self):
        self.title("Part XI.2 — Singular Values from AᵀA", "Turn SVD into an eigenvalue problem")
        self.play(Write(self.matrix(r"A=\begin{bmatrix}0&-1\\3&0\end{bmatrix}")))
        self.cc("The right singular vectors are eigenvectors of A transpose A. The eigenvalues of A transpose A are the squared singular values.", 3.1)
        self.play(Write(self.eq(r"A^TA=\begin{bmatrix}9&0\\0&1\end{bmatrix}", 0.78, 0.82)))
        self.play(Write(self.eq(r"\lambda_1=9,\quad\lambda_2=1", 0.86, 0.12)))
        self.play(Write(self.eq(r"\sigma_i=\sqrt{\lambda_i}", 0.92, -0.58)))
        self.play(Write(self.eq(r"\boxed{\sigma_1=3,\qquad\sigma_2=1}", 0.86, -1.34)))
        self.cc("This is the key computational bridge: ordinary eigenvalue machinery gives us the singular values after one symmetric positive-semidefinite matrix is formed.", 2.9)
        self.wait(2)


class Part11_03_RightSingularVectors(SVDLesson):
    def construct(self):
        self.title("Part XI.3 — Right Singular Vectors", "The input directions")
        ax = self.axes2d()
        self.play(Create(ax))
        e1 = Arrow(ax.c2p(0, 0), ax.c2p(2, 0), buff=0, color=VECTOR_A, stroke_width=6)
        e2 = Arrow(ax.c2p(0, 0), ax.c2p(0, 2), buff=0, color=VECTOR_B, stroke_width=6)
        self.play(GrowArrow(e1), GrowArrow(e2))
        self.play(Write(self.matrix(r"A^TA=\begin{bmatrix}9&0\\0&1\end{bmatrix}")))
        self.cc("The eigenvectors of A transpose A are the right singular vectors. For this example they are simply the coordinate directions.", 3.0)
        self.play(Write(self.eq(r"v_1=\begin{bmatrix}1\\0\end{bmatrix},\qquad v_2=\begin{bmatrix}0\\1\end{bmatrix}", 0.74, 0.55)))
        self.play(Write(self.eq(r"V=\begin{bmatrix}1&0\\0&1\end{bmatrix}", 0.78, -0.30)))
        self.cc("The right singular vectors describe the special input directions before the main stretching stage.", 2.8)
        self.wait(2)


class Part11_04_LeftSingularVectors(SVDLesson):
    def construct(self):
        self.title("Part XI.4 — Left Singular Vectors", "Where the input directions land")
        self.play(Write(self.matrix(r"Av_1=3u_1,\qquad Av_2=1u_2")))
        self.cc("Once a right singular vector is known, apply A to it and divide by its singular value. That produces the corresponding left singular vector.", 3.1)
        self.play(Write(self.eq(r"Av_1=\begin{bmatrix}0\\3\end{bmatrix}=3\begin{bmatrix}0\\1\end{bmatrix}", 0.74, 0.80)))
        self.play(Write(self.eq(r"Av_2=\begin{bmatrix}-1\\0\end{bmatrix}=1\begin{bmatrix}-1\\0\end{bmatrix}", 0.74, 0.02)))
        self.play(Write(self.eq(r"u_1=\begin{bmatrix}0\\1\end{bmatrix},\qquad u_2=\begin{bmatrix}-1\\0\end{bmatrix}", 0.70, -0.78)))
        self.play(Write(self.eq(r"U=\begin{bmatrix}0&-1\\1&0\end{bmatrix}", 0.78, -1.54)))
        self.cc("The columns of U are orthonormal output directions. SVD therefore keeps the input and output geometry separated cleanly.", 2.9)
        self.wait(2)


class Part11_05_AssemblingSVD(SVDLesson):
    def construct(self):
        self.title("Part XI.5 — Assemble UΣVᵀ", "Reconstruct the original matrix")
        self.play(Write(self.eq(r"U=\begin{bmatrix}0&-1\\1&0\end{bmatrix}", 0.72, 1.35)))
        self.play(Write(self.eq(r"\Sigma=\begin{bmatrix}3&0\\0&1\end{bmatrix}", 0.72, 0.55)))
        self.play(Write(self.eq(r"V^T=\begin{bmatrix}1&0\\0&1\end{bmatrix}", 0.72, -0.25)))
        self.play(Write(self.eq(r"U\Sigma=\begin{bmatrix}0&-1\\3&0\end{bmatrix}", 0.74, -1.05)))
        self.play(Write(self.eq(r"\boxed{U\Sigma V^T=\begin{bmatrix}0&-1\\3&0\end{bmatrix}=A}", 0.68, -1.95)))
        self.cc("The three stages reconstruct A exactly. This is not an approximation: every entry is recovered by multiplying the three factors.", 3.0)
        self.wait(2)


class Part11_06_SphereToEllipse(SVDLesson):
    def construct(self):
        self.title("Part XI.6 — Sphere to Ellipse", "SVD explains the geometry of a linear map")
        ax = self.axes2d(x_range=(-4, 4), y_range=(-4, 4))
        self.play(Create(ax))
        circle = Circle(radius=1.5, color=HIGHLIGHT, stroke_width=4).move_to(ax.c2p(0, 0))
        self.play(Create(circle))
        self.cc("Start with the unit circle. The singular directions are perpendicular, so the matrix turns this circle into an ellipse whose semiaxis lengths are the singular values.", 3.2)
        ellipse = Ellipse(width=2 * 1.0, height=2 * 3.0, color=VECTOR_A, stroke_width=4).move_to(ax.c2p(0, 0))
        self.play(ReplacementTransform(circle, ellipse), run_time=2.2)
        self.play(Write(self.eq(r"\text{semiaxis lengths}=\sigma_1,\sigma_2", 0.78, 1.05)))
        self.play(Write(self.eq(r"\boxed{3\text{ and }1}", 0.96, 0.35)))
        self.cc("The longest output radius has length three, the shortest has length one. Those two lengths are the singular values.", 2.8)
        self.wait(2)


class Part11_07_SingularValuesAndStretching(SVDLesson):
    def construct(self):
        self.title("Part XI.7 — Singular Values and Stretching", "Largest, smallest, and rank information")
        self.play(Write(self.eq(r"\sigma_{\max}=3,\qquad\sigma_{\min}=1", 0.90, 1.10)))
        self.play(Write(self.eq(r"\|Ax\|\le\sigma_{\max}\|x\|", 0.92, 0.35)))
        self.play(Write(self.eq(r"\text{maximum stretch}=3", 0.82, -0.40)))
        self.play(Write(self.eq(r"\text{minimum stretch}=1", 0.82, -1.10)))
        self.cc("The largest singular value is the operator norm in Euclidean space. The smallest is the minimum stretch when the matrix is square and invertible.", 3.0)
        self.play(Write(self.eq(r"\|A\|_2=\sigma_1=3", 0.86, -1.82)))
        self.wait(2)


class Part11_08_RankAndZeroSingularValues(SVDLesson):
    def construct(self):
        self.title("Part XI.8 — Rank and Zero Singular Values", "Zero singular values reveal lost directions")
        self.play(Write(self.eq(r"\sigma_i=0\Rightarrow\text{a direction is annihilated}", 0.82, 1.05)))
        self.cc("A zero singular value means one input direction is sent to zero. That is exactly the same kind of information described by the null space and rank.", 3.0)
        self.play(Write(self.eq(r"\operatorname{rank}(A)=\#\{\sigma_i>0\}", 0.76, 0.30)))
        self.play(Write(self.eq(r"\operatorname{nullity}(A)=\#\{\sigma_i=0\}", 0.76, -0.42)))
        self.play(Write(self.eq(r"\boxed{\text{rank = number of nonzero singular values}}", 0.69, -1.22)))
        self.cc("SVD therefore links the fundamental subspaces chapter to a numerical decomposition that quantifies exactly how much information survives.", 3.0)
        self.wait(2)


class Part11_09_Pseudoinverse(SVDLesson):
    def construct(self):
        self.title("Part XI.9 — The Moore–Penrose Pseudoinverse", "Invert the nonzero singular values instead of the whole matrix")
        self.play(Write(self.eq(r"A=U\Sigma V^T", 0.96, 1.30)))
        self.play(Write(self.eq(r"\Sigma^+=\begin{bmatrix}\frac13&0\\0&1\end{bmatrix}", 0.82, 0.48)))
        self.play(Write(self.eq(r"A^+=V\Sigma^+U^T", 0.88, -0.30)))
        self.play(Write(self.eq(r"\boxed{A^+=\begin{bmatrix}0&\frac13\\-1&0\end{bmatrix}}", 0.72, -1.12)))
        self.cc("For invertible matrices the pseudoinverse equals the ordinary inverse. SVD generalizes the idea by reciprocating only nonzero singular values and leaving zero singular values at zero.", 3.2)
        self.wait(2)


class Part11_10_LowRankApproximation(SVDLesson):
    def construct(self):
        self.title("Part XI.10 — Low-Rank Approximation", "Keep the strongest singular directions")
        self.play(Write(self.eq(r"A=\sigma_1u_1v_1^T+\sigma_2u_2v_2^T", 0.82, 1.05)))
        self.play(Write(self.eq(r"A_1=\sigma_1u_1v_1^T", 0.90, 0.25)))
        self.play(Write(self.eq(r"A=\begin{bmatrix}0&-1\\3&0\end{bmatrix}", 0.78, -0.55)))
        self.play(Write(self.eq(r"A_1=\begin{bmatrix}0&0\\3&0\end{bmatrix}", 0.78, -1.18)))
        self.play(Write(self.eq(r"\|A-A_1\|_2=\sigma_2=1", 0.78, -1.90)))
        self.cc("The best rank-one approximation keeps the singular component with the largest singular value. The discarded singular value controls the spectral-norm error.", 3.2)
        self.wait(2)


class Part11_11_SVDMastery(SVDLesson):
    def construct(self):
        self.title("Part XI.11 — SVD Mastery", "One decomposition connects geometry, rank, inversion, and compression")
        summary = VGroup(
            Text("AᵀA → right singular vectors + squared singular values", font_size=20),
            Text("σᵢ → principal stretch factors", font_size=20),
            Text("U → output singular directions", font_size=20),
            Text("A = UΣVᵀ → exact reconstruction", font_size=20),
            Text("rank → number of nonzero σᵢ", font_size=20),
            Text("A⁺ → reciprocate nonzero singular values", font_size=20),
            Text("low-rank approximation → keep the largest σᵢ", font_size=20),
            Text("SVD → geometry + numerical structure", font_size=20),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15).to_edge(RIGHT, buff=0.03).shift(DOWN * 0.02)
        self.play(LaggedStart(*[Write(s) for s in summary], lag_ratio=0.11), run_time=3.0)
        self.cc("The singular value decomposition is powerful because one factorization answers several questions at once: what directions matter, how strongly they stretch, what information is lost, and how to approximate or invert the map.", 3.6)
        self.play(Write(self.eq(r"\boxed{A=U\Sigma V^T}", 1.05, -2.35)))
        self.play(Write(Text("Part XI complete: SVD turns a linear map into understandable orthogonal directions and scalar strengths.", font_size=22, color=YELLOW_B).to_edge(DOWN, buff=0.38)))
        self.wait(3)


__all__ = [name for name in globals() if name.startswith("Part11_") or name == "SVDLesson"]
