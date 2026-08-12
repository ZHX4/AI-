from manim import *

BG = "#0b1020"
TEXT = WHITE
ACCENT = BLUE_C
VECTOR_A = BLUE_C
VECTOR_B = YELLOW_C
VECTOR_C = GREEN_C
HIGHLIGHT = RED_C


class LessonScene(Scene):
    """Base scene for long-form, captioned mathematics lessons."""

    def setup(self):
        self.camera.background_color = BG

    def title(self, text, subtitle=None):
        t = Text(text, font_size=42, weight=BOLD).to_edge(UP)
        self.play(Write(t))
        if subtitle:
            s = Text(subtitle, font_size=23, color=GREY_B).next_to(t, DOWN, buff=0.16)
            self.play(FadeIn(s))
        self.wait(1)
        return VGroup(t, *([s] if subtitle else []))

    def cc(self, text, seconds=3.0, width=11.5, size=27):
        """Show a subtitle/closed-caption line, then return it for later cleanup."""
        caption = Text(
            text,
            font_size=size,
            color=GREY_A,
            line_spacing=0.9,
            margin=0.08,
        )
        caption.set_max_width(width)
        caption.to_edge(DOWN, buff=0.28)
        self.play(FadeIn(caption, shift=UP * 0.12), run_time=0.35)
        self.wait(seconds)
        return caption

    def beat(self, seconds=1.0):
        """A small pedagogical pause so viewers can process a construction."""
        self.wait(seconds)

    def emphasize(self, text, seconds=2.5):
        phrase = Text(text, font_size=30, color=WHITE)
        box = SurroundingRectangle(phrase, buff=0.25, corner_radius=0.12)
        group = VGroup(box, phrase).move_to([0, -1.6, 0])
        self.play(Create(box), Write(phrase))
        self.wait(seconds)
        return group


def plane(x_range=(-7, 7), y_range=(-4, 4), x_length=12, y_length=7):
    return NumberPlane(
        x_range=[x_range[0], x_range[1], 1],
        y_range=[y_range[0], y_range[1], 1],
        x_length=x_length,
        y_length=y_length,
        background_line_style={"stroke_opacity": 0.22},
        axis_config={"stroke_opacity": 0.75, "stroke_width": 2},
    )


def arrow_from(axes, coords, color=VECTOR_A, label=None, label_color=None):
    origin = axes.coords_to_point(0, 0)
    endpoint = axes.c2p(*coords)
    arr = Arrow(
        origin,
        endpoint,
        buff=0.0,
        color=color,
        stroke_width=7,
        max_tip_length_to_length_ratio=0.12,
    )
    if label:
        lab = MathTex(label, color=label_color or color, font_size=36).next_to(
            arr.get_end(), UR, buff=0.12
        )
        return VGroup(arr, lab)
    return arr


def coord_label(axes, coords, label, color=WHITE):
    return MathTex(label, color=color, font_size=30).next_to(
        axes.c2p(*coords), DOWN + LEFT, buff=0.08
    )


def section_text(text, y=2.6):
    return Text(text, font_size=28, color=GREY_B).move_to([0, y, 0])


def formula(text, scale=0.8):
    return MathTex(text).scale(scale)


def explain(scene, text, seconds=2.2):
    return scene.cc(text, seconds=seconds)


def component_guides(axes, x, y, color=GREY_B):
    """Dashed horizontal/vertical guides for a 2D vector endpoint."""
    return VGroup(
        DashedLine(axes.c2p(x, 0), axes.c2p(x, y), color=color, dash_length=0.12),
        DashedLine(axes.c2p(0, y), axes.c2p(x, y), color=color, dash_length=0.12),
    )


def coordinate_dot(axes, coords, color=HIGHLIGHT, radius=0.07):
    return Dot(axes.c2p(*coords), radius=radius, color=color)
