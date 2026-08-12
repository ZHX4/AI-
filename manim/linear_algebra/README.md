# Linear Algebra — Manim Visual Course

A long-form, first-principles linear algebra course for AI/ML students, built with Manim Community.

This project is a **visual textbook**, not a formula checklist. Each major idea receives its own animation, geometric interpretation, derivation, worked examples, conceptual recap, and CC-style on-screen explanations.

## Course architecture

The curriculum is organized into 13 parts:

1. **Foundations** — scalars, vectors, coordinates, operations, magnitude, linear combinations
2. **Vector Spaces** — span, independence, basis, dimension, subspaces, nonstandard coordinates, fundamental subspaces
3. **Matrices** — matrix structure, matrix-vector multiplication, columns, transformations, addition/scaling, multiplication, composition, identity, transpose, inverse
4. **Systems of Equations** — Ax=b, geometric constraints, augmented matrices, row operations, Gaussian elimination, back substitution, RREF, solution cases
5. **Geometry** — dot products, norms, distance, angles, orthogonality, projections, orthogonal complements, Gram-Schmidt
6. **Determinants** — signed area/volume, orientation, determinant properties, row operations, cofactor expansion, invertibility
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

Part II contains eleven long-form lessons in `parts/part_02_vector_spaces.py`. See [`parts/PART_II_VECTOR_SPACES.md`](parts/PART_II_VECTOR_SPACES.md).

## Part III status

Part III contains eleven long-form lessons in `parts/part_03_matrices_final.py`. See [`parts/PART_III_MATRICES.md`](parts/PART_III_MATRICES.md).

## Part IV status

Part IV contains eleven long-form lessons in `parts/part_04_systems_final.py`. See [`parts/PART_IV_SYSTEMS.md`](parts/PART_IV_SYSTEMS.md).

## Part V status

Part V contains eleven long-form geometry lessons in `parts/part_05_geometry_final.py`. See [`parts/PART_V_GEOMETRY.md`](parts/PART_V_GEOMETRY.md).

## Part VI status

Part VI contains eleven long-form determinant lessons in `parts/part_06_determinants_canonical.py`:

- `Part6_01_WhatDeterminantMeasures`
- `Part6_02_TwoByTwoSignedArea`
- `Part6_03_DeterminantAsAreaScale`
- `Part6_04_ThreeByThreeVolume`
- `Part6_05_OrientationAndSign`
- `Part6_06_DeterminantProperties`
- `Part6_07_RowOperationsAndDeterminant`
- `Part6_08_CofactorExpansion`
- `Part6_09_DeterminantAndInvertibility`
- `Part6_10_DeterminantAndProducts`
- `Part6_11_DeterminantMastery`

See [`parts/PART_VI_DETERMINANTS.md`](parts/PART_VI_DETERMINANTS.md). The older `part_06_determinants_final.py` path is retained only as a compatibility shim.

## Repository layout

```text
manim/linear_algebra/
├── course.py                              # initial 15-topic prototype
├── utils.py                               # shared animation/teaching helpers
├── render_all.py                          # prototype renderer
├── render_part1.py                        # authoritative Part I renderer
├── render_part2.py                        # authoritative Part II renderer
├── render_part3.py                        # authoritative Part III renderer
├── render_part4.py                        # authoritative Part IV renderer
├── render_part5.py                        # authoritative Part V renderer
├── render_part6.py                        # authoritative Part VI renderer
├── verify_part1.py                        # Part I source checks
├── verify_part2.py                        # Part II source checks
├── verify_part3.py                        # Part III source checks
├── verify_part4.py                        # Part IV source checks
├── verify_part5.py                        # Part V source checks
├── verify_part6.py                        # Part VI source checks
├── parts/
│   ├── __init__.py
│   ├── part_01_foundations_final.py
│   ├── PART_I_FOUNDATIONS.md
│   ├── part_02_vector_spaces.py
│   ├── PART_II_VECTOR_SPACES.md
│   ├── part_03_matrices_final.py
│   ├── PART_III_MATRICES.md
│   ├── part_04_systems_final.py
│   ├── PART_IV_SYSTEMS.md
│   ├── part_05_geometry_final.py
│   ├── PART_V_GEOMETRY.md
│   ├── part_06_determinants_canonical.py
│   ├── part_06_determinants_final.py  # compatibility shim
│   └── PART_VI_DETERMINANTS.md
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

Render Part VI:

```bash
uv run python render_part6.py
```

Verify Part VI:

```bash
uv run python verify_part6.py
```

Generated media stays outside Git.

## Important distinction

The original `course.py` remains as the initial 15-topic prototype. The `parts/` structure is the **authoritative long-form curriculum** going forward. New parts must follow the deeper teaching standard above rather than adding shallow topic-level scenes.
