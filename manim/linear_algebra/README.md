# Linear Algebra — Manim Visual Course

A long-form, first-principles linear algebra course for AI/ML students, built with Manim Community.

This project is a **visual textbook**, not a formula checklist. Each major idea receives its own animation, geometric interpretation, derivation, worked examples, conceptual recap, and CC-style on-screen explanations.

## Course architecture

The curriculum is organized into 13 parts:

1. **Foundations** — scalars, vectors, coordinates, operations, magnitude, linear combinations
2. **Vector Spaces** — span, independence, basis, dimension, subspaces, nonstandard coordinates, fundamental subspaces
3. **Matrices** — matrix structure, matrix-vector multiplication, columns, transformations, addition/scaling, multiplication, composition, identity, transpose, inverse
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

Every lesson follows:

**intuition → geometric construction → CC explanation → algebra → worked example → interpretation → visual recap → transition**

CC-style text is part of the lesson itself. Captions explain what the viewer is seeing, why the next animation happens, and how the geometry corresponds to the equation. The target is that a lesson remains understandable even without spoken narration.

The visual language uses coordinate axes, labeled vectors, moving points, subspaces, transformed grids, highlighted equations, pauses for reasoning, and deliberate transitions. The teaching philosophy is inspired by high-quality visual mathematics without copying another creator's scripts, narration, or exact presentation.

## Part I status

Part I contains eight long-form lessons. See [`parts/PART_I_FOUNDATIONS.md`](parts/PART_I_FOUNDATIONS.md).

## Part II status

Part II contains eleven long-form lessons, all implemented in one canonical source file `parts/part_02_vector_spaces.py`. See [`parts/PART_II_VECTOR_SPACES.md`](parts/PART_II_VECTOR_SPACES.md).

## Part III status

Part III contains eleven long-form lessons, all implemented in one canonical source file `parts/part_03_matrices_final.py`:

- `Part3_01_WhatIsAMatrix`
- `Part3_02_MatrixVectorMultiplication`
- `Part3_03_ColumnsBuildTheOutput`
- `Part3_04_MatrixAsTransformation`
- `Part3_05_MatrixAdditionAndScaling`
- `Part3_06_MatrixMultiplication`
- `Part3_07_CompositionOfTransformations`
- `Part3_08_IdentityMatrix`
- `Part3_09_Transpose`
- `Part3_10_InverseMatrix`
- `Part3_11_MatrixMastery`

See [`parts/PART_III_MATRICES.md`](parts/PART_III_MATRICES.md).

## Repository layout

```text
manim/linear_algebra/
├── course.py                              # initial 15-topic prototype
├── utils.py                               # shared animation/teaching helpers
├── render_all.py                          # prototype renderer
├── render_part1.py                        # authoritative Part I renderer
├── render_part2.py                        # authoritative Part II renderer
├── render_part3.py                        # authoritative Part III renderer
├── verify_part1.py                        # Part I source checks
├── verify_part2.py                        # Part II source checks
├── verify_part3.py                        # Part III source checks
├── parts/
│   ├── __init__.py
│   ├── part_01_foundations_final.py
│   ├── PART_I_FOUNDATIONS.md
│   ├── part_02_vector_spaces.py
│   ├── PART_II_VECTOR_SPACES.md
│   ├── part_03_matrices_final.py
│   └── PART_III_MATRICES.md
├── .github/workflows/manim-linear-algebra.yml
├── __init__.py
├── pyproject.toml
└── README.md
```

## Setup

The project targets **Manim Community 0.20.1**. Current Manim Community documentation provides the `Matrix`, `ApplyMatrix`, `Arrow`, and coordinate-system APIs used by the course. citeturn722788search7turn722788search0turn722788search10turn279489search9

```bash
cd manim/linear_algebra
uv python install
uv sync
uv run manim checkhealth
```

Render Part I:

```bash
uv run python render_part1.py
```

Render Part II:

```bash
uv run python render_part2.py
```

Render Part III:

```bash
uv run python render_part3.py
```

Verify Part II:

```bash
uv run python verify_part2.py
```

Verify Part III:

```bash
uv run python verify_part3.py
```

Generated media stays outside Git.

## Important distinction

The original `course.py` remains as the initial 15-topic prototype. The `parts/` structure is the **authoritative long-form curriculum** going forward. New parts must follow the deeper teaching standard above rather than adding shallow topic-level scenes.
