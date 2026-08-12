from manim import *
from ..utils import *


class FoundationLesson(LessonScene):
    """Convenience base for Part I lessons."""

    def axes(self):
        ax = Axes(
            x_range=[-6, 6, 1],
            y_range=[-5, 5, 1],
            x_length=9.5,
            y_length=7,
            axis_config={"include_numbers": True, "stroke_width": 2},
        )
        ax.to_edge(LEFT, buff=0.4)
        return ax


class Part1_01_ScalarsAndVectors(FoundationLesson):
    def construct(self):
        self.title("Part I.1 — Scalars vs Vectors", "Why direction changes the kind of information we can represent")
        ax = self.axes()
        self.play(Create(ax))
        self.cc("Before talking about vectors, notice that not every quantity needs a direction.", 2.5)

        scalar = MathTex(r"5\ \text{meters}").scale(1.1).to_edge(RIGHT).shift(UP * 1.5)
        self.play(Write(scalar))
        self.cc("A scalar tells us only an amount. Five meters is a size, not a direction.", 3)
        self.play(FadeOut(scalar))

        self.cc("A vector tells us an amount and a direction at the same time.", 2.5)
        v = arrow_from(ax, (4, 2), VECTOR_A, r"\vec v")
        guides = component_guides(ax, 4, 2)
        self.play(GrowArrow(v[0]), Write(v[1]), Create(guides), run_time=1.8)
        coords = coord_label(ax, (4, 2), r"(4,2)", VECTOR_A)
        self.play(Write(coords))
        self.cc("The arrow means: move four units horizontally and two units vertically.", 3)
        self.cc("The tail can move anywhere. What matters is the displacement from tail to tip.", 3)

        shifted = Arrow(ax.c2p(-4, -1), ax.c2p(0, 1), buff=0, color=VECTOR_A, stroke_width=7)
        self.play(TransformFromCopy(v[0], shifted), run_time=1.4)
        self.cc("Here is the same vector starting somewhere else. Its location changed, but its displacement did not.", 3)
        self.play(FadeOut(shifted), FadeOut(v), FadeOut(guides), FadeOut(coords))

        key = MathTex(r"\boxed{\text{vector} = \text{magnitude + direction}}").scale(0.9).to_edge(RIGHT)
        self.play(Write(key))
        self.cc("This distinction becomes fundamental when we describe velocity, forces, geometry, and machine-learning data.", 3)
        self.wait(2)


class Part1_02_CoordinatesAndComponents(FoundationLesson):
    def construct(self):
        self.title("Part I.2 — Coordinates and Components", "Turning geometric motion into numbers")
        ax = self.axes()
        self.play(Create(ax))
        self.cc("Coordinates are not the vector itself. They are the numbers we use to describe the vector in a chosen basis.", 3.2)

        v = arrow_from(ax, (3, 4), VECTOR_A, r"\vec v")
        guides = component_guides(ax, 3, 4, VECTOR_B)
        self.play(GrowArrow(v[0]), Write(v[1]), Create(guides), run_time=1.6)
        self.play(Write(coord_label(ax, (3, 4), r"(3,4)", VECTOR_A)))
        self.cc("This vector has an x-component of three and a y-component of four.", 2.5)

        vx = MathTex(r"v_x=3").scale(1.0).to_edge(RIGHT).shift(UP * 1.3)
        vy = MathTex(r"v_y=4").scale(1.0).to_edge(RIGHT).shift(UP * 0.2)
        column = Matrix([[3], [4]]).scale(0.9).to_edge(RIGHT).shift(DOWN * 1.1)
        self.play(Write(vx), Write(vy))
        self.cc("We can collect those components into a column vector.", 2.2)
        self.play(Write(column))
        self.cc("The picture and the column are two representations of the same mathematical object.", 2.8)

        self.play(FadeOut(v), FadeOut(guides), FadeOut(vx), FadeOut(vy), FadeOut(column))
        u = arrow_from(ax, (-2, 3), VECTOR_B, r"\vec u")
        self.play(GrowArrow(u[0]), Write(u[1]))
        self.play(Write(MathTex(r"\vec u=\begin{bmatrix}-2\\3\end{bmatrix}").scale(0.8).to_edge(RIGHT).shift(UP * 0.8)))
        self.cc("Negative components are not errors. They simply mean movement in the negative coordinate direction.", 3)
        self.wait(2)


class Part1_03_VectorAddition(FoundationLesson):
    def construct(self):
        self.title("Part I.3 — Vector Addition", "The tip-to-tail rule and the parallelogram picture")
        ax = self.axes()
        self.play(Create(ax))
        a = arrow_from(ax, (3, 1), VECTOR_A, r"\vec a")
        b = arrow_from(ax, (1, 3), VECTOR_B, r"\vec b")
        self.play(GrowArrow(a[0]), Write(a[1]), GrowArrow(b[0]), Write(b[1]), run_time=1.6)
        self.cc("Adding vectors means combining their displacements. We can do this geometrically or component by component.", 3)

        shifted_b = Arrow(ax.c2p(3, 1), ax.c2p(4, 4), buff=0, color=VECTOR_B, stroke_width=7)
        shifted_a = Arrow(ax.c2p(1, 3), ax.c2p(4, 4), buff=0, color=VECTOR_A, stroke_width=7)
        self.play(TransformFromCopy(b[0], shifted_b), TransformFromCopy(a[0], shifted_a), run_time=1.5)
        self.cc("Slide the second vector so its tail meets the first vector's tip. The final tip is the sum.", 3)
        result = arrow_from(ax, (4, 4), HIGHLIGHT, r"\vec a+\vec b")
        self.play(GrowArrow(result[0]), Write(result[1]))
        self.play(Write(MathTex(r"\begin{bmatrix}3\\1\end{bmatrix}+\begin{bmatrix}1\\3\end{bmatrix}=\begin{bmatrix}4\\4\end{bmatrix}").scale(0.72).to_edge(RIGHT).shift(DOWN * 1.2)))
        self.cc("Notice what happened numerically: horizontal components added to horizontal components, and vertical components added to vertical components.", 3.2)

        para = Polygon(ax.c2p(0,0), ax.c2p(3,1), ax.c2p(4,4), ax.c2p(1,3), color=GREY_B, stroke_opacity=0.7)
        self.play(Create(para))
        self.cc("The same result appears as the diagonal of a parallelogram. This picture will return throughout linear algebra.", 3)
        self.wait(2)


class Part1_04_VectorSubtraction(FoundationLesson):
    def construct(self):
        self.title("Part I.4 — Vector Subtraction", "Finding the displacement from one vector to another")
        ax = self.axes()
        self.play(Create(ax))
        a = arrow_from(ax, (4, 3), VECTOR_A, r"\vec a")
        b = arrow_from(ax, (1, 1), VECTOR_B, r"\vec b")
        self.play(GrowArrow(a[0]), Write(a[1]), GrowArrow(b[0]), Write(b[1]))
        self.cc("Subtraction asks a geometric question: what vector takes us from b to a?", 3)

        displacement = Arrow(ax.c2p(1,1), ax.c2p(4,3), buff=0, color=HIGHLIGHT, stroke_width=7)
        self.play(GrowArrow(displacement))
        self.cc("Start at b and point toward a. That arrow is a minus b.", 2.6)
        self.play(Write(MathTex(r"\vec a-\vec b=\begin{bmatrix}4\\3\end{bmatrix}-\begin{bmatrix}1\\1\end{bmatrix}=\begin{bmatrix}3\\2\end{bmatrix}").scale(0.68).to_edge(RIGHT).shift(DOWN * 1.1)))
        self.cc("The same operation works algebraically because subtracting a vector is the same as adding its opposite.", 3)

        neg = arrow_from(ax, (-1,-1), VECTOR_C, r"-\vec b")
        self.play(GrowArrow(neg[0]), Write(neg[1]))
        self.play(Write(MathTex(r"\vec a-\vec b=\vec a+(-\vec b)").scale(0.8).to_edge(RIGHT).shift(UP * 1.5)))
        self.cc("Negation flips direction while keeping the magnitude unchanged. That is why subtraction fits naturally into vector addition.", 3.2)
        self.wait(2)


class Part1_05_ScalingAndUnitVectors(FoundationLesson):
    def construct(self):
        self.title("Part I.5 — Scaling and Unit Vectors", "What happens when we multiply a vector by a number?")
        ax = self.axes()
        self.play(Create(ax))
        v = arrow_from(ax, (2, 1), VECTOR_A, r"\vec v")
        self.play(GrowArrow(v[0]), Write(v[1]))
        self.cc("Multiplying a vector by a scalar changes its size. A positive scalar keeps the direction; a negative scalar reverses it.", 3.2)

        two = arrow_from(ax, (4, 2), VECTOR_B, r"2\vec v")
        self.play(GrowArrow(two[0]), Write(two[1]))
        self.play(Write(MathTex(r"2\vec v=\begin{bmatrix}4\\2\end{bmatrix}").scale(0.85).to_edge(RIGHT).shift(UP * 1.2)))
        self.cc("Multiplying by two doubles every component and therefore doubles the length.", 2.6)

        neg = arrow_from(ax, (-2, -1), HIGHLIGHT, r"-\vec v")
        self.play(GrowArrow(neg[0]), Write(neg[1]))
        self.cc("Multiplying by minus one keeps the length but turns the arrow around.", 2.5)

        self.play(FadeOut(two), FadeOut(neg))
        unit = MathTex(r"\hat v=\frac{\vec v}{\|\vec v\|}").scale(1.0).to_edge(RIGHT).shift(UP * 0.9)
        mag = MathTex(r"\|\vec v\|=\sqrt{2^2+1^2}=\sqrt5").scale(0.78).to_edge(RIGHT)
        self.play(Write(mag), Write(unit))
        self.cc("A unit vector is a vector whose length is exactly one. We create one by dividing by the original magnitude.", 3.2)
        self.play(Write(MathTex(r"\|\hat v\|=1").scale(0.95).to_edge(RIGHT).shift(DOWN * 1.1)))
        self.cc("Unit vectors are useful whenever we want direction without carrying an arbitrary scale along with it.", 3)
        self.wait(2)


class Part1_06_MagnitudeAndDistance(FoundationLesson):
    def construct(self):
        self.title("Part I.6 — Magnitude and Distance", "Recovering length from components")
        ax = self.axes()
        self.play(Create(ax))
        v = arrow_from(ax, (3,4), VECTOR_A, r"\vec v")
        guides = component_guides(ax,3,4)
        self.play(GrowArrow(v[0]), Write(v[1]), Create(guides))
        self.cc("The components form a right triangle. The vector is the hypotenuse.", 2.7)

        formula1 = MathTex(r"\|\vec v\|^2=3^2+4^2").scale(1.0).to_edge(RIGHT).shift(UP * 1.3)
        formula2 = MathTex(r"\|\vec v\|=\sqrt{3^2+4^2}=5").scale(0.88).to_edge(RIGHT)
        self.play(Write(formula1)); self.cc("So the Pythagorean theorem becomes the length formula for a vector.", 2.5)
        self.play(Write(formula2)); self.cc("A vector with components three and four has magnitude five.", 2.4)

        p = coordinate_dot(ax, (-2,-1), VECTOR_B)
        q = coordinate_dot(ax, (2,2), HIGHLIGHT)
        segment = Line(ax.c2p(-2,-1), ax.c2p(2,2), color=GREEN_C, stroke_width=6)
        self.play(FadeOut(v), FadeOut(guides), FadeOut(formula1), FadeOut(formula2), FadeIn(p), FadeIn(q), Create(segment))
        self.play(Write(MathTex(r"\Delta=\begin{bmatrix}2-(-2)\\2-(-1)\end{bmatrix}=\begin{bmatrix}4\\3\end{bmatrix}").scale(0.72).to_edge(RIGHT).shift(UP * 1.1)))
        self.cc("Distance between two points is simply the magnitude of their difference vector.", 3)
        self.play(Write(MathTex(r"d(P,Q)=\|Q-P\|=\sqrt{4^2+3^2}=5").scale(0.8).to_edge(RIGHT)))
        self.cc("This is the bridge between vector algebra and ordinary Euclidean geometry.", 2.8)
        self.wait(2)


class Part1_07_LinearCombinations(FoundationLesson):
    def construct(self):
        self.title("Part I.7 — Linear Combinations", "The operation that quietly powers almost everything later")
        ax = self.axes()
        self.play(Create(ax))
        u = arrow_from(ax, (2,1), VECTOR_A, r"\vec u")
        v = arrow_from(ax, (-1,2), VECTOR_B, r"\vec v")
        self.play(GrowArrow(u[0]), Write(u[1]), GrowArrow(v[0]), Write(v[1]))
        self.cc("A linear combination means scaling vectors and then adding the results.", 2.6)

        eq = MathTex(r"\vec w=2\vec u+3\vec v").scale(1.0).to_edge(RIGHT).shift(UP * 1.2)
        self.play(Write(eq))
        two_u = arrow_from(ax, (4,2), VECTOR_A, r"2\vec u")
        three_v = Arrow(ax.c2p(4,2), ax.c2p(1,8), buff=0, color=VECTOR_B, stroke_width=7)
        self.play(GrowArrow(two_u[0]), Write(two_u[1]), GrowArrow(three_v), run_time=1.5)
        self.cc("First scale u by two. Then place three copies of v tip-to-tail.", 3)

        result = arrow_from(ax, (1,8), HIGHLIGHT, r"\vec w")
        self.play(GrowArrow(result[0]), Write(result[1]))
        self.play(Write(MathTex(r"2\begin{bmatrix}2\\1\end{bmatrix}+3\begin{bmatrix}-1\\2\end{bmatrix}=\begin{bmatrix}1\\8\end{bmatrix}").scale(0.68).to_edge(RIGHT).shift(DOWN * 0.5)))
        self.cc("The same construction is algebraically simple: multiply components, then add them componentwise.", 3)
        self.cc("Later, span will ask: which endpoints are reachable by all possible linear combinations?", 3)
        self.cc("Basis will ask for a small independent collection that can generate the whole space.", 3)
        self.play(FadeOut(two_u), FadeOut(three_v), FadeOut(result), FadeOut(eq))
        self.play(Write(MathTex(r"\boxed{\vec w=a\vec u+b\vec v}").scale(1.05).to_edge(RIGHT)))
        self.cc("Remember this pattern. It is the language that connects vectors, bases, matrices, eigenvectors, and machine learning.", 3.5)
        self.wait(2)


class Part1_08_FoundationsRecap(FoundationLesson):
    def construct(self):
        self.title("Part I.8 — Foundations Recap", "From pictures to algebra")
        ax = self.axes()
        self.play(Create(ax))
        v = arrow_from(ax, (3,2), VECTOR_A, r"\vec v")
        self.play(GrowArrow(v[0]), Write(v[1]))
        self.cc("Let's compress the entire first part into one mental model.", 2.5)

        items = VGroup(
            MathTex(r"\vec v=\begin{bmatrix}v_x\\v_y\end{bmatrix}"),
            MathTex(r"\|\vec v\|=\sqrt{v_x^2+v_y^2}"),
            MathTex(r"\vec a+\vec b=\begin{bmatrix}a_x+b_x\\a_y+b_y\end{bmatrix}"),
            MathTex(r"c\vec v=\begin{bmatrix}cv_x\\cv_y\end{bmatrix}"),
            MathTex(r"\vec w=a\vec u+b\vec v"),
        ).scale(0.72).arrange(DOWN, aligned_edge=LEFT, buff=0.34).to_edge(RIGHT, buff=0.35)
        self.play(LaggedStart(*[Write(x) for x in items], lag_ratio=0.45), run_time=3)
        self.cc("A vector is geometry expressed numerically: components encode movement, magnitude measures length, and linear combinations build new vectors.", 3.5)

        for text in [
            "Vectors are not tied to one location.",
            "Negative components simply indicate direction.",
            "Subtraction is a displacement.",
            "Scaling changes size and possibly direction.",
            "Linear combinations are the foundation for span and basis.",
        ]:
            self.play(FadeOut(*items))
            statement = Text(text, font_size=31).to_edge(RIGHT, buff=0.35)
            self.play(Write(statement))
            self.cc(text, 2.2, size=25)
            self.play(FadeOut(statement))

        final = Text("Next: Span, basis, dimension, and the geometry of vector spaces.", font_size=29, color=YELLOW_B).to_edge(DOWN, buff=0.75)
        self.play(Write(final))
        self.wait(3)
