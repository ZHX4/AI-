from manim import *
from ..utils import *


class SystemsLesson(LessonScene):
    """Shared helpers for the canonical Part IV systems-of-equations lessons."""

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

    def line(self, ax, slope, intercept, color):
        xmin, xmax = ax.x_range[0], ax.x_range[1]
        return ax.plot(lambda x: slope * x + intercept, color=color, x_range=[xmin, xmax])

    def dot(self, ax, xy, color=HIGHLIGHT, radius=0.09):
        return Dot(ax.c2p(*xy), radius=radius, color=color)


class Part4_01_AxEqualsB(SystemsLesson):
    def construct(self):
        self.title("Part IV.1 — The Equation Ax = b", "A system is one vector equation containing several scalar equations")
        ax = self.axes2d(); self.play(Create(ax))
        L1 = self.line(ax, -1, 5, VECTOR_A)
        L2 = self.line(ax, 2, -3, VECTOR_B)
        self.play(Create(L1), Create(L2))
        p = self.dot(ax, (2, 3), HIGHLIGHT)
        self.play(FadeIn(p, scale=0.5))
        self.cc("A system asks for the point that satisfies every equation at the same time. On this graph, that means the intersection of the two lines.", 3.5)
        self.play(Write(self.eq(r"x+y=5", 0.88, 1.45)))
        self.play(Write(self.eq(r"2x-y=1", 0.88, 0.70)))
        self.cc("The first line has slope negative one and intercept five. The second has slope two and intercept negative three. Their intersection is the common solution.", 3.1)
        self.play(Write(self.eq(r"\begin{cases}x+y=5\\2x-y=1\end{cases}", 0.72, -0.15)))
        self.play(Write(self.eq(r"\begin{bmatrix}1&1\\2&-1\end{bmatrix}\begin{bmatrix}x\\y\end{bmatrix}=\begin{bmatrix}5\\1\end{bmatrix}", 0.60, -1.15)))
        self.cc("Those scalar equations compress into one matrix equation: A x equals b. That notation will let us solve many equations systematically.", 3.4)
        self.play(Write(self.eq(r"\vec x=\begin{bmatrix}2\\3\end{bmatrix}", 0.82, -2.05)))
        self.wait(2)


class Part4_02_GeometricMeaning(SystemsLesson):
    def construct(self):
        self.title("Part IV.2 — Geometric Meaning of a System", "Each equation describes a geometric constraint")
        ax = self.axes2d()
        self.play(Create(ax))
        L1 = self.line(ax, -1, 5, VECTOR_A)
        L2 = self.line(ax, 2, -3, VECTOR_B)
        self.play(Create(L1))
        self.cc("Start with only the first equation. It does not pick one point; it describes an entire line of possible solutions.", 3.0)
        self.play(Create(L2))
        self.cc("Adding the second equation narrows the candidates to points that lie on both lines. In two dimensions, that is an intersection problem.", 3.1)
        self.play(Write(self.eq(r"\text{one equation}\Rightarrow\text{a line of candidates}", 0.65, 1.35)))
        self.play(Write(self.eq(r"\text{two equations}\Rightarrow\text{common intersection(s)}", 0.61, 0.45)))
        self.cc("The solution is not created by algebraic manipulation. The algebra is a method for finding the geometry that was already there.", 3.1)
        self.play(Write(self.eq(r"\operatorname{Sol}(Ax=b)=\{\text{vectors }x\text{ satisfying every equation}\}", 0.56, -0.75)))
        self.play(FadeIn(self.dot(ax, (2, 3), HIGHLIGHT), scale=0.5))
        self.play(Write(self.eq(r"(x,y)=(2,3)", 0.82, -1.65)))
        self.wait(2)


class Part4_03_AugmentedMatrix(SystemsLesson):
    def construct(self):
        self.title("Part IV.3 — The Augmented Matrix", "Keep the coefficients and the constants in one object")
        self.play(Write(self.eq(r"\begin{cases}x+y=5\\2x-y=1\end{cases}", 0.86, 1.40)))
        self.cc("The left side contains the coefficients of the unknowns. The right side contains the constants. We can store both parts together.", 3.0)
        self.play(Write(self.eq(r"\left[\begin{array}{cc|c}1&1&5\\2&-1&1\end{array}\right]", 1.0, 0.25)))
        self.cc("The vertical bar separates the coefficient matrix from the right-hand side vector b. It keeps the structure visible during elimination.", 2.8)
        self.play(Write(self.eq(r"\left[\begin{array}{cc|c}a_{11}&a_{12}&b_1\\a_{21}&a_{22}&b_2\end{array}\right]", 0.70, -0.80)))
        self.play(Write(self.eq(r"\text{same augmented matrix}\iff\text{same encoded system}", 0.62, -1.75)))
        self.cc("Once the system is in this form, we can manipulate rows instead of rewriting the equations over and over.", 3.0)
        self.wait(2)


class Part4_04_ElementaryRowOperations(SystemsLesson):
    def construct(self):
        self.title("Part IV.4 — Elementary Row Operations", "Change the form without changing the solution set")
        self.play(Write(self.eq(r"R_1\leftrightarrow R_2", 0.86, 1.35)))
        self.play(Write(self.eq(r"R_1\leftarrow cR_1,\quad c\neq0", 0.82, 0.55)))
        self.play(Write(self.eq(r"R_2\leftarrow R_2+cR_1", 0.82, -0.25)))
        self.cc("There are exactly three elementary row operations: swap two rows, multiply a row by a nonzero constant, or add a multiple of one row to another.", 3.4)
        self.play(Write(self.eq(r"\text{Each operation produces an equivalent system.}", 0.78, -1.20)))
        self.cc("A row is an equation. Swapping equations changes only their order. Scaling by a nonzero number preserves its solution set. Replacing one equation by itself plus a multiple of another preserves the common solutions too.", 4.2)
        self.play(Write(self.eq(r"\operatorname{Sol}(S)=\operatorname{Sol}(S')", 0.92, -2.05)))
        self.wait(2)


class Part4_05_GaussianElimination(SystemsLesson):
    def construct(self):
        self.title("Part IV.5 — Gaussian Elimination", "Systematically create zeros below pivots")
        self.play(Write(self.eq(r"\left[\begin{array}{cc|c}1&1&5\\2&-1&1\end{array}\right]", 0.95, 1.40)))
        self.cc("Choose a pivot in the first column. Then eliminate the entry underneath it so the first unknown can be isolated later.", 3.0)
        self.play(Write(self.eq(r"R_2\leftarrow R_2-2R_1", 0.78, 0.50)))
        self.play(Write(self.eq(r"\left[\begin{array}{cc|c}1&1&5\\0&-3&-9\end{array}\right]", 0.95, -0.20)))
        self.cc("Now the second row contains only one unknown. The triangular structure is the key: solve the bottom equation first, then substitute upward.", 3.3)
        self.play(Write(self.eq(r"-3y=-9\Rightarrow y=3", 0.82, -0.95)))
        self.play(Write(self.eq(r"x+y=5\Rightarrow x=2", 0.82, -1.65)))
        self.play(Write(self.eq(r"\boxed{(x,y)=(2,3)}", 0.90, -2.35)))
        self.cc("Gaussian elimination did not guess the answer. It transformed the system into an equivalent form where the answer became easy to read.", 3.2)
        self.wait(2)


class Part4_06_BackSubstitution(SystemsLesson):
    def construct(self):
        self.title("Part IV.6 — Back Substitution", "Read the triangular system from the bottom upward")
        self.play(Write(self.eq(r"\left[\begin{array}{ccc|c}1&2&-1&4\\0&3&2&7\\0&0&5&10\end{array}\right]", 0.82, 1.15)))
        self.cc("After elimination, the last row is often the easiest equation. Start there. Then carry each known value upward into the row above.", 3.3)
        self.play(Write(self.eq(r"5z=10\Rightarrow z=2", 0.84, 0.25)))
        self.play(Write(self.eq(r"3y+2z=7\Rightarrow y=1", 0.84, -0.45)))
        self.play(Write(self.eq(r"x+2y-z=4\Rightarrow x=4", 0.78, -1.15)))
        self.play(Write(self.eq(r"\boxed{(x,y,z)=(4,1,2)}", 0.90, -1.95)))
        self.cc("Back substitution works because each row has fewer unresolved variables than the row above. The triangular form created that dependency structure for us.", 3.3)
        self.wait(2)


class Part4_07_RREF(SystemsLesson):
    def construct(self):
        self.title("Part IV.7 — Reduced Row Echelon Form", "Continue elimination until every pivot is isolated")
        self.play(Write(self.eq(r"\left[\begin{array}{cc|c}1&1&5\\2&-1&1\end{array}\right]", 0.90, 1.30)))
        self.cc("Gaussian elimination stops at an upper-triangular form. Reduced row echelon form goes further: every pivot is one, and every other entry in a pivot column is zero.", 3.4)
        self.play(Write(self.eq(r"\sim\left[\begin{array}{cc|c}1&0&2\\0&1&3\end{array}\right]", 0.95, 0.15)))
        self.cc("Now the pivot columns are unit columns. The solution can be read directly without back substitution.", 2.8)
        self.play(Write(self.eq(r"x=2,\qquad y=3", 0.92, -0.70)))
        self.play(Write(self.eq(r"\text{RREF gives a canonical reduced description}", 0.62, -1.55)))
        self.cc("RREF is unique for a given matrix. Different valid row-reduction paths can look different along the way, but they must end at the same reduced row echelon form.", 3.4)
        self.wait(2)


class Part4_08_ThreeSolutionCases(SystemsLesson):
    def construct(self):
        self.title("Part IV.8 — The Three Possible Solution Cases", "Unique, none, or infinitely many")
        ax = self.axes2d(x_range=(-1, 6), y_range=(-1, 7)); self.play(Create(ax))

        unique1 = self.line(ax, -1, 5, VECTOR_A)
        unique2 = self.line(ax, 2, -3, VECTOR_B)
        self.play(Create(unique1), Create(unique2))
        self.cc("First case: the lines cross exactly once, so there is one solution.", 2.5)
        self.play(Write(self.eq(r"\boxed{\text{one solution}}", 0.75, 1.60)))
        self.play(FadeOut(unique1), FadeOut(unique2))

        no1 = self.line(ax, -1, 2, VECTOR_A)
        no2 = self.line(ax, -1, 5/2, VECTOR_B)
        self.play(Create(no1), Create(no2))
        self.cc("Second case: the lines are parallel and distinct. No point lies on both, so the system is inconsistent.", 3.0)
        self.play(Write(self.eq(r"\boxed{\text{no solution}}", 0.75, 1.60)))
        self.play(FadeOut(no1), FadeOut(no2))

        inf1 = self.line(ax, -1, 2, VECTOR_A)
        inf2 = self.line(ax, -1, 2, VECTOR_B)
        self.play(Create(inf1), Create(inf2))
        self.cc("Third case: the equations describe the same line. Every point on that line satisfies both, so infinitely many solutions exist.", 3.1)
        self.play(Write(self.eq(r"\boxed{\text{infinitely many solutions}}", 0.67, 1.60)))
        self.play(Write(self.eq(r"\operatorname{Sol}=\{(x,y):x+y=2\}", 0.72, -1.35)))
        self.wait(2)


class Part4_09_HomogeneousSystems(SystemsLesson):
    def construct(self):
        self.title("Part IV.9 — Homogeneous Systems", "The special system Ax = 0")
        ax = Axes(x_range=[-4, 4, 1], y_range=[-4, 4, 1], x_length=7.0, y_length=6.2, axis_config={"include_numbers": True}).to_edge(LEFT, buff=0.35)
        self.play(Create(ax))
        self.play(Write(self.eq(r"A\vec x=\vec0", 0.95, 1.35)))
        self.cc("A homogeneous system has zero on the right-hand side. The zero vector is always a solution because A times zero is zero.", 3.0)
        L = ax.plot(lambda x: -x, color=VECTOR_A, x_range=[-4, 4])
        self.play(Create(L))
        self.cc("For the system x+y=0, the entire line y=-x is made of solutions. Homogeneous systems therefore reveal null-space geometry naturally.", 3.2)
        self.play(Write(self.eq(r"\begin{cases}x+y=0\\\text{solutions: }(t,-t)\end{cases}", 0.70, 0.25)))
        self.play(Write(self.eq(r"\vec x=t\begin{bmatrix}1\\-1\end{bmatrix}", 0.82, -0.80)))
        self.cc("This is a direct connection to Part II: the solution set of Ax=0 is exactly the null space of A.", 3.0)
        self.play(Write(self.eq(r"\operatorname{Null}(A)=\{x:A x=0\}", 0.75, -1.70)))
        self.wait(2)


class Part4_10_ThreeByThreeWorkedSystem(SystemsLesson):
    def construct(self):
        self.title("Part IV.10 — Full 3×3 Worked System", "From equations to elimination to the final vector")
        self.play(Write(self.eq(r"\begin{cases}x+y+z=6\\2x-y+z=3\\x+2y-z=2\end{cases}", 0.78, 1.45)))
        self.cc("For three unknowns, the same method scales directly. We first build the augmented matrix, then eliminate systematically.", 3.0)
        self.play(Write(self.eq(r"\left[\begin{array}{ccc|c}1&1&1&6\\2&-1&1&3\\1&2&-1&2\end{array}\right]", 0.76, 0.25)))
        self.play(Write(self.eq(r"R_2\leftarrow R_2-2R_1,\quad R_3\leftarrow R_3-R_1", 0.58, -0.65)))
        self.play(Write(self.eq(r"\left[\begin{array}{ccc|c}1&1&1&6\\0&-3&-1&-9\\0&1&-2&-4\end{array}\right]", 0.74, -1.20)))
        self.cc("Now eliminate the second-column entry in the third row. Adding one third of row two is enough because the pivot is negative three.", 3.2)
        self.play(Write(self.eq(r"R_3\leftarrow R_3+\frac13R_2", 0.66, -1.85)))
        self.play(Write(self.eq(r"\left[\begin{array}{ccc|c}1&1&1&6\\0&-3&-1&-9\\0&0&-\frac73&-7\end{array}\right]", 0.70, -2.45)))
        self.cc("The system is triangular. Solve upward: z is three, then y is two, then x is one.", 2.9)
        self.play(Write(self.eq(r"\boxed{(x,y,z)=(1,2,3)}", 0.92, -3.0)))
        self.wait(2)


class Part4_11_SystemsMastery(SystemsLesson):
    def construct(self):
        self.title("Part IV.11 — Systems Mastery", "The complete mental model")
        self.play(Write(self.eq(r"A\vec x=\vec b", 1.12, 1.65)))
        self.cc("A system is a compatibility question: which input vectors x produce the required output b under the matrix transformation A?", 3.3)
        summary = VGroup(
            Text("Geometry → intersections / solution sets", font_size=22),
            Text("Augmented matrix → compact system representation", font_size=22),
            Text("Row operations → equivalent systems", font_size=22),
            Text("Gaussian elimination → triangular form", font_size=22),
            Text("RREF → direct reading of pivots and solutions", font_size=22),
            Text("Three outcomes → one / none / infinitely many", font_size=22),
            Text("Ax = 0 → null-space geometry", font_size=22),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.17).to_edge(RIGHT, buff=0.10).shift(DOWN * 0.35)
        self.play(LaggedStart(*[Write(item) for item in summary], lag_ratio=0.18), run_time=2.7)
        self.cc("The algebra and geometry are saying the same thing in two languages. Row reduction is powerful because it preserves the solution set while making the structure easier to see.", 3.6)
        self.play(Write(Text("Part IV complete: solve systems by seeing their structure.", font_size=26, color=YELLOW_B).to_edge(DOWN, buff=0.48)))
        self.wait(3)


__all__ = [name for name in globals() if name.startswith("Part4_") or name == "SystemsLesson"]
