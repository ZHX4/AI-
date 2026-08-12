# Part III — Matrices

Part III turns the vector ideas from Parts I–II into a complete geometric and algebraic language for matrices.

## Lessons

1. **What Is a Matrix?** — dimensions, rows, columns, input/output spaces.
2. **Matrix–Vector Multiplication** — row-dot-product interpretation and `Ax` as a vector-to-vector rule.
3. **Columns Build the Output** — `Ax` as a weighted combination of matrix columns.
4. **Matrix as a Transformation** — basis vectors, deformed grids, and the geometric meaning of columns.
5. **Matrix Addition and Scaling** — entrywise addition and scalar multiplication.
6. **Matrix Multiplication** — row-by-column multiplication and dimension compatibility.
7. **Composition of Transformations** — `AB` as sequential application and why order matters.
8. **Identity Matrix** — the neutral transformation.
9. **Transpose** — rows becoming columns and reversal of multiplication order.
10. **Inverse Matrix** — the transformation that undoes an invertible transformation.
11. **Matrix Mastery** — integrated visual recap and transition to systems of equations.

## Teaching rhythm

Every lesson follows:

**question → geometry → CC explanation → algebra → worked example → interpretation → recap → connection forward**

The lessons use coordinate axes, labeled vectors, explicit numerical examples, highlighted equations, and persistent closed-caption-style explanations. The captions are written as the lesson's written narration, so the reasoning remains intelligible with audio muted.

## Mathematical checkpoints

The course includes explicit regression checks for:

- `[[2,1],[1,2]] [3,1]^T = [7,5]^T`
- `3[2,1]^T + [1,2]^T = [7,5]^T`
- `[[1,2],[0,1]][[2,1],[1,0]] = [[4,1],[1,0]]`
- For `A=[[1,1],[0,1]]`, `B=[[0,-1],[1,0]]`, and `v=[2,1]^T`: `Bv=[-1,2]^T`, `ABv=[1,2]^T`, `BAv=[-1,3]^T`
- `[[2,1],[1,1]] [[1,-1],[-1,2]] = I`

Determinant theory and full system-solving are intentionally reserved for later parts of the curriculum.

## Rendering

From `manim/linear_algebra`:

```bash
uv run python render_part3.py
```

Source verification:

```bash
uv run python verify_part3.py
```
