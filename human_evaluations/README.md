# Human Evaluations

This folder contains the human evaluation results for Mafin 2.5 with GPT-4o and DeepSeek-V3 as base models.

Below is the labeling system we used in the human evaluations.

### Labels:

- **AL** (_Answers Aligned_)
  - Mafin’s answer aligns with the benchmark answer, both in terms of conclusion and methodology.
- **NAL** (_Not Aligned_)
  - Mafin’s answer does not align with the benchmark answer, due to either failing to find the necessary data or misinterpreting retrieved data.
- **BE** (_Benchmark Error_)
  - The benchmark answer contains incorrect or misleading figures and results, while Mafin's answer is valid and supported by evidence.
- **MVA** (_Multiple Valid Approaches_)
  - Mafin and the benchmark used different valid methodologies or perspectives to address the problem.
- **SEDC** (_Same Evidence Different Conclusion_)
  - Mafin and the benchmark used the same evidence but arrived at different valid conclusions, due to differences in interpretation, reasoning, or framing of the question.
