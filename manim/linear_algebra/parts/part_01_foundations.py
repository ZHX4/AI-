from manim import *

try:
    from ..utils import *
except ImportError:
    from utils import *


class FoundationLesson(LessonScene):
    """Shared setup for Part I: visual, captioned vector foundations."""

    def axes(self):
        ax = Axes(
            x_range=[-5, 5, 1],
            y_range=[-4, 4, 1],
            x_length=8.8,
            y_length=6.4,
            axis_config={"include_numbers": True, "stroke_width": 2},
        )
        ax.to_edge(LEFT, buff=0.35)
        return ax

    def side_formula(self, latex, scale=0.75, shift=ORIGIN):
        return MathTex(latex).scale(scale).to_edge(RIGHT, buff=0.35).shift(shift)


class Part1_01_ScalarsAndVectors(FoundationLesson):
    """Scalars, vectors, displacement, and the translation-invariance of vectors."""

    def construct(self):
        self.title(
            "Part I.1 — Scalars vs Vectors",
            "Why direction changes the kind of information we can represent",
        )
        ax = self.axes()
        self.play(Create(ax))

        self.cc("Start with a simple question: what information does a number actually carry?", 2.8)
        scalar = MathTex(r"5\,\mathrm{m}").scale(1.25).to_edge(RIGHT).shift(UP * 1.4)
        self.play(Write(scalar))
        self.cc("Five meters tells us an amount. It does not tell us which way to move.", 3.0)
        self.play(FadeOut(scalar))

        v = arrow_from(ax, (3, 2), VECTOR_A, r"\vec v")
        guides = component_guides(ax, 3, 2, GREY_B)
        point = coordinate_dot(ax, (3, 2), HIGHLIGHT)
        self.play(GrowArrow(v[0]), Write(v[1]), Create(guides), FadeIn(point), run_time=1.5)
        self.play(Write(coord_label(ax, (3, 2), r"(3,2)", HIGHLIGHT)))
        self.cc("A vector carries both size and direction. From the origin, this one means three units right and two units up.", 3.2)

        shifted = Arrow(
            ax.c2p(-4, -2),
            ax.c2p(-1, 0),
            buff=0,
            color=VECTOR_A,
            stroke_width=7,
            max_tip_length_to_length_ratio=0.12,
        )
        self.play(TransformFromCopy(v[0], shifted), run_time=1.3)
        self.cc("Now move the same arrow somewhere else. Its location changed, but its displacement did not.", 3.2)
        self.play(FadeOut(shifted))

        key = MathTex(r"\boxed{\text{vector} = \text{magnitude + direction}}").scale(0.88)
        key.to_edge(RIGHT, buff=0.35).shift(UP * 0.6)
        self.play(Write(key))
        self.cc("That is why vectors are the natural language for velocity, force, displacement, and geometric motion.", 3.0)
        self.wait(1.5)

        self.play(FadeOut(v), FadeOut(guides), FadeOut(point), FadeOut(key))
        self.cc("Keep one idea in mind: a vector describes a change, not a location.", 2.8)
        self.wait(1.5)


class Part1_02_CoordinatesAndComponents(FoundationLesson):
    """Coordinates, components, negative directions, and column-vector notation."""

    def construct(self):
        self.title(
            "Part I.2 — Coordinates and Components",
            "Turning geometric motion into numbers",
        )
        ax = self.axes()
        self.play(Create(ax))

        self.cc("A geometric vector is continuous; coordinates give us a precise numerical description of it.", 3.0)
        v = arrow_from(ax, (3, 4), VECTOR_A, r"\vec v")
        guides = component_guides(ax, 3, 4, VECTOR_B)
        self.play(GrowArrow(v[0]), Write(v[1]), Create(guides), run_time=1.5)
        self.play(Write(coord_label(ax, (3, 4), r"(3,4)", HIGHLIGHT)))
        self.cc("The horizontal component is 3 and the vertical component is 4. Together they completely determine this vector in this coordinate system.", 3.4)

        vx = self.side_formula(r"v_x=3", 0.95, UP * 1.5)
        vy = self.side_formula(r"v_y=4", 0.95, UP * 0.5)
        column = Matrix([[3], [4]]).scale(0.9).to_edge(RIGHT, buff=0.5).shift(DOWN * 1.0)
        self.play(Write(vx), Write(vy))
        self.cc("We can package the components into a column vector. This is the notation you will see everywhere in linear algebra and machine learning.", 3.2)
        self.play(Write(column))
        self.cc("The picture and the column are two ways of representing the same vector.", 2.8)

        self.play(FadeOut(v), FadeOut(guides), FadeOut(vx), FadeOut(vy), FadeOut(column))
        u = arrow_from(ax, (-2, 3), VECTOR_B, r"\vec u")
        ug = component_guides(ax, -2, 3, GREY_B)
        self.play(GrowArrow(u[0]), Write(u[1]), Create(ug))
        neg = self.side_formula(r"\vec u=\begin{bmatrix}-2\\3\end{bmatrix}", 0.78, UP * 0.9)
        self.play(Write(neg))
        self.cc("A negative component simply means motion in the negative direction of that axis. It is not a special kind of vector.", 3.1)
        self.cc("Changing coordinates is not changing the underlying geometric idea; it is changing how we describe it.", 2.8)
        self.wait(1.5)


class Part1_03_VectorAddition(FoundationLesson):
    """Tip-to-tail addition, parallelogram geometry, and componentwise addition."""

    def construct(self):
        self.title(
            "Part I.3 — Vector Addition",
            "The tip-to-tail rule and the parallelogram picture",
        )
        ax = self.axes()
        self.play(Create(ax))

        a = arrow_from(ax, (3, 1), VECTOR_A, r"\vec a")
        b = arrow_from(ax, (1, 3), VECTOR_B, r"\vec b")
        self.play(GrowArrow(a[0]), Write(a[1]), GrowArrow(b[0]), Write(b[1]), run_time=1.4)
        self.cc("Addition means combining displacements. Geometrically, place one vector after the other.", 3.0)

        moved_b = Arrow(ax.c2p(3, 1), ax.c2p(4, 4), buff=0, color=VECTOR_B, stroke_width=7)
        self.play(TransformFromCopy(b[0], moved_b), run_time=1.3)
        self.cc("Slide b without changing its direction or length. Its tail now sits at the tip of a.", 2.8)

        result = arrow_from(ax, (4, 4), HIGHLIGHT, r"\vec a+\vec b")
        self.play(GrowArrow(result[0]), Write(result[1]))
        self.cc("The arrow from the original tail to the final tip is the sum.", 2.5)

        formula = self.side_formula(
            r"\begin{bmatrix}3\\1\end{bmatrix}+\begin{bmatrix}1\\3\end{bmatrix}=\begin{bmatrix}4\\4\end{bmatrix}",
            0.68,
            DOWN * 0.8,
        )
        self.play(Write(formula))
        self.cc("Numerically, horizontal components add to horizontal components, and vertical components add to vertical components.", 3.2)

        para = Polygon(
            ax.c2p(0, 0), ax.c2p(3, 1), ax.c2p(4, 4), ax.c2p(1, 3),
            color=GREY_B, stroke_opacity=0.8,
        )
        self.play(Create(para))
        diagonal = Arrow(ax.c2p(0, 0), ax.c2p(4, 4), buff=0, color=HIGHLIGHT, stroke_width=7)
        self.play(ReplacementTransform(result[0], diagonal), run_time=1.1)
        self.cc("The same result is the diagonal of a parallelogram. This geometric picture will keep reappearing in later parts.", 3.0)
        self.wait(1.5)


class Part1_04_VectorSubtraction(FoundationLesson):
    """Subtraction as displacement and as addition of an inverse vector."""

    def construct(self):
        self.title(
            "Part I.4 — Vector Subtraction",
            "Finding the displacement from one point to another",
        )
        ax = self.axes()
        self.play(Create(ax))

        a = arrow_from(ax, (4, 3), VECTOR_A, r"\vec a")
        b = arrow_from(ax, (1, 1), VECTOR_B, r"\vec b")
        self.play(GrowArrow(a[0]), Write(a[1]), GrowArrow(b[0]), Write(b[1]), run_time=1.4)
        self.cc("Subtraction answers a very geometric question: what displacement takes us from b to a?", 3.0)

        displacement = Arrow(ax.c2p(1, 1), ax.c2p(4, 3), buff=0, color=HIGHLIGHT, stroke_width=7)
        self.play(GrowArrow(displacement))
        self.cc("Start at the endpoint of b and point toward the endpoint of a. That displacement is a minus b.", 3.0)

        result = self.side_formula(
            r"\vec a-\vec b=\begin{bmatrix}4\\3\end{bmatrix}-\begin{bmatrix}1\\1\end{bmatrix}=\begin{bmatrix}3\\2\end{bmatrix}",
            0.62,
            DOWN * 0.7,
        )
        self.play(Write(result))
        self.cc("The component calculation agrees with the geometric arrow: four minus one is three, and three minus one is two.", 3.0)

        neg = arrow_from(ax, (-1, -1), VECTOR_C, r"-\vec b")
        self.play(GrowArrow(neg[0]), Write(neg[1]))
        identity = self.side_formula(r"\vec a-\vec b=\vec a+(-\vec b)", 0.82, UP * 1.1)
        self.play(Write(identity))
        self.cc("Subtraction is not a separate mystery. It is addition after reversing the second vector.", 3.0)
        self.wait(1.5)

        self.play(FadeOut(neg), FadeOut(identity), FadeOut(result))
        self.cc("Whenever you see a difference of vectors, ask: what displacement connects the two geometric endpoints?", 3.0)
        self.wait(1.5)


class Part1_05_ScalingAndUnitVectors(FoundationLesson):
    """Scalar multiplication, reversal, zero vector, and normalization."""

    def construct(self):
        self.title(
            "Part I.5 — Scaling and Unit Vectors",
            "How a number changes the size and direction of a vector",
        )
        ax = self.axes()
        self.play(Create(ax))

        v = arrow_from(ax, (2, 1), VECTOR_A, r"\vec v")
        self.play(GrowArrow(v[0]), Write(v[1]))
        self.cc("Scalar multiplication means multiplying every component by the same number.", 2.8)

        two = arrow_from(ax, (4, 2), VECTOR_B, r"2\vec v")
        half = arrow_from(ax, (1, 0.5), VECTOR_C, r"\frac12\vec v")
        self.play(GrowArrow(two[0]), Write(two[1]), GrowArrow(half[0]), Write(half[1]), run_time=1.4)
        self.cc("A factor of two doubles the vector; a factor of one-half shrinks it to half its length.", 3.0)

        neg = arrow_from(ax, (-2, -1), HIGHLIGHT, r"-\vec v")
        self.play(GrowArrow(neg[0]), Write(neg[1]))
        self.cc("A negative scalar also reverses the direction. Multiplication by minus one preserves the length but flips the arrow.", 3.0)

        self.play(FadeOut(two), FadeOut(half), FadeOut(neg))
        mag = self.side_formula(r"\|\vec v\|=\sqrt{2^2+1^2}=\sqrt5", 0.78, UP * 1.2)
        unit = self.side_formula(r"\hat v=\frac{\vec v}{\|\vec v\|}", 0.95, ORIGIN)
        unit_length = self.side_formula(r"\|\hat v\|=1", 0.9, DOWN * 1.1)
        self.play(Write(mag))
        self.cc("To keep only the direction, divide by the vector's magnitude. The result is called a unit vector.", 3.2)
        self.play(Write(unit), Write(unit_length))
        self.cc("Normalization changes the scale but deliberately preserves direction. This idea will become important for angles, projections, optimization, and embeddings.", 3.3)
        self.wait(1.5)


class Part1_06_MagnitudeAndDistance(FoundationLesson):
    """Magnitude from the Pythagorean theorem and distance via a difference vector."""

    def construct(self):
        self.title(
            "Part I.6 — Magnitude and Distance",
            "Recovering geometric length from components",
        )
        ax = self.axes()
        self.play(Create(ax))

        v = arrow_from(ax, (3, 4), VECTOR_A, r"\vec v")
        guides = component_guides(ax, 3, 4, VECTOR_B)
        self.play(GrowArrow(v[0]), Write(v[1]), Create(guides), run_time=1.4)
        self.cc("The components create a right triangle. The vector itself is the hypotenuse.", 2.8)

        pyth = self.side_formula(r"\|\vec v\|^2=3^2+4^2", 0.95, UP * 1.2)
        length = self.side_formula(r"\|\vec v\|=\sqrt{3^2+4^2}=5", 0.82, ORIGIN)
        self.play(Write(pyth))
        self.cc("So the Pythagorean theorem becomes the length formula for a vector.", 2.8)
        self.play(Write(length))
        self.cc("This famous three-four-five triangle gives us a clean numerical example: the vector has magnitude five.", 2.8)

        self.play(FadeOut(v), FadeOut(guides), FadeOut(pyth), FadeOut(length))
        p = coordinate_dot(ax, (-2, -1), VECTOR_B)
        q = coordinate_dot(ax, (2, 2), HIGHLIGHT)
        self.play(FadeIn(p), FadeIn(q))
        segment = Line(ax.c2p(-2, -1), ax.c2p(2, 2), color=VECTOR_C, stroke_width=6)
        self.play(Create(segment))
        self.play(Write(coord_label(ax, (-2, -1), r"P", VECTOR_B)))
        self.play(Write(coord_label(ax, (2, 2), r"Q", HIGHLIGHT)))
        self.cc("Now forget the origin. We want the distance between two arbitrary points P and Q.", 2.7)

        delta = self.side_formula(
            r"\overrightarrow{PQ}=Q-P=\begin{bmatrix}4\\3\end{bmatrix}",
            0.72,
            UP * 1.0,
        )
        dist = self.side_formula(
            r"d(P,Q)=\|Q-P\|=\sqrt{4^2+3^2}=5",
            0.72,
            DOWN * 0.6,
        )
        self.play(Write(delta))
        self.cc("The difference Q minus P creates a vector describing the displacement from P to Q.", 3.0)
        self.play(Write(dist))
        self.cc("Then distance is just the magnitude of that difference vector. Vector subtraction has turned into ordinary geometry.", 3.2)
        self.wait(1.5)


class Part1_07_LinearCombinations(FoundationLesson):
    """Linear combinations with bounded coordinates so every construction stays visible."""

    def construct(self):
        self.title(
            "Part I.7 — Linear Combinations",
            "The operation that quietly powers span, bases, matrices, and ML",
        )
        ax = self.axes()
        self.play(Create(ax))

        u = arrow_from(ax, (2, 1), VECTOR_A, r"\vec u")
        v = arrow_from(ax, (-1, 2), VECTOR_B, r"\vec v")
        self.play(GrowArrow(u[0]), Write(u[1]), GrowArrow(v[0]), Write(v[1]), run_time=1.4)
        self.cc("A linear combination is a recipe: choose numbers, scale the vectors, then add the results.", 2.9)

        equation = self.side_formula(r"\vec w=2\vec u+\vec v", 0.95, UP * 1.5)
        self.play(Write(equation))
        scaled_u = arrow_from(ax, (4, 2), VECTOR_A, r"2\vec u")
        self.play(GrowArrow(scaled_u[0]), Write(scaled_u[1]))
        self.cc("First, scale u by two. Its endpoint moves from (2,1) to (4,2).", 2.7)

        moved_v = Arrow(ax.c2p(4, 2), ax.c2p(3, 4), buff=0, color=VECTOR_B, stroke_width=7)
        self.play(TransformFromCopy(v[0], moved_v), run_time=1.2)
        self.cc("Now place one copy of v tip-to-tail with the scaled u.", 2.7)

        result = arrow_from(ax, (3, 4), HIGHLIGHT, r"\vec w")
        self.play(GrowArrow(result[0]), Write(result[1]))
        numeric = self.side_formula(
            r"2\begin{bmatrix}2\\1\end{bmatrix}+\begin{bmatrix}-1\\2\end{bmatrix}=\begin{bmatrix}3\\4\end{bmatrix}",
            0.68,
            DOWN * 0.9,
        )
        self.play(Write(numeric))
        self.cc("The algebra matches the geometry exactly: two times (2,1), plus (-1,2), gives (3,4).", 3.1)

        self.play(FadeOut(scaled_u), FadeOut(moved_v), FadeOut(result), FadeOut(equation), FadeOut(numeric))
        self.cc("Now imagine allowing many different coefficients. The set of every endpoint we can reach is going to become a central object: the span.", 3.5)
        self.wait(1.5)


class Part1_08_VectorAlgebraAndMastery(FoundationLesson):
    """Core vector laws plus a compact worked problem and transition to Part II."""

    def construct(self):
        self.title(
            "Part I.8 — Vector Algebra and Mastery",
            "The rules that make vector arithmetic behave like a coherent algebra",
        )
        ax = self.axes()
        self.play(Create(ax))
        self.cc("We have enough geometric intuition to collect the algebraic rules that make all of these operations consistent.", 3.0)

        laws = VGroup(
            MathTex(r"\vec a+\vec b=\vec b+\vec a"),
            MathTex(r"(\vec a+\vec b)+\vec c=\vec a+(\vec b+\vec c)"),
            MathTex(r"\vec a+\vec 0=\vec a"),
            MathTex(r"\vec a+(-\vec a)=\vec 0"),
            MathTex(r"k(\vec a+\vec b)=k\vec a+k\vec b"),
            MathTex(r"(k+m)\vec a=k\vec a+m\vec a"),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.28).scale(0.62).to_edge(RIGHT, buff=0.28)
        self.play(LaggedStart(*[Write(x) for x in laws], lag_ratio=0.15, run_time=2.2))
        self.cc("These are not decorative rules. They let us rearrange and simplify vector expressions without changing the geometric result.", 3.3)

        self.play(FadeOut(laws))
        a = arrow_from(ax, (2, 1), VECTOR_A, r"\vec a")
        b = arrow_from(ax, (1, -2), VECTOR_B, r"\vec b")
        self.play(GrowArrow(a[0]), Write(a[1]), GrowArrow(b[0]), Write(b[1]))
        self.cc("Let's finish with a complete example. We will compute a combination before drawing the answer.", 2.8)

        work1 = self.side_formula(r"2\vec a-\vec b", 0.95, UP * 1.35)
        work2 = self.side_formula(
            r"=2\begin{bmatrix}2\\1\end{bmatrix}-\begin{bmatrix}1\\-2\end{bmatrix}",
            0.7,
            UP * 0.35,
        )
        work3 = self.side_formula(r"=\begin{bmatrix}3\\4\end{bmatrix}", 0.9, DOWN * 0.7)
        self.play(Write(work1)); self.cc("First identify the vector combination we are asking for.", 2.0)
        self.play(Write(work2)); self.cc("Then apply the scalar multiplication and subtraction component by component.", 2.6)
        self.play(Write(work3)); self.cc("The resulting vector is (3,4). Now the picture should agree with the arithmetic.", 2.5)

        answer = arrow_from(ax, (3, 4), HIGHLIGHT, r"2\vec a-\vec b")
        self.play(GrowArrow(answer[0]), Write(answer[1]))
        self.cc("The endpoint matches the computed components. Algebra and geometry are saying the same thing in two languages.", 3.1)

        self.play(FadeOut(work1), FadeOut(work2), FadeOut(work3))
        recap = VGroup(
            Text("Part I mastered", font_size=34, weight=BOLD),
            MathTex(r"\text{vector}\rightarrow\text{components}\rightarrow\text{operations}\rightarrow\text{linear combinations}"),
            Text("Next: which vectors can generate which spaces?", font_size=27, color=GREY_B),
        ).arrange(DOWN, buff=0.38).scale(0.75)
        recap.to_edge(RIGHT, buff=0.25)
        self.play(Write(recap))
        self.cc("You are ready for the next question: when we vary the coefficients in a linear combination, what entire region of space can we reach?", 3.6)
        self.wait(2.0)
