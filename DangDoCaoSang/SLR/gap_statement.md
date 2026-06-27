# Gap Statement

Based on the evidence synthesis, this SLR identifies the following research gap:

> Current LLM-based unit test generation research shows promising results in code coverage and automated test creation, but there is still insufficient evidence on whether context-enriched prompting and repair can consistently produce executable, fault-revealing, and evolution-robust unit tests across real-world projects.

This gap has three dimensions:

1. **Metric gap:** Many studies still prioritize coverage and compilation rate, while mutation score, bug detection, and regression robustness are less consistently used.
2. **Context gap:** Existing studies use different prompt contexts, but there is no clear evaluation of which context components are most useful.
3. **Practicality gap:** Tool-level and industrial constraints such as dependencies, repair cost, token cost, and developer acceptance are not uniformly measured.

Therefore, a useful next experiment should evaluate an LLM-based unit-test generation approach that combines source-code context, dependency-aware retrieval, and automated repair, then compare it against a baseline LLM prompt and a traditional automated test-generation tool.
