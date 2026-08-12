from math import sqrt

from manim import *
from ..utils import *


class GeometryLesson(LessonScene):
    """Shared helpers for the canonical Part V geometry lessons."""

    def axes2d(self, x_range=(-1, 7), y_range=(-1, 7)):
        ax = Axes(
            x_range=[x_range[0], x_range[1], 1],
            y_range=[y_range[0], y_range[1], 1],
            x_length=8.0,
            y_length=6.2,
            axis_config={"include_numbers": True, "stroke_width": 2},
        ).to_edge(LEFT, buff=0.28)
        return ax

    def eq(self, latex, scale=0.68, y=0):
        return MathTex(latex).scale(scale).to_edge(RIGHT, buff=0.25).shift(UP * y)

    def vector(self, ax, xy, color, label):
        return arrow_from(ax, xy, color, label)


class Part5_01_DotProductComputation(GeometryLesson):
    def construct(self):
        self.title("Part V.1 — The Dot Product", "Multiply corresponding components, then add")
        ax = self.axes2d(); self.play(Create(ax))
        u = self.vector(ax, (3, 1), VECTOR_A, r"\vec u")
        v = self.vector(ax, (1, 2), VECTOR_B, r"\vec v")
        self.play(GrowArrow(u[0]), Write(u[1]), GrowArrow(v[0]), Write(v[1]))
        self.cc("The dot product combines two vectors into one scalar number. Start with the coordinates and multiply matching components.", 3.0)
        self.play(Write(self.eq(r"\vec u=\begin{bmatrix}3\\1\end{bmatrix},\quad\vec v=\begin{bmatrix}1\\2\end{bmatrix}", 0.62, 1.55)))
        self.play(Write(self.eq(r"\vec u\cdot\vec v=3(1)+1(2)", 0.86, 0.60)))
        self.play(Write(self.eq(r"\boxed{\vec u\cdot\vec v=5}", 0.96, -0.35)))
        self.cc("The result is a scalar, not a vector. Later we will discover that this number also measures alignment between the two directions.", 3.0)
        self.play(Write(self.eq(r"\vec u\cdot\vec v=\sum_i u_i v_i", 0.86, -1.45)))
        self.wait(2)


class Part5_02_DotProductGeometry(GeometryLesson):
    def construct(self):
        self.title("Part V.2 — Geometric Meaning of the Dot Product", "Projection turns the algebra into geometry")
        ax = self.axes2d(x_range=(-1, 6), y_range=(-1, 5)); self.play(Create(ax))
        a = self.vector(ax, (4, 0), VECTOR_A, r"\vec a")
        b = self.vector(ax, (2, 3), VECTOR_B, r"\vec b")
        self.play(GrowArrow(a[0]), Write(a[1]), GrowArrow(b[0]), Write(b[1]))
        self.cc("The first vector lies horizontally, so the shadow of b onto a is easy to see: it has length two.", 2.9)
        shadow = DashedLine(ax.c2p(2, 0), ax.c2p(2, 3), color=GREY_B, dash_length=0.12)
        self.play(Create(shadow))
        self.play(Write(self.eq(r"\vec a\cdot\vec b=4(2)=8", 0.90, 1.35)))
        self.cc("The dot product equals the length of a times the signed projection of b onto a. Here that is four times two, giving eight.", 3.2)
        self.play(Write(self.eq(r"\vec a\cdot\vec b=\|\vec a\|\,\|\vec b\|\cos\theta", 0.72, 0.15)))
        self.play(Write(self.eq(r"\text{projection length of }\vec b\text{ onto }\vec a=\|\vec b\|\cos\theta", 0.57, -0.85)))
        self.cc("This is the bridge between component algebra and geometry. A large positive dot product means the vectors point strongly in the same direction; a negative one means they oppose each other.", 3.5)
        self.wait(2)


class Part5_03_NormAndVectorLength(GeometryLesson):
    def construct(self):
        self.title("Part V.3 — Norm and Vector Length", "The dot product measures length when a vector meets itself")
        ax = self.axes2d(x_range=(-1, 5), y_range=(-1, 5)); self.play(Create(ax))
        v = self.vector(ax, (3, 4), HIGHLIGHT, r"\vec v")
        self.play(GrowArrow(v[0]), Write(v[1]))
        guides = component_guides(ax, 3, 4)
        self.play(Create(guides))
        self.cc("The vector has horizontal component three and vertical component four. Its length is the hypotenuse of a right triangle.", 2.8)
        self.play(Write(self.eq(r"\|\vec v\|=\sqrt{3^2+4^2}=5", 0.90, 1.25)))
        self.cc("The same result comes directly from the dot product: v dotted with itself is its squared length.", 2.8)
        self.play(Write(self.eq(r"\vec v\cdot\vec v=3^2+4^2=25", 0.84, 0.35)))
        self.play(Write(self.eq(r"\boxed{\|\vec v\|=\sqrt{\vec v\cdot\vec v}}", 0.83, -0.60)))
        self.cc("This definition is extremely important because it generalizes the ordinary Pythagorean length formula to any dimension.", 3.0)
        self.play(Write(self.eq(r"\|\vec v\|=\sqrt{\sum_i v_i^2}", 0.82, -1.55)))
        self.wait(2)


class Part5_04_DistanceBetweenPoints(GeometryLesson):
    def construct(self):
        self.title("Part V.4 — Distance Between Points", "Subtract first, then take the norm")
        ax = self.axes2d(x_range=(-1, 7), y_range=(-1, 7)); self.play(Create(ax))
        p = coordinate_dot(ax, (1, 1), VECTOR_A, 0.10)
        q = coordinate_dot(ax, (4, 5), VECTOR_B, 0.10)
        lp = coord_label(ax, (1, 1), r"P=(1,1)", VECTOR_A)
        lq = coord_label(ax, (4, 5), r"Q=(4,5)", VECTOR_B)
        segment = Line(p.get_center(), q.get_center(), color=HIGHLIGHT, stroke_width=7)
        self.play(FadeIn(p), FadeIn(q), Write(lp), Write(lq), Create(segment))
        self.cc("Distance is the length of the displacement vector from one point to the other.", 2.5)
        self.play(Write(self.eq(r"\overrightarrow{PQ}=Q-P=\begin{bmatrix}3\\4\end{bmatrix}", 0.66, 1.30)))
        self.play(Write(self.eq(r"d(P,Q)=\|Q-P\|=\sqrt{3^2+4^2}=5", 0.74, 0.35)))
        self.cc("The order changes the displacement direction, but not its length. That is why both P to Q and Q to P have the same distance.", 2.9)
        self.play(Write(self.eq(r"d(P,Q)=d(Q,P)", 0.90, -0.65)))
        self.play(Write(self.eq(r"d(P,Q)=\sqrt{\sum_i (q_i-p_i)^2}", 0.73, -1.55)))
        self.wait(2)


class Part5_05_AngleAndCauchySchwarz(GeometryLesson):
    def construct(self):
        self.title("Part V.5 — Angles and Alignment", "The dot product reveals the angle between vectors")
        ax = self.axes2d(x_range=(-1, 4), y_range=(-1, 4)); self.play(Create(ax))
        u = self.vector(ax, (1, 0), VECTOR_A, r"\vec u")
        v = self.vector(ax, (1, sqrt(3)), VECTOR_B, r"\vec v")
        self.play(GrowArrow(u[0]), Write(u[1]), GrowArrow(v[0]), Write(v[1]))
        self.cc("Choose vectors with a 60-degree opening. We can recover that angle from the dot product formula.", 2.7)
        self.play(Write(self.eq(r"\vec u\cdot\vec v=1", 0.88, 1.40)))
        self.play(Write(self.eq(r"\|\vec u\|=1,\quad\|\vec v\|=2", 0.78, 0.65)))
        self.play(Write(self.eq(r"\cos\theta=\frac{\vec u\cdot\vec v}{\|\vec u\|\|\vec v\|}=\frac12", 0.70, -0.10)))
        self.play(Write(self.eq(r"\boxed{\theta=60^\circ}", 0.96, -1.0)))
        self.cc("Because the cosine has absolute value at most one, the dot product satisfies the Cauchy–Schwarz inequality.", 2.8)
        self.play(Write(self.eq(r"|\vec u\cdot\vec v|\leq\|\vec u\|\,\|\vec v\|", 0.88, -1.70)))
        self.cc("Equality occurs when the two vectors are linearly dependent. This identifies perfect directional alignment or opposition.", 3.0)
        self.wait(2)


class Part5_06_Orthogonality(GeometryLesson):
    def construct(self):
        self.title("Part V.6 — Orthogonality", "Perpendicular vectors are exactly the vectors with zero dot product")
        ax = self.axes2d(x_range=(-1, 5), y_range=(-3, 5)); self.play(Create(ax))
        u = self.vector(ax, (2, 1), VECTOR_A, r"\vec u")
        v = self.vector(ax, (1, -2), VECTOR_B, r"\vec v")
        self.play(GrowArrow(u[0]), Write(u[1]), GrowArrow(v[0]), Write(v[1]))
        self.cc("These two vectors form a right angle. Algebraically, we can verify that without measuring the picture.", 2.7)
        self.play(Write(self.eq(r"\vec u\cdot\vec v=2(1)+1(-2)=0", 0.84, 1.35)))
        self.play(Write(self.eq(r"\boxed{\vec u\perp\vec v\iff\vec u\cdot\vec v=0}", 0.80, 0.20)))
        self.cc("Zero dot product means the vectors contribute no component in each other's direction. That idea will control projections, orthogonal complements, and Gram–Schmidt.", 3.2)
        self.play(Write(self.eq(r"\text{orthogonal}=\text{no directional overlap}", 0.72, -0.85)))
        self.wait(2)


class Part5_07_Projection(GeometryLesson):
    def construct(self):
        self.title("Part V.7 — Projection", "Find the part of one vector that lies along another")
        ax = self.axes2d(x_range=(-1, 5), y_range=(-1, 5)); self.play(Create(ax))
        a = self.vector(ax, (2, 1), VECTOR_A, r"\vec a")
        b = self.vector(ax, (3, 2), VECTOR_B, r"\vec b")
        self.play(GrowArrow(a[0]), Write(a[1]), GrowArrow(b[0]), Write(b[1]))
        self.cc("Projection asks a precise question: how much of b points in the direction of a?", 2.6)
        self.play(Write(self.eq(r"\operatorname{proj}_{\vec a}\vec b=\frac{\vec a\cdot\vec b}{\vec a\cdot\vec a}\vec a", 0.68, 1.40)))
        self.play(Write(self.eq(r"\vec a\cdot\vec b=8,\quad\vec a\cdot\vec a=5", 0.78, 0.55)))
        self.play(Write(self.eq(r"\boxed{\operatorname{proj}_{\vec a}\vec b=\frac85\begin{bmatrix}2\\1\end{bmatrix}=\begin{bmatrix}\frac{16}{5}\\\frac85\end{bmatrix}}", 0.61, -0.35)))
        projection_point = coordinate_dot(ax, (16 / 5, 8 / 5), HIGHLIGHT, 0.09)
        self.play(FadeIn(projection_point, scale=0.5))
        self.cc("The projection endpoint lies on the line spanned by a. It is the closest point on that line to b, and the leftover part will be perpendicular.", 3.1)
        self.play(Write(self.eq(r"\vec b-\operatorname{proj}_{\vec a}\vec b\perp\vec a", 0.73, -1.40)))
        self.wait(2)


class Part5_08_OrthogonalDecomposition(GeometryLesson):
    def construct(self):
        self.title("Part V.8 — Orthogonal Decomposition", "Every vector splits into parallel + perpendicular parts")
        ax = self.axes2d(x_range=(-1, 5), y_range=(-1, 5)); self.play(Create(ax))
        a = self.vector(ax, (2, 1), VECTOR_A, r"\vec a")
        b = self.vector(ax, (3, 2), HIGHLIGHT, r"\vec b")
        pvec = self.vector(ax, (16 / 5, 8 / 5), VECTOR_B, r"\vec p")
        self.play(GrowArrow(a[0]), Write(a[1]), GrowArrow(b[0]), Write(b[1]))
        self.play(GrowArrow(pvec[0]), Write(pvec[1]))
        self.cc("We have already found the part of b parallel to a. Call it p. The remainder is what is left after removing that parallel component.", 3.0)
        self.play(Write(self.eq(r"\vec p=\operatorname{proj}_{\vec a}\vec b", 0.80, 1.35)))
        self.play(Write(self.eq(r"\vec r=\vec b-\vec p=\begin{bmatrix}-\frac15\\\frac25\end{bmatrix}", 0.70, 0.50)))
        self.cc("Now verify the key geometric fact: the remainder is perpendicular to the direction we projected onto.", 2.6)
        self.play(Write(self.eq(r"\vec a\cdot\vec r=2(-\frac15)+1(\frac25)=0", 0.76, -0.25)))
        self.play(Write(self.eq(r"\boxed{\vec b=\vec p+\vec r,\qquad\vec p\parallel\vec a,\quad\vec r\perp\vec a}", 0.66, -1.25)))
        self.cc("This is the geometric heart of projection. A vector is split into the part along a subspace and the part orthogonal to it.", 3.2)
        self.wait(2)


class Part5_09_OrthogonalComplements(GeometryLesson):
    def construct(self):
        self.title("Part V.9 — Orthogonal Complements", "Collect every vector perpendicular to a subspace")
        ax = self.axes2d(x_range=(-4, 4), y_range=(-4, 4)); self.play(Create(ax))
        line = ax.plot(lambda x: x / 2, color=VECTOR_A, x_range=[-4, 4])
        ortho = ax.plot(lambda x: -2 * x, color=VECTOR_B, x_range=[-2, 2])
        self.play(Create(line), Create(ortho))
        self.cc("Take the line spanned by (2,1). Its orthogonal complement contains every vector perpendicular to that direction.", 3.0)
        self.play(Write(self.eq(r"S=\operatorname{span}\left\{\begin{bmatrix}2\\1\end{bmatrix}\right\}", 0.76, 1.45)))
        self.play(Write(self.eq(r"S^\perp=\operatorname{span}\left\{\begin{bmatrix}1\\-2\end{bmatrix}\right\}", 0.67, 0.55)))
        self.play(Write(self.eq(r"\begin{bmatrix}2\\1\end{bmatrix}\cdot\begin{bmatrix}1\\-2\end{bmatrix}=0", 0.75, -0.35)))
        self.cc("The two lines cross at the origin and are perpendicular. In higher dimensions, the same definition describes an entire orthogonal subspace rather than only one perpendicular line.", 3.2)
        self.play(Write(self.eq(r"S^\perp=\{x:x\cdot s=0\;\text{for every }s\in S\}", 0.60, -1.35)))
        self.wait(2)


class Part5_10_GramSchmidt(GeometryLesson):
    def construct(self):
        self.title("Part V.10 — Gram–Schmidt", "Turn independent vectors into an orthonormal basis")
        ax = self.axes2d(x_range=(-1, 4), y_range=(-1, 4)); self.play(Create(ax))
        u1 = self.vector(ax, (1, 1), VECTOR_A, r"\vec u_1")
        u2 = self.vector(ax, (1, 0), VECTOR_B, r"\vec u_2")
        self.play(GrowArrow(u1[0]), Write(u1[1]), GrowArrow(u2[0]), Write(u2[1]))
        self.cc("Suppose two independent vectors span a plane, but they are not perpendicular. Gram–Schmidt keeps the span while making the directions orthogonal.", 3.2)
        self.play(Write(self.eq(r"\vec v_1=\vec u_1=\begin{bmatrix}1\\1\end{bmatrix}", 0.72, 1.35)))
        self.play(Write(self.eq(r"\operatorname{proj}_{\vec v_1}\vec u_2=\frac12\begin{bmatrix}1\\1\end{bmatrix}", 0.63, 0.45)))
        self.play(Write(self.eq(r"\vec v_2=\vec u_2-\operatorname{proj}_{\vec v_1}\vec u_2=\begin{bmatrix}\frac12\\-\frac12\end{bmatrix}", 0.60, -0.50)))
        self.cc("The second vector is changed only by removing its component along the first. That guarantees the remainder is perpendicular to v1.", 3.1)
        self.play(Write(self.eq(r"\vec v_1\cdot\vec v_2=0", 0.90, -1.35)))
        self.cc("Finally normalize each vector so both have length one. The result is an orthonormal basis for the same span.", 2.9)
        self.play(Write(self.eq(r"\vec q_1=\frac1{\sqrt2}\begin{bmatrix}1\\1\end{bmatrix},\quad\vec q_2=\frac1{\sqrt2}\begin{bmatrix}1\\-1\end{bmatrix}", 0.60, -2.15)))
        self.play(Write(self.eq(r"Q=\begin{bmatrix}\vec q_1&\vec q_2\end{bmatrix},\qquad Q^TQ=I", 0.66, -2.90)))
        self.wait(2)


class Part5_11_GeometryMastery(GeometryLesson):
    def construct(self):
        self.title("Part V.11 — Geometry Mastery", "One geometric language tying the chapter together")
        self.play(Write(self.eq(r"\vec u\cdot\vec v=\|\vec u\|\|\vec v\|\cos\theta", 0.78, 1.55)))
        self.cc("The dot product measures alignment. From that one idea, length, distance, angles, perpendicularity, and projection all follow.", 3.1)
        summary = VGroup(
            Text("Dot product → alignment", font_size=22),
            Text("Norm → length", font_size=22),
            Text("Distance → norm of a displacement", font_size=22),
            Text("Angle → normalized dot product", font_size=22),
            Text("Orthogonality → zero dot product", font_size=22),
            Text("Projection → parallel component", font_size=22),
            Text("Orthogonal complement → all perpendicular directions", font_size=22),
            Text("Gram–Schmidt → orthonormalize a basis", font_size=22),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.14).to_edge(RIGHT, buff=0.10).shift(DOWN * 0.35)
        self.play(LaggedStart(*[Write(item) for item in summary], lag_ratio=0.16), run_time=2.8)
        self.cc("The important habit is to ask geometric questions: How long? How far? How aligned? What part lies along a direction? What remains perpendicular? Those questions lead directly to the formulas.", 3.7)
        self.play(Write(Text("Part V complete: vectors now have a geometric language.", font_size=26, color=YELLOW_B).to_edge(DOWN, buff=0.48)))
        self.wait(3)


__all__ = [name for name in globals() if name.startswith("Part5_") or name == "GeometryLesson"]
