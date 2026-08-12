# Linear Algebra — Manim Visual Course

A long-form, first-principles linear algebra course rendered with **Manim Community**.

The course is designed for an AI/ML student. Every lesson emphasizes coordinate geometry, explicit formulas, worked numerical examples, and animated transformations.

## Course sequence

| # | Lesson | Core ideas |
|---|---|---|
| 01 | Vectors | coordinates, displacement, magnitude, negation |
| 02 | Vector Operations | addition, subtraction, scalar multiplication, linear combinations |
| 03 | Span, Basis & Dimension | span, independence, basis, dimension |
| 04 | Matrices as Transformations | matrix action, basis vectors, shear, rotation |
| 05 | Matrix Multiplication & Systems | composition, Ax=b, geometric solution |
| 06 | Determinant & Inverse | area scaling, collapse, invertibility |
| 07 | Dot Product & Geometry | length, angle, orthogonality, normalization |
| 08 | Projection & Least Squares | closest point, residual, least-squares intuition |
| 09 | Rank & Null Space | independent information, rank, null space |
| 10 | Eigenvalues & Eigenvectors | invariant directions, characteristic equation, diagonalization |
| 11 | Symmetric Matrices & Quadratic Forms | xᵀAx, level sets, positive definiteness |
| 12 | SVD | orthogonal directions, singular values, rotation/stretch/rotation |
| 13 | PCA | centering, covariance, variance directions, dimensionality reduction |
| 14 | Conditioning & Numerical Stability | condition number, error amplification |
| 15 | Linear Algebra for ML | representations, layers, loss geometry, gradients |

## Repository layout

```text
manim/linear_algebra/
├── course.py          # all 15 lesson scenes
├── utils.py           # reusable teaching/animation primitives
├── render_all.py      # renders every lesson sequentially
├── pyproject.toml     # pins Manim Community 0.20.1
└── README.md
```

## Setup

The project targets **Manim Community 0.20.1**. The current Manim documentation recommends an isolated environment and specifically recommends `uv` for project dependency management.

```bash
cd manim/linear_algebra
uv python install
uv sync
uv run manim checkhealth
```

Render one lesson:

```bash
uv run manim -pqh course.py Lesson01Vectors
```

Examples:

```bash
uv run manim -pqh course.py Lesson08ProjectionLeastSquares
uv run manim -pqh course.py Lesson10Eigen
uv run manim -pqh course.py Lesson13PCA
```

Render the full course:

```bash
uv run python render_all.py
```

Rendered media is intentionally ignored by Git.

## Pedagogical order

vectors → linear combinations → span/basis → transformations → systems → inner products/projections → rank → eigenvectors → SVD/PCA → numerical stability → ML.

Each scene is deliberately longer than a short-form animation: it introduces the idea, constructs the geometry, shows the equations, works a numerical example, and then interprets the result.
