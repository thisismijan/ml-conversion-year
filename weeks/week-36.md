# Week 36 — Phase 6: Evals & research method

**Topic:** What makes an experiment valid

## Goals
- Hypotheses, baselines, ablations, controlled experiments, statistical significance, variance, reproducibility, benchmark contamination

## Resources
- **[Paper]** Show Your Work: Improved Reporting of Experimental Results — Dodge, Gururangan, Card, Schwartz, Smith (EMNLP 2019) — https://aclanthology.org/D19-1224/ — point-estimate comparisons mislead; report expected performance vs compute budget, directly informs the 'how I'll know it worked' template
- **[Paper]** Deep Reinforcement Learning that Matters — Henderson et al. — https://arxiv.org/abs/1709.06560 — canonical demonstration of how much variance/seeds/hyperparameters swing reported results
- **[Survey]** Benchmark Data Contamination of Large Language Models: A Survey — https://arxiv.org/abs/2406.04244 — current survey of contamination failure modes, needed before trusting any benchmark number
- **[Checklist]** NeurIPS Paper Checklist Guidelines — https://neurips.cc/public/guides/PaperChecklist — field-standard checklist for what makes an ML experimental claim valid, reusable as the literal template

**Stretch:** Reproduce one small claim from the Dodge et al. paper's budget-vs-performance framing on your own Week 1 linear regression.

## Milestone / exercise
Write a one-page 'how I'll know if this change worked' template you'll reuse in Phase 8.

## Daily plan (10h)
- **Mon** (2h): Read Dodge et al. 'Show Your Work'
- **Tue** (2h): Read Henderson et al. 'Deep RL that Matters' + skim the benchmark contamination survey
- **Wed** (2h): Project build (no video) — draft your 'how I'll know if this change worked' one-page template
- **Thu** (2h): Cross-check the template against the NeurIPS Paper Checklist; revise
- **Fri** (1.5h + 0.5h): Reproduce one small claim from Dodge et al.'s framing on your Week 1 linear regression -> video: what makes an ML claim trustworthy

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
