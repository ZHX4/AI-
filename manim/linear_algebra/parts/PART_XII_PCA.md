# Part XII — Principal Component Analysis

11 lessons: PCA intuition; centering; covariance; principal directions; maximum variance; projection; reconstruction; explained variance; PCA from SVD; higher-dimensional PCA; mastery.

Canonical dataset:
\[
q_1=\frac1{\sqrt2}(1,1)^T,\quad q_2=\frac1{\sqrt2}(1,-1)^T,
\]
with observations \(\{\pm\sqrt3 q_1,\pm q_2\}\). The population-style covariance convention is used throughout:
\[
C=\frac1nX_c^TX_c=\begin{bmatrix}1&\frac12\\\frac12&1\end{bmatrix}.
\]
Hence
\[
Cq_1=\frac32q_1,\qquad Cq_2=\frac12q_2,
\]
so PC1 explains \(\frac{3/2}{2}=75\%\) of the variance. The first-PC reconstruction has mean squared squared-error \(1/2\).

The chapter explicitly uses \(1/n\); using \(1/(n-1)\) changes only the eigenvalue scale, not the principal directions.
