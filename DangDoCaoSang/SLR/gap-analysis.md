# Gap Analysis

## GAP-A: Evaluation gap

Most studies evaluate LLM-generated tests using coverage-oriented metrics such as line coverage, branch coverage, or compilation rate. However, coverage does not always indicate that the generated test can detect real behavioral faults. Mutation score and bug-revealing ability are used in some studies, but they are not yet consistently integrated into the evaluation design.

**Evidence:** TestPilot, ChatUniTest, CODAMOSA, CoverUp, and JUnit generation studies all report coverage-related results, while MuTAP and ACH emphasize mutation-guided or fault-oriented test generation.

---

## GAP-B: Context gap

Existing LLM-based unit test generation approaches rely heavily on the quality of prompt context. Some studies use source code, signatures, examples, or documentation, but fewer studies systematically compare which combination of context helps the model produce executable and meaningful tests.

**Evidence:** TestPilot uses signatures, implementations, and documentation examples; ChatUniTest uses adaptive focal context; MocklessTester uses context-enriched generation. However, there is no single accepted context protocol.

---

## GAP-C: Robustness gap

Many generated unit tests perform well on the original version of a program but may become unstable when the software evolves. This is important because unit tests are expected to support regression testing over time.

**Evidence:** The software evolution study shows that LLM-generated tests degrade when semantic-altering or semantic-preserving changes are introduced.

---

## GAP-D: Practicality gap

Industrial and large-project studies show that cost, repair iterations, dependency handling, and developer acceptance are major barriers. Academic benchmarks often underrepresent these practical constraints.

**Evidence:** ACH at Meta, MocklessTester, and AgoneTest provide more practical insights, but their industrial or tool-specific settings make direct comparison difficult.

---

## BỔ SUNG THEO RBL-2 - Chốt GAP

**GAP Chính:** Evaluation gap - thiếu đánh giá lấy mutation score/fault-revealing ability làm tiêu chí chính cho unit tests sinh bởi LLM, thay vì chỉ dựa vào coverage hoặc compilation rate.

**GAP Secondary:** Context gap - thiếu ablation rõ ràng về loại prompt context nào giúp tăng khả năng sinh test chạy được và phát hiện lỗi.

## BỔ SUNG THEO RBL-2 - Phản chứng cho GAP Chính

GAP tuyên bố: Chưa có đủ bằng chứng nhất quán rằng context-enriched prompting + automated repair giúp unit tests do LLM sinh ra đạt mutation score/fault-revealing ability cao hơn baseline prompting.

| Paper | Đã làm chưa? | Ghi chú |
|---|---|---|
| TestPilot | Không | Chủ yếu báo cáo coverage/repair, không lấy mutation score làm claim chính. |
| JUnit LLM Study | Không | Có compilation/correctness/coverage nhưng chưa tập trung mutation score. |
| CODAMOSA | Một phần | Dùng search/coverage, không kiểm tra context-enriched prompt + repair. |
| ChatUniTest | Một phần | Có validation-repair nhưng không đặt mutation score làm metric chính. |
| MuTAP | Có một phần | Có mutation testing, nhưng chưa kiểm tra đầy đủ context-enriched prompting + repair theo ablation. |
| CoverUp | Không | Tập trung coverage. |
| Open-source LLM Study | Không | So sánh model/prompt, thiếu mutation-centered protocol. |
| MocklessTester | Có một phần | Có mutation score, nhưng vẫn cần replication và baseline rõ hơn. |

## BỔ SUNG THEO RBL-2 - Feasibility Check

| Tiêu chí | Mức | Ghi chú |
|---|---|---|
| Dataset | ✅ | Có thể dùng Defects4J hoặc project Java nhỏ. |
| Tool/API | ✅ | GPT-4o mini/GPT-4o; PIT mutation testing; Maven/JUnit. |
| Compute | ⚠️ | Mutation testing tốn thời gian, cần giảm còn 20-30 classes. |
| Ground Truth | ✅ | Mutation score không cần nhãn expert thủ công. |
| Skills | ✅ | Có thể triển khai bằng Java test runner và PIT. |
| Thời gian | ⚠️ | Cần downscope số class và số vòng repair. |
| Contribution | ✅ | Đóng góp rõ vì đo khả năng phát hiện lỗi thay vì chỉ coverage. |

**Quyết định:** Không có ❌, có 2 ⚠️. GAP chính khả thi.
