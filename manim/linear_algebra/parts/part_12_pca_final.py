from math import sqrt

import numpy as np
from manim import *

from ..utils import HIGHLIGHT, LessonScene, VECTOR_A, VECTOR_B


class PCALesson(LessonScene):
    """Canonical Part XII: PCA from centering through reconstruction and SVD."""

    Q1 = np.array([1 / sqrt(2), 1 / sqrt(2)], dtype=float)
    Q2 = np.array([1 / sqrt(2), -1 / sqrt(2)], dtype=float)
    LAMBDAS = (1.5, 0.5)

    # Four exact centered observations, chosen so C = (1/n) X^T X exactly equals
    # [[1, 1/2], [1/2, 1]].
    DATA = np.array(
        [
            sqrt(3) * Q1,
            -sqrt(3) * Q1,
            Q2,
            -Q2,
        ],
        dtype=float,
    )

    def axes2d(self, x_range=(-2.5, 2.5), y_range=(-2.5, 2.5)):
        return Axes(
            x_range=[x_range[0], x_range[1], 1],
            y_range=[y_range[0], y_range[1], 1],
            x_length=7.2,
            y_length=6.0,
            axis_config={"include_numbers": True, "stroke_width": 2},
        ).to_edge(LEFT, buff=0.22)

    def eq(self, latex, scale=0.67, y=0):
        return MathTex(latex).scale(scale).to_edge(RIGHT, buff=0.14).shift(UP * y)

    def matrix(self, latex, scale=0.68, y=1.55):
        return MathTex(latex).scale(scale).to_edge(RIGHT, buff=0.14).shift(UP * y)

    def scatter(self, ax, pts=None, radius=0.07, mob_color=HIGHLIGHT):
        pts = self.DATA if pts is None else np.asarray(pts)
        return VGroup(*[Dot(ax.c2p(float(x), float(y)), radius=radius, color=mob_color) for x, y in pts])

    def principal_lines(self, ax):
        n = 2.25
        q1 = Line(ax.c2p(-n * self.Q1[0], -n * self.Q1[1]), ax.c2p(n * self.Q1[0], n * self.Q1[1]), color=VECTOR_A, stroke_width=4)
        q2 = Line(ax.c2p(-n * self.Q2[0], -n * self.Q2[1]), ax.c2p(n * self.Q2[0], n * self.Q2[1]), color=VECTOR_B, stroke_width=4)
        return q1, q2


class Part12_01_PCAIntuition(PCALesson):
    def construct(self):
        self.title("Part XII.1 — PCA Intuition", "Find the directions that capture the most variation")
        ax = self.axes2d()
        self.play(Create(ax))
        points = self.scatter(ax)
        self.play(FadeIn(points, lag_ratio=0.12))
        self.cc("Principal component analysis looks for a direction along which the data varies the most. That direction becomes the first principal component.", 3.2)
        q1, q2 = self.principal_lines(ax)
        self.play(Create(q1), Create(q2))
        self.play(Write(self.eq(r"\text{PC}_1=\text{direction of maximum variance}", 0.70, 0.92)))
        self.play(Write(self.eq(r"\text{PC}_2=\text{best orthogonal remaining direction}", 0.66, 0.15)))
        self.cc("The components are perpendicular here because the covariance matrix is symmetric. PCA turns a cloud of correlated coordinates into new uncorrelated coordinates.", 3.0)
        self.wait(2)


class Part12_02_CenteringData(PCALesson):
    def construct(self):
        self.title("Part XII.2 — Centering the Data", "Move the mean to the origin before measuring variation")
        ax = self.axes2d(x_range=(-1, 4), y_range=(-1, 4))
        self.play(Create(ax))
        shifted = self.DATA + np.array([1.5, 1.0])
        p = self.scatter(ax, shifted)
        mean = Dot(ax.c2p(1.5, 1.0), color=VECTOR_B, radius=0.10)
        self.play(FadeIn(p, lag_ratio=0.12), FadeIn(mean))
        self.play(Write(self.eq(r"\mu=\frac1n\sum_{i=1}^n x_i", 0.90, 0.95)))
        self.play(Write(self.eq(r"X_c=X-\mathbf{1}\mu^T", 0.86, 0.20)))
        self.cc("Subtracting the mean removes the absolute location of the cloud. PCA then analyzes only how the observations vary around their center.", 3.1)
        centered = self.scatter(ax, self.DATA)
        self.play(FadeOut(p), FadeOut(mean), FadeIn(centered, lag_ratio=0.12))
        self.play(Write(self.eq(r"\boxed{\text{center first, then analyze variation}}", 0.72, -0.85)))
        self.wait(2)


class Part12_03_CovarianceMatrix(PCALesson):
    def construct(self):
        self.title("Part XII.3 — Covariance Matrix", "Turn the cloud into a matrix of variances and covariances")
        self.play(Write(self.eq(r"C=\frac1nX_c^TX_c", 0.95, 1.05)))
        self.play(Write(self.eq(r"C=\begin{bmatrix}1&\frac12\\\frac12&1\end{bmatrix}", 0.80, 0.12)))
        self.play(Write(self.eq(r"\operatorname{Var}(x)=1,\quad\operatorname{Var}(y)=1", 0.66, -0.82)))
        self.play(Write(self.eq(r"\operatorname{Cov}(x,y)=\frac12>0", 0.70, -1.58)))
        self.cc("The diagonal entries measure variance. The off-diagonal entries measure how the two coordinates move together. A positive covariance tilts the cloud toward a common increasing direction.", 3.1)
        self.wait(2)


class Part12_04_PrincipalDirections(PCALesson):
    def construct(self):
        self.title("Part XII.4 — Principal Directions", "Eigenvectors of covariance become PCA axes")
        self.play(Write(self.matrix(r"C=\begin{bmatrix}1&\frac12\\\frac12&1\end{bmatrix}")))
        self.play(Write(self.eq(r"Cq_1=\frac32q_1", 0.88, 0.82)))
        self.play(Write(self.eq(r"q_1=\frac1{\sqrt2}\begin{bmatrix}1\\1\end{bmatrix}", 0.76, 0.05)))
        self.play(Write(self.eq(r"Cq_2=\frac12q_2", 0.88, -0.72)))
        self.play(Write(self.eq(r"q_2=\frac1{\sqrt2}\begin{bmatrix}1\\-1\end{bmatrix}", 0.76, -1.52)))
        self.cc("The eigenvectors of the covariance matrix are the principal directions. The corresponding eigenvalues tell us how much variance lies along each direction.", 3.1)
        self.wait(2)


class Part12_05_MaximumVariance(PCALesson):
    def construct(self):
        self.title("Part XII.5 — Maximum Variance", "Why the first component is an optimization problem")
        ax = self.axes2d()
        self.play(Create(ax))
        points = self.scatter(ax)
        self.play(FadeIn(points, lag_ratio=0.10))
        q1, q2 = self.principal_lines(ax)
        self.play(Create(q1), Create(q2))
        self.play(Write(self.eq(r"\max_{\|w\|=1}\operatorname{Var}(X_cw)", 0.82, 1.00)))
        self.play(Write(self.eq(r"\boxed{w=q_1,\quad\text{maximum}=\lambda_1=\frac32}", 0.68, 0.10)))
        self.cc("Among all unit directions, q1 captures the largest possible variance. The optimization condition becomes the eigenvalue equation for the covariance matrix.", 3.0)
        self.play(Write(self.eq(r"Cw=\lambda w", 0.92, -0.85)))
        self.wait(2)


class Part12_06_ProjectionOntoPCs(PCALesson):
    def construct(self):
        self.title("Part XII.6 — Projection onto Principal Components", "Convert each observation into principal coordinates")
        ax = self.axes2d()
        self.play(Create(ax))
        points = self.scatter(ax)
        q1, q2 = self.principal_lines(ax)
        self.play(FadeIn(points, lag_ratio=0.10), Create(q1), Create(q2))
        self.play(Write(self.eq(r"z_i=q_1^Tx_i", 0.92, 1.00)))
        self.play(Write(self.eq(r"z=Q^Tx", 0.86, 0.28)))
        self.play(Write(self.eq(r"\pm\sqrt3,\ 0,\ 0", 0.88, -0.45)))
        self.cc("Projection replaces the original coordinates with coordinates along the principal directions. Because the principal axes are orthonormal, Q transpose performs this change of coordinates.", 3.0)
        self.wait(2)


class Part12_07_Reconstruction(PCALesson):
    def construct(self):
        self.title("Part XII.7 — Reconstruction", "Turn reduced coordinates back into approximate data")
        ax = self.axes2d()
        self.play(Create(ax))
        original = self.scatter(ax)
        self.play(FadeIn(original, lag_ratio=0.10))
        reconstructed = np.array([sqrt(3) * self.Q1, -sqrt(3) * self.Q1, [0, 0], [0, 0]], dtype=float)
        approx = self.scatter(ax, reconstructed, mob_color=VECTOR_A)
        self.play(FadeIn(approx, lag_ratio=0.10))
        self.play(Write(self.eq(r"\hat x_i=z_iq_1", 0.88, 0.95)))
        self.play(Write(self.eq(r"\hat x_i=(q_1q_1^T)x_i", 0.80, 0.18)))
        self.cc("Keeping only the first principal component preserves the dominant direction but discards the orthogonal variation. Reconstruction is therefore approximate for points that contain PC2 information.", 3.1)
        self.wait(2)


class Part12_08_ExplainedVariance(PCALesson):
    def construct(self):
        self.title("Part XII.8 — Explained Variance", "Measure how much information each component keeps")
        self.play(Write(self.eq(r"\lambda_1=\frac32,\qquad\lambda_2=\frac12", 0.90, 1.00)))
        self.play(Write(self.eq(r"\text{total variance}=\frac32+\frac12=2", 0.80, 0.28)))
        self.play(Write(self.eq(r"\text{PC}_1=\frac{\lambda_1}{\lambda_1+\lambda_2}=\frac34=75\%", 0.72, -0.52)))
        self.play(Write(self.eq(r"\text{PC}_2=25\%", 0.82, -1.30)))
        self.cc("Explained variance tells us the fraction of total variation captured by each component. Here one direction preserves three quarters of the variance.", 3.0)
        self.wait(2)


class Part12_09_PCAFromSVD(PCALesson):
    def construct(self):
        self.title("Part XII.9 — PCA from SVD", "The SVD gives the same principal directions")
        self.play(Write(self.eq(r"X_c=U\Sigma V^T", 0.98, 1.05)))
        self.play(Write(self.eq(r"C=\frac1nX_c^TX_c=V\frac{\Sigma^2}{n}V^T", 0.67, 0.20)))
        self.play(Write(self.eq(r"\text{columns of }V=\text{principal directions}", 0.72, -0.70)))
        self.play(Write(self.eq(r"\lambda_i=\frac{\sigma_i^2}{n}", 0.82, -1.42)))
        self.cc("This is the key computational connection: PCA can be obtained from the right singular vectors of the centered data matrix, with covariance eigenvalues equal to squared singular values divided by n.", 3.1)
        self.wait(2)


class Part12_10_HigherDimensionalPCA(PCALesson):
    def construct(self):
        self.title("Part XII.10 — Higher-Dimensional PCA", "Compress many features into a few directions")
        self.play(Write(self.eq(r"X_c\in\mathbb{R}^{n\times d}", 0.95, 1.05)))
        self.play(Write(self.eq(r"C=\frac1nX_c^TX_c\in\mathbb{R}^{d\times d}", 0.78, 0.30)))
        self.play(Write(self.eq(r"q_1,\ldots,q_k\quad\text{= top eigenvectors}", 0.76, -0.46)))
        self.play(Write(self.eq(r"Z=X_cQ_k", 0.95, -1.22)))
        self.play(Write(self.eq(r"k\ll d", 0.92, -1.92)))
        self.cc("Nothing essential about PCA depends on two dimensions. In high dimensions, we keep the leading eigen-directions and represent each observation with far fewer coordinates.", 3.0)
        self.wait(2)


class Part12_11_PCAMastery(PCALesson):
    def construct(self):
        self.title("Part XII.11 — PCA Mastery", "The complete PCA pipeline")
        summary = VGroup(
            Text("1. Center the data", font_size=21),
            Text("2. Build the covariance matrix", font_size=21),
            Text("3. Find covariance eigenvectors", font_size=21),
            Text("4. Sort by descending eigenvalue", font_size=21),
            Text("5. Project onto the top components", font_size=21),
            Text("6. Reconstruct if needed", font_size=21),
            Text("7. Measure explained variance", font_size=21),
            Text("8. Use SVD for the numerical implementation", font_size=21),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.14).to_edge(RIGHT, buff=0.04).shift(DOWN * 0.03)
        self.play(LaggedStart(*[Write(x) for x in summary], lag_ratio=0.10), run_time=2.8)
        self.cc("PCA is not just a plotting trick. It is a principled change of coordinates that keeps the directions carrying the most variance and discards less informative directions.", 3.5)
        self.play(Write(self.eq(r"\boxed{\text{PCA} = \text{center} \rightarrow \text{covariance} \rightarrow \text{eigenvectors} \rightarrow \text{project}}", 0.60, -2.30)))
        self.wait(3)


__all__ = [name for name in globals() if name.startswith("Part12_") or name == "PCALesson"]
