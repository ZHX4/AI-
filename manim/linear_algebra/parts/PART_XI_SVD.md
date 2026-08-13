# Part XI — Singular Value Decomposition

## Teaching goal

Explain SVD as a geometric and computational decomposition rather than a formula to memorize.

## Lessons

1. **SVD Intuition** — one matrix as orthogonal change → diagonal stretching → orthogonal change.
2. **Singular Values from AᵀA** — eigenvalues of AᵀA are squared singular values.
3. **Right Singular Vectors** — eigenvectors of AᵀA define input directions.
4. **Left Singular Vectors** — normalized images of right singular vectors define output directions.
5. **Assembling UΣVᵀ** — reconstruct the exact matrix.
6. **Sphere to Ellipse** — singular values become ellipse semiaxis lengths.
7. **Singular Values and Stretching** — operator norm and extremal stretch.
8. **Rank and Zero Singular Values** — zeros reveal annihilated directions and rank deficiency.
9. **Moore–Penrose Pseudoinverse** — invert nonzero singular values and preserve the correct null-space behavior.
10. **Low-Rank Approximation** — keep the largest singular components and quantify the error.
11. **SVD Mastery** — connect geometry, rank, inversion, and compression.

## Canonical example

\[
A=\begin{bmatrix}0&-1\\3&0\end{bmatrix}
\]

with

\[
U=\begin{bmatrix}0&-1\\1&0\end{bmatrix},\quad
\Sigma=\begin{bmatrix}3&0\\0&1\end{bmatrix},\quad
V=I.
\]

Thus

\[
A=U\Sigma V^T,
\qquad
A^+ = V\Sigma^+U^T
=\begin{bmatrix}0&\frac13\\-1&0\end{bmatrix}.
\]

## Teaching standard

Every lesson follows:

**intuition → geometry → CC explanation → algebra → exact worked example → interpretation → recap → transition**

The visual target is a long-form lesson where captions explain the reason for each mathematical transition.
