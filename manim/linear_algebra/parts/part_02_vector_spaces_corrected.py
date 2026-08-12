from .part_02_vector_spaces import *

class Part2_01_Span(VectorSpaceLesson):
    def construct(self):
        self.title("Part II.1 — Span", "Which vectors can we build from a collection of vectors?")
        ax = self.axes2d(); self.play(Create(ax))
        u = arrow_from(ax, (2, 1), VECTOR_A, r"\vec u")
        v = arrow_from(ax, (-1, 2), VECTOR_B, r"\vec v")
        self.play(GrowArrow(u[0]), Write(u[1]), GrowArrow(v[0]), Write(v[1]))
        self.cc("We ask which vectors are reachable by linear combinations of the vectors we are given.", 3)
        target = arrow_from(ax, (3, 4), HIGHLIGHT, r"\vec w")
        self.play(GrowArrow(target[0]), Write(target[1]))
        self.play(Write(self.eq(r"\vec w=2\vec u+\vec v=\begin{bmatrix}3\\4\end{bmatrix}", 0.82, 1.45)))
        self.cc("Here 2u+v really is (3,4): 2(2,1)+(-1,2)=(3,4).", 3.2)
        grid = VGroup()
        for a in range(-4, 5):
            for b in range(-4, 5):
                x, y = 2*a-b, a+2*b
                if -5 <= x <= 5 and -5 <= y <= 5:
                    grid.add(self.span_point(ax, (x, y), GREEN_C))
        self.play(LaggedStart(*[FadeIn(p, scale=0.5) for p in grid], lag_ratio=0.015), run_time=3)
        self.play(Write(self.eq(r"\operatorname{span}\{\vec u,\vec v\}=\mathbb R^2", 0.78, 0.2)))
        self.cc("Because the two generators are independent, their span fills the entire plane.", 3)
        self.wait(2)

class Part2_11_FourFundamentalSubspaces(LessonScene):
    def construct(self):
        self.title("Part II.11 — The Four Fundamental Subspaces", "One concrete matrix, four spaces, two orthogonal pairs")
        ax = Axes(x_range=[-5,5,1], y_range=[-5,5,1], x_length=8.4, y_length=6.8, axis_config={"include_numbers": True, "stroke_width": 2}).to_edge(LEFT, buff=0.35)
        self.play(Create(ax))
        self.cc("Use one matrix so every one of the four spaces has a concrete geometric meaning.", 3)
        self.play(Write(MathTex(r"A=\begin{bmatrix}1&2\\0&0\end{bmatrix}").scale(0.9).to_edge(RIGHT).shift(UP*2)))
        col=Arrow(ax.c2p(0,0),ax.c2p(1,0),buff=0,color=VECTOR_A,stroke_width=7)
        row=Arrow(ax.c2p(0,0),ax.c2p(2,1),buff=0,color=VECTOR_B,stroke_width=7)
        null=Arrow(ax.c2p(0,0),ax.c2p(-2,1),buff=0,color=HIGHLIGHT,stroke_width=7)
        left=Arrow(ax.c2p(0,0),ax.c2p(0,1),buff=0,color=YELLOW_C,stroke_width=7)
        self.play(GrowArrow(col),GrowArrow(row),GrowArrow(null),GrowArrow(left))
        self.play(Write(MathTex(r"\operatorname{Col}(A)=\operatorname{span}\left\{\begin{bmatrix}1\\0\end{bmatrix}\right\}").scale(0.55).to_edge(RIGHT).shift(UP*0.8)))
        self.play(Write(MathTex(r"\operatorname{Row}(A)=\operatorname{span}\left\{\begin{bmatrix}1&2\end{bmatrix}\right\}").scale(0.55).to_edge(RIGHT).shift(UP*0.0)))
        self.play(Write(MathTex(r"\operatorname{Null}(A)=\operatorname{span}\left\{\begin{bmatrix}-2\\1\end{bmatrix}\right\}").scale(0.55).to_edge(RIGHT).shift(DOWN*0.8)))
        self.play(Write(MathTex(r"\operatorname{Null}(A^T)=\operatorname{span}\left\{\begin{bmatrix}0\\1\end{bmatrix}\right\}").scale(0.55).to_edge(RIGHT).shift(DOWN*1.6)))
        self.cc("The row and ordinary null spaces are perpendicular because (1,2) dot (-2,1) is zero. The column space and transpose null space are also perpendicular.", 4)
        self.play(Write(MathTex(r"\operatorname{Row}(A)\perp\operatorname{Null}(A),\qquad \operatorname{Col}(A)\perp\operatorname{Null}(A^T)").scale(0.55).to_edge(DOWN)))
        self.wait(3)
