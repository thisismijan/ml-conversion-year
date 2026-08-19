# Week 18 — Phase 3: Transformers

**Topic:** Compare to real GPT-2/3

## Goals
- Read GPT-2/GPT-3 lineage papers, compare to your implementation

## Resources
- **[Paper]** Language Models are Unsupervised Multitask Learners (GPT-2) — Radford et al., OpenAI — https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf (code: https://github.com/openai/gpt-2)
- **[Paper]** Language Models are Few-Shot Learners (GPT-3) — Brown et al. — https://arxiv.org/abs/2005.14165 — read the architecture section (2.1), skim the scaling results; this is the direct lineage from your from-scratch model
- **[Blog]** The Illustrated GPT-2 — Jay Alammar — https://jalammar.github.io/illustrated-gpt2/ — bridges 'Attention Is All You Need' and your toy GPT to the real GPT-2 architecture, good structure for the milestone write-up

**Stretch:** Tabulate your model's config (n_layer, n_head, d_model, params) side-by-side with GPT-2-small's (12, 12, 768, 124M) in the write-up.

## Milestone / exercise
Milestone: gpt-from-scratch repo + technical write-up of every component.

## Daily plan (10h)
- **Mon** (2h): Read the GPT-2 paper (Radford et al.), focus on architecture/training details
- **Tue** (2h): Read the GPT-3 paper section 2.1 (architecture), skim the scaling results
- **Wed** (2h): Project build (no video) — write the gpt-from-scratch technical write-up, component by component
- **Thu** (2h): Tabulate your config vs GPT-2-small (12, 12, 768, 124M); note every architectural gap
- **Fri** (1.5h + 0.5h): Finish the write-up, polish the repo README -> video: my GPT vs the real thing — milestone wrap

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
