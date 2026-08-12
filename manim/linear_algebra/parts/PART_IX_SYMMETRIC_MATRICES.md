# Part IX — Symmetric Matrices

Part IX is the bridge between eigenvalue theory and quadratic-form geometry.

## Lessons

1. Symmetry Intuition — `A = A^T`
2. Orthogonal Eigenvectors — distinct eigenvalues give orthogonal eigendirections
3. Spectral Theorem — `A = QΛQ^T`
4. Building `Q` and `Λ` — normalize eigenvectors and construct an orthogonal basis
5. Quadratic Forms — `q(x)=x^T A x`
6. Principal Axes — rotate into eigenvector coordinates
7. Rayleigh Quotient — eigenvalues as extremal values
8. Positive Definite Matrices
9. Negative Definite and Indefinite Matrices
10. Semidefinite Matrices and Eigenvalue Tests
11. Symmetric Matrix Mastery

## Canonical examples

Primary symmetric matrix:

`A = [[3,1],[1,3]]`

Eigenvalues:

`4, 2`

Orthonormal eigenvectors:

`q1 = (1/sqrt(2))(1,1)`

`q2 = (1/sqrt(2))(1,-1)`

Spectral decomposition:

`A = Q Λ Q^T`

Quadratic form:

`q(x,y) = 3x^2 + 2xy + 3y^2`

Principal-axis form:

`q = 4u^2 + 2v^2`

The principal-axis lesson uses `4u^2 + 2v^2 = 1`, whose full axis lengths are `1` and `sqrt(2)`.

## Teaching standard

Every scene follows the course standard:

**intuition → geometric construction → CC explanation → algebra → worked example → interpretation → recap**

The emphasis is on understanding why symmetric matrices are especially well behaved: orthogonal eigenvectors, orthogonal diagonalization, principal axes, and complete definiteness classification from eigenvalue signs.
