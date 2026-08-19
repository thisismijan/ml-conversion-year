# Week 37 — Phase 6: Evals & research method

**Topic:** Evaluation design

## Goals
- LLM-as-judge, human evaluation, evaluation design pitfalls

## Resources
- **[Paper]** Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena — Zheng et al. — https://arxiv.org/abs/2306.05685 — the reference paper for LLM-as-judge methodology, biases (position/verbosity/self-enhancement), and mitigations
- **[Framework]** HELM (Holistic Evaluation of Language Models) — Stanford CRFM — https://crfm.stanford.edu/helm/ — how to design a multi-metric eval instead of a single leaderboard number
- **[Blog]** An LLM-as-Judge Won't Save The Product—Fixing Your Process Will — Eugene Yan — https://eugeneyan.com/writing/eval-process/ — practical pitfalls of eval design in real systems
- **[Repo/Docs]** lm-evaluation-harness — EleutherAI — https://github.com/EleutherAI/lm-evaluation-harness — the standard open-source harness; read docs/task_guide.md to see how a real eval task is specified

**Stretch:** Sketch your week 38 eval (RoPE vs learned pos-emb) as a formal lm-eval-harness-style task spec, even if you run it with your own code.

## Milestone / exercise
Design (don't run yet) an eval for one modification to your GPT.

## Daily plan (10h)
- **Mon** (2h): Read Zheng et al. 'Judging LLM-as-a-Judge' (MT-Bench/Chatbot Arena)
- **Tue** (2h): Skim HELM's multi-metric design + Eugene Yan's eval-process pitfalls post
- **Wed** (2h): Project build (no video) — pick your modification to test (RoPE vs learned positional embeddings at longer context)
- **Thu** (2h): Design the eval: metrics, baselines, controls; sketch it as an lm-eval-harness-style task spec
- **Fri** (1.5h + 0.5h): Finalize the eval design doc, don't run it yet -> video: designing an eval before you run it

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
