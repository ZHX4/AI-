# Part V — Geometry

Part V develops the geometric language of linear algebra from the dot product.

## Lessons

1. **Dot Product Computation** — component-wise multiplication and scalar output
2. **Geometric Meaning of the Dot Product** — projection and alignment
3. **Norm and Vector Length** — self-dot-product and generalized Pythagorean length
4. **Distance Between Points** — displacement followed by the norm
5. **Angles and Alignment** — cosine formula and Cauchy–Schwarz
6. **Orthogonality** — zero dot product and perpendicular directions
7. **Projection** — formula, exact numerical example, and closest point on a line
8. **Orthogonal Decomposition** — parallel plus perpendicular components
9. **Orthogonal Complements** — the complete set of directions perpendicular to a subspace
10. **Gram–Schmidt** — orthogonalization and normalization into an orthonormal basis
11. **Geometry Mastery** — a visual recap connecting all concepts

## Teaching pattern

Every lesson uses the course standard:

**intuition → geometric construction → CC explanation → algebra → worked example → interpretation → visual recap**

The lessons use explicit coordinate axes, vector arrows, projection shadows, line/subspace geometry, and long CC-style explanations intended to work as narration support or standalone captions.

## Exact examples used

- Dot product: `(3,1) · (1,2) = 5`
- Norm: `||(3,4)|| = 5`
- Distance from `(1,1)` to `(4,5)`: `5`
- Angle example: `(1,0)` and `(1,√3)` give `60°`
- Orthogonality: `(2,1) · (1,-2) = 0`
- Projection of `(3,2)` onto `span{(2,1)}`:
  `proj = (16/5, 8/5)`
- Orthogonal remainder: `(-1/5, 2/5)`
- Orthogonal complement of `span{(2,1)}`: `span{(1,-2)}`
- Gram–Schmidt from `(1,1)` and `(1,0)` gives
  `q1 = (1/√2)(1,1)` and `q2 = (1/√2)(1,-1)`

## Verification

Run:

```bash
uv run python verify_part5.py
```

The verifier checks the eleven scene classes, CC coverage, exact numerical geometry, the canonical renderer, and the absence of the superseded Part V source.
