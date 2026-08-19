# Week 01 — Phase 0: Python for ML

**Topic:** Linear regression from scratch

## Goals
- NumPy: ndarray shapes, broadcasting, slicing, vectorisation
- matplotlib, Jupyter, basic pandas
- Python typing/dataclasses, virtual envs
- matmul, reshape, transpose, squeeze/unsqueeze, concat, reductions

## Resources
- **[Docs]** NumPy Quickstart — NumPy.org (official) — https://numpy.org/doc/stable/user/quickstart.html — canonical intro to ndarrays, shapes, indexing, reshaping/transposing
- **[Docs]** Broadcasting — NumPy.org (official) — https://numpy.org/doc/stable/user/basics.broadcasting.html — the broadcasting rules you need before vectorising anything
- **[Docs]** 10 Minutes to pandas — pandas.pydata.org (official) — https://pandas.pydata.org/docs/user_guide/10min.html — just enough pandas to load/inspect a dataset before dropping into NumPy
- **[Tutorial]** Linear Regression with Gradient Descent from Scratch in NumPy — Towards Data Science — https://towardsdatascience.com/linear-regression-with-gradient-descent-from-scratch-in-numpy-d894a800a2ca/ — walks prediction -> MSE -> gradients -> update loop, matches this week's milestone directly

**Stretch:** Regress on `sklearn.datasets.fetch_california_housing()` — the modern standard toy dataset (Boston Housing is deprecated/removed from scikit-learn).

## Milestone / exercise
Implement linear regression with NumPy (no sklearn): prediction -> MSE -> gradients -> gradient descent -> plot loss.

## Daily plan (10h)
- **Mon** (2h): NumPy Quickstart + Broadcasting docs — practice ndarray shapes, slicing, matmul/reshape/transpose in a scratch notebook
- **Tue** (2h): 10 Minutes to pandas; set up Jupyter/venv; load fetch_california_housing(), inspect with pandas/matplotlib
- **Wed** (2h): Project build (no video) — implement prediction (Xw+b) and MSE loss in NumPy
- **Thu** (2h): Implement gradients + gradient descent loop; use the Towards Data Science walkthrough where stuck; debug convergence
- **Fri** (1.5h + 0.5h): Plot the loss curve, sanity-check against sklearn's LinearRegression -> record video: how gradient descent finds the line

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
