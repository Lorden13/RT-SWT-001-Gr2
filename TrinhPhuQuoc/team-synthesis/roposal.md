# Research Proposal

**Title:** Evaluating LoRA Fine-Tuned LLaMA-3-8B for Automated BDD Test Generation from Connextra User Stories

**Team:** Group 2  
**Members:**  
1. Ngô Đình Khoa (SE196737)  
2. Trịnh Phú Quốc (SE190287)  
3. Trần Đăng Khoa (SE194398)  
4. Đặng Đỗ Cao Sang (SE193269)  
5. Đào Lý Phi Hùng (SE172826)  
**Topic Code:** RT-SWT-SE1905  
**Submission Date:** 2026-06-14  
**Version:** 1.0  
**Status:** Pending Approval

---

## 2. Research Problem Statement

### 2.1 Background & Importance

Behavior-Driven Development (BDD) is an Agile software development methodology that fosters collaboration among developers, testers, and business stakeholders by defining system requirements in structured, human-readable Gherkin scenarios (written in `Given-When-Then` format). By bridging the gap between natural language requirements and executable tests, BDD ensures that the software behaves exactly as specified by the business. However, manually authoring Gherkin scenarios and translating them into corresponding test code—commonly known as step definitions—is a time-consuming, error-prone process that demands significant engineering effort (Fernandes et al. 2025). 

To optimize this process, automated BDD test generation has emerged as a key area of interest in software engineering research. Leveraging large language models (LLMs) to automatically generate Gherkin scenarios and step definitions directly from user stories promises to accelerate testing cycles and ensure consistency between documentation and code. This automated generation is particularly valuable when user stories follow the standardized Connextra format (`As a [role], I want [feature], so that [benefit]`), as it provides a structured context that LLMs can exploit for test generation (Rathnayake et al. 2026).

Evaluating LLM-based BDD generation is crucial for software testing teams seeking to adopt AI-assisted workflows. While proprietary frontier models such as GPT-4o have demonstrated strong zero-shot capabilities, their deployment is often constrained by concerns over data privacy, proprietary source code leakage, and high API costs. Consequently, fine-tuning smaller, open-source models like LLaMA-3-8B using parameter-efficient fine-tuning (PEFT) methods like Low-Rank Adaptation (LoRA) has become a compelling alternative (Selfbehave et al. 2026). Demonstrating that a local, fine-tuned open-source model can achieve performance comparable to a frontier commercial model would allow organizations to deploy cost-effective, secure, and fully customized BDD test generation pipelines. This research is important for both academic researchers investigating AI-assisted software engineering and industrial software testing teams seeking practical automation solutions.

### 2.2 State of the Art

Several recent studies have investigated the application of LLMs to automated test generation, exploring different models, prompting strategies, and evaluation metrics.

Fernandes et al. (2025) evaluated the performance of multiple LLMs—including GPT-3.5, GPT-4, LLaMA-3, Phi-3, Gemini, and DeepSeek R1—in generating Gherkin scenarios from a dataset of 34 user stories in the FinTech domain. The study measured semantic quality using the METEOR score and found that Gemini zero-shot achieved the highest score of 0.84. However, the study was limited to Gherkin scenario generation alone (excluding step definitions) and evaluated only a small-scale, single-domain dataset.

Rathnayake et al. (2026) addressed the data limitation by presenting a dataset of 500 real-world agile user stories, complete with requirement descriptions and manual BDD scenarios. Using GPT-4o under a zero-shot prompting configuration, the author evaluated semantic similarity using BERTScore and Cosine Semantic Similarity, achieving a BERTScore of 91.16% and a Cosine Similarity of 53.96%. Although this study established a strong benchmark on a realistic dataset, it only generated Gherkin feature files without the accompanying executable step definitions, leaving the downstream test execution gap unaddressed.

Karpurapu et al. (2024) focused on syntax correctness, evaluating GPT-3.5, GPT-4, Llama-2, and PaLM-2 in generating Gherkin syntax. Using `gherkin-lint` as the validation metric, the author reported a 100% syntax accuracy rate for GPT-4 and a 92% rate for Llama-2 under a few-shot setting. However, this evaluation did not verify the executable nature of the generated code (such as checking python step definitions) and did not perform any semantic comparisons against expert baseline tests.

Selfbehave et al. (2026) explored fine-tuning LLaMA-3-8B using LoRA for BDD test generation, measuring correctness via Gherkin syntax compilation rates. The study demonstrated that the fine-tuned LLaMA-3-8B model could achieve a syntax compilation rate of 99.2%. Nevertheless, a major limitation of this work was its reliance on synthetic datasets generated via self-instruct prompting rather than real-world multi-domain user stories, which may not reflect the complexity and ambiguity of actual industrial requirements.

### 2.3 GAP

Based on a synthesis of 15 primary studies in the domain of automated BDD test generation, the following research GAPs have been identified:

#### Primary GAP (GAP-T)
*   **GAP Statement:** Co-generation of Gherkin Scenarios and Step Definitions from Connextra User Stories using modern LLMs.
*   **Unresolved Reason:** Prior works focus almost exclusively on generating Gherkin scenarios independently. The co-generation of both the structured feature descriptions (Gherkin) and their corresponding executable test code (step definitions) in a single workflow remains unexplored for modern LLMs.
*   **Supporting Papers:** 14 out of 15 reviewed studies (e.g., Fernandes et al. 2025, Rathnayake et al. 2026, dos Santos et al. 2026) did not attempt or evaluate co-generation.

#### Secondary GAP (GAP-M)
*   **GAP Statement:** Absence of a dual static validation mechanism (combining Gherkin Parser Validation and Python AST Validation) prior to semantic similarity evaluation.
*   **Unresolved Reason:** Existing studies evaluate semantic similarity or syntax correctness in isolation. No study implements a dual-filter static validation pipeline to filter out syntactically invalid artifacts before computing semantic similarity (Cosine Similarity) against expert-written baselines, leading to potentially misleading semantic scores on unparseable code.
*   **Supporting Papers:** 15 out of 15 reviewed studies (e.g., Karpurapu et al. 2024, Tesfalidet et al. 2025) lack an integrated dual-parser static validation step.

#### Supporting GAP (GAP-D)
*   **GAP Statement:** Lack of empirical evaluation on large-scale, multi-domain, real-world agile datasets.
*   **Unresolved Reason:** The majority of studies rely on synthetic, closed, or small-scale (e.g., 5 to 34 samples) datasets from a single domain. This limits the generalizability of their findings to realistic industrial software engineering contexts.
*   **Supporting Papers:** 13 out of 15 reviewed studies (excluding Rathnayake et al. 2026) suffer from small-scale or synthetic dataset limitations.

### 2.4 Motivation

If these GAPs remain unresolved, software development teams will continue to face high integration barriers when adopting AI-generated testing. Generating Gherkin scenarios without step definitions provides only half-automated testing, forcing QA engineers to manually write boilerplate python code, which defeats the purpose of end-to-end automation. Furthermore, evaluating LLMs without a dual static validation filter risks deploying code that contains basic syntax errors, which wastes execution resources and decreases developer trust.

Evaluating whether a fine-tuned, open-source model (LLaMA-3-8B LoRA-FT) can achieve performance comparable to a frontier proprietary model (GPT-4o) on real-world datasets is critical. If successful, it establishes that cost-effective, local models can be reliably deployed for complex code-and-specification co-generation tasks, resolving data security concerns and API dependencies for software testing teams globally. This study therefore aims to provide empirical evidence for the practical adoption of open-source LLMs in end-to-end BDD automation workflows.

---

## 3. Related Work

### 3.1 Overview

The following table summarizes the primary studies most relevant to automated Gherkin scenario and step definition generation:

| Paper | Tool / LLM | Dataset (Size) | Metric | Best Result | Limitation |
|:---|:---|:---|:---|:---|:---|
| **Rathnayake et al. 2026** | GPT-4o (Zero-shot) | 500 User Stories | BERTScore, Cosine Semantic Similarity | BERTScore = 91.16%, Cosine = 53.96% | Excluded step definition generation; no dual static validation. |
| **Fernandes et al. 2025** | GPT-3.5, GPT-4, LLaMA-3, Phi-3, Gemini, DeepSeek R1 | 34 User Stories | METEOR Score | METEOR = 0.84 (Gemini zero-shot) | Evaluated Gherkin scenario generation only; small single-domain dataset. |
| **Selfbehave et al. 2026** | LLaMA-3-8B (LoRA-FT) | Synthetic Dataset | Syntax compilation rate | 99.2% Gherkin syntax accuracy | Relied entirely on synthetic (AI-generated) datasets. |
| **Karpurapu et al. 2024** | GPT-3.5, GPT-4, Llama-2, PaLM-2 | Small sample | Syntax accuracy via `gherkin-lint` | 100% syntax accuracy (GPT-4) | No step definition validation; no semantic similarity evaluation. |
| **Tesfalidet et al. 2025** | GPT-4 | 10–20 User Stories | Cosine Similarity, Behave execution rate | Similarity = 0.81, Executable rate = 85% | Small sample size; restricted to Fintech domain; no dual parser check. |
| **dos Santos et al. 2026** | ChatGPT, Gemini, Grok, GitHub Copilot | 34 User Stories | Acceptance criteria coverage, Accuracy | High coverage for ChatGPT | Small dataset size; generated Gherkin scenarios only (no step code). |
| **Mendoza et al. 2024** | ChatGPT-4, ChatGPT-3.5, Gemini, Copilot | 5 User Stories | Likert scale (human evaluation) | High human acceptability | Tiny dataset size; subjective evaluation prone to bias. |
| **Bergsmann et al. 2024** | Multi-Agent LLMs | Small-scale web apps | Test generation success rate | High success rate | Relied on complex, high-latency, and costly multi-agent systems. |

### 3.2 Pattern Analysis

*   **Observation 1:** *Most studies evaluate semantic quality using similarity-based metrics.* As demonstrated in Fernandes et al. (2025) and Rathnayake et al. (2026), metrics such as METEOR, BERTScore, and Cosine Semantic Similarity are widely used to assess how closely AI-generated Gherkin scenarios match expert-written ground truth tests.
*   **Observation 2:** *Most datasets contain fewer than 50 user stories.* Except for Rathnayake et al. (2026), which introduced a 500-sample benchmark, related works such as Fernandes et al. (2025), dos Santos et al. (2026), and Mendoza et al. (2024) rely on extremely small datasets (ranging from 5 to 34 stories), limiting external validity.
*   **Observation 3:** *Few studies evaluate complete BDD artifact generation.* The majority of research focuses on Gherkin feature file generation alone (e.g., Fernandes et al. (2025), Karpurapu et al. (2024)). Studies that attempt step definition generation (e.g., Tesfalidet et al. (2025)) rarely combine Gherkin parsing and code execution validation under a unified static check.
*   **Observation 4:** *Open-source LLM fine-tuning remains underexplored.* While commercial API-driven models are heavily represented in literature, only a few studies (e.g., Selfbehave et al. (2026)) explore the fine-tuning of open-source models like LLaMA-3, and these studies often rely on synthetic rather than real-world user stories.

### 3.3 GAP Mapping

The following table maps the identified research GAPs to the reviewed literature evidence and confirms their status:

| GAP | Evidence | Status |
|:---|:---|:---|
| **GAP-T (Technology)** | 15 reviewed studies; no study evaluates co-generation of Gherkin scenarios and Step Definitions | Confirmed |
| **GAP-M (Metric)** | 15 reviewed studies; no study combines Gherkin Parser Validation and Python AST Validation | Confirmed |
| **GAP-D (Dataset)** | 13 out of 15 reviewed studies rely on synthetic or small-scale datasets, highlighting a gap in empirical evaluation on realistic, multi-domain agile user stories. | Confirmed |

---

# 4. Research Questions & PICO

## 4.1 Main Research Question

Can a LoRA fine-tuned LLaMA-3-8B co-generate Gherkin scenarios and step definitions that achieve semantic similarity ≥ 0.85 and executable syntax rate ≥ 85%, while providing performance comparable to GPT-4o zero-shot generation?

This main research question investigates the feasibility of employing a smaller, parameter-efficiently fine-tuned open-source large language model (LLaMA-3-8B LoRA-FT) as a secure and cost-effective alternative to state-of-the-art commercial API-based models (such as GPT-4o zero-shot) for automated specification and test code generation. By establishing quantitative performance thresholds for semantic similarity and syntactic executability, this study aims to determine if local, open-source model interventions can achieve a practical quality level that meets expert standards without relying on cloud-based commercial services.

## 4.2 Sub-Research Questions

### RQ1 – Semantic Similarity

Does LLaMA-3-8B LoRA-FT achieve a Cosine Semantic Similarity score of at least 0.85 compared with expert-written BDD scenarios?

This sub-question evaluates the semantic alignment of the generated Gherkin test scenarios with expert-written reference standards (Ground Truth). By computing the Cosine Similarity over SBERT embeddings (`all-MiniLM-L6-v2`), the analysis measures whether the model-generated tests capture the correct business logic and acceptance criteria described in the Connextra user stories.

---

### RQ2 – Executable Syntax Rate

Does LLaMA-3-8B LoRA-FT achieve an Executable Syntax Rate of at least 85% after Gherkin Parser Validation and Python AST Validation?

This sub-question evaluates the structural correctness and compilation capability of the co-generated specifications and test code. Using Gherkin parser validation and Python AST syntax tree checks, this metric guarantees that the generated test suite is executable and free from static compilation errors prior to runtime execution.

---

### RQ3 – Comparative Evaluation

Is there a statistically significant difference between LLaMA-3-8B LoRA-FT and GPT-4o in terms of semantic similarity and executable syntax rate?

This sub-question evaluates whether there is a statistically significant difference between the performance of LLaMA-3-8B LoRA-FT and GPT-4o in terms of semantic similarity and executable syntax rate. The results provide empirical evidence regarding whether the observed performance differences between the two models are statistically significant.

## 4.3 PICO Framework

| Element          | Description                                                                                                                                                                                    |
| ---------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Population (P)   | 100 randomly sampled Connextra-format User Stories selected from the Rathnayake et al. (2026) dataset containing 500 User Stories, 500 Requirement Descriptions, and 500 Manual BDD Scenarios. Samples are selected using Simple Random Sampling (seed = 42, without replacement). |
| Intervention (I) | LoRA fine-tuned LLaMA-3-8B used to co-generate Gherkin Scenarios and Python Step Definitions.                                                                                                  |
| Comparison (C)   | GPT-4o Zero-shot Generation and Expert-written Ground Truth BDD Scenarios.                                                                                                                     |
| Outcome (O)      | Cosine Semantic Similarity (Threshold ≥ 0.85) and Executable Syntax Rate (Threshold ≥ 85%) measured using Gherkin Parser Validation and Python AST Validation.                                 |

The PICO framework systematically structures the empirical design of this study to address the identified research GAPs. The population (P) comprises 100 randomly sampled Connextra-format User Stories selected from the Rathnayake et al. (2026) dataset containing 500 User Stories, 500 Requirement Descriptions, and 500 Manual BDD Scenarios, selected using Simple Random Sampling (seed = 42, without replacement), addressing the synthetic/small-scale dataset gap (GAP-D). The intervention (I) utilizes a LoRA fine-tuned LLaMA-3-8B model for the co-generation of specification scenarios and step code, addressing the co-generation technology gap (GAP-T). The baseline comparison (C) employs GPT-4o zero-shot and manual expert scripts as quality standards. Lastly, the outcomes (O) enforce a dual static validation pipeline (GAP-M) combined with SBERT semantic similarity to ensure the quality and validity of the generated testing suites.

---

# 5. Experimental Protocol

## 5.1 Dataset

This study utilizes the dataset published by Rathnayake et al. (2026). The dataset contains:
*   500 User Stories
*   500 Requirement Descriptions
*   500 Manual BDD Scenarios

For the experimental subset, we select **100 samples** using **Simple Random Sampling** (with **seed = 42** and **without replacement**). This dataset was selected because it represents a realistic, multi-domain industrial software project containing agile requirements, offering an objective benchmark that avoids the limitations of small-scale or synthetic datasets.

## 5.2 Experimental Pipeline

The experimental workflow is structured into six sequential phases:
1.  **Dataset Preparation:** Draw 100 random samples from the source dataset.
2.  **BDD Artifact Generation:** Input the selected user stories into the target models to generate specifications and code.
3.  **Static Validation:** Apply the dual parser filters to check structural correctness.
4.  **Semantic Evaluation:** Compute similarity metrics on the validated artifacts.
5.  **Metric Aggregation:** Compile and organize final accuracy and similarity scores.
6.  **Statistical Analysis:** Run significance tests to analyze the comparative performance.

Below is the simple pipeline architecture:

```
Connextra User Story
        ↓
┌─────────────────────┐
│ LLaMA-3-8B LoRA-FT  │
│ GPT-4o Zero-shot    │
└─────────────────────┘
        ↓
Generate:
* Gherkin Scenario
* Python Step Definitions
        ↓
Gherkin Parser Validation
        ↓
Python AST Validation
        ↓
Cosine Similarity Evaluation
        ↓
Statistical Analysis
```

## 5.3 Prompt Template

Both the intervention and baseline models are prompted using a single, simple prompt template:

```
You are an expert BDD engineer.

Given a Connextra User Story, generate:
1. A Gherkin Scenario
2. Corresponding Python Step Definitions

Requirements:
* Follow Given-When-Then format.
* Produce executable Python code.
* Maintain consistency between scenario steps and step definitions.

User Story:
{USER_STORY}
```

## 5.4 Model Configuration

### GPT-4o Baseline
*   **Model:** GPT-4o
*   **Prompting Strategy:** Zero-shot
*   **Temperature:** 0
*   **Top_p:** 1

### LLaMA-3-8B LoRA-FT
*   **Base Model:** LLaMA-3-8B
*   **Fine-Tuning Method:** LoRA
*   **Note:** Detailed hyperparameters will be reported during the experiment phase.

## 5.5 Measurement Procedure

### Semantic Similarity
*   **Metric:** Cosine Similarity
*   **Embedding Model:** `all-MiniLM-L6-v2`
*   **Threshold:** 0.85
*   **Description:** Semantic similarity is computed between the generated BDD artifacts and the expert-written Ground Truth artifacts to evaluate whether the generated outputs preserve the intended business logic and testing requirements.

### Executable Syntax Rate
*   **Validation:** Gherkin Parser Validation & Python AST Validation
*   **Threshold:** 85%
*   **Description:** An artifact pair is considered executable only if both validation procedures are passed (Gherkin parsing and Python AST compile successfully).

## 5.6 Statistical Analysis

The hypotheses will be tested using the following statistical tests at a significance level of **$\alpha = 0.05$**:

| Research Question | Statistical Test |
| :--- | :--- |
| **RQ1** | One-Sample Wilcoxon Signed-Rank Test |
| **RQ2** | Binomial Exact Test |
| **RQ3** | Paired Wilcoxon Signed-Rank Test |

---

# 6. Evaluation Plan

## 6.1 Hypothesis Mapping

The following table maps the research questions to their metrics, evaluation thresholds, and statistical tests:

| RQ | Metric | Threshold | Statistical Test |
| :--- | :--- | :--- | :--- |
| **RQ1** | Cosine Semantic Similarity | 0.85 | One-Sample Wilcoxon |
| **RQ2** | Executable Syntax Rate | 85% | Binomial Exact Test |
| **RQ3** | Performance Difference (LLaMA-3-8B vs GPT-4o) | N/A | Paired Wilcoxon |

## 6.2 Decision Criteria

### RQ1
Reject $H_0$ if:
*   $p < 0.05$
*   Median Similarity $\ge 0.85$

### RQ2
Reject $H_0$ if:
*   $p < 0.05$
*   Syntax Rate $\ge 85\%$

### RQ3
Reject $H_0$ if:
*   $p < 0.05$
*   *Interpretation:* A statistically significant difference exists between LLaMA-3-8B LoRA-FT and GPT-4o.

## 6.3 Expected Outcomes

### Outcome A (Optimal Case)
*   **Criteria:** Similarity $\ge 0.85$, Syntax $\ge 85\%$, and no significant difference from GPT-4o.
*   **Interpretation:** LLaMA-3-8B LoRA-FT is a viable open-source alternative to commercial frontier models for local deployment.

### Outcome B (Sub-optimal Case)
*   **Criteria:** Target thresholds (0.85 similarity and 85% syntax) achieved, but a significant difference exists.
*   **Interpretation:** The model is usable for BDD workflows but exhibits performance differences compared with GPT-4o.

### Outcome C (Infeasible Case)
*   **Criteria:** Target thresholds are not achieved.
*   **Interpretation:** Further model improvement, prompt engineering, or alternative fine-tuning parameters are required before practical adoption.
