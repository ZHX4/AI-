# Part VI — Determinants

Part VI develops determinants as a geometric and algebraic concept rather than as a formula to memorize.

## Lessons

1. What a determinant measures
2. The 2×2 determinant and signed area
3. Determinant as an area scale factor
4. The 3×3 determinant and signed volume
5. Orientation and the sign
6. Determinant properties
7. Row operations and determinant
8. Cofactor expansion
9. Determinant and invertibility
10. Determinants of products
11. Determinant mastery

## Teaching standard

Each scene follows the course standard:

**intuition → geometric construction → CC explanation → equation → worked example → interpretation → recap**

The central mental model is:

\[
\det(A)=\text{oriented volume scale factor}.
\]

In 2D this is signed area; in 3D it is signed volume. The absolute value gives the size scale, the sign records orientation, and zero means that dimension has collapsed.

## Verification

```bash
uv run python verify_part6.py
```

## Rendering

```bash
uv run python render_part6.py
```

The authoritative source is `parts/part_06_determinants_final.py`.
