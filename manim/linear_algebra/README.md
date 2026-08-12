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
7. **Fundamental Subspaces** — rank, pivots, column/row/null/left-null spaces, rank-nullity, orthogonality pairs
8. **Eigenvalues** — eigenvectors, characteristic polynomial, eigenspaces, multiplicities, diagonalization, powers, dynamical behavior
9. **Symmetric Matrices** — spectral theorem, orthogonal eigenvectors, quadratic forms, principal axes, Rayleigh quotient, definiteness
10. **Decompositions** — LU, QR, change of basis, orthogonal matrices, linear operators
11. **SVD** — singular vectors, singular values, geometry, pseudoinverse, low-rank approximation
12. **PCA** — centering, covariance, variance, principal directions, projection, reconstruction
13. **Numerical + ML Connections** — conditioning, stability, least squares, regression, neural networks, embeddings

## Teaching standard

Every lesson follows:

**intuition → geometric construction → CC explanation → algebra → worked example → interpretation → visual recap → transition**

CC-style text is part of the lesson itself. Captions explain what the viewer is seeing, why the next animation happens, and how the geometry corresponds to the equation. The target is that a lesson remains understandable even without spoken narration.

The visual language uses coordinate axes, labeled vectors, moving points, subspaces, transformed grids, highlighted equations, pauses for reasoning, and deliberate transitions. The teaching philosophy is inspired by high-quality visual mathematics without copying another creator's scripts, narration, or exact presentation.

## Part I–VIII status

Parts I–VIII are implemented as the authoritative long-form curriculum. Each has its own renderer, verifier, curriculum document, and CI coverage.

## Part IX status

Part IX contains eleven long-form symmetric-matrix lessons in `parts/part_09_symmetric_matrices_final.py`:

- `Part9_01_SymmetryIntuition`
- `Part9_02_OrthogonalEigenvectors`
- `Part9_03_SpectralTheorem`
- `Part9_04_BuildingQAndLambda`
- `Part9_05_QuadraticForms`
- `Part9_06_PrincipalAxes`
- `Part9_07_RayleighQuotient`
- `Part9_08_PositiveDefinite`
- `Part9_09_NegativeAndIndefinite`
- `Part9_10_SemidefiniteAndTests`
- `Part9_11_SymmetricMatrixMastery`

See [`parts/PART_IX_SYMMETRIC_MATRICES.md`](parts/PART_IX_SYMMETRIC_MATRICES.md).

## Repository layout

```text
manim/linear_algebra/
├── course.py
├── utils.py
├── render_all.py
├── render_part1.py ... render_part9.py
├── verify_part1.py ... verify_part9.py
├── parts/
│   ├── part_01_foundations_final.py
│   ├── part_02_vector_spaces.py
│   ├── part_03_matrices_final.py
│   ├── part_04_systems_final.py
│   ├── part_05_geometry_final.py
│   ├── part_06_determinants_canonical.py
│   ├── part_07_fundamental_subspaces_canonical.py
│   ├── part_08_eigenvalues_canonical.py
│   ├── part_09_symmetric_matrices_final.py
│   ├── PART_I_FOUNDATIONS.md
│   ├── PART_II_VECTOR_SPACES.md
│   ├── PART_III_MATRICES.md
│   ├── PART_IV_SYSTEMS.md
│   ├── PART_V_GEOMETRY.md
│   ├── PART_VI_DETERMINANTS.md
│   ├── PART_VII_FUNDAMENTAL_SUBSPACES.md
│   ├── PART_VIII_EIGENVALUES.md
│   └── PART_IX_SYMMETRIC_MATRICES.md
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

Render Part IX:

```bash
uv run python render_part9.py
```

Verify Part IX:

```bash
uv run python verify_part9.py
```

Generated media stays outside Git.

## Important distinction

The original `course.py` remains as the initial prototype. The `parts/` structure is the **authoritative long-form curriculum** going forward. New parts must follow the deeper teaching standard above rather than adding shallow topic-level scenes.
