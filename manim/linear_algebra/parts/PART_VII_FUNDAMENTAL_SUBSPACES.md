# Part VII — Fundamental Subspaces

Part VII turns the matrix into a structural map. One concrete matrix is used repeatedly so the viewer can see how rank, pivots, column space, row space, null space, left null space, rank–nullity, and orthogonality are different views of the same object.

Canonical matrix:

\[
A=\begin{bmatrix}
1&2&3\\
0&1&1\\
1&3&4
\end{bmatrix}
\]

Key exact facts:

\[
r_3=r_1+r_2,\qquad c_3=c_1+c_2,
\]
\[
\operatorname{rank}(A)=2,
\]
\[
\operatorname{Null}(A)=\operatorname{span}\left\{\begin{bmatrix}-1\\-1\\1\end{bmatrix}\right\},
\]
\[
\operatorname{Null}(A^T)=\operatorname{span}\left\{\begin{bmatrix}-1\\-1\\1\end{bmatrix}\right\},
\]
\[
\operatorname{rank}(A)+\operatorname{nullity}(A)=2+1=3.
\]

## Lessons

1. **Rank Intuition** — independent directions versus redundancy.
2. **Column Space** — all reachable outputs and its dimension.
3. **Row Space** — independent row directions and its connection to \(\operatorname{Col}(A^T)\).
4. **Null Space** — solving \(Ax=0\) and interpreting invisible input directions.
5. **Left Null Space** — solving \(A^Ty=0\) and interpreting row dependencies.
6. **Four Fundamental Subspaces** — how the four spaces divide the input/output structure.
7. **Rank, Pivots, and Independent Directions** — RREF, pivot columns, and column-space bases.
8. **Rank–Nullity Theorem** — visible plus invisible input dimensions.
9. **Orthogonality Pairs** — \(\operatorname{Null}(A)=\operatorname{Row}(A)^\perp\) and \(\operatorname{Null}(A^T)=\operatorname{Col}(A)^\perp\).
10. **Dimensions and Structure** — the four dimension formulas for an \(m\times n\) matrix of rank \(r\).
11. **Fundamental Subspaces Mastery** — complete structural synthesis.

Every lesson follows the course standard:

**intuition → geometric construction → CC explanation → algebra → worked example → interpretation → visual recap → transition**
