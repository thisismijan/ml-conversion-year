# Week 33 — Phase 5: Post-training & RL

**Topic:** Build a preference dataset

## Goals
- Preference data collection/format

## Resources
- **[Dataset/Reference]** Anthropic hh-rlhf — https://huggingface.co/datasets/Anthropic/hh-rlhf — study the chosen/rejected jsonl format as the schema to mimic (can be self-generated with two sampling temperatures + your own ranking)
- **[Docs]** TRL DPOTrainer data format — Hugging Face — https://huggingface.co/docs/trl/en/index — confirms the exact prompt/chosen/rejected field names expected downstream in week 35


## Milestone / exercise
Create a small preference dataset (can be synthetic/self-generated).

## Daily plan (10h)
- **Mon** (2h): Study Anthropic hh-rlhf's chosen/rejected jsonl schema
- **Tue** (2h): TRL DPOTrainer data format docs — confirm exact field names needed
- **Wed** (2h): Project build — generate response pairs from your SFT model at two sampling temperatures
- **Thu** (2h): Rank pairs yourself (or with a simple heuristic/LLM judge) into chosen/rejected; format as jsonl
- **Fri** (1.5h + 0.5h): Validate the dataset loads correctly against TRL's expected schema -> video: where preference data actually comes from

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
