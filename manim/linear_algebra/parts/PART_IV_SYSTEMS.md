# Part IV — Systems of Equations

Part IV turns matrix ideas into a systematic method for solving equations. The central object is

\[
A\vec x=\vec b.
\]

The lessons move from geometry to algebra and back again so that row reduction is understood as a structure-preserving transformation, not a collection of mechanical rules.

## Lessons

1. **Ax = b** — a system as one vector equation and as intersecting constraints.
2. **Geometric Meaning** — equations as lines and solution sets.
3. **Augmented Matrix** — compactly encoding coefficients and constants.
4. **Elementary Row Operations** — the three legal transformations and why they preserve solutions.
5. **Gaussian Elimination** — pivot creation, elimination, and triangular form.
6. **Back Substitution** — solving a triangular system from the bottom upward.
7. **RREF** — canonical reduced form and direct reading of solutions.
8. **Three Solution Cases** — unique solution, no solution, infinitely many solutions.
9. **Homogeneous Systems** — `Ax = 0` and the connection to null space.
10. **Full 3×3 Example** — a complete elimination workflow with verification.
11. **Systems Mastery** — the geometric and algebraic ideas unified.

## Teaching rhythm

Every lesson follows:

**question → visual geometry → CC explanation → algebra → worked example → interpretation → recap**

The CC is part of the lesson and is designed to remain understandable when the animation is muted.

## Core numerical examples

### 2×2 system

\[
\begin{cases}
x+y=5\\
2x-y=1
\end{cases}
\qquad\Longrightarrow\qquad
(x,y)=(2,3).
\]

### Gaussian elimination

\[
\left[\begin{array}{cc|c}
1&1&5\\
2&-1&1
\end{array}\right]
\xrightarrow{R_2\leftarrow R_2-2R_1}
\left[\begin{array}{cc|c}
1&1&5\\
0&-3&-9
\end{array}\right].
\]

### 3×3 system

\[
\begin{cases}
x+y+z=6\\
2x-y+z=3\\
x+2y-z=2
\end{cases}
\qquad\Longrightarrow\qquad
(x,y,z)=(1,2,3).
\]

## Rendering

From `manim/linear_algebra`:

```bash
uv run python render_part4.py
```

Source and mathematical verification:

```bash
uv run python verify_part4.py
```

The authoritative source is `parts/part_04_systems_final.py`.
