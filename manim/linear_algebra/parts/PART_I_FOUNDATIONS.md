# Part I — Foundations

Part I is the beginning of the long-form visual linear algebra course. It is intentionally slower than a typical tutorial: each lesson introduces intuition, constructs the geometry, writes the algebra, works a numerical example, and closes with a conceptual takeaway.

Every lesson uses on-screen **CC-style explanation text** so the viewer can follow the reasoning even without narration.

## Lessons

### I.1 Scalars vs Vectors
- scalar vs directional information
- displacement as the core vector idea
- why a vector can move without changing
- coordinate representation

### I.2 Coordinates and Components
- x/y components
- column-vector representation
- negative components
- coordinates vs the underlying geometric vector

### I.3 Vector Addition
- componentwise addition
- tip-to-tail construction
- parallelogram construction
- geometric meaning of the result

### I.4 Vector Subtraction
- displacement from one vector endpoint to another
- subtraction as addition of an opposite
- geometric meaning of a difference vector

### I.5 Scaling and Unit Vectors
- positive and negative scalar multiplication
- length scaling
- direction reversal
- normalization and unit vectors

### I.6 Magnitude and Distance
- Pythagorean interpretation
- vector norm
- distance as the norm of a difference
- worked coordinate example

### I.7 Linear Combinations
- scaling and combining multiple vectors
- geometric construction
- componentwise calculation
- why linear combinations become the language of span, basis, and matrices

### I.8 Foundations Recap
- one mental model connecting all Part I operations
- key equations
- conceptual recap before moving to vector spaces

## Rendering

From `manim/linear_algebra`:

```bash
uv run manim -pqh render_part1.py Part1_01_ScalarsAndVectors
```

Or render all Part I scenes:

```bash
for scene in Part1_01_ScalarsAndVectors Part1_02_CoordinatesAndComponents Part1_03_VectorAddition Part1_04_VectorSubtraction Part1_05_ScalingAndUnitVectors Part1_06_MagnitudeAndDistance Part1_07_LinearCombinations Part1_08_FoundationsRecap; do
  uv run manim -qh render_part1.py "$scene" || exit 1
done
```

## Teaching standard

The target is not a compressed formula sheet. Each scene should make the viewer understand **why** the formula exists before asking them to remember it. Animations should expose the connection between coordinates, arrows, geometry, and algebra rather than treating them as separate subjects.
