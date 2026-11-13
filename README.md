# Enhancing PyCEFR Analysis with Qwen3-4B

**Generating Natural-Language Explanations of Python Programming Concepts**

This repository contains the materials for a final course project at East China University of Science and Technology (ECUST). The project combines **PyCEFR**, a static-analysis tool that assigns CEFR-inspired categories (A1–C2) to detected Python programming constructs, with **Qwen3-4B** to generate beginner-friendly explanations of structured analysis results.

The aim is to examine whether an LLM can explain PyCEFR output while **preserving its factual information**. This project does **not** train a new model, estimate a student's programming proficiency, or independently validate PyCEFR's construct classifications.

## Project Workflow

1. **Prepare data:** Create 30 short Python source files with different language constructs.
2. **Analyze code:** Run PyCEFR to obtain structured JSON records containing detected CEFR-inspired levels and programming concepts.
3. **Derive reference labels:** Calculate counts, totals, the most frequent level, and the highest detected level from the PyCEFR records.
4. **Generate explanations:** Provide each PyCEFR record to pretrained Qwen3-4B using a zero-shot prompt. Generation was performed in Google Colab on an NVIDIA T4 GPU with 4-bit model loading.
5. **Evaluate factual consistency:** Compare the generated text against four PyCEFR-derived reference fields, using an evaluation script and manual review where automated extraction is ambiguous.

**Pipeline:** Python samples → PyCEFR analysis → structured JSON → Qwen3-4B explanation → factual evaluation against PyCEFR-derived labels.

## Dataset and Reference Labels

The evaluation set contains **30 author-prepared Python files**. The derived reference data records:

- Total number of detected programming elements
- Counts at A1, A2, B1, B2, C1, and C2
- Most frequent detected level
- Highest detected level

The 30 files contain **1,075 PyCEFR-detected elements** in total. These labels are derived from PyCEFR's output; they are **not independent expert-annotated ground truth**. A1 is the most frequent category in every file, which limits what can be concluded from the most-frequent-level accuracy.

## Model and Prompting

- **Model:** Qwen3-4B (pretrained)
- **Approach:** Zero-shot prompting; no fine-tuning
- **Environment:** Google Colab, NVIDIA T4 GPU
- **Model loading:** 4-bit quantization with BitsAndBytes and Hugging Face Transformers
- **Input:** Per-file PyCEFR JSON record
- **Output:** Six-part natural-language explanation covering totals, level distribution, most frequent level, highest detected level, programming concepts, and overall interpretation

Prompt versions and saved output artifacts are organized under `results/`. Development-time prompt revisions were not evaluated as a controlled prompt-comparison experiment.

## Results

Each of the 30 model explanations was checked on four factual criteria (**120 checks** in total). The final counts below reflect manual adjudication of ambiguous automatic results.

| Evaluation criterion | Correct / 30 | Accuracy |
| --- | ---: | ---: |
| Total number of elements | 25 | 83.33% |
| CEFR level distribution | 29 | 96.67% |
| Most frequent level | 30 | 100.00% |
| Highest detected level | 28 | 93.33% |
| **All factual checks** | **112 / 120** | **93.33%** |

The main errors involved incorrect arithmetic, incomplete level distributions, and incorrect highest-level identification. For example, for `sample27.py`, the generated explanation reported **56** elements when the PyCEFR-derived total was **60**.

**Interpretation:** The 93.33% figure measures agreement with four selected fields in PyCEFR output. It is **not** an assessment of educational effectiveness, explanation readability, Python-code correctness, or the validity of PyCEFR's CEFR-inspired categories. The result comes from one evaluated model run on a small, purpose-built dataset.

## Repository Structure

```text
.
├── .github/workflows/     # GitHub workflow files
├── DATA_CSV/              # Tabular data produced or used by the analysis
├── DATA_JSON/             # PyCEFR dataset and summary JSON records
├── pycefr_dataset/        # Prepared Python sample files / dataset materials
├── results/               # Prompts, generated explanations, and evaluation results
├── src/                   # Source code
├── README.md
├── CITATION.MD
├── LICENSE
└── .gitignore
```

## Reproducing the Evaluation

The intended order of work is:

1. Prepare or retrieve the Python samples under `pycefr_dataset/`.
2. Run the PyCEFR analysis to produce the JSON records in `DATA_JSON/`.
3. Derive the reference-label CSV from those records.
4. Generate or load the saved Qwen3-4B explanations from `results/`.
5. Run the factual-evaluation script and manually inspect cases flagged as ambiguous.
6. Compare the final results with the per-field summary above.

**Reproducibility note:** Exact installation commands and script arguments depend on the committed implementation. The reported experiment did not preserve every dependency version, model revision, or text-generation setting, so full run-to-run reproduction cannot be guaranteed from the available records.

## Limitations and Future Improvements

The experiment uses a small, non-random dataset and one evaluated model run. The most frequent level is A1 for all 30 samples, and factual checks do not independently assess the pedagogical quality of explanations.

Two proposed improvements are:

1. **Deterministic precomputation:** Calculate numerical fields in Python before asking the LLM to explain them.
2. **Post-generation validation:** Check the generated explanation against the original structured record and flag mismatches or omissions.

These improvements are proposals; they were **not implemented or evaluated** as part of the reported 93.33% result.

## Attribution and References

This project uses **PyCEFR**, developed and published by its original authors. Please retain the upstream attribution and applicable license terms for any reused code. The Qwen3-4B model is also an independently developed pretrained model; this repository does not claim ownership of it.

- Robles, G., et al. (2022). *pycefr: Python Competency Level through Code Analysis*. Proceedings of the 30th IEEE/ACM International Conference on Program Comprehension, 173–177. https://doi.org/10.1145/3524610.3527878
- Yang, A., et al. (2025). *Qwen3 Technical Report*. https://arxiv.org/abs/2505.09388

## Project Context

Final course report — **Theory and Practice of Big Language Model**, East China University of Science and Technology (2026).
