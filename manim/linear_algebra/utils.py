from manim import *

BG = "#0b1020"
TEXT = WHITE
ACCENT = BLUE_C
VECTOR_A = BLUE_C
VECTOR_B = YELLOW_C
VECTOR_C = GREEN_C
HIGHLIGHT = RED_C

class LessonScene(Scene):
    def setup(self):
        self.camera.background_color = BG

    def title(self, text, subtitle=None):
        t = Text(text, font_size=42, weight=BOLD).to_edge(UP)
        self.play(Write(t))
        if subtitle:
            s = Text(subtitle, font_size=24, color=GREY_B).next_to(t, DOWN, buff=0.18)
            self.play(FadeIn(s))
        self.wait(1)
        return VGroup(t, *([s] if subtitle else []))

def plane(x_range=(-7,7), y_range=(-4,4), x_length=12, y_length=7):
    return NumberPlane(
        x_range=[x_range[0], x_range[1], 1],
        y_range=[y_range[0], y_range[1], 1],
        x_length=x_length, y_length=y_length,
        background_line_style={"stroke_opacity": 0.22},
        axis_config={"stroke_opacity": 0.75, "stroke_width": 2},
    )

def arrow_from(axes, coords, color=VECTOR_A, label=None, label_color=None):
    a = axes.coords_to_point(0,0)
    b = axes.c2p(*coords)
    arr = Arrow(a, b, buff=0.0, color=color, stroke_width=7, max_tip_length_to_length_ratio=0.12)
    if label:
        lab = MathTex(label, color=label_color or color, font_size=36).next_to(arr.get_end(), UR, buff=0.12)
        return VGroup(arr, lab)
    return arr

def coord_label(axes, coords, label, color=WHITE):
    return MathTex(label, color=color, font_size=30).next_to(axes.c2p(*coords), DOWN+LEFT, buff=0.08)

def section_text(text, y=2.6):
    return Text(text, font_size=28, color=GREY_B).move_to([0,y,0])

def formula(text, scale=0.8):
    return MathTex(text).scale(scale)

def explain(scene, text, seconds=2.2):
    m=Text(text, font_size=27, color=GREY_A, line_spacing=0.8)
    m.to_edge(DOWN, buff=0.35)
    scene.play(FadeIn(m, shift=UP*0.15))
    scene.wait(seconds)
    return m
