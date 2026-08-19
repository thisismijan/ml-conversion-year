"""
Generates weeks/week-NN.md for all 52 weeks.
Edit WEEKS/RESOURCES below to tweak content, then rerun.
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

# Curated, hand-verified resources per week (courses/books/papers/repos, all free unless noted).
# Format per week: (list of "- **[Type]** Title — Author/Org — URL — why" lines, optional stretch line or None)
RESOURCES = {
1: ([
    "- **[Docs]** NumPy Quickstart — NumPy.org (official) — https://numpy.org/doc/stable/user/quickstart.html — canonical intro to ndarrays, shapes, indexing, reshaping/transposing",
    "- **[Docs]** Broadcasting — NumPy.org (official) — https://numpy.org/doc/stable/user/basics.broadcasting.html — the broadcasting rules you need before vectorising anything",
    "- **[Docs]** 10 Minutes to pandas — pandas.pydata.org (official) — https://pandas.pydata.org/docs/user_guide/10min.html — just enough pandas to load/inspect a dataset before dropping into NumPy",
    "- **[Tutorial]** Linear Regression with Gradient Descent from Scratch in NumPy — Towards Data Science — https://towardsdatascience.com/linear-regression-with-gradient-descent-from-scratch-in-numpy-d894a800a2ca/ — walks prediction -> MSE -> gradients -> update loop, matches this week's milestone directly",
   ], "Regress on `sklearn.datasets.fetch_california_housing()` — the modern standard toy dataset (Boston Housing is deprecated/removed from scikit-learn)."),

2: ([
    "- **[Video]** Essence of Linear Algebra (16-part playlist) — 3Blue1Brown — https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab — fastest way to rebuild geometric intuition (span, basis, determinant, eigenvectors ch.14) before touching notation again",
    "- **[Book, ch. 2 & 4]** Mathematics for Machine Learning — Deisenroth, Faisal, Ong (free PDF) — https://mml-book.github.io/book/mml-book.pdf — ch.2 (linear algebra: rank, norms) and ch.4 (matrix decompositions: eigendecomposition, SVD) go straight from theorem to ML use case",
    "- **[Lecture]** 18.06 Linear Algebra, lectures 21 & 29 — Gilbert Strang, MIT OCW — https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/ — lecture 21 (eigenvalues/eigenvectors) and lecture 29 (SVD), the two concepts this week's milestone needs",
    "- **[Problem sets]** 18.06 course materials — MIT — https://github.com/mitmath/1806 — use the psets as the diagnostic rather than writing your own from scratch",
   ], "Read the SVD section of Strang's *ZoomNotes* (linked from the 18.06 OCW page) before writing the SVD/PCA milestone page — a 2-page distillation of lecture 29."),
3: ([
    "- **[Video]** Essence of Calculus — 3Blue1Brown — https://www.youtube.com/@3blue1brown — chain rule and derivative-as-slope intuition, watch before deriving backprop by hand",
    "- **[Notes]** CS231n Optimization: Backpropagation — Andrej Karpathy / Stanford — https://cs231n.github.io/optimization-2/ — the canonical 'circuits and gates' chain-rule explanation, matches this week's milestone (manual derivation + numerical check)",
    "- **[Guide]** The Matrix Calculus You Need for Deep Learning — Parr & Howard — https://explained.ai/matrix-calculus/ (also arXiv:1802.01528) — going from scalar chain rule to the Wx+b gradient in matrix form",
    "- **[Interactive]** Seeing Theory, ch. 1-4 (Basic Probability, Compound Probability, Distributions, Bayesian Inference) — Brown University — https://seeing-theory.brown.edu/ — visual, self-testable coverage of expectation/variance/covariance/Bayes' theorem",
   ], "Implement CS231n's 'staged computation' sigmoid-circuit example yourself before the 1-layer network derivation — smallest possible warm-up for the same technique."),
3.5: None,
4: ([
    "- **[Blog]** Visual Information Theory — Chris Olah — https://colah.github.io/posts/2015-09-Visual-Information/ — best available entropy/cross-entropy/KL-divergence explainer, builds intuition before implementing softmax+cross-entropy from scratch",
    "- **[Notes]** Linear Classification: Softmax classifier & cross-entropy — CS231n / Karpathy — https://cs231n.github.io/linear-classify/#softmax — worked derivation matching the 'implement it yourself' milestone directly",
    "- **[Paper/Survey]** An Overview of Gradient Descent Optimization Algorithms — Sebastian Ruder — https://arxiv.org/abs/1609.04747 — SGD -> momentum -> AdaGrad/RMSprop -> Adam derivations in one place, exactly what you need to implement SGD and Adam in NumPy",
    "- **[Notes]** Neural Networks Part 3: Learning and Evaluation — CS231n — https://cs231n.github.io/neural-networks-3/ — practical companion on LR schedules, weight decay, train/val/test methodology",
   ], "After implementing Adam, reproduce Ruder's toy loss-landscape comparison plot (different optimizers converging at different rates) on a simple 2D function."),

5: ([
    "- **[Tutorial]** Learn the Basics (Quickstart -> Tensors -> Autograd -> Optimization) — PyTorch official docs — https://docs.pytorch.org/tutorials/beginner/basics/intro.html — the canonical, official walkthrough of exactly this week's tensor/device/autograd basics",
    "- **[Article]** PyTorch in One Hour: From Tensors to Training Neural Networks on Multiple GPUs — Sebastian Raschka — https://sebastianraschka.com/teaching/pytorch-1h/ — dense single-sitting refresher on tensors/devices/autograd",
    "- **[Docs]** torch.Tensor attributes (shape, dtype, device, requires_grad) — PyTorch docs — https://docs.pytorch.org/docs/stable/tensors.html — primary reference for this week's exact goals",
   ], None),
6: ([
    "- **[Video]** The spelled-out intro to neural networks and backpropagation: building micrograd — Andrej Karpathy, *Neural Networks: Zero to Hero* ep.1 — https://www.youtube.com/watch?v=44_j7ufypfw — this IS the 'Value(2)*Value(3), c.backward()' milestone, taught step by step",
    "- **[Repo]** karpathy/micrograd — Andrej Karpathy — https://github.com/karpathy/micrograd — ~150-line reference implementation to test your engine against after you build your own, not to copy upfront",
    "- **[Series]** Neural Networks: Zero to Hero — Andrej Karpathy — https://karpathy.ai/zero-to-hero.html — full series landing page, useful for orientation across weeks 6-10",
   ], None),
7: ([
    "- **[Video]** Building makemore Part 2: MLP — Andrej Karpathy — https://www.youtube.com/watch?v=TCH_1BHY58I — builds an MLP + training loop in PyTorch from scratch, directly matching this week's milestone",
    "- **[Tutorial]** Learn the Basics: Build Model / Autograd / Optimization — PyTorch official docs — https://docs.pytorch.org/tutorials/beginner/basics/intro.html — reference for nn.Module, loss functions, optimizer API while building the MLP by hand",
   ], None),
8: ([
    "- **[Tutorial]** Training a Classifier (CIFAR-10) — PyTorch official docs — https://docs.pytorch.org/tutorials/beginner/blitz/cifar10_tutorial.html — official end-to-end datasets/batching/training-loop/eval tutorial, exact scope of this week's milestone",
    "- **[Docs]** Datasets & DataLoaders — PyTorch official docs — https://docs.pytorch.org/tutorials/beginner/basics/data_tutorial.html — canonical reference for batching/epoch mechanics",
   ], None),
9: ([
    "- **[Notes]** CS231n: Neural Networks Part 2 (Setting up the data and the loss) — Stanford CS231n — https://cs231n.github.io/neural-networks-2/ — the standard reference on weight-init pitfalls and regularization/dropout",
    "- **[Notes]** CS231n: Neural Networks Part 3 (Learning and Evaluation) — Stanford CS231n — https://cs231n.github.io/neural-networks-3/ — babysitting the learning process via loss curves, exactly the diagnostic skill this week's milestone requires",
   ], "Deliberately reproduce vanishing gradients with a deep sigmoid MLP and fix it with better init/normalization, per CS231n's guidance."),
10: ([
    "- **[Repo]** tinygrad/tinygrad — tiny corp / George Hotz — https://github.com/tinygrad/tinygrad — read (don't copy) as a real-world minimal, from-scratch autodiff + NN framework, positioned between micrograd and PyTorch",
    "- **[Repo]** karpathy/micrograd — Andrej Karpathy — https://github.com/karpathy/micrograd — revisit your Week 6 engine and extend it toward this week's tensor-level milestone",
    ], "Write a short README section comparing your design decisions against tinygrad's (e.g. lazy eval, ops as a small closed set)."),

11: ([
    "- **[Video+Repo]** The spelled-out intro to language modeling: building makemore — Andrej Karpathy — https://www.youtube.com/watch?v=PaCmpygFfXo (repo: https://github.com/karpathy/makemore) — builds exactly a bigram character-level LM from counting through to a tiny neural net, the direct template for this week's milestone",
    "- **[Series]** Neural Networks: Zero to Hero — Andrej Karpathy — https://karpathy.ai/zero-to-hero.html — index of the whole series, see how this week fits weeks 12-17",
    "- **[Blog]** The Illustrated GPT-2 (Visualizing Transformer Language Models) — Jay Alammar — https://jalammar.github.io/illustrated-gpt2/ — conceptual grounding for tokens/embeddings/context windows before touching attention",
   ], "After the bigram model, try a simple trigram extension by hand to feel why it doesn't scale — motivates attention next week."),
12: ([
    "- **[Paper]** Attention Is All You Need — Vaswani et al. (2017) — https://arxiv.org/abs/1706.03762 — the primary source; read section 3.2 (Attention) closely, skim the rest",
    "- **[Blog]** The Illustrated Transformer — Jay Alammar — https://jalammar.github.io/illustrated-transformer/ — the canonical plain-English + diagram walkthrough of Q/K/V and softmax(QK^T/sqrt(d))V",
    "- **[Video]** Let's build GPT: from scratch, in code, spelled out (first ~40 min, self-attention derivation) — Andrej Karpathy — https://www.youtube.com/watch?v=kCc8FmEb1nY — watch only through the self-attention section this week; save the rest for weeks 13-17",
   ], "Draw the Q/K/V matrix shapes for a toy 4-token, 8-dim example by hand before writing any code."),
13: ([
    "- **[Video]** Let's build GPT (self-attention head implementation segment) — Andrej Karpathy — https://www.youtube.com/watch?v=kCc8FmEb1nY — builds a Head module from raw matmuls, no nn.MultiheadAttention",
    "- **[Code]** The Annotated Transformer — Sasha Rush / Harvard NLP — https://nlp.seas.harvard.edu/annotated-transformer/ (repo: https://github.com/harvardnlp/annotated-transformer) — line-by-line PyTorch implementation to check your from-scratch attention against",
    "- **[Reference]** CS231n Gradient checks notes — Stanford — https://cs231n.github.io/neural-networks-3/ — relative-error thresholds and float64 precision guidance for this week's numerical gradient check",
   ], "Also gradient-check against PyTorch autograd directly (torch.autograd.gradcheck) as a second, independent verification."),
14: ([
    "- **[Video]** Let's build GPT (multi-head attention, positional encoding, LayerNorm, residuals segment) — Andrej Karpathy — https://www.youtube.com/watch?v=kCc8FmEb1nY",
    "- **[Blog]** Transformer Architecture: The Positional Encoding — Amirhossein Kazemnejad — https://kazemnejad.com/blog/transformer_architecture_positional_encoding/ — deep-dive on why sinusoidal positional encodings work and their relative-position property",
    "- **[Blog]** The Illustrated Transformer — Jay Alammar — https://jalammar.github.io/illustrated-transformer/ — clear diagrams for multi-head split/concat and the residual+LayerNorm sublayers",
   ], "Compare causal (decoder) masking vs no masking by visualizing the attention matrix as a heatmap for both."),
15: ([
    "- **[Video]** Let's build GPT (assembling the Transformer Block: attention + MLP + norm + residual) — Andrej Karpathy — https://www.youtube.com/watch?v=kCc8FmEb1nY",
    "- **[Code]** nanoGPT model.py — Andrej Karpathy — https://github.com/karpathy/nanoGPT/blob/master/model.py — canonical minimal, readable reference for a correctly-assembled GPT block to unit-test your own against",
    "- **[Code]** The Annotated Transformer, EncoderLayer/DecoderLayer — Harvard NLP — https://nlp.seas.harvard.edu/annotated-transformer/ — second independent reference implementation for cross-checking block structure",
   ], "Write a unit test that feeds a fixed-seed input through your block and asserts output shape and that gradients flow to every parameter."),
16: ([
    "- **[Repo]** nanoGPT — Andrej Karpathy — https://github.com/karpathy/nanoGPT — 'the simplest, fastest repository for training/finetuning medium-sized GPTs,' the direct target architecture for stacking blocks into a full model",
    "- **[Video]** Let's build GPT (full model assembly + generation loop) — Andrej Karpathy — https://www.youtube.com/watch?v=kCc8FmEb1nY",
    "- **[Repo]** minGPT — Andrej Karpathy — https://github.com/karpathy/minGPT — even smaller (~300 line) reference if nanoGPT feels too dense",
   ], "Print total parameter count and compare it against a back-of-envelope calc (embedding + per-layer attention/MLP params x n_layer)."),
17: ([
    "- **[Video]** Let's build GPT (training loop, loss curves, sampling) — Andrej Karpathy — https://www.youtube.com/watch?v=kCc8FmEb1nY",
    "- **[Docs]** How to generate text: using different decoding methods — Hugging Face — https://huggingface.co/docs/transformers/main_classes/text_generation — official reference for temperature/top-k/top-p sampling semantics and application order",
   ], "Plot validation loss for 2-3 different learning rates on the same chart to build intuition before Phase 4's scaling-laws work."),
18: ([
    "- **[Paper]** Language Models are Unsupervised Multitask Learners (GPT-2) — Radford et al., OpenAI — https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf (code: https://github.com/openai/gpt-2)",
    "- **[Paper]** Language Models are Few-Shot Learners (GPT-3) — Brown et al. — https://arxiv.org/abs/2005.14165 — read the architecture section (2.1), skim the scaling results; this is the direct lineage from your from-scratch model",
    "- **[Blog]** The Illustrated GPT-2 — Jay Alammar — https://jalammar.github.io/illustrated-gpt2/ — bridges 'Attention Is All You Need' and your toy GPT to the real GPT-2 architecture, good structure for the milestone write-up",
   ], "Tabulate your model's config (n_layer, n_head, d_model, params) side-by-side with GPT-2-small's (12, 12, 768, 124M) in the write-up."),

19: ([
    "- **[Video+Repo]** Let's build the GPT Tokenizer — Andrej Karpathy — https://www.youtube.com/watch?v=zduSFxRajkE (repo: https://github.com/karpathy/minbpe) — builds a BPE tokenizer from scratch, the exact milestone for this week; minbpe's exercise.md has 4 progressive steps to a GPT-4-equivalent tokenizer",
    "- **[Docs]** SentencePiece — Google (GitHub) — https://github.com/google/sentencepiece — compare against a production BPE/unigram library after building your own",
   ], "Diff your tokenizer's vocab/merges against tiktoken's cl100k_base on a shared text sample."),
20: ([
    "- **[Paper]** RoFormer: Enhanced Transformer with Rotary Position Embedding — Su et al. — https://arxiv.org/abs/2104.09864 — the RoPE paper itself",
    "- **[Repo]** RoFormer reference implementation — ZhuiyiTechnology — https://github.com/ZhuiyiTechnology/roformer — original authors' code to check your implementation against",
   ], "Plot attention score decay vs relative token distance before/after adding RoPE."),
21: ([
    "- **[Paper]** Root Mean Square Layer Normalization — Zhang & Sennrich — https://arxiv.org/abs/1910.07467 — the RMSNorm paper",
    "- **[Paper]** GLU Variants Improve Transformer — Noam Shazeer — https://arxiv.org/abs/2002.05202 — introduces SwiGLU, now standard in LLaMA/PaLM/DeepSeek",
   ], "Ablate LayerNorm-vs-RMSNorm and ReLU-vs-SwiGLU independently; log both loss curves on the same plot."),
22: ([
    "- **[Paper]** GQA: Training Generalized Multi-Query Transformer Models from Multi-Head Checkpoints — Ainslie et al. — https://arxiv.org/abs/2305.13245 — the GQA paper, this week's implementation target",
    "- **[Paper]** FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness — Dao et al. — https://arxiv.org/abs/2205.14135 — read for understanding, no need to implement the CUDA kernel",
    "- **[Blog]** Mixture of Experts Explained — Hugging Face — https://huggingface.co/blog/moe — survey-level MoE explainer matching this week's 'conceptual' scope",
   ], "If you want a from-scratch MoE reference without committing to implementing it: https://huggingface.co/blog/AviSoori1x/makemoe-from-scratch"),
23: ([
    "- **[Paper]** Scaling Laws for Neural Language Models — Kaplan et al. — https://arxiv.org/abs/2001.08361 — original scaling-law formulation (params/data/compute power laws)",
    "- **[Paper]** Training Compute-Optimal Large Language Models (Chinchilla) — Hoffmann et al. — https://arxiv.org/abs/2203.15556 — the paper to compare your own model's token budget against",
   ], "Compute where your GPT would sit on the Chinchilla compute-optimal frontier if scaled to 1B/10B params."),
24: ([
    "- **[Docs]** PEFT Quicktour — Hugging Face — https://huggingface.co/docs/peft/quicktour — practical LoRA fine-tune of an open model, this week's milestone",
    "- **[Paper]** LoRA: Low-Rank Adaptation of Large Language Models — Hu et al. — https://arxiv.org/abs/2106.09685 — read before using the library",
    "- **[Paper]** QLoRA: Efficient Finetuning of Quantized LLMs — Dettmers et al. — https://arxiv.org/abs/2305.14314 — 4-bit NF4 + LoRA",
    "- **[Docs]** Quantization overview (bitsandbytes/GPTQ/AWQ) — Hugging Face Transformers docs — https://huggingface.co/docs/transformers/main_classes/quantization",
   ], "Fine-tune the same base model with both full LoRA (16-bit) and QLoRA (4-bit) and compare memory/quality."),
25: ([
    "- **[Paper]** LoRA: Low-Rank Adaptation of Large Language Models — Hu et al. — https://arxiv.org/abs/2106.09685 — re-read sections 4 & 7 closely for the delta-W = BA math you're implementing",
    "- **[Repo]** loralib — Microsoft — https://github.com/microsoft/LoRA — minimal reference implementation to check your from-scratch version against",
   ], "Sweep rank r and plot trainable-param-count vs eval loss on your own GPT."),
26: ([
    "- No new external resources — pure integration of weeks 19-25 (BPE, RoPE, RMSNorm/SwiGLU, GQA, LoRA) inside your own modern-gpt repo.",
   ], "Write a short design-doc/README section mapping each modification to its source paper — good scaffolding for the Friday video."),
27: ([
    "- **[Docs]** PEFT Quicktour — Hugging Face — https://huggingface.co/docs/peft/quicktour — same doc as week 24, now for a real end-to-end fine-tune + evaluate pass with your own LoRA implementation",
    "- **[Paper]** QLoRA: Efficient Finetuning of Quantized LLMs — Dettmers et al. — https://arxiv.org/abs/2305.14314 — Guanaco eval methodology as a template for evaluating your fine-tune",
   ], "Compare your from-scratch LoRA fine-tune's outputs against a PEFT-library LoRA fine-tune of the same base model on the same data."),

28: ([
    "- **[Free book]** Introduction to Machine Learning Interviews — Chip Huyen — https://huyenchip.com/ml-interviews-book/ — free, and closer to research/ML-infra interview shape than generic ML-breadth prep",
    "- **[Book]** Designing Machine Learning Systems — Chip Huyen (O'Reilly 2022) — companion free booklet: https://github.com/chiphuyen/machine-learning-systems-design",
    "- **[Book]** Machine Learning System Design Interview — Ali Aminian & Alex Xu (ByteByteGo 2023) — 7-step framework + worked ML-serving-style problems",
   ], None),

29: ([
    "- **[Course]** Spinning Up in Deep RL — OpenAI — https://spinningup.openai.com/en/latest/ — Part 1 (RL intro) + Part 3 (policy gradient derivation), the cleanest free intro, code included",
    "- **[Repo]** spinningup vpg.py — OpenAI — https://github.com/openai/spinningup/blob/master/docs/algorithms/vpg.rst — reference implementation to check your bandit/gridworld policy-gradient code against",
   ], "Implement REINFORCE on a multi-armed bandit before attempting gridworld — isolates the policy-gradient math from credit-assignment-over-time complexity."),
30: ([
    "- **[Paper]** Proximal Policy Optimization Algorithms — Schulman et al. (2017) — https://arxiv.org/abs/1707.06347 — the PPO paper, focus on the clipped surrogate objective",
    "- **[Paper]** Training language models to follow instructions with human feedback (InstructGPT) — Ouyang et al., OpenAI (2022) — https://arxiv.org/abs/2203.02155 — the canonical SFT->RM->PPO pipeline diagram (Fig. 2) is exactly what you're asked to reproduce from memory",
    "- **[Blog]** Illustrating Reinforcement Learning from Human Feedback (RLHF) — Hugging Face — https://huggingface.co/blog/rlhf — accessible pipeline walkthrough, good complement before tackling the paper",
   ], None),
31: ([
    "- **[Paper]** Direct Preference Optimization: Your Language Model is Secretly a Reward Model — Rafailov et al. (2023) — https://arxiv.org/abs/2305.18290 — section 4 has the derivation you're asked to implement from",
    "- **[Paper]** Constitutional AI: Harmlessness from AI Feedback — Bai et al., Anthropic (2022) — https://arxiv.org/abs/2212.08073 — the RLAIF reference; SL-CAI + RL-CAI two-stage pipeline",
   ], None),
32: ([
    "- **[Docs]** TRL SFTTrainer — Hugging Face — https://huggingface.co/docs/trl/en/index — reference for pipeline shape (data formatting, loss masking) even if you write your own loop",
    "- **[Dataset]** Stanford Alpaca — tatsu-lab — https://github.com/tatsu-lab/stanford_alpaca — 52K instruction/response pairs, simple JSON format, good size for a small model SFT run",
   ], None),
33: ([
    "- **[Dataset/Reference]** Anthropic hh-rlhf — https://huggingface.co/datasets/Anthropic/hh-rlhf — study the chosen/rejected jsonl format as the schema to mimic (can be self-generated with two sampling temperatures + your own ranking)",
    "- **[Docs]** TRL DPOTrainer data format — Hugging Face — https://huggingface.co/docs/trl/en/index — confirms the exact prompt/chosen/rejected field names expected downstream in week 35",
   ], None),
34: ([
    "- **[Docs]** TRL RewardTrainer — Hugging Face — https://huggingface.co/docs/trl/en/index — scalar reward head over a base model, Bradley-Terry pairwise loss",
    "- **[Paper]** InstructGPT — Ouyang et al. — https://arxiv.org/abs/2203.02155 — section 3.2 covers reward model training and loss specifically",
   ], None),
35: ([
    "- **[Paper]** Direct Preference Optimization — Rafailov et al. — https://arxiv.org/abs/2305.18290",
    "- **[Docs]** TRL DPOTrainer — Hugging Face — https://huggingface.co/docs/trl/en/index — validate your from-scratch DPO loss against a known-correct implementation",
   ], "Report win-rate of DPO vs SFT vs base using your own GPT as an LLM-judge, foreshadowing Phase 6's eval-design work."),

36: ([
    "- **[Paper]** Show Your Work: Improved Reporting of Experimental Results — Dodge, Gururangan, Card, Schwartz, Smith (EMNLP 2019) — https://aclanthology.org/D19-1224/ — point-estimate comparisons mislead; report expected performance vs compute budget, directly informs the 'how I'll know it worked' template",
    "- **[Paper]** Deep Reinforcement Learning that Matters — Henderson et al. — https://arxiv.org/abs/1709.06560 — canonical demonstration of how much variance/seeds/hyperparameters swing reported results",
    "- **[Survey]** Benchmark Data Contamination of Large Language Models: A Survey — https://arxiv.org/abs/2406.04244 — current survey of contamination failure modes, needed before trusting any benchmark number",
    "- **[Checklist]** NeurIPS Paper Checklist Guidelines — https://neurips.cc/public/guides/PaperChecklist — field-standard checklist for what makes an ML experimental claim valid, reusable as the literal template",
   ], "Reproduce one small claim from the Dodge et al. paper's budget-vs-performance framing on your own Week 1 linear regression."),
37: ([
    "- **[Paper]** Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena — Zheng et al. — https://arxiv.org/abs/2306.05685 — the reference paper for LLM-as-judge methodology, biases (position/verbosity/self-enhancement), and mitigations",
    "- **[Framework]** HELM (Holistic Evaluation of Language Models) — Stanford CRFM — https://crfm.stanford.edu/helm/ — how to design a multi-metric eval instead of a single leaderboard number",
    "- **[Blog]** An LLM-as-Judge Won't Save The Product—Fixing Your Process Will — Eugene Yan — https://eugeneyan.com/writing/eval-process/ — practical pitfalls of eval design in real systems",
    "- **[Repo/Docs]** lm-evaluation-harness — EleutherAI — https://github.com/EleutherAI/lm-evaluation-harness — the standard open-source harness; read docs/task_guide.md to see how a real eval task is specified",
   ], "Sketch your week 38 eval (RoPE vs learned pos-emb) as a formal lm-eval-harness-style task spec, even if you run it with your own code."),
38: ([
    "- **[Repo/Docs]** lm-evaluation-harness — EleutherAI — https://github.com/EleutherAI/lm-evaluation-harness — reuse its task/metric structure to run your own controlled comparison consistently",
    "- **[Checklist]** NeurIPS Paper Checklist Guidelines — https://neurips.cc/public/guides/PaperChecklist — use again here as the pre-registration checklist before running the experiment",
   ], "Run the RoPE-vs-learned-positional comparison at 2-3 context lengths, not just one, to see if the effect is length-dependent."),
39: ([
    "- **[Essay]** How to Write a Great Research Paper — Simon Peyton Jones — https://simon.peytonjones.org/great-research-paper/ — seven concrete, ML-agnostic suggestions for getting an idea from your head into the reader's",
    "- **[Essay]** Ten Simple Rules for Structuring Papers — PLOS Comp Bio — https://journals.plos.org/ploscompbiol/article?id=10.1371%2Fjournal.pcbi.1003453 — practical structure rules (one point per paragraph, context-content-conclusion)",
    "- **[Essay]** Research as a Stochastic Decision Process — Jacob Steinhardt — https://cs.stanford.edu/~jsteinhardt/ResearchasaStochasticDecisionProcess.html — reframes what-to-work-on-next and de-risking; also directly reusable in Phase 8",
   ], "Have someone outside your immediate context read only your abstract/intro and try to restate your hypothesis and result back to you."),

40: ([
    "- **[Reference]** GPU Glossary (memory hierarchy, CUDA programming model, thread hierarchy) — Modal — https://modal.com/gpu-glossary — best free from-scratch primer on SM/warp/HBM/shared-memory concepts for ML engineers",
    "- **[Worklog]** How to Optimize a CUDA Matmul Kernel for cuBLAS-like Performance — Simon Boehm — https://siboehm.com/articles/22/CUDA-MMM — iteratively optimizes naive matmul to ~95% of cuBLAS, makes compute-vs-memory-bound concrete",
    "- **[Tutorial]** PyTorch Profiler recipe — PyTorch — https://docs.pytorch.org/tutorials/recipes/recipes/profiler_recipe.html — the tool needed to profile your matmul",
    "- **[Article]** Understanding Application Performance with Roofline Modeling — Towards Data Science — https://towardsdatascience.com/understanding-application-performance-with-roofline-modeling/ — arithmetic-intensity framework to classify compute- vs memory-bound",
   ], "Try Boehm's kernel progression yourself in a minimal CUDA or Triton snippet, not just read it."),
41: ([
    "- **[Docs]** Caching (KV cache) — Hugging Face Transformers — https://huggingface.co/docs/transformers/en/cache_explanation — official explanation of use_cache/past_key_values",
    "- **[Blog]** LLM Inference Series: 3. KV caching explained — Pierre Lienhart — https://medium.com/@plienhar/llm-inference-series-3-kv-caching-unveiled-048152e461c8 — why KV cache turns per-token cost from quadratic to linear",
    "- **[Blog/code]** Inference Server From Scratch — Part 2: Real Model — Pavel Belevich — https://medium.com/@pbelevich/inference-server-from-scratch-part-2-real-model-c69b803d59ee — a real greedy_generate() loop to study/adapt",
   ], "Log wall-clock time for the prefill step vs each decode step separately to see the asymmetry firsthand."),
42: ([
    "- **[Paper]** Orca: A Distributed Serving System for Transformer-Based Generative Models — Yu et al., OSDI 2022 — https://www.usenix.org/conference/osdi22/presentation/yu — the iteration-level/continuous batching paper",
    "- **[Paper]** Efficient Memory Management for Large Language Model Serving with PagedAttention (vLLM) — Kwon et al. — https://arxiv.org/abs/2309.06180",
    "- **[Paper+repo]** FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness — Dao et al. — https://arxiv.org/abs/2205.14135 (repo: https://github.com/dao-ailab/flash-attention)",
    "- **[Docs]** vLLM Optimization and Tuning — https://docs.vllm.ai/en/stable/configuration/optimization/ — concrete knobs (max-num-seqs, max-num-batched-tokens) that map straight to the batching concepts",
   ], "Read 'Inside vLLM: Anatomy of a High-Throughput LLM Inference System' to see how a production system combines all of the above: https://vllm.ai/blog/2025-09-05-anatomy-of-vllm"),
43: ([
    "- **[Interactive book]** The Ultra-Scale Playbook: Training LLMs on GPU Clusters — Hugging Face (nanotron) — https://huggingface.co/spaces/nanotron/ultrascale-playbook — grounded in 4,000+ real scaling experiments; covers DP/TP/PP/context-parallel/ZeRO in one place",
    "- **[Docs]** Parallelism methods — Hugging Face Transformers — https://huggingface.co/docs/transformers/en/perf_train_gpu_many",
    "- **[Tutorial]** Getting Started with FSDP — PyTorch — https://docs.pytorch.org/tutorials/intermediate/FSDP1_tutorial.html (note: FSDP2 is now current)",
    "- **[Docs]** NCCL documentation — NVIDIA — https://docs.nvidia.com/deeplearning/nccl/ — reference for what's actually moving data between GPUs under DDP/FSDP",
   ], None),
44: ([
    "- **[Blog/code]** Inference Server From Scratch — Part 1: OpenAI API — Pavel Belevich — https://pbelevich.github.io/2025/09/10/Inference_Server_From_Scratch_-_Part_1.html — builds a minimal FastAPI server speaking the OpenAI /v1/chat/completions wire format, streamed via SSE, a near-exact match for this week's milestone",
    "- **[Docs]** FastAPI StreamingResponse — used throughout the above and in most LLM-serving tutorials for token-by-token output",
   ], "Match the OpenAI wire format so any OpenAI-client library can hit your server later."),
45: ([
    "- **[Paper]** Orca: A Distributed Serving System for Transformer-Based Generative Models — Yu et al. — https://www.usenix.org/conference/osdi22/presentation/yu — iteration-level scheduling is the core idea here",
    "- **[Docs]** vLLM scheduling/continuous-batching docs — https://docs.vllm.ai/en/stable/configuration/optimization/",
    "- **[Blog]** Inside vLLM: Anatomy of a High-Throughput LLM Inference System — https://vllm.ai/blog/2025-09-05-anatomy-of-vllm — shows the schedule -> execute -> postprocess loop, a direct model for your own scheduler",
   ], "Write the 'scheduler ~ matching engine, TTFT ~ tick-to-trade' mapping as a one-page design note before writing code — forces the trading-domain transfer to be explicit, not just a metaphor."),
46: ([
    "- **[Handbook]** Key metrics for LLM inference — BentoML LLM Inference Handbook — https://bentoml.com/llm/llm-inference-basics/llm-inference-metrics — defines TTFT/TPOT/throughput precisely",
    "- **[Blog]** LLM Inference SLO Engineering: TTFT, ITL, and P99 Latency Budgets for Production AI — Spheron — https://www.spheron.network/blog/llm-inference-slo-ttft-itl-latency-budget-guide-2026/ — directly frames P50/P95/P99/P99.9 tradeoffs",
    "- **[Blog]** LLM Benchmarking: Latency, Throughput, TTFT, TPS — Neel Mishra — https://neelmishra.github.io/blog/mlops/llm-inference/inference-benchmarking.html",
   ], "Compare your P50/P99 methodology against vLLM's own benchmark_serving.py (in the vLLM repo) as a reference implementation, without depending on vLLM itself."),
47: ([
    "- **[Paper]** Efficiently Scaling Transformer Inference — Pope et al. (Google), MLSys 2023 Outstanding Paper — https://arxiv.org/abs/2211.05102 — gold-standard example of a rigorous latency/throughput/MFU writeup; model your llm-engine writeup's structure on this paper's Pareto-frontier framing",
   ], "Reuse week 46's metrics resources for the benchmark-harness section of the writeup."),

48: ([
    "- **[Paper]** Efficient Memory Management for Large Language Model Serving with PagedAttention (vLLM) — Kwon et al., SOSP 2023 — https://arxiv.org/abs/2309.06180 — reference architecture for KV-cache memory management",
    "- **[Paper]** Orca: A Distributed Serving System for Transformer-Based Generative Models — Yu et al., OSDI 2022 — https://www.usenix.org/conference/osdi22/presentation/yu — introduces continuous/iteration-level batching, the direct analogue of matching-engine order-by-order processing vs batch auctions",
    "- **[Paper]** SARATHI: Efficient LLM Inference by Piggybacking Decodes with Chunked Prefills — Agrawal et al. — https://arxiv.org/abs/2308.16369 — chunked-prefill scheduling, useful for interleaving big and small jobs fairly",
    "- **[Paper]** Efficiently Scaling Transformer Inference — Pope et al. — https://arxiv.org/abs/2211.05102 — classic latency/FLOPs-utilization tradeoff analysis for large-model serving",
    "- **[Paper]** SLO-Aware Scheduling for Large Language Model Inferences — Huang et al. (2025) — https://arxiv.org/abs/2504.14966 — recent SLO/tail-latency-aware scheduler design, closest match to 'hit a P99 target under bursty load'",
    "- **[Paper]** A Predictive and Synergistic Two-Layer Scheduling Framework for LLM Serving — (2025) — https://arxiv.org/abs/2509.23384 — two-layer (engine + cluster) SLO-aware batching/routing, a comparison point for your own scheduler design",
    "- **[Talk]** How NOT to Measure Latency — Gil Tene, QCon/Azul — https://www.youtube.com/watch?v=lJ8ydIuPFeU — the 'Coordinated Omission' problem; watch before designing any P99/P999 measurement, directly reusable from your trading background",
   ], "No single canonical paper yet bridges LLM-serving scheduling and market-microstructure queueing theory — that gap is itself the novelty angle for this research question. Skim the vLLM v0.6.0 performance blog (https://blog.vllm.ai/2024/09/05/perf-update.html) for a benchmarking-methodology template."),
49: ([
    "- **[Guide]** SIGPLAN Empirical Evaluation Guidelines — https://www.sigplan.org/Resources/EmpiricalEvaluation/ — checklist of patterns/anti-patterns for systems-paper evaluations, use to design the controlled experiment",
    "- **[Guide]** How to Do Statistical Evaluations in ECE/CS Papers: A Practical Playbook for Defensible Results — Krishnamachari — https://arxiv.org/abs/2605.00428 — claim -> design -> analysis -> reporting chain; apply directly to baseline vs policy comparison",
    "- **[Talk]** How NOT to Measure Latency — Gil Tene (see week 48) — re-watch when defining the experiment's measurement protocol, not just when reading about it",
   ], None),
50: ([
    "- **[Reference]** vLLM benchmark harness / methodology (ShareGPT-based, TTFT/ITL/P99) — https://blog.vllm.ai/2024/09/05/perf-update.html — concrete example of load-generation + percentile logging to mirror for your own llm-engine",
    "- **[Guide]** SIGPLAN Empirical Evaluation Guidelines (reuse from week 49) — for iterating on results without p-hacking the ablations",
   ], None),
51: ([
    "- **[Guide]** How to Do Statistical Evaluations in ECE/CS Papers (reuse from week 49) — https://arxiv.org/abs/2605.00428 — its guidance on investigating anomalous/outlier results defensibly rather than discarding them",
    "- **[Talk]** How NOT to Measure Latency — Gil Tene — Coordinated Omission is the single most likely explanation for a weird tail-latency anomaly; check for it first",
   ], None),
52: ([
    "- **[Guide]** Notes On Writing Effective Empirical Software Engineering Papers: An Opinionated Primer — https://arxiv.org/abs/2506.11002 — practical, short guide to structuring the writeup (claims -> evidence -> limitations)",
    "- **[Example]** vLLM Blog performance posts — https://blog.vllm.ai/2024/09/05/perf-update.html — model for a short, credible, benchmarks-first systems writeup/blog post rather than a full academic paper",
   ], "Cross-post the final writeup's abstract as the closing summary of your Friday video series."),
}

TEMPLATE = """# Week {n:02d} — {phase}

**Topic:** {topic}

## Goals
{goals}

## Resources
{resources}
{stretch}

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
    res_lines, stretch = RESOURCES.get(n, ([], None))
    resources_md = "\n".join(res_lines) if res_lines else "- (none needed this week)"
    stretch_md = f"\n**Stretch:** {stretch}" if stretch else ""
    text = TEMPLATE.format(n=int(n), phase=phase, topic=topic, goals=goals_md,
                            resources=resources_md, stretch=stretch_md, milestone=milestone)
    with open(f"weeks/week-{int(n):02d}.md", "w") as f:
        f.write(text)

print(f"Generated {len([k for k,v in WEEKS.items() if v])} week files.")
