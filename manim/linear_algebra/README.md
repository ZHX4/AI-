# Linear Algebra — Manim Visual Course

A long-form, first-principles linear algebra course for AI/ML students, built with Manim Community.

This project is being developed as a **visual textbook**, not a formula checklist. Each major idea should receive its own animation, geometric interpretation, derivation, worked examples, conceptual recap, and CC-style on-screen explanations.

## Course architecture

The curriculum is organized into 13 parts:

1. **Foundations** — scalars, vectors, coordinates, operations, magnitude, linear combinations
2. **Vector Spaces** — span, independence, basis, dimension, subspaces, coordinates
3. **Matrices** — matrix-vector multiplication, matrix operations, composition, transpose, inverse
4. **Systems of Equations** — Ax=b, elimination, row operations, RREF, solution geometry
5. **Geometry** — dot products, angles, orthogonality, projections, Gram-Schmidt
6. **Determinants** — area/volume scaling, orientation, invertibility, determinant properties
7. **Fundamental Subspaces** — rank, nullity, column/row/null/left-null spaces, rank-nullity
8. **Eigenvalues** — eigenvectors, characteristic polynomial, multiplicities, diagonalization, powers
9. **Symmetric Matrices** — spectral theorem, orthogonal eigenvectors, quadratic forms, definiteness
10. **Decompositions** — LU, QR, change of basis, orthogonal matrices, linear operators
11. **SVD** — singular vectors, singular values, geometry, pseudoinverse, low-rank approximation
12. **PCA** — centering, covariance, variance, principal directions, projection, reconstruction
13. **Numerical + ML Connections** — conditioning, stability, least squares, regression, neural networks, embeddings

## Teaching standard

Every lesson should follow the pattern:

**intuition → geometric construction → algebra → worked example → generalization → visual recap**

CC-style text is part of the lesson itself. Captions should explain what the viewer is seeing, why the next animation happens, and how the geometry corresponds to the equation. The goal is that the lesson remains understandable even with no spoken narration.

The visual language should use coordinate axes, labeled vectors, moving points, transformed grids, highlighted equations, pauses for reasoning, and deliberate transitions. Avoid rushing from formula to formula.

The style should be inspired by the **teaching principles** of excellent mathematical animation—especially intuition, visualization, and gradual abstraction—without copying another creator's scripts, narration, or exact presentation.

## Part I status

Part I is the first rebuilt section and currently contains eight long-form lessons:

- `Part1_01_ScalarsAndVectors`
- `Part1_02_CoordinatesAndComponents`
- `Part1_03_VectorAddition`
- `Part1_04_VectorSubtraction`
- `Part1_05_ScalingAndUnitVectors`
- `Part1_06_MagnitudeAndDistance`
- `Part1_07_LinearCombinations`
- `Part1_08_FoundationsRecap`

See [`parts/PART_I_FOUNDATIONS.md`](parts/PART_I_FOUNDATIONS.md).

## Repository layout

```text
manim/linear_algebra/
├── course.py
├── utils.py
├── render_all.py
├── render_part1.py
├── parts/
│   ├── __init__.py
│   ├── part_01_foundations.py
│   └── PART_I_FOUNDATIONS.md
├── __init__.py
├── pyproject.toml
└── README.md
```

## Setup

The project targets **Manim Community 0.20.1**.

```bash
cd manim/linear_algebra
uv python install
uv sync
uv run manim checkhealth
```

Render a Part I lesson:

```bash
uv run manim -pqh render_part1.py Part1_01_ScalarsAndVectors
```

Render the whole Part I sequence with the commands listed in `parts/PART_I_FOUNDATIONS.md`.

Generated media stays outside Git.

## Important distinction

The original `course.py` is retained as the initial 15-topic prototype. The new `parts/` structure is the **authoritative long-form curriculum** going forward. New parts should be implemented to the deeper teaching standard above rather than simply adding another topic-level scene.
