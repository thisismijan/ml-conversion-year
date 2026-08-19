"""
Generates weeks/week-NN.md for all 52 weeks.
Edit WEEKS below to tweak content, then rerun.
"""
import os

WEEKS = {
1: ("Phase 0: Python for ML", "Linear regression from scratch",
    ["NumPy: ndarray shapes, broadcasting, slicing, vectorisation",
     "matplotlib, Jupyter, basic pandas",
     "Python typing/dataclasses, virtual envs",
     "matmul, reshape, transpose, squeeze/unsqueeze, concat, reductions"],
    "Implement linear regression with NumPy (no sklearn): prediction -> MSE -> gradients -> gradient descent -> plot loss."),

2: ("Phase 1: Math refresh", "Diagnostic + linear algebra",
    ["Diagnostic problem set: lin alg, calc, probability, stats (find real gaps, not assumed ones)",
     "Scalars/vectors/matrices/tensors, dot product, matmul, transpose, inverse",
     "Linear transformations, basis, rank, norms, eigenvalues/eigenvectors, SVD",
     "Connect to ML: tokens -> embedding matrix -> X @ W"],
    "Write a page connecting SVD/eigenvectors to something in ML (e.g. PCA or attention)."),
3: ("Phase 1: Math refresh", "Calculus + probability",
    ["Derivatives, partial derivatives, gradients, chain rule, computational graphs",
     "Manually differentiate y = Wx + b, loss = (y-target)^2",
     "Random variables, distributions, expectation, variance, covariance, Bayes' theorem, likelihood"],
    "Manually derive backprop for a 1-layer network on paper, then verify numerically in code."),
3.5: None,
4: ("Phase 1: Math refresh", "Info theory + optimisation",
    ["Entropy, cross-entropy, KL divergence, perplexity, softmax, log-probs (stat-mech parallel: Boltzmann distribution)",
     "Implement softmax and cross-entropy yourself",
     "SGD, momentum, Adam, learning rate, weight decay, regularisation, train/val/test"],
    "Implement SGD and Adam with NumPy. Milestone: explain 'how does a neural net learn' end-to-end, in code."),

5: ("Phase 2: PyTorch fundamentals", "Tensors + GPU execution",
    ["x.shape, x.dtype, x.device, x.requires_grad", "CPU <-> GPU movement", "PyTorch 'Learn the Basics' tutorial"],
    "Port your NumPy linear regression to PyTorch tensors."),
6: ("Phase 2: PyTorch fundamentals", "Autograd (build your own)",
    ["Build a miniature autograd engine: Value(2)*Value(3), c.backward()", "Computation graphs, gradient accumulation"],
    "micrograd-style engine, tested against PyTorch's autograd on the same expression."),
7: ("Phase 2: PyTorch fundamentals", "Neural networks", 
    ["Linear layer, activation, MLP, loss, optimiser, training loop from scratch in PyTorch"],
    "Train an MLP on a toy dataset end to end."),
8: ("Phase 2: PyTorch fundamentals", "Image classifier (vehicle, not destination)",
    ["Datasets, batching, epochs, training/validation, checkpoints, hyperparameters"],
    "Train an image classifier; log train/val curves."),
9: ("Phase 2: PyTorch fundamentals", "Deep learning behaviour",
    ["Initialization, exploding/vanishing gradients, normalization, dropout, LR schedules"],
    "Deliberately break a model 3 ways (bad init, no norm, huge LR) and diagnose each from the loss curve."),
10: ("Phase 2: PyTorch fundamentals", "Minimal-abstraction reimplementation",
     ["Rewrite your NN with minimal nn.* usage — most forward/training logic by hand"],
     "Milestone: tinygrad repo — your own autodiff + NN library, README with design notes."),

11: ("Phase 3: Transformers", "Language models 101",
     ["Tokenization, vocabulary, embeddings, context windows, autoregressive prediction"],
     "Build a bigram language model; generate (bad) text."),
12: ("Phase 3: Transformers", "Attention, conceptually",
     ["Read 'Attention Is All You Need' (don't rush the whole paper)",
      "Q=XWq, K=XWk, V=XWv, softmax(QK^T/sqrt(d))V — understand each operation"],
     "Write a plain-English + math walkthrough of self-attention (this is your video script)."),
13: ("Phase 3: Transformers", "Implement self-attention",
     ["No nn.MultiheadAttention — build it from matmuls"],
     "Self-attention module passing a numerical gradient check."),
14: ("Phase 3: Transformers", "Multi-head + positional + norm",
     ["Causal masking, multi-head attention, positional encoding, layer norm, residual connections"],
     "Add all four to your attention module."),
15: ("Phase 3: Transformers", "Transformer block",
     ["Assemble attention + MLP + norm + residuals into one block"],
     "A single working Transformer block, unit-tested."),
16: ("Phase 3: Transformers", "Stack it: build GPT",
     ["Stack blocks into a full model"],
     "A tiny, architecturally-correct GPT."),
17: ("Phase 3: Transformers", "Train it",
     ["Tokenisation, batches, sequence length, LR, validation loss, sampling temperature, top-k"],
     "Train on a small corpus; sample text at a few temperatures."),
18: ("Phase 3: Transformers", "Compare to real GPT-2/3", 
     ["Read GPT-2/GPT-3 lineage papers, compare to your implementation"],
     "Milestone: gpt-from-scratch repo + technical write-up of every component."),

19: ("Phase 4: Modern LLM", "BPE tokenisation",
     ["BPE / SentencePiece-style approaches"], "Implement a BPE tokenizer yourself."),
20: ("Phase 4: Modern LLM", "RoPE",
     ["Rotary position embeddings — theory and implementation"], "Swap learned pos-embeddings for RoPE in your GPT."),
21: ("Phase 4: Modern LLM", "RMSNorm + SwiGLU",
     ["RMSNorm vs LayerNorm, SwiGLU activation"], "Swap in RMSNorm + SwiGLU, compare training curves."),
22: ("Phase 4: Modern LLM", "GQA/MQA + FlashAttention + MoE (survey)",
     ["Grouped/multi-query attention, FlashAttention, mixture of experts (conceptual)"],
     "Implement GQA in your GPT (MoE/FlashAttention: understand, don't necessarily implement)."),
23: ("Phase 4: Modern LLM", "Scaling",
     ["Parameter count, FLOPs, training tokens, compute-optimal training, scaling laws"],
     "Estimate compute-optimal token count for your model size; compare to Chinchilla."),
24: ("Phase 4: Modern LLM", "Fine-tuning landscape",
     ["SFT, LoRA, QLoRA, PEFT, quantisation — survey"], "Fine-tune an open small model using an existing LoRA library."),
25: ("Phase 4: Modern LLM", "Implement LoRA yourself",
     ["Low-rank adapter math and implementation"], "LoRA implemented from scratch, applied to your GPT."),
26: ("Phase 4: Modern LLM", "Integrate everything",
     ["GPT v1 -> RoPE -> RMSNorm -> GQA -> LoRA -> fine-tuned model"], "modern-gpt repo assembling the full stack."),
27: ("Phase 4: Modern LLM", "Fine-tune + evaluate",
     ["Run a real fine-tune with your LoRA implementation"], "Milestone: modern-gpt repo complete + fine-tuned checkpoint."),

28: ("Checkpoint week", "Portfolio + interview gut-check",
     ["Tidy tinygrad, gpt-from-scratch, modern-gpt as public repos with clear READMEs",
      "Do 1-2 mock ML-infra / research-engineer interviews",
      "Reassess pace for phases 5-8 based on actual (not planned) progress"],
     "Public, polished versions of the first 3 milestone repos. Notes on interview feedback."),

29: ("Phase 5: Post-training & RL", "RL basics",
     ["States/actions/rewards, policies, value functions, policy gradients"], "Implement a tiny policy-gradient example (e.g. bandit or gridworld)."),
30: ("Phase 5: Post-training & RL", "PPO + RLHF pipeline",
     ["PPO, RLHF pipeline: pretrain -> SFT -> reward model -> policy optimisation"], "Diagram the full RLHF pipeline from memory."),
31: ("Phase 5: Post-training & RL", "DPO / RLAIF",
     ["DPO derivation, RLAIF"], "Implement DPO loss from the paper's derivation."),
32: ("Phase 5: Post-training & RL", "SFT on your model",
     ["Supervised fine-tuning pipeline"], "SFT your GPT on an instruction dataset."),
33: ("Phase 5: Post-training & RL", "Build a preference dataset",
     ["Preference data collection/format"], "Create a small preference dataset (can be synthetic/self-generated)."),
34: ("Phase 5: Post-training & RL", "Train a reward/preference model",
     ["Reward model architecture and training"], "Train a preference model on your dataset."),
35: ("Phase 5: Post-training & RL", "Run DPO, compare",
     ["Run DPO end to end"], "Milestone: mini-post-training-lab — compare base vs SFT vs DPO on an eval set."),

36: ("Phase 6: Evals & research method", "What makes an experiment valid",
     ["Hypotheses, baselines, ablations, controlled experiments, statistical significance, variance, reproducibility, benchmark contamination"],
     "Write a one-page 'how I'll know if this change worked' template you'll reuse in Phase 8."),
37: ("Phase 6: Evals & research method", "Evaluation design",
     ["LLM-as-judge, human evaluation, evaluation design pitfalls"], "Design (don't run yet) an eval for one modification to your GPT."),
38: ("Phase 6: Evals & research method", "Run the experiment",
     ["E.g. does RoPE outperform learned positional embeddings at longer context?"], "Run the experiment you designed; collect results."),
39: ("Phase 6: Evals & research method", "Write it up",
     ["Analysis, writing for a technical audience"], "Milestone: 3-5 page research report, hypothesis -> methodology -> result -> discussion."),

40: ("Phase 7: ML systems", "GPU fundamentals",
     ["CPU vs GPU, CUDA, kernels, warps, memory hierarchy, HBM, compute vs memory bound"], "Profile a matmul; identify if it's compute- or memory-bound."),
41: ("Phase 7: ML systems", "Inference pipeline",
     ["prompt -> prefill -> KV cache -> decode -> sampling"], "Diagram + implement a minimal prefill/decode loop with KV cache."),
42: ("Phase 7: ML systems", "Batching",
     ["Static vs continuous batching, quantisation, FlashAttention"], "Add basic batching to your inference loop."),
43: ("Phase 7: ML systems", "Distributed training concepts",
     ["Tensor/pipeline/data parallelism, FSDP, NCCL, checkpointing"], "Write up how you'd parallelise training your GPT across N GPUs (design doc, doesn't need real hardware)."),
44: ("Phase 7: ML systems", "Inference server v1",
     ["HTTP request -> model.generate() -> response"], "A minimal working inference server."),
45: ("Phase 7: ML systems", "Scheduler + dynamic batching",
     ["requests -> scheduler -> dynamic batching -> model -> KV cache -> streaming output",
      "Trading-latency framing: scheduler ~ matching engine, TTFT ~ tick-to-trade"],
     "Add a request scheduler with dynamic batching to your server."),
46: ("Phase 7: ML systems", "Streaming + measurement",
     ["TTFT, TPOT, throughput (tokens/sec), GPU memory utilisation, P50/P99/P999 latency (bring trading rigor here)"],
     "Add streaming output; build a benchmark harness reporting P50/P99/P999, not just averages."),
47: ("Phase 7: ML systems", "Benchmark + writeup",
     ["Consolidate benchmarks, compare batching strategies"], "Milestone: llm-engine repo with benchmarks and a latency writeup."),

48: ("Phase 8: Research project", "Pick the question + read literature",
     ["Candidate: batching/scheduling policy vs P99 latency under bursty load, feed-handler parallels"],
     "Finalise research question; annotated bibliography of 5-10 relevant papers."),
49: ("Phase 8: Research project", "Baseline + experiment design",
     ["Implement baseline, design controlled experiment (reuse Phase 6 template)"], "Working baseline + written experiment design."),
50: ("Phase 8: Research project", "Run experiments",
     ["Run, log, and iterate"], "Raw results + first-pass analysis."),
51: ("Phase 8: Research project", "Analyse + investigate anomalies",
     ["Dig into anything unexpected"], "Finalised results, graphs."),
52: ("Phase 8: Research project", "Write it up + wrap portfolio",
     ["Technical paper/blog post; final polish pass on all 6 portfolio items"],
     "Milestone: published research writeup + complete portfolio of 5 repos + 1 research project."),
}

TEMPLATE = """# Week {n:02d} — {phase}

**Topic:** {topic}

## Goals
{goals}

## Milestone / exercise
{milestone}

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
"""

os.makedirs("weeks", exist_ok=True)
for n, data in WEEKS.items():
    if data is None:
        continue
    phase, topic, goals, milestone = data
    goals_md = "\n".join(f"- {g}" for g in goals)
    text = TEMPLATE.format(n=int(n), phase=phase, topic=topic, goals=goals_md, milestone=milestone)
    with open(f"weeks/week-{int(n):02d}.md", "w") as f:
        f.write(text)

print(f"Generated {len([k for k,v in WEEKS.items() if v])} week files.")
