from manim import *
from ..utils import *


class FoundationLesson(LessonScene):
    def axes(self):
        ax = Axes(x_range=[-6,6,1], y_range=[-5,5,1], x_length=9.2, y_length=6.6,
                  axis_config={"include_numbers": True, "stroke_width": 2})
        ax.to_edge(LEFT, buff=0.35)
        return ax

    def eq(self, s, scale=0.7, y=0):
        return MathTex(s).scale(scale).to_edge(RIGHT, buff=0.28).shift(UP*y)


class Part1_01_ScalarsAndVectors(FoundationLesson):
    def construct(self):
        self.title("Part I.1 — Scalars vs Vectors", "Amount versus amount + direction")
        ax=self.axes(); self.play(Create(ax))
        self.cc("A scalar gives an amount. A vector gives an amount together with a direction.",3)
        s=MathTex(r"5\,m").scale(1.1).to_edge(RIGHT).shift(UP*1.5); self.play(Write(s))
        self.cc("Five meters tells us how much distance we have, but not which way.",2.8); self.play(FadeOut(s))
        v=arrow_from(ax,(4,2),VECTOR_A,r"\vec v"); g=component_guides(ax,4,2,GREY_B)
        self.play(GrowArrow(v[0]),Write(v[1]),Create(g),FadeIn(coordinate_dot(ax,(4,2))))
        self.play(Write(coord_label(ax,(4,2),r"(4,2)",VECTOR_A)))
        self.cc("This arrow means four units right and two units up. The important object is the displacement.",3)
        shifted=Arrow(ax.c2p(-4,-1),ax.c2p(0,1),buff=0,color=VECTOR_A,stroke_width=7)
        self.play(TransformFromCopy(v[0],shifted)); self.cc("Move the tail and the displacement stays the same.",2.7)
        self.play(Write(self.eq(r"\boxed{\text{vector}=\text{magnitude + direction}}",.82,-1.2)))
        self.cc("That distinction will later describe geometry, motion, forces, and data.",2.8); self.wait(2)


class Part1_02_CoordinatesAndComponents(FoundationLesson):
    def construct(self):
        self.title("Part I.2 — Coordinates and Components", "Turning geometry into numbers")
        ax=self.axes(); self.play(Create(ax)); self.cc("Coordinates describe a vector relative to a chosen coordinate system.",2.8)
        v=arrow_from(ax,(3,4),VECTOR_A,r"\vec v"); g=component_guides(ax,3,4,VECTOR_B)
        self.play(GrowArrow(v[0]),Write(v[1]),Create(g),Write(coord_label(ax,(3,4),r"(3,4)",VECTOR_A)))
        self.cc("The horizontal component is 3 and the vertical component is 4.",2.5)
        self.play(Write(self.eq(r"\vec v=\begin{bmatrix}3\\4\end{bmatrix}",.9,1.2)))
        self.cc("The arrow and the column vector are two representations of the same object.",3)
        self.play(FadeOut(v),FadeOut(g)); u=arrow_from(ax,(-2,3),VECTOR_B,r"\vec u"); self.play(GrowArrow(u[0]),Write(u[1]))
        self.play(Write(self.eq(r"\vec u=\begin{bmatrix}-2\\3\end{bmatrix}",.82,.6)))
        self.cc("A negative component simply means movement in the negative coordinate direction.",2.8); self.wait(2)


class Part1_03_VectorAddition(FoundationLesson):
    def construct(self):
        self.title("Part I.3 — Vector Addition", "Tip-to-tail and parallelogram constructions")
        ax=self.axes(); self.play(Create(ax))
        a=arrow_from(ax,(3,1),VECTOR_A,r"\vec a"); b=arrow_from(ax,(1,3),VECTOR_B,r"\vec b")
        self.play(GrowArrow(a[0]),Write(a[1]),GrowArrow(b[0]),Write(b[1])); self.cc("Adding vectors combines their displacements.",2.5)
        sb=Arrow(ax.c2p(3,1),ax.c2p(4,4),buff=0,color=VECTOR_B,stroke_width=7)
        sa=Arrow(ax.c2p(1,3),ax.c2p(4,4),buff=0,color=VECTOR_A,stroke_width=7)
        self.play(TransformFromCopy(b[0],sb),TransformFromCopy(a[0],sa)); self.cc("Move one vector tip-to-tail with the other. The final tip is the sum.",2.8)
        r=arrow_from(ax,(4,4),HIGHLIGHT,r"\vec a+\vec b"); self.play(GrowArrow(r[0]),Write(r[1]))
        self.play(Write(self.eq(r"\begin{bmatrix}3\\1\end{bmatrix}+\begin{bmatrix}1\\3\end{bmatrix}=\begin{bmatrix}4\\4\end{bmatrix}",.6,-.4)))
        self.cc("The x-components add to x-components, and y-components add to y-components.",3)
        p=Polygon(ax.c2p(0,0),ax.c2p(3,1),ax.c2p(4,4),ax.c2p(1,3),color=GREY_B); self.play(Create(p))
        self.cc("The same result is the diagonal of a parallelogram.",2.8); self.wait(2)


class Part1_04_VectorSubtraction(FoundationLesson):
    def construct(self):
        self.title("Part I.4 — Vector Subtraction", "A difference is a displacement")
        ax=self.axes(); self.play(Create(ax))
        a=arrow_from(ax,(4,3),VECTOR_A,r"\vec a"); b=arrow_from(ax,(1,1),VECTOR_B,r"\vec b")
        self.play(GrowArrow(a[0]),Write(a[1]),GrowArrow(b[0]),Write(b[1])); self.cc("What vector takes us from b to a?",2.5)
        d=Arrow(ax.c2p(1,1),ax.c2p(4,3),buff=0,color=HIGHLIGHT,stroke_width=7); self.play(GrowArrow(d))
        self.cc("Start at b and point to a. That displacement is a minus b.",2.7)
        self.play(Write(self.eq(r"\vec a-\vec b=\begin{bmatrix}4\\3\end{bmatrix}-\begin{bmatrix}1\\1\end{bmatrix}=\begin{bmatrix}3\\2\end{bmatrix}",.58,.2)))
        self.play(Write(self.eq(r"\vec a-\vec b=\vec a+(-\vec b)",.78,-1.4)))
        self.cc("Negation reverses direction, so subtraction is addition of the opposite vector.",3); self.wait(2)


class Part1_05_ScalingAndUnitVectors(FoundationLesson):
    def construct(self):
        self.title("Part I.5 — Scaling and Unit Vectors", "Changing length and normalizing direction")
        ax=self.axes(); self.play(Create(ax)); v=arrow_from(ax,(2,1),VECTOR_A,r"\vec v"); self.play(GrowArrow(v[0]),Write(v[1]))
        self.cc("A positive scalar changes size without changing direction. A negative scalar reverses direction.",3)
        two=arrow_from(ax,(4,2),VECTOR_B,r"2\vec v"); neg=arrow_from(ax,(-2,-1),HIGHLIGHT,r"-\vec v")
        self.play(GrowArrow(two[0]),Write(two[1]),GrowArrow(neg[0]),Write(neg[1]))
        self.play(Write(self.eq(r"2\vec v=\begin{bmatrix}4\\2\end{bmatrix}",.8,1.2))); self.cc("Multiplying by two doubles every component and doubles the length.",2.5)
        self.play(FadeOut(two),FadeOut(neg)); self.play(Write(self.eq(r"\|\vec v\|=\sqrt{2^2+1^2}=\sqrt5",.76,1.0)))
        self.play(Write(self.eq(r"\hat v=\frac{\vec v}{\|\vec v\|}",.88,-.1))); self.cc("Dividing by the magnitude produces a unit vector with the same direction.",2.8)
        self.play(Write(self.eq(r"\|\hat v\|=1",.88,-1.35))); self.cc("Normalization keeps direction while removing arbitrary scale.",2.5); self.wait(2)


class Part1_06_MagnitudeAndDistance(FoundationLesson):
    def construct(self):
        self.title("Part I.6 — Magnitude and Distance", "Length from components")
        ax=self.axes(); self.play(Create(ax)); v=arrow_from(ax,(3,4),VECTOR_A,r"\vec v"); g=component_guides(ax,3,4,GREY_B)
        self.play(GrowArrow(v[0]),Write(v[1]),Create(g)); self.cc("The components form a right triangle, with the vector as the hypotenuse.",2.8)
        self.play(Write(self.eq(r"\|\vec v\|^2=3^2+4^2",.88,1.2))); self.cc("The Pythagorean theorem becomes the vector norm formula.",2.5)
        self.play(Write(self.eq(r"\|\vec v\|=\sqrt{3^2+4^2}=5",.82,.0))); self.cc("So a 3-4 vector has length exactly five.",2.3)
        p=coordinate_dot(ax,(-2,-1),VECTOR_B); q=coordinate_dot(ax,(2,2),HIGHLIGHT); seg=Line(ax.c2p(-2,-1),ax.c2p(2,2),color=GREEN_C,stroke_width=6)
        self.play(FadeOut(v),FadeOut(g),FadeIn(p),FadeIn(q),Create(seg)); self.play(Write(self.eq(r"Q-P=\begin{bmatrix}4\\3\end{bmatrix}",.82,.9)))
        self.cc("Distance between two points comes from their difference vector.",2.8)
        self.play(Write(self.eq(r"d(P,Q)=\|Q-P\|=\sqrt{4^2+3^2}=5",.7,-.5))); self.cc("Distance is simply the magnitude of the displacement from one point to the other.",2.8); self.wait(2)


class Part1_07_LinearCombinations(FoundationLesson):
    def construct(self):
        self.title("Part I.7 — Linear Combinations", "Scaling and combining vectors")
        ax=self.axes(); self.play(Create(ax))
        u=arrow_from(ax,(2,.5),VECTOR_A,r"\vec u"); v=arrow_from(ax,(-1,.5),VECTOR_B,r"\vec v")
        self.play(GrowArrow(u[0]),Write(u[1]),GrowArrow(v[0]),Write(v[1])); self.cc("A linear combination scales vectors and then adds the results.",2.7)
        self.play(Write(self.eq(r"\vec w=2\vec u+3\vec v",.94,1.4)))
        su=Arrow(ax.c2p(0,0),ax.c2p(4,1),buff=0,color=VECTOR_A,stroke_width=7); self.play(GrowArrow(su))
        self.cc("First scale u by two: four right and one up.",2.5)
        sv=Arrow(ax.c2p(4,1),ax.c2p(1,2.5),buff=0,color=VECTOR_B,stroke_width=7); self.play(GrowArrow(sv))
        self.cc("Then add three copies of v. Three copies contribute three left and one-and-a-half up.",3.1)
        out=Arrow(ax.c2p(0,0),ax.c2p(1,2.5),buff=0,color=HIGHLIGHT,stroke_width=7); self.play(GrowArrow(out))
        self.play(Write(self.eq(r"2\begin{bmatrix}2\\0.5\end{bmatrix}+3\begin{bmatrix}-1\\0.5\end{bmatrix}=\begin{bmatrix}1\\2.5\end{bmatrix}",.53,-.7)))
        self.cc("Both the geometry and the component calculation land at the same endpoint.",3)
        self.play(Write(self.eq(r"\boxed{\vec w=a\vec u+b\vec v}",.92,-2.0))); self.cc("This is the basic language behind span, basis, matrices, and later machine-learning representations.",3.2); self.wait(2)


class Part1_08_FoundationsRecap(FoundationLesson):
    def construct(self):
        self.title("Part I.8 — Foundations Recap", "One mental model connecting the first seven lessons")
        ax=self.axes(); self.play(Create(ax)); v=arrow_from(ax,(3,2),VECTOR_A,r"\vec v"); self.play(GrowArrow(v[0]),Write(v[1]))
        self.cc("Everything so far is about describing and manipulating displacement.",2.7)
        fs=VGroup(
            MathTex(r"\vec v=\begin{bmatrix}v_x\\v_y\end{bmatrix}"),
            MathTex(r"\|\vec v\|=\sqrt{v_x^2+v_y^2}"),
            MathTex(r"\vec a+\vec b=\begin{bmatrix}a_x+b_x\\a_y+b_y\end{bmatrix}"),
            MathTex(r"c\vec v=\begin{bmatrix}cv_x\\cv_y\end{bmatrix}"),
            MathTex(r"\vec w=a\vec u+b\vec v"),
        ).scale(.63).arrange(DOWN,aligned_edge=LEFT,buff=.28).to_edge(RIGHT,buff=.25)
        self.play(LaggedStart(*[Write(x) for x in fs],lag_ratio=.3),run_time=2.6); self.cc("Components encode movement; the norm measures length; addition combines movement; scaling changes size; linear combinations build new vectors.",3.6)
        self.play(FadeOut(fs));
        for t in ["A vector is a displacement, not a location.","Negative components describe direction.","A difference of points is a displacement vector.","A unit vector preserves direction and removes scale.","Linear combinations build new vectors from old ones."]:
            q=Text(t,font_size=28).to_edge(RIGHT,buff=.25); self.play(Write(q)); self.cc(t,2.3,size=24); self.play(FadeOut(q))
        end=Text("Next: span, independence, basis, dimension, and vector spaces.",font_size=27,color=YELLOW_B).to_edge(DOWN,buff=.6); self.play(Write(end)); self.wait(3)
