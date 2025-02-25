# :rocket: Mafin2.5-FinanceBench

This repository contains the results of our finance benchmark evaluations using our Mafin2.5 system. These evaluations are based on the FinanceBench benchmark as introduced in the paper 
📄 [FinanceBench: A New Benchmark for Financial Question Answering](https://arxiv.org/pdf/2311.11944).

### Mafin2.5 Introduction

**Mafin2.5** is our latest **financial AI model**, built on **Vectify’s RAG 3.0 framework**, which enhances performance through **reinforcement learning (RL) with Monte Carlo Tree Search (MCTS)**. This approach improves **multi-step reasoning, retrieval accuracy, and financial task automation**.  

**Mafin1**, our earlier model, focused on **fine-tuning embedding models** for financial AI. For a detailed explanation, refer to our technical report:  📄 **[Mafin: Enhancing Black-Box Embeddings with Model-Augmented Fine-Tuning](https://arxiv.org/abs/2402.12177)**.  This foundational work laid the groundwork for **embedding optimization and improved knowledge retrieval** in financial applications.  


### Benchmark Overview

[FinanceBench](https://arxiv.org/pdf/2311.11944) is a pioneering test suite designed to evaluate the performance of large language models (LLMs) on open-book financial question answering (QA). It includes questions about publicly traded companies, each accompanied by corresponding answers and evidence strings. 
It has the following key features:
- **Ecologically valid questions:** Covers a diverse set of scenarios relevant to publicly traded companies.
- **Model evaluation:** Includes assessment of 16 state-of-the-art model configurations such as GPT-4.
- **Limitations identified:** Highlights the limitations of current LLMs for financial QA, including hallucinations and refusal to answer.

### Evaluation Protocol  

We follow a **realistic and practical evaluation setup**, where all documents are stored in a **single database**, and Mafin2.5 is tested on the [FinanceBench public set](https://github.com/patronus-ai/financebench). This approach ensures that our model is evaluated under conditions that closely resemble real-world financial applications.  For transparency, we have **open-sourced our evaluation code** in **[Evaluation Code](https://github.com/VectifyAI/Mafin2.5-FinanceBench/blob/main/eval.py)**.  

In cases where questions are **ambiguous, have multiple valid answers, or are deemed invalid**, we rely on **expert human annotations** to ensure fair and accurate evaluation. For more details, see **[Human Evaluation](https://github.com/VectifyAI/Mafin2.5-FinanceBench/tree/main/human_evaluations)**.


## Results
### 1. Mafin Model Evolution
![evolution](https://github.com/user-attachments/assets/a7f78677-64ac-4bc6-9311-6dfc8bc19033)


This figure showcases the progression of Mafin models, highlighting the significant improvement in accuracy from **Mafin 1 to Mafin 2.5**. The latest iteration, **Mafin 2.5**, achieves a remarkable accuracy of **98.7%**, demonstrating major advancements in reasoning and retrieval capabilities.


### 2. Mafin2.5 Performance Across Base Models
<img width="1020" alt="comparison" src="https://github.com/user-attachments/assets/f98957f4-dcdd-45fb-807e-198cb73b9452" />


As a RAG 3.0 model, Mafin 2.5 is capable of leveraging different base models while maintaining **consistent high performance (98.7%)**. The above figure illustrates its effectiveness across **ChatGPT 4o** and **Deepseek v3**, indicating that its strong performance is **independent of the underlying LLM**. Notably, **Deepseek v3 is a privately deployable model**, offering an alternative for organizations requiring on-premise or self-hosted AI solutions.


### 3. Comparison with Market Players

![sandian8](https://github.com/user-attachments/assets/469e2df8-64b5-4a15-9427-be83719dac2d)





<div align="center">

| Method               | Accuracy (%) | Full Benchmark? (Coverage) |  Results Public? | Source |
|----------------------|-------------|----------------------------|-----------------|--------|
| Mafin2.5           | **98.7**      | **Yes (100%)**             | **Yes**         | [link](https://github.com/VectifyAI/Mafin2.5-FinanceBench) |
| Quantly             | 94           | **Yes (100%)**             |  No              | [link](https://quantly.substack.com/p/evaluation-of-quantly-on-financebench) |
| Fintool             | 98           | No (66.7%)                 |  No              | [link](https://fintool.com/benchmark/chatgpt-versus-fintool) |
| ChatGPT 4o + Search | 31           | No (66.7%)                 |  No              | [link](https://fintool.com/benchmark/chatgpt-versus-fintool) |
| Perplexity          | 45           | No (66.7%)                 |  No              | [link](https://fintool.com/benchmark/perplexity-versus-fintool) |

</div>

This benchmark comparison demonstrates **Mafin 2.5's superiority** over competitors, achieving the **highest accuracy (98.7%)** while covering the **full benchmark (100%)**. Unlike some competitors that only evaluate on **partial benchmarks**, Mafin 2.5 provides a **comprehensive** and **rigorous** assessment.





### Key Takeaways
1. **Mafin 2.5 demonstrates massive improvements over previous versions**, significantly increasing accuracy from **Mafin 1 (38.0%) to Mafin 2.5 (98.7%)**, showcasing strong advancements in financial AI reasoning.
2. **Mafin 2.5 is highly adaptable across different base models**, achieving **identical high performance (98.7%)** on both **ChatGPT 4o (public cloud) and Deepseek v3 (private deployable)**, making it flexible for various deployment needs.
3. **Mafin 2.5 outperforms market competitors while covering the full benchmark (100%)**, ensuring a **more comprehensive and fair evaluation** compared to models that only test on 66.7% of the dataset.



## Limitations of the Current Benchmark  

1. **Errors and Ambiguities in Evaluation**  
   The current benchmark may contain inconsistencies, ambiguities, or errors in ground truth answers, which can lead to misleading performance evaluations. These issues must be addressed to ensure a fair and reliable assessment of AI capabilities. Establishing a more rigorous annotation and validation process is essential for improving benchmark accuracy.

2. **Lack of Multi-Document Reasoning Tasks**  
   The current benchmark primarily focuses on simple retrieval tasks based on a single document. However, real-world financial applications require more advanced reasoning capabilities, including multi-step retrieval across multiple documents. To improve the benchmark, we call for the inclusion of complex reasoning tasks that better reflect real-world decision-making and analysis.


## Contact
If you have questions about these results or want to try our model, email us at contact@vectify.ai.
