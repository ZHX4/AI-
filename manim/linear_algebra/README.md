# Linear Algebra — Manim Visual Course

A long-form, first-principles linear algebra course for AI/ML students, built with Manim Community.

This project is a **visual textbook**, not a formula checklist. Each major idea receives its own animation, geometric interpretation, derivation, worked examples, conceptual recap, and CC-style on-screen explanations.

## Course architecture

The curriculum is organized into 13 parts:

1. **Foundations** — scalars, vectors, coordinates, operations, magnitude, linear combinations
2. **Vector Spaces** — span, independence, basis, dimension, subspaces, nonstandard coordinates, fundamental subspaces
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

Every lesson follows:

**intuition → geometric construction → CC explanation → algebra → worked example → interpretation → visual recap → transition**

CC-style text is part of the lesson itself. Captions explain what the viewer is seeing, why the next animation happens, and how the geometry corresponds to the equation. The target is that a lesson remains understandable even without spoken narration.

The visual language uses coordinate axes, labeled vectors, moving points, subspaces, transformed grids, highlighted equations, pauses for reasoning, and deliberate transitions. The teaching philosophy is inspired by high-quality visual mathematics without copying another creator's scripts, narration, or exact presentation.

## Part I status

Part I contains eight long-form lessons:

- `Part1_01_ScalarsAndVectors`
- `Part1_02_CoordinatesAndComponents`
- `Part1_03_VectorAddition`
- `Part1_04_VectorSubtraction`
- `Part1_05_ScalingAndUnitVectors`
- `Part1_06_MagnitudeAndDistance`
- `Part1_07_LinearCombinations`
- `Part1_08_FoundationsRecap`

See [`parts/PART_I_FOUNDATIONS.md`](parts/PART_I_FOUNDATIONS.md).

## Part II status

Part II contains eleven long-form lessons, all implemented in one canonical source file:

- `Part2_01_Span`
- `Part2_02_LinearDependence`
- `Part2_03_LinearIndependence`
- `Part2_04_Basis`
- `Part2_05_Dimension`
- `Part2_06_CoordinatesInANonstandardBasis`
- `Part2_07_Subspaces`
- `Part2_08_ColumnSpace`
- `Part2_09_RowSpaceAndNullSpace`
- `Part2_10_RankNullity`
- `Part2_11_FourFundamentalSubspaces`

See [`parts/PART_II_VECTOR_SPACES.md`](parts/PART_II_VECTOR_SPACES.md).

## Repository layout

```text
manim/linear_algebra/
├── course.py                              # initial 15-topic prototype
├── utils.py                               # shared animation/teaching helpers
├── render_all.py                          # prototype renderer
├── render_part1.py                        # authoritative Part I renderer
├── render_part2.py                        # authoritative Part II renderer
├── verify_part1.py                        # Part I source checks
├── verify_part2.py                        # Part II source checks
├── parts/
│   ├── __init__.py
│   ├── part_01_foundations_final.py
│   ├── PART_I_FOUNDATIONS.md
│   ├── part_02_vector_spaces.py           # canonical Part II source
│   └── PART_II_VECTOR_SPACES.md
├── .github/workflows/manim-linear-algebra.yml
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

Render Part I:

```bash
uv run python render_part1.py
```

Render Part II:

```bash
uv run python render_part2.py
```

Verify Part II source structure and regression checkpoints:

```bash
uv run python verify_part2.py
```

Generated media stays outside Git.

## Important distinction

The original `course.py` remains as the initial 15-topic prototype. The `parts/` structure is the **authoritative long-form curriculum** going forward. New parts must follow the deeper teaching standard above rather than adding shallow topic-level scenes.
