# Part XIII — Numerical Linear Algebra + Machine Learning

Part XIII closes the course by connecting the mathematical structures developed in Parts I–XII to reliable computation and modern ML workflows.

## Lessons

1. Numerical Linear Algebra — exact mathematics versus finite computation.
2. Conditioning — problem sensitivity and condition numbers.
3. Floating-Point Error — representation, rounding, and cancellation.
4. Stable Algorithms — pivoting, QR, SVD, and algorithmic stability.
5. Least Squares — projection, residual orthogonality, and closest fits.
6. Normal Equations vs QR — equivalent goals with different numerical behavior.
7. Linear Regression — least squares as an ML training objective.
8. Gradient Descent — iterative optimization of a quadratic objective.
9. Neural Networks — matrix layers, biases, and nonlinearities.
10. Embeddings and Similarity — vector representations and cosine geometry.
11. Numerical + ML Mastery — synthesis from linear algebra to ML systems.

## Teaching standard

Every scene follows the course pattern:

**intuition → geometry → CC explanation → algebra → exact example → interpretation → recap**

The chapter deliberately distinguishes:

- the mathematical conditioning of a problem;
- the numerical stability of an algorithm;
- the effect of finite precision;
- the ML objective being optimized.

## Exact regression examples

The verifier uses:

\[
A=\operatorname{diag}(1,10^{-3}),\qquad \kappa_2(A)=10^3,
\]

and the regression design matrix

\[
X=\begin{bmatrix}1&0\\1&2\\1&4\end{bmatrix},
\qquad
y=\begin{bmatrix}1\\2\\3\end{bmatrix},
\]

whose least-squares solution is

\[
\hat\beta=\begin{bmatrix}1\\\frac12\end{bmatrix}.
\]

For the squared-loss objective,

\[
\nabla L(\beta)=2X^T(X\beta-y),
\]

and at \(\beta=0\),

\[
\nabla L(0)=\begin{bmatrix}-12\\-16\end{bmatrix}.
\]

The gradient-descent visualization uses

\[
J(\theta)=(\theta-0.5)^2+0.5
\]

with \(\eta=0.3\), producing the checked sequence

\[
\theta_0=-1.2,\quad \theta_1=-0.42,\quad \theta_2=0.132.
\]

## Repository commands

Render all Part XIII scenes:

```bash
uv run python render_part13.py
```

Verify the mathematics and wiring:

```bash
uv run python verify_part13.py
```
