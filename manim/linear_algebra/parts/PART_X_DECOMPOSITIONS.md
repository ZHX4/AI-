# Part X — Decompositions

Part X explains how linear algebra objects can be rewritten as simpler, interpretable pieces.

## Lessons

1. Change of Basis Intuition — a vector stays fixed while coordinates change.
2. Coordinate Transformations — forward and inverse basis-coordinate maps.
3. Similarity Transformations — the same linear operator represented in another basis.
4. Orthogonal Matrices — rotations/reflections and preservation of Euclidean geometry.
5. LU Factorization — elimination stored as triangular factors.
6. Solving Systems with LU — forward substitution followed by back substitution.
7. QR Factorization — orthonormal columns and an upper-triangular coordinate matrix.
8. QR Geometry — the geometric meaning of Q and R.
9. Linear Operators — the abstract rule behind a matrix representation.
10. Decomposition Comparison — when each factorization is useful.
11. Decompositions Mastery — synthesis and transition to later numerical methods.

## Canonical worked examples

### Change of basis

\[
B=\begin{bmatrix}1&1\\1&-1\end{bmatrix},\qquad
B^{-1}=\frac12\begin{bmatrix}1&1\\1&-1\end{bmatrix}.
\]

### LU

\[
A=\begin{bmatrix}4&3\\6&3\end{bmatrix}
=\begin{bmatrix}1&0\\\frac32&1\end{bmatrix}
\begin{bmatrix}4&3\\0&-\frac32\end{bmatrix}.
\]

For
\[
b=\begin{bmatrix}10\\12\end{bmatrix},
\]
the triangular solves give
\[
y=\begin{bmatrix}10\\-3\end{bmatrix},\qquad
x=\begin{bmatrix}1\\2\end{bmatrix}.
\]

### QR

\[
A=\begin{bmatrix}1&1\\1&0\end{bmatrix}=QR,
\]
where
\[
Q=\frac1{\sqrt2}\begin{bmatrix}1&1\\1&-1\end{bmatrix},\qquad
R=\begin{bmatrix}\sqrt2&\frac1{\sqrt2}\\0&\frac1{\sqrt2}\end{bmatrix}.
\]

The source verifier checks these identities exactly up to floating-point tolerance.
