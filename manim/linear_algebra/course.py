from manim import *
from utils import *

class Lesson01Vectors(LessonScene):
    def construct(self):
        self.title("Lesson 01 — Vectors", "Coordinates, direction, magnitude, and geometric meaning")
        ax = Axes(x_range=[-5,5,1], y_range=[-4,4,1], x_length=9, y_length=6, axis_config={"include_numbers": True})
        ax.to_edge(LEFT, buff=0.45)
        self.play(Create(ax)); self.play(FadeIn(section_text("A vector is a directed displacement.", 3.0)))
        v=arrow_from(ax,(3,2),VECTOR_A,r"\vec v")
        self.play(GrowArrow(v[0]), Write(v[1])); self.wait(1.5)
        c=coord_label(ax,(3,2),r"(3,2)",VECTOR_A); self.play(Write(c))
        txt=explain(self,"The endpoint tells us the components: 3 units horizontally and 2 units vertically.",2.5)
        comp_x=DashedLine(ax.c2p(3,0),ax.c2p(3,2),color=VECTOR_A); comp_y=DashedLine(ax.c2p(0,2),ax.c2p(3,2),color=VECTOR_A)
        self.play(Create(comp_x),Create(comp_y),run_time=1.2)
        f=formula(r"\vec v=\begin{bmatrix}3\\2\end{bmatrix}",0.9).to_edge(RIGHT).shift(UP*1.4); self.play(Write(f)); self.wait(1)
        mag=formula(r"\|\vec v\|=\sqrt{3^2+2^2}=\sqrt{13}\approx3.606",0.72).to_edge(RIGHT); self.play(Write(mag)); self.wait(2)
        self.play(FadeOut(txt), FadeOut(f), FadeOut(mag), FadeOut(c), FadeOut(v), FadeOut(comp_x), FadeOut(comp_y))
        v2=arrow_from(ax,(-2,3),VECTOR_B,r"\vec w"); self.play(GrowArrow(v2[0]),Write(v2[1])); self.play(Write(coord_label(ax,(-2,3),r"(-2,3)",VECTOR_B))); self.wait(1)
        neg=formula(r"-\vec w=\begin{bmatrix}2\\-3\end{bmatrix}",0.82).to_edge(RIGHT).shift(UP*0.8); self.play(Write(neg)); self.play(v2[0].animate.put_start_and_end_on(ax.c2p(0,0),ax.c2p(2,-3))); self.wait(1.5)
        exp=explain(self,"Negating a vector reverses its direction but keeps exactly the same magnitude.",2.5); self.play(FadeOut(exp),FadeOut(neg))
        u=arrow_from(ax,(1,2),VECTOR_C,r"\vec u"); self.play(GrowArrow(u[0]),Write(u[1]))
        sum_arrow=arrow_from(ax,(-1,5),HIGHLIGHT,r"\vec w+\vec u"); self.play(GrowArrow(sum_arrow[0]),Write(sum_arrow[1]))
        ex=formula(r"\begin{bmatrix}-2\\3\end{bmatrix}+\begin{bmatrix}1\\2\end{bmatrix}=\begin{bmatrix}-1\\5\end{bmatrix}",0.7).to_edge(RIGHT); self.play(Write(ex)); self.wait(2); self.play(FadeOut(ex))
        self.play(Write(Text("Key idea: vectors encode movement, not a location.",font_size=30,color=YELLOW_B).to_edge(DOWN))); self.wait(3)

class Lesson02VectorOperations(LessonScene):
    def construct(self):
        self.title("Lesson 02 — Vector Operations", "Addition, subtraction, scalar multiplication, and linear combinations")
        ax=Axes(x_range=[-6,6,1],y_range=[-5,5,1],x_length=10,y_length=7,axis_config={"include_numbers":True}); self.play(Create(ax))
        a=arrow_from(ax,(3,1),VECTOR_A,r"\vec a"); b=arrow_from(ax,(1,3),VECTOR_B,r"\vec b"); self.play(GrowArrow(a[0]),Write(a[1]),GrowArrow(b[0]),Write(b[1])); self.wait(1)
        parallelogram=Polygon(ax.c2p(0,0),ax.c2p(3,1),ax.c2p(4,4),ax.c2p(1,3),color=GREY_B,stroke_opacity=.8); self.play(Create(parallelogram))
        s=arrow_from(ax,(4,4),VECTOR_C,r"\vec a+\vec b"); self.play(GrowArrow(s[0]),Write(s[1])); self.play(Write(formula(r"\vec a+\vec b=\begin{bmatrix}4\\4\end{bmatrix}",.82).to_edge(RIGHT))); self.wait(2)
        self.play(FadeOut(parallelogram)); d=arrow_from(ax,(2,-2),HIGHLIGHT,r"\vec a-\vec b"); self.play(GrowArrow(d[0]),Write(d[1])); self.play(Write(formula(r"\vec a-\vec b=\vec a+(-\vec b)=\begin{bmatrix}2\\-2\end{bmatrix}",.66).to_edge(RIGHT))); self.wait(2)
        k=formula(r"2\vec a=\begin{bmatrix}6\\2\end{bmatrix}",.9).to_edge(RIGHT).shift(DOWN*1.4); self.play(Write(k)); self.play(a[0].animate.put_start_and_end_on(ax.c2p(0,0),ax.c2p(6,2))); self.wait(2)
        combo=formula(r"3\vec a-2\vec b=3\begin{bmatrix}3\\1\end{bmatrix}-2\begin{bmatrix}1\\3\end{bmatrix}=\begin{bmatrix}7\\-3\end{bmatrix}",.66).to_edge(RIGHT); self.play(Write(combo)); self.wait(2)
        note=explain(self,"Linear combinations are the basic language behind span, basis, matrix multiplication, and many ML models.",3); self.wait(1); self.play(FadeOut(note)); self.play(Write(Text("Practice: predict the endpoint before watching the arrow move.",font_size=28,color=YELLOW_B).to_edge(DOWN))); self.wait(3)

class Lesson03SpanBasisDimension(LessonScene):
    def construct(self):
        self.title("Lesson 03 — Span, Basis, and Dimension", "How vectors generate spaces")
        ax=Axes(x_range=[-5,5,1],y_range=[-4,4,1],x_length=9,y_length=6,axis_config={"include_numbers":True}); self.play(Create(ax))
        i=arrow_from(ax,(1,0),VECTOR_A,r"\vec e_1"); j=arrow_from(ax,(0,1),VECTOR_B,r"\vec e_2"); self.play(GrowArrow(i[0]),Write(i[1]),GrowArrow(j[0]),Write(j[1]))
        self.play(Write(formula(r"\vec x=x_1\vec e_1+x_2\vec e_2",.9).to_edge(RIGHT).shift(UP*1.4)))
        grid=VGroup(*[Line(ax.c2p(x,-4),ax.c2p(x,4),stroke_opacity=.12) for x in range(-5,6)], *[Line(ax.c2p(-5,y),ax.c2p(5,y),stroke_opacity=.12) for y in range(-4,5)]); self.play(Create(grid),run_time=1.5)
        self.play(Write(explain(self,"Because every point in the plane can be written this way, e1 and e2 span R².",2.8))); self.wait(1)
        dep1=arrow_from(ax,(2,1),VECTOR_A,r"\vec u"); dep2=arrow_from(ax,(4,2),VECTOR_B,r"2\vec u"); self.play(GrowArrow(dep1[0]),Write(dep1[1]),GrowArrow(dep2[0]),Write(dep2[1]))
        self.play(Write(formula(r"\vec v=2\vec u\quad\Rightarrow\quad\text{dependent}",.74).to_edge(RIGHT).shift(DOWN*1))); self.wait(2); self.play(FadeOut(dep1),FadeOut(dep2))
        basis=VGroup(MathTex(r"\{\vec u,\vec v\}\text{ is a basis if:}"),MathTex(r"1.\ \text{independent}"),MathTex(r"2.\ \text{spans the space}")).arrange(DOWN,aligned_edge=LEFT); basis.scale(.75).to_edge(RIGHT); self.play(Write(basis)); self.wait(2.5)
        self.play(Write(formula(r"\dim(\mathbb R^2)=2,\qquad \dim(\mathbb R^3)=3",.82).to_edge(DOWN))); self.wait(3)

class Lesson04MatricesTransformations(LessonScene):
    def construct(self):
        self.title("Lesson 04 — Matrices as Transformations", "A matrix is a rule that moves vectors")
        ax=NumberPlane(x_range=[-5,5,1],y_range=[-4,4,1],x_length=10,y_length=7,background_line_style={"stroke_opacity":.18}); self.play(Create(ax))
        e1=Arrow(ax.c2p(0,0),ax.c2p(1,0),buff=0,color=VECTOR_A,stroke_width=7); e2=Arrow(ax.c2p(0,0),ax.c2p(0,1),buff=0,color=VECTOR_B,stroke_width=7); self.play(GrowArrow(e1),GrowArrow(e2))
        M=MathTex(r"A=\begin{bmatrix}2&1\\0&1\end{bmatrix}").to_corner(UR); self.play(Write(M)); self.wait(1)
        self.play(ax.animate.apply_matrix([[2,1],[0,1]]), e1.animate.put_start_and_end_on(ax.c2p(0,0),ax.c2p(2,0)), e2.animate.put_start_and_end_on(ax.c2p(0,0),ax.c2p(1,1)),run_time=2.5)
        self.play(Write(explain(self,"The grid shears and stretches because the matrix changes the basis directions.",2.8))); self.wait(1)
        self.play(Write(formula(r"A\begin{bmatrix}x\\y\end{bmatrix}=\begin{bmatrix}2x+y\\y\end{bmatrix}",.9).to_edge(RIGHT).shift(DOWN*1))); self.wait(2); self.play(FadeOut(M))
        rot=MathTex(r"R(\theta)=\begin{bmatrix}\cos\theta&-\sin\theta\\\sin\theta&\cos\theta\end{bmatrix}").to_edge(UP); self.play(Write(rot)); self.wait(1); self.play(ax.animate.rotate(PI/4),run_time=2); self.wait(2)
        self.play(Write(Text("Matrices let us reason about geometry using algebra.",font_size=30,color=YELLOW_B).to_edge(DOWN))); self.wait(3)

class Lesson05MatrixMultiplication(LessonScene):
    def construct(self):
        self.title("Lesson 05 — Matrix Multiplication & Linear Systems", "Composition, rows, columns, and Ax=b")
        A=Matrix([[2,1],[1,3]],left_bracket="[",right_bracket="]").scale(.9).shift(LEFT*3); x=Matrix([["x"],["y"]]).scale(.9).shift(DOWN*2.6); B=Matrix([[5],[7]]).scale(.9).shift(RIGHT*3); self.play(Write(A),Write(x),Write(B))
        eq=MathTex("A\\mathbf{x}=\\mathbf{b}").scale(1.1).move_to(UP*2.4); self.play(Write(eq)); self.wait(1)
        mult=MathTex(r"\begin{bmatrix}2&1\\1&3\end{bmatrix}\begin{bmatrix}x\\y\end{bmatrix}=\begin{bmatrix}2x+y\\x+3y\end{bmatrix}").scale(.78).move_to(ORIGIN); self.play(Write(mult)); self.wait(2)
        system=MathTex(r"2x+y=5,\qquad x+3y=7").scale(.9).move_to(DOWN*1.8); self.play(Write(system)); self.wait(2)
        sol=MathTex(r"x=\frac85,\qquad y=\frac75").scale(.95).move_to(DOWN*3.1); self.play(Write(sol)); self.wait(2); self.play(FadeOut(eq),FadeOut(mult),FadeOut(system),FadeOut(sol),FadeOut(A),FadeOut(x),FadeOut(B))
        plane2=plane(); self.play(Create(plane2)); line1=plane2.plot(lambda t: 5-2*t,x_range=[-1,4],color=VECTOR_A); line2=plane2.plot(lambda t: (7-t)/3,x_range=[-1,4],color=VECTOR_B); inter=Dot(plane2.c2p(1.6,1.8),color=HIGHLIGHT); self.play(Create(line1),Create(line2),FadeIn(inter),run_time=2)
        self.play(Write(explain(self,"A linear system can be viewed geometrically: each equation defines a set of points; the solution is their intersection.",3))); self.wait(3)

class Lesson06DeterminantInverse(LessonScene):
    def construct(self):
        self.title("Lesson 06 — Determinant and Inverse", "Area scaling, invertibility, and when Ax=b has a unique solution")
        ax=NumberPlane(x_range=[-4,4,1],y_range=[-4,4,1],x_length=7,y_length=7,background_line_style={"stroke_opacity":.17}).to_edge(LEFT); self.play(Create(ax))
        square=Polygon(ax.c2p(0,0),ax.c2p(2,0),ax.c2p(2,1),ax.c2p(0,1),color=VECTOR_A,fill_opacity=.3); self.play(Create(square))
        A=MathTex(r"A=\begin{bmatrix}2&1\\1&2\end{bmatrix}").to_edge(RIGHT).shift(UP*1.4); d=MathTex(r"\det(A)=2\cdot2-1\cdot1=3").to_edge(RIGHT); self.play(Write(A),Write(d)); self.play(square.animate.apply_matrix([[2,1],[1,2]]),run_time=2)
        self.play(Write(explain(self,"The absolute determinant is the factor by which area scales. A zero determinant means the plane collapses into a lower-dimensional set.",3))); self.wait(1)
        inv=MathTex(r"A^{-1}=\frac{1}{\det(A)}\begin{bmatrix}d&-b\\-c&a\end{bmatrix}",font_size=34).to_edge(RIGHT).shift(DOWN*1.3); self.play(Write(inv)); self.wait(2)
        zero=MathTex(r"\det\begin{bmatrix}1&2\\2&4\end{bmatrix}=0").to_edge(RIGHT).shift(DOWN*2.6); self.play(Write(zero))
        collapse=NumberPlane(x_range=[-4,4,1],y_range=[-4,4,1],x_length=7,y_length=7,background_line_style={"stroke_opacity":.17}).to_edge(LEFT); self.play(Transform(ax,collapse)); self.play(ax.animate.apply_matrix([[1,2],[2,4]]),run_time=2)
        self.play(Write(Text("No inverse: the transformation loses information.",font_size=29,color=HIGHLIGHT).to_edge(DOWN))); self.wait(3)

class Lesson07DotProduct(LessonScene):
    def construct(self):
        self.title("Lesson 07 — Dot Product & Geometry", "Length, angle, orthogonality, and similarity")
        ax=Axes(x_range=[-5,5,1],y_range=[-4,4,1],x_length=9,y_length=6,axis_config={"include_numbers":True}); self.play(Create(ax))
        a=arrow_from(ax,(3,1),VECTOR_A,r"\vec a"); b=arrow_from(ax,(1,3),VECTOR_B,r"\vec b"); self.play(GrowArrow(a[0]),Write(a[1]),GrowArrow(b[0]),Write(b[1]))
        dot=MathTex(r"\vec a\cdot\vec b=3(1)+1(3)=6").to_edge(RIGHT).shift(UP*1.7); self.play(Write(dot)); self.wait(2)
        angle=MathTex(r"\vec a\cdot\vec b=\|\vec a\|\|\vec b\|\cos\theta").to_edge(RIGHT); self.play(Write(angle)); self.wait(2)
        self.play(Write(explain(self,"The dot product measures alignment. Positive means an acute angle; zero means 90°; negative means an obtuse angle.",3))); self.wait(1)
        perp1=arrow_from(ax,(4,2),VECTOR_C,r"\vec p"); perp2=arrow_from(ax,(-2,4),HIGHLIGHT,r"\vec q"); self.play(GrowArrow(perp1[0]),Write(perp1[1]),GrowArrow(perp2[0]),Write(perp2[1]))
        ort=MathTex(r"\vec p\cdot\vec q=4(-2)+2(4)=0").to_edge(RIGHT).shift(DOWN*1.7); self.play(Write(ort)); self.wait(2)
        norm=MathTex(r"\hat a=\frac{\vec a}{\|\vec a\|}").to_edge(RIGHT).shift(DOWN*2.7); self.play(Write(norm)); self.wait(2)
        self.play(Write(Text("Unit vectors preserve direction while normalizing length to 1.",font_size=27,color=YELLOW_B).to_edge(DOWN))); self.wait(3)

class Lesson08ProjectionLeastSquares(LessonScene):
    def construct(self):
        self.title("Lesson 08 — Projection & Least Squares", "The closest point on a line")
        ax=Axes(x_range=[-1,6,1],y_range=[-1,6,1],x_length=8,y_length=7,axis_config={"include_numbers":True}); self.play(Create(ax))
        u=arrow_from(ax,(4,2),VECTOR_A,r"\vec u"); x=arrow_from(ax,(3,5),VECTOR_B,r"\vec x"); self.play(GrowArrow(u[0]),Write(u[1]),GrowArrow(x[0]),Write(x[1]))
        line=ax.plot(lambda t:.5*t,x_range=[0,6],color=VECTOR_A); self.play(Create(line)); foot=Dot(ax.c2p(3.6,1.8),color=HIGHLIGHT); proj=arrow_from(ax,(3.6,1.8),HIGHLIGHT,r"\operatorname{proj}_{u}x"); perp=DashedLine(ax.c2p(3.6,1.8),ax.c2p(3,5),color=GREY_B); self.play(FadeIn(foot),GrowArrow(proj[0]),Write(proj[1]),Create(perp))
        form=MathTex(r"\operatorname{proj}_{u}(x)=\frac{x\cdot u}{u\cdot u}u").to_edge(RIGHT).shift(UP*1.4); self.play(Write(form)); self.wait(2)
        calc=MathTex(r"x=\begin{bmatrix}3\\5\end{bmatrix},\ u=\begin{bmatrix}4\\2\end{bmatrix}\Rightarrow\operatorname{proj}_{u}(x)=\frac{22}{20}\begin{bmatrix}4\\2\end{bmatrix}").scale(.7).to_edge(RIGHT); self.play(Write(calc)); self.wait(2)
        resid=MathTex(r"x-\operatorname{proj}_{u}(x)\ \perp\ u").scale(.9).to_edge(RIGHT).shift(DOWN*1.6); self.play(Write(resid)); self.wait(2)
        self.play(Write(explain(self,"Least squares generalizes this idea: when data do not fit a model exactly, choose the parameters that make the residual as small and orthogonal as possible.",3))); self.wait(3)

class Lesson09Rank(LessonScene):
    def construct(self):
        self.title("Lesson 09 — Linear Independence, Rank, and Null Space", "How much information does a matrix really contain?")
        A=Matrix([[1,2,3],[2,4,6],[1,1,1]]).scale(.85).to_edge(LEFT).shift(UP*.5); self.play(Write(A)); self.play(Write(MathTex("A").next_to(A,UP))); self.wait(1)
        rows=MathTex(r"R_2=2R_1").scale(.8).to_edge(RIGHT).shift(UP*1.7); self.play(Write(rows)); rank=MathTex(r"\operatorname{rank}(A)=2").scale(1).to_edge(RIGHT); self.play(Write(rank)); self.wait(2)
        null=MathTex(r"A\vec x=0").scale(1).to_edge(RIGHT).shift(DOWN*1.2); self.play(Write(null)); self.wait(2)
        self.play(Write(explain(self,"The rank counts independent directions in the column space. The null space contains inputs that the transformation sends to zero.",3))); self.wait(2)
        ax=Axes(x_range=[-4,4,1],y_range=[-4,4,1],x_length=6,y_length=6,axis_config={"include_numbers":True}).to_edge(RIGHT).shift(DOWN*.4); self.play(Create(ax)); line=ax.plot(lambda t:2*t,x_range=[-2,2],color=VECTOR_A); self.play(Create(line)); self.play(Write(Text("All multiples of a dependent vector form a line.",font_size=25,color=GREY_A).next_to(ax,DOWN))); self.wait(3)

class Lesson10Eigen(LessonScene):
    def construct(self):
        self.title("Lesson 10 — Eigenvalues & Eigenvectors", "Directions that survive a transformation")
        ax=NumberPlane(x_range=[-4,4,1],y_range=[-4,4,1],x_length=7,y_length=7,background_line_style={"stroke_opacity":.17}).to_edge(LEFT); self.play(Create(ax))
        A=MathTex(r"A=\begin{bmatrix}3&1\\0&2\end{bmatrix}").to_edge(RIGHT).shift(UP*1.5); self.play(Write(A))
        v=arrow_from(ax,(2,0),VECTOR_A,r"v_1"); w=arrow_from(ax,(0,2),VECTOR_B,r"v_2"); self.play(GrowArrow(v[0]),Write(v[1]),GrowArrow(w[0]),Write(w[1]))
        self.play(Write(explain(self,"An eigenvector changes only by a scalar factor: Av=lambda v. Its direction is preserved.",3))); self.play(ax.animate.apply_matrix([[3,1],[0,2]]),run_time=2)
        lam=MathTex(r"A\vec v_1=3\vec v_1,\qquad A\vec v_2=2\vec v_2").scale(.85).to_edge(RIGHT); self.play(Write(lam)); self.wait(2)
        char=MathTex(r"\det(A-\lambda I)=0").scale(1.05).to_edge(RIGHT).shift(DOWN*1.4); self.play(Write(char)); self.wait(2); diag=MathTex(r"A=PDP^{-1}").scale(1.05).to_edge(RIGHT).shift(DOWN*2.6); self.play(Write(diag)); self.wait(2)
        self.play(Write(Text("This is why eigen-analysis matters in dynamical systems, PCA, PageRank, and many ML methods.",font_size=25,color=YELLOW_B).to_edge(DOWN))); self.wait(3)

class Lesson11QuadraticForms(LessonScene):
    def construct(self):
        self.title("Lesson 11 — Symmetric Matrices & Quadratic Forms", "From xᵀAx to ellipses and curvature")
        ax=Axes(x_range=[-4,4,1],y_range=[-4,4,1],x_length=7,y_length=7,axis_config={"include_numbers":True}).to_edge(LEFT); self.play(Create(ax))
        A=MathTex(r"A=\begin{bmatrix}2&0\\0&1\end{bmatrix}").to_edge(RIGHT).shift(UP*1.5); q=MathTex(r"q(x)=x^TAx=2x^2+y^2").to_edge(RIGHT); self.play(Write(A),Write(q))
        ellipse=ax.plot_implicit(lambda x,y:2*x*x+y*y-4,color=VECTOR_A); self.play(Create(ellipse),run_time=2)
        self.play(Write(explain(self,"A symmetric matrix defines a quadratic form. Level sets of the form can reveal geometry such as ellipses and curvature.",3))); self.wait(2)
        eig=MathTex(r"\lambda_1=2,\quad\lambda_2=1").scale(.9).to_edge(RIGHT).shift(DOWN*1.4); self.play(Write(eig)); self.wait(2)
        self.play(Write(Text("Positive eigenvalues here mean the quadratic form is positive definite.",font_size=26,color=YELLOW_B).to_edge(DOWN))); self.wait(3)

class Lesson12SVD(LessonScene):
    def construct(self):
        self.title("Lesson 12 — Singular Value Decomposition", "Rotate → stretch → rotate")
        txt=MathTex(r"A=U\Sigma V^T").scale(1.2).to_edge(UP); self.play(Write(txt))
        left=NumberPlane(x_range=[-3,3,1],y_range=[-3,3,1],x_length=5,y_length=5,background_line_style={"stroke_opacity":.15}).to_edge(LEFT); right=NumberPlane(x_range=[-3,3,1],y_range=[-3,3,1],x_length=5,y_length=5,background_line_style={"stroke_opacity":.15}).to_edge(RIGHT); self.play(Create(left),Create(right))
        v=Arrow(left.c2p(0,0),left.c2p(2,1),buff=0,color=VECTOR_A,stroke_width=7); self.play(GrowArrow(v)); self.play(Write(explain(self,"SVD decomposes any real matrix into orthogonal directions and nonnegative stretches.",3)))
        labels=VGroup(MathTex("V^T"),MathTex("\\Sigma"),MathTex("U")).arrange(RIGHT).move_to(ORIGIN).shift(DOWN*.1); self.play(Write(labels)); self.wait(2)
        self.play(left.animate.rotate(PI/6),run_time=1.5); self.play(Transform(v,Arrow(left.c2p(0,0),left.c2p(2.7,.3),buff=0,color=VECTOR_A,stroke_width=7)),run_time=1.5); self.wait(1)
        self.play(right.animate.apply_matrix([[2,0],[0,.7]]),run_time=2); self.play(Write(MathTex(r"\sigma_1\ge\sigma_2\ge0").scale(.9).to_edge(DOWN))); self.wait(2)
        self.play(Write(Text("SVD powers compression, denoising, recommender systems, embeddings, and PCA.",font_size=27,color=YELLOW_B).to_edge(DOWN).shift(UP*.6))); self.wait(3)

class Lesson13PCA(LessonScene):
    def construct(self):
        self.title("Lesson 13 — PCA", "Finding the directions where data vary the most")
        ax=Axes(x_range=[-5,5,1],y_range=[-5,5,1],x_length=9,y_length=7,axis_config={"include_numbers":True}); self.play(Create(ax))
        pts=[(-3,-2),(-2,-1),(-1,-.4),(0,.2),(1,.7),(2,1.4),(3,2),(2.3,2.5),(-2.5,-.8)]; dots=VGroup(*[Dot(ax.c2p(x,y),radius=.07,color=VECTOR_A) for x,y in pts]); self.play(LaggedStart(*[FadeIn(d) for d in dots],lag_ratio=.08)); mean=Dot(ax.c2p(.2,.8),color=HIGHLIGHT,radius=.11); self.play(FadeIn(mean))
        self.play(Write(explain(self,"PCA first centers the data. Then it finds orthogonal directions ranked by variance.",3)))
        pc1=Arrow(ax.c2p(-3.2,-1.9),ax.c2p(3.3,2.4),buff=0,color=VECTOR_B,stroke_width=7); pc2=Arrow(ax.c2p(-1.7,3.6),ax.c2p(2.1,-2.2),buff=0,color=VECTOR_C,stroke_width=5); self.play(GrowArrow(pc1),GrowArrow(pc2))
        lab=MathTex(r"\text{PC}_1=\text{largest variance}").to_edge(UP).shift(DOWN*.7); self.play(Write(lab)); self.wait(2)
        cov=MathTex(r"C=\frac{1}{n-1}X_c^TX_c").scale(.9).to_edge(RIGHT).shift(DOWN*1); self.play(Write(cov)); self.wait(2)
        eig=MathTex(r"Cv_i=\lambda_i v_i,\quad \lambda_1\ge\lambda_2").scale(.75).to_edge(RIGHT).shift(DOWN*2.1); self.play(Write(eig)); self.wait(2)
        self.play(Write(Text("Projection onto the first components compresses data while preserving the dominant structure.",font_size=25,color=YELLOW_B).to_edge(DOWN))); self.wait(3)

class Lesson14Conditioning(LessonScene):
    def construct(self):
        self.title("Lesson 14 — Conditioning & Numerical Stability", "Why mathematically correct algorithms can still be numerically fragile")
        A=MathTex(r"A=\begin{bmatrix}1&1\\1&1.0001\end{bmatrix}").scale(1.0).move_to(LEFT*3); self.play(Write(A)); k=MathTex(r"\kappa(A)=\frac{\sigma_{\max}}{\sigma_{\min}}\gg1").scale(.9).move_to(RIGHT*2.5); self.play(Write(k)); self.wait(2)
        self.play(Write(explain(self,"A poorly conditioned matrix amplifies input errors. Small perturbations can create large changes in the solution.",3))); self.wait(2)
        x=MathTex(r"Ax=b,\qquad b\rightarrow b+\delta b").scale(.9).move_to(DOWN*.7); self.play(Write(x)); self.wait(2)
        err=MathTex(r"\frac{\|\delta x\|}{\|x\|}\ \lesssim\ \kappa(A)\frac{\|\delta b\|}{\|b\|}").scale(.85).to_edge(DOWN); self.play(Write(err)); self.wait(3)
        self.play(Write(Text("For AI: stable preprocessing, well-scaled features, and avoiding unnecessary matrix inverses matter.",font_size=26,color=YELLOW_B).to_edge(DOWN).shift(UP*.7))); self.wait(3)

class Lesson15LinearAlgebraForML(LessonScene):
    def construct(self):
        self.title("Lesson 15 — Linear Algebra in Machine Learning", "A synthesis: vectors → matrices → optimization → representations")
        flow=VGroup(MathTex(r"\text{data }x\in\mathbb R^d"),MathTex(r"\downarrow"),MathTex(r"\text{matrix }W"),MathTex(r"\downarrow"),MathTex(r"z=Wx+b"),MathTex(r"\downarrow"),MathTex(r"\text{loss }L(z,y)"),MathTex(r"\downarrow"),MathTex(r"\nabla_W L")).arrange(DOWN,buff=.25).scale(.82)
        self.play(LaggedStart(*[Write(m) for m in flow],lag_ratio=.12)); self.wait(2)
        ax=Axes(x_range=[-4,4,1],y_range=[-1,8,1],x_length=7,y_length=5,axis_config={"include_numbers":True}).to_edge(RIGHT); self.play(Create(ax)); g=ax.plot(lambda x:(x-1.2)**2+.6,x_range=[-2.5,3.5],color=VECTOR_A); dot=Dot(ax.c2p(3,3.84),color=HIGHLIGHT); self.play(Create(g),FadeIn(dot))
        self.play(Write(explain(self,"Gradient descent moves parameters in a direction that decreases the loss. The geometry underneath is linear algebra plus calculus.",3))); self.play(dot.animate.move_to(ax.c2p(1.2,.6)),run_time=2); self.wait(2)
        recap=VGroup(Text("You now have the core toolkit:",font_size=29),MathTex(r"\text{vectors, span, basis, matrices, systems, determinants}"),MathTex(r"\text{dot products, projections, rank, eigenvalues, SVD, PCA}"),Text("These are the coordinates behind modern ML.",font_size=29,color=YELLOW_B)).arrange(DOWN,buff=.3).scale(.78).move_to(LEFT*2+DOWN*.1)
        self.play(FadeOut(flow)); self.play(Write(recap)); self.wait(4)
