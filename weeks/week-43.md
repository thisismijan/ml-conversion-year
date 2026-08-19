# Week 43 — Phase 7: ML systems

**Topic:** Distributed training concepts

## Goals
- Tensor/pipeline/data parallelism, FSDP, NCCL, checkpointing

## Resources
- **[Interactive book]** The Ultra-Scale Playbook: Training LLMs on GPU Clusters — Hugging Face (nanotron) — https://huggingface.co/spaces/nanotron/ultrascale-playbook — grounded in 4,000+ real scaling experiments; covers DP/TP/PP/context-parallel/ZeRO in one place
- **[Docs]** Parallelism methods — Hugging Face Transformers — https://huggingface.co/docs/transformers/en/perf_train_gpu_many
- **[Tutorial]** Getting Started with FSDP — PyTorch — https://docs.pytorch.org/tutorials/intermediate/FSDP1_tutorial.html (note: FSDP2 is now current)
- **[Docs]** NCCL documentation — NVIDIA — https://docs.nvidia.com/deeplearning/nccl/ — reference for what's actually moving data between GPUs under DDP/FSDP


## Milestone / exercise
Write up how you'd parallelise training your GPT across N GPUs (design doc, doesn't need real hardware).

## Daily plan (10h)
- **Mon** (2h): Theory / implement concepts
- **Tue** (2h): Theory / implementation
- **Wed** (2h): Project build (no videos)
- **Thu** (2h): Reading / experiments & debugging
- **Fri** (1.5h + 0.5h): Read a paper / reproduce a result -> curate into weekly video

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
