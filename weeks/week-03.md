# Week 03 — Phase 1: Math refresh

**Topic:** Calculus + probability

## Goals
- Derivatives, partial derivatives, gradients, chain rule, computational graphs
- Manually differentiate y = Wx + b, loss = (y-target)^2
- Random variables, distributions, expectation, variance, covariance, Bayes' theorem, likelihood

## Resources
- **[Video]** Essence of Calculus — 3Blue1Brown — https://www.youtube.com/@3blue1brown — chain rule and derivative-as-slope intuition, watch before deriving backprop by hand
- **[Notes]** CS231n Optimization: Backpropagation — Andrej Karpathy / Stanford — https://cs231n.github.io/optimization-2/ — the canonical 'circuits and gates' chain-rule explanation, matches this week's milestone (manual derivation + numerical check)
- **[Guide]** The Matrix Calculus You Need for Deep Learning — Parr & Howard — https://explained.ai/matrix-calculus/ (also arXiv:1802.01528) — going from scalar chain rule to the Wx+b gradient in matrix form
- **[Interactive]** Seeing Theory, ch. 1-4 (Basic Probability, Compound Probability, Distributions, Bayesian Inference) — Brown University — https://seeing-theory.brown.edu/ — visual, self-testable coverage of expectation/variance/covariance/Bayes' theorem

**Stretch:** Implement CS231n's 'staged computation' sigmoid-circuit example yourself before the 1-layer network derivation — smallest possible warm-up for the same technique.

## Milestone / exercise
Manually derive backprop for a 1-layer network on paper, then verify numerically in code.

## Daily plan (10h)
- **Mon** (2h): 3Blue1Brown Essence of Calculus (derivative, chain rule episodes)
- **Tue** (2h): CS231n Optimization: Backpropagation notes; work through the staged-computation sigmoid-circuit example
- **Wed** (2h): Project build — manually differentiate y=Wx+b, loss=(y-target)^2 on paper, writing out every chain-rule step
- **Thu** (2h): Seeing Theory ch.1-4 (probability/distributions/Bayes); Matrix Calculus guide for the matrix-form gradient
- **Fri** (1.5h + 0.5h): Verify your manual backprop derivation numerically in code (finite differences) -> video: chain rule as circuits

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
