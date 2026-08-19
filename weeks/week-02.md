# Week 02 — Phase 1: Math refresh

**Topic:** Diagnostic + linear algebra

## Goals
- Diagnostic problem set: lin alg, calc, probability, stats (find real gaps, not assumed ones)
- Scalars/vectors/matrices/tensors, dot product, matmul, transpose, inverse
- Linear transformations, basis, rank, norms, eigenvalues/eigenvectors, SVD
- Connect to ML: tokens -> embedding matrix -> X @ W

## Resources
- **[Video]** Essence of Linear Algebra (16-part playlist) — 3Blue1Brown — https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab — fastest way to rebuild geometric intuition (span, basis, determinant, eigenvectors ch.14) before touching notation again
- **[Book, ch. 2 & 4]** Mathematics for Machine Learning — Deisenroth, Faisal, Ong (free PDF) — https://mml-book.github.io/book/mml-book.pdf — ch.2 (linear algebra: rank, norms) and ch.4 (matrix decompositions: eigendecomposition, SVD) go straight from theorem to ML use case
- **[Lecture]** 18.06 Linear Algebra, lectures 21 & 29 — Gilbert Strang, MIT OCW — https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/ — lecture 21 (eigenvalues/eigenvectors) and lecture 29 (SVD), the two concepts this week's milestone needs
- **[Problem sets]** 18.06 course materials — MIT — https://github.com/mitmath/1806 — use the psets as the diagnostic rather than writing your own from scratch

**Stretch:** Read the SVD section of Strang's *ZoomNotes* (linked from the 18.06 OCW page) before writing the SVD/PCA milestone page — a 2-page distillation of lecture 29.

## Milestone / exercise
Write a page connecting SVD/eigenvectors to something in ML (e.g. PCA or attention).

## Daily plan (10h)
- **Mon** (2h): Take the mitmath/1806 diagnostic pset cold, no notes — mark what you don't remember
- **Tue** (2h): 3Blue1Brown Essence of Linear Algebra eps 1-8 (vectors, span, transformations, determinant), targeting your diagnostic gaps
- **Wed** (2h): Project build — MML book ch.2 exercises (rank, norms) + Strang lecture 21 (eigenvalues/eigenvectors)
- **Thu** (2h): Strang lecture 29 (SVD) + ZoomNotes distillation; connect tokens -> embedding matrix -> X@W conceptually
- **Fri** (1.5h + 0.5h): Write the SVD/eigenvectors -> PCA or attention page -> video: SVD explained with a diagram

## Checklist
- [ ] Core reading/lecture done
- [ ] Exercise/milestone implemented
- [ ] Code pushed to relevant repo
- [ ] Friday video recorded & published
- [ ] Notes on what was hard / what to revisit

## Video outline (draft while working, don't leave to Friday)
1. What I set out to learn this week
2. The one concept that took longest to click, explained simply
3. Demo of the code/result
4. What's next
