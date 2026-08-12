# Part I — Foundations

Part I is the first complete teaching unit of the visual linear algebra course. It is deliberately slow and explanatory: intuition comes first, the geometry is constructed on screen, the algebra is introduced when it becomes necessary, and each lesson contains a concrete numerical example.

Every lesson uses **CC-style on-screen explanation text**. The CC is written as lesson narration, not as a label: it explains what the viewer should notice, why the step works, and what concept it prepares for next.

## Lessons

### I.1 — Scalars vs Vectors
- scalar quantities versus directional quantities
- magnitude and direction
- displacement as the core vector interpretation
- translating a vector without changing the vector
- why vectors describe changes rather than locations

### I.2 — Coordinates and Components
- coordinate axes and component interpretation
- x/y components
- column-vector notation
- negative components
- coordinates as a representation relative to a coordinate system

### I.3 — Vector Addition
- combining displacements
- tip-to-tail construction
- parallelogram construction
- componentwise addition
- geometric and algebraic agreement

### I.4 — Vector Subtraction
- difference as a displacement between endpoints
- componentwise subtraction
- opposite vectors
- subtraction as addition of an inverse

### I.5 — Scaling and Unit Vectors
- positive scalar multiplication
- shrinking and stretching
- negative scalar multiplication and direction reversal
- magnitude under scaling
- normalization
- unit vectors and why direction-only representations matter

### I.6 — Magnitude and Distance
- vector norm from the Pythagorean theorem
- a complete 3-4-5 numerical example
- distance between arbitrary points
- the difference vector as the bridge from points to vectors

### I.7 — Linear Combinations
- scaling several vectors
- tip-to-tail construction of a combination
- componentwise calculation
- a bounded worked example that stays inside the axes
- why linear combinations lead directly to span and basis

### I.8 — Vector Algebra and Mastery
- commutativity
- associativity
- additive identity and inverse
- distributivity over vector addition
- scalar distributivity
- a complete worked combination: `2a - b`
- final conceptual bridge to vector spaces

## Lesson design standard

Every lesson follows the same teaching rhythm:

1. **Question / motivation** — what problem are we trying to represent?
2. **Geometric construction** — show the idea with axes, arrows, points, or transformations.
3. **CC explanation** — explain the visual change in complete sentences.
4. **Equation** — introduce the symbolic form only after the visual meaning is established.
5. **Worked example** — calculate with explicit numerical values.
6. **Interpretation** — connect the calculation back to the geometry.
7. **Transition** — explain why the current idea is needed for the next part.

The course is inspired by the broader philosophy of visual mathematics: build intuition first, use animation to expose structure, and let equations explain the geometry rather than replace it. It does not copy another creator's scripts, narration, or exact presentation.

## Rendering

From `manim/linear_algebra`:

```bash
uv run manim -pqh parts/part_01_foundations.py Part1_01_ScalarsAndVectors
```

Render all eight lessons:

```bash
uv run python render_part1.py
```

Individual scenes can also be rendered directly with Manim by using their class names.

## Quality requirements

- Keep all important geometric objects inside the visible coordinate range.
- Use explicit numerical examples rather than only symbolic formulas.
- Do not introduce a formula without explaining the geometric meaning behind it.
- Use CC text frequently enough that a viewer can follow the lesson without audio.
- Leave small processing pauses after nontrivial constructions.
- Reuse terminology consistently across later parts.
