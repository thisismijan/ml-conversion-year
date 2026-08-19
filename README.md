# SWE → ML/Research Engineer: 12-Month Conversion

**Starting point:** Senior SWE, low-latency trading + crypto custodian background, physics undergrad (math last touched 2016).
**Target:** ML/Research Engineer roles at frontier labs (research engineering, ML systems).
**Budget:** 10 hrs/week × 52 weeks ≈ 520 hours. 30% consuming material, 70% implementing.
**Format:** Weekly GitHub issue = weekly plan + checklist + becomes the outline for a Friday progress video.

---

## Phase map

| Phase | Weeks | Focus | Milestone |
|---|---|---|---|
| 0 | 1 | Python/NumPy for ML | Linear regression from scratch |
| 1 | 2–4 | Math refresh (linear algebra, calc, probability, info theory) — diagnostic-gated | Explain backprop math from memory |
| 2 | 5–10 | NN fundamentals + PyTorch + autograd | `tinygrad` — autodiff + NN lib from scratch |
| 3 | 11–18 | Transformers → build a GPT | `gpt-from-scratch` + writeup |
| 4 | 19–27 | Modern LLM: RoPE/GQA/RMSNorm, scaling, LoRA/QLoRA | `modern-gpt` + fine-tuned model |
| — | 28 | **Checkpoint week**: tidy repos, mock ML-infra interviews, reassess pace | — |
| 5 | 29–35 | Post-training: SFT → preference data → DPO/RLHF | `mini-post-training-lab` |
| 6 | 36–39 | Evals + research methodology | 3–5 page research report |
| 7 | 40–47 | ML systems / low-latency inference | `llm-engine` (batching/KV cache/benchmarks) |
| 8 | 48–52 | Independent research project | Code + benchmarks + paper/blog post |

Two floating buffer weeks are absorbed into the above (life happens — see below).

## Trading/custodian alignment

- **Phase 7** is the natural home: reframe the inference server as a matching engine — scheduler ~ order matching, TTFT ~ tick-to-trade latency, continuous batching under load ~ queueing/tail-latency. Measure P50/P99/P999, not just averages.
- **Phase 8 research project**: candidate question — *what batching/scheduling policy minimizes P99 latency for LLM serving under bursty load, and what does that borrow from market-data feed-handler design?*
- **Custodian background** → one deliberate exercise on checkpoint integrity / reproducible training runs treated with the same rigor as key management (Phase 6 or 8).

## What we're deliberately not studying

Generic AI courses, prompt engineering courses, LangChain tutorials, endless RAG apps, "10 AI projects in Python," months of pure theoretical math, every classical ML algorithm, Kaggle competitions, certificates.

## Weekly routine

| Day | Time | Activity |
|---|---|---|
| Mon | 60+60 min | Theory / implement concepts |
| Tue | 45+75 min | Theory / implementation |
| Wed | 120 min | Project build (no videos) |
| Thu | 30+90 min | Reading / experiments-debugging |
| Fri | 45+45 min | Read a paper / reproduce a result → **curate into weekly YouTube video** |

The Friday video is the old "notes" step repurposed — scripting the explanation + demo is the Feynman-technique revision, not extra hours.

## Portfolio (5 repos + 1 research project)

1. `tinygrad` — autodiff + neural nets from scratch
2. `gpt-from-scratch` — tokenizer → attention → transformer → training
3. `modern-gpt` — RoPE/GQA/RMSNorm/LoRA + experiments
4. `mini-post-training-lab` — SFT → preferences → DPO → evals
5. `llm-engine` — batching/KV cache/inference/benchmarks, trading-latency framing
6. Independent research project (Phase 8)

## Repo structure

```
weeks/week-01.md ... week-52.md   # one file per week: goals, exercises, checklist, video outline
.github/setup_project.sh          # run once with `gh` CLI to create milestones + all 52 issues + Project board
```

## Setup (once you're at a laptop with `gh` installed)

```bash
gh auth login
cd ml-conversion-year
gh repo create ml-conversion-year --public --source=. --push
bash .github/setup_project.sh
```

That script creates 9 milestones (one per phase) and 52 issues (one per week, pre-filled from `weeks/week-NN.md`), and adds them all to a GitHub Project board with a status column per phase.

## Doing this from mobile right now

You don't need `gh` to get started today:
1. On github.com (mobile browser or app) → **New repository** → name it `ml-conversion-year`, public, initialize with README.
2. Paste this file's contents in as the README (I'll hand you the raw text).
3. Use **Add file → Create new file** to add `weeks/week-01.md` (also below) — that's everything you need to start Week 1 tonight.
4. Milestones/issues/Project board can wait until you've got `gh` — nothing about starting the work depends on them.
