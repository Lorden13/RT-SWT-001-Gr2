# Research Proposal

## 1. Tiêu đề & Thông tin nhóm

*   **Tên đề tài:** Evaluating LoRA Fine-Tuned LLaMA-3-8B for Automated BDD Test Generation from Connextra User Stories
*   **Nhóm:** Group 2  
*   **Thành viên:**  
    1. Ngô Đình Khoa (SE196737)  
    2. Trịnh Phú Quốc (SE190287)  
    3. Trần Đăng Khoa (SE194398)  
    4. Đặng Đỗ Cao Sang (SE193269)  
    5. Đào Lý Phi Hùng (SE172826)  
*   **Topic Code:** RT-SWT-SE1905  
*   **Ngày nộp:** 2026-06-14  
*   **Version:** 1.0  
*   **Trạng thái:** Đang chờ phê duyệt

---

## 2. Problem Statement

### 2.1 Bối cảnh & Tầm quan trọng

Behavior-Driven Development (BDD) là một phương pháp phát triển phần mềm Agile giúp tăng cường sự hợp tác giữa lập trình viên, kiểm thử viên và các bên liên quan bằng cách đặc tả yêu cầu hệ thống dưới dạng kịch bản Gherkin dễ đọc (`Given-When-Then`). Bằng cách kết nối giữa yêu cầu ngôn ngữ tự nhiên và kiểm thử thực thi, BDD đảm bảo phần mềm hoạt động đúng nghiệp vụ. Tuy nhiên, việc viết kịch bản Gherkin và chuyển đổi thủ công chúng thành mã kiểm thử (Step Definitions) tiêu tốn nhiều thời gian và dễ xảy ra lỗi nghiệp vụ (Fernandes et al. 2025).

Để tối ưu hóa, tự động hóa sinh kiểm thử BDD từ User Stories là một hướng nghiên cứu then chốt. Việc sử dụng các mô hình ngôn ngữ lớn (LLM) để sinh kịch bản và Step Definitions từ User Stories định dạng Connextra (`As a [role], I want [feature], so that [benefit]`) hứa hẹn tăng tốc quy trình kiểm thử và đảm bảo tính nhất quán giữa tài liệu và mã nguồn (Rathnayake et al. 2026).

Đánh giá các quy trình sinh BDD bằng LLM là rất quan trọng. Mặc dù các mô hình đóng như GPT-4o có khả năng zero-shot mạnh mẽ, việc triển khai chúng bị hạn chế bởi lo ngại bảo mật dữ liệu doanh nghiệp và chi phí API cao. Do đó, tinh chỉnh mô hình nguồn mở như LLaMA-3-8B bằng phương pháp LoRA (QLoRA 4-bit) là một giải pháp thay thế hấp dẫn (Selfbehave et al. 2026). Việc chứng minh mô hình nguồn mở tinh chỉnh đạt hiệu năng tương đương mô hình đóng thương mại sẽ giúp các tổ chức xây dựng quy trình tự động hóa kiểm thử BDD cục bộ, bảo mật và tiết kiệm chi phí.

### 2.2 State of the Art

Nhiều nghiên cứu gần đây đã ứng dụng LLM cho tự động hóa sinh ca kiểm thử:

Fernandes et al. (2025) đánh giá các mô hình như GPT-4, LLaMA-3, Gemini, DeepSeek R1 trên 34 User Stories miền FinTech bằng điểm tương đồng ngữ nghĩa METEOR. Gemini zero-shot đạt điểm cao nhất (0.84). Tuy nhiên, nghiên cứu chỉ giới hạn ở sinh kịch bản Gherkin (chưa sinh Step Definitions) và quy mô mẫu nhỏ.

Rathnayake et al. (2026) đóng góp bộ dữ liệu benchmark 500 User Stories thực tế kèm kịch bản viết tay. GPT-4o zero-shot đạt tương đồng ngữ nghĩa BERTScore 91.16% và Cosine Similarity 53.96%. Tuy nhiên, nghiên cứu này mới chỉ dừng lại ở sinh kịch bản Gherkin mà chưa giải quyết bài toán sinh mã Step Definitions thực thi.

Karpurapu et al. (2024) tập trung vào độ chính xác cú pháp Gherkin tĩnh qua `gherkin-lint`, báo cáo tỷ lệ đúng 100% cho GPT-4 và 92% cho Llama-2 ở few-shot. Tuy nhiên, nghiên cứu chưa kiểm tra cú pháp Step Definitions đi kèm và chưa đánh giá tương đồng ngữ nghĩa với Ground Truth.

Selfbehave et al. (2026) tinh chỉnh LLaMA-3-8B bằng LoRA, đạt tỷ lệ biên dịch cú pháp Gherkin 99.2%. Hạn chế lớn nhất là nghiên cứu chỉ thực nghiệm trên dữ liệu tự sinh (synthetic) bằng self-instruct thay vì User Stories thực tế đa miền của doanh nghiệp.

### 2.3 GAP (Khoảng trống nghiên cứu)

Dựa trên tổng hợp 15 bài báo khoa học chính thức, nhóm xác định 3 khoảng trống nghiên cứu:
*   **GAP-T (Technology - Chính):** Chưa có nghiên cứu nào đánh giá quy trình đồng sinh (co-generation) cả kịch bản Gherkin và Step Definitions từ Connextra User Stories bằng các mô hình nguồn mở cỡ nhỏ (8B) tinh chỉnh LoRA trên dữ liệu thực tế (Hỗ trợ bởi: Fernandes et al. 2025, Rathnayake et al. 2026, dos Santos et al. 2026).
*   **GAP-M (Metric - Phụ):** Thiếu một cơ chế kiểm định tĩnh kép (kết hợp Gherkin Parser và Python AST Parser) trước khi tiến hành đo độ tương đồng ngữ nghĩa Cosine Similarity với kịch bản chuẩn (Hỗ trợ bởi: Karpurapu et al. 2024, Tesfalidet et al. 2025).
*   **GAP-D (Dataset - Hỗ trợ):** Thiếu thực nghiệm trên các tập dữ liệu benchmark đa miền thực tế quy mô lớn thay vì dữ liệu tự sinh hoặc tập dữ liệu nhỏ từ 5-34 mẫu (Hỗ trợ bởi: Rathnayake et al. 2026).

### 2.4 Motivation

Nếu các khoảng trống này không được giải quyết, các doanh nghiệp sẽ tiếp tục phụ thuộc vào các API đóng đắt đỏ và đối mặt rủi ro bảo mật dữ liệu. Sinh kịch bản Gherkin thiếu Step Definitions chỉ giải quyết được một nửa bài toán tự động hóa. Hơn nữa, việc đánh giá thiếu bộ lọc tĩnh kép sẽ dẫn đến rủi ro triển khai mã nguồn lỗi cú pháp, gây lãng phí tài nguyên thực thi và giảm lòng tin của kỹ sư phát triển. Nghiên cứu thực nghiệm so sánh LLaMA-3-8B LoRA-FT với GPT-4o trên dữ liệu thực tế sẽ cung cấp minh chứng khoa học để doanh nghiệp tự tin triển khai giải pháp BDD local bảo mật.

---

## 3. Related Work

### 3.1 Overview

Bảng dưới đây tóm tắt các công trình liên quan trực tiếp nhất đến tác vụ sinh kịch bản Gherkin và Step Definitions:

| Paper | Tool / LLM | Dataset (Size) | Metric | Best Result | Limitation |
|:---|:---|:---|:---|:---|:---|
| **Rathnayake et al. 2026** | GPT-4o (Zero-shot) | 500 User Stories | BERTScore, Cosine Semantic Similarity | BERTScore = 91.16%, Cosine = 53.96% | Loại trừ sinh step definitions; không có kiểm định tĩnh kép. |
| **Fernandes et al. 2025** | GPT-3.5, GPT-4, LLaMA-3, Gemini, DeepSeek R1 | 34 User Stories | METEOR Score | METEOR = 0.84 (Gemini zero-shot) | Chỉ sinh kịch bản Gherkin; cỡ mẫu nhỏ, đơn miền. |
| **Selfbehave et al. 2026** | LLaMA-3-8B (LoRA-FT) | Synthetic Dataset | Tỷ lệ cú pháp tĩnh | 99.2% đúng cú pháp Gherkin | Hoàn toàn phụ thuộc vào dữ liệu tự sinh bằng AI. |
| **Karpurapu et al. 2024** | GPT-3.5, GPT-4, Llama-2 | Cỡ mẫu nhỏ | Cú pháp qua `gherkin-lint` | 100% đúng cú pháp (GPT-4) | Không sinh Step Definitions; không đánh giá ngữ nghĩa. |
| **Tesfalidet et al. 2025** | GPT-4 | 10–20 User Stories | Cosine Similarity, Behave run rate | Similarity = 0.81, Executable rate = 85% | Cỡ mẫu nhỏ; giới hạn miền FinTech; thiếu parser tĩnh kép. |
| **dos Santos et al. 2026** | ChatGPT, Gemini, Grok, Copilot | 34 User Stories | Độ phủ tiêu chí nghiệm thu | Độ phủ cao cho ChatGPT | Quy mô dữ liệu nhỏ; chỉ sinh kịch bản Gherkin. |
| **Mendoza et al. 2024** | ChatGPT-4, Gemini, Copilot | 5 User Stories | Thang đo Likert (đánh giá người) | Điểm chấp nhận người cao | Cỡ mẫu cực nhỏ (5 mẫu); đánh giá cảm quan. |
| **Bergsmann et al. 2024** | Multi-Agent LLMs | 12-15 web apps | Tỷ lệ chạy test thành công | Tỷ lệ thành công cao | Dựa trên hệ thống multi-agent độ trễ cao, tốn token. |

### 3.2 Pattern Analysis

*   **Observation 1:** Các nghiên cứu đánh giá chất lượng ngôn ngữ chủ yếu dùng các độ đo tương đồng ngữ nghĩa như METEOR, BERTScore, Cosine Similarity so với Ground Truth (Fernandes et al. 2025, Rathnayake et al. 2026).
*   **Observation 2:** Đa số nghiên cứu thực nghiệm bị giới hạn bởi cỡ mẫu rất nhỏ (<50 stories), ngoại trừ Rathnayake et al. (2026) đóng góp 500 mẫu, gây ảnh hưởng đến tính hợp lệ bên ngoài.
*   **Observation 3:** Hầu hết nghiên cứu bỏ qua tính thực thi đồng thời của BDD. Các nghiên cứu sinh Step Definitions (Tesfalidet et al. 2025) chưa tích hợp quy trình lọc tĩnh kép trước khi đo ngữ nghĩa.
*   **Observation 4:** Hướng tinh chỉnh mô hình nguồn mở local (như LLaMA-3) còn hạn chế và chủ yếu dùng dữ liệu tự sinh (Selfbehave et al. 2026), chưa được kiểm chứng trên User Stories thực tế của doanh nghiệp.

### 3.3 GAP Mapping

Bảng ánh xạ các GAP nghiên cứu phát hiện được từ tài liệu rà soát:

| GAP | Bằng chứng tài liệu | Trạng thái |
|:---|:---|:---|
| **GAP-T (Technology)** | 15 nghiên cứu; không có công trình nào đồng sinh kịch bản Gherkin và Step Definitions | Xác nhận |
| **GAP-M (Metric)** | 15 nghiên cứu; thiếu quy trình tích hợp Gherkin Parser và Python AST Parser làm chốt chặn | Xác nhận |
| **GAP-D (Dataset)** | 13/15 nghiên cứu sử dụng tập dữ liệu tự sinh hoặc cỡ mẫu nhỏ dưới 50 mẫu | Xác nhận |

---

## 4. Research Questions

### 4.1 Main Research Question

Liệu mô hình nguồn mở tinh chỉnh LoRA LLaMA-3-8B có khả năng đồng sinh kịch bản Gherkin và Step Definitions đạt độ tương đồng ngữ nghĩa $\ge 0.85$ và tỷ lệ cú pháp tĩnh khả thi $\ge 85\%$, đồng thời mang lại hiệu năng tương đương với GPT-4o zero-shot hay không?

### 4.2 Sub-Research Questions

#### RQ1 – Semantic Similarity (Độ tương đồng ngữ nghĩa)
Mô hình LLaMA-3-8B LoRA-FT có đạt độ tương đồng ngữ nghĩa Cosine Similarity tối thiểu 0.85 (tính qua SBERT `all-MiniLM-L6-v2`) so với kịch bản Ground Truth viết bởi chuyên gia hay không?
*   *Hệ giả thuyết:*
    $$\text{H0}_{1a}: \text{Median}(\text{Similarity}_{\text{LLaMA-FT}}) \le 0.85$$
    $$\text{H1}_{1a}: \text{Median}(\text{Similarity}_{\text{LLaMA-FT}}) > 0.85$$

#### RQ2 – Executable Syntax Rate (Tỷ lệ cú pháp tĩnh khả thi)
Mô hình LLaMA-3-8B LoRA-FT có đạt tỷ lệ cú pháp tĩnh hợp lệ tối thiểu 85% sau khi qua bộ lọc kép Gherkin Parser và Python AST Validation hay không?
*   *Hệ giả thuyết:*
    $$\text{H0}_{2a}: p_{\text{syntax\_LLaMA}} \le 0.85$$
    $$\text{H1}_{2a}: p_{\text{syntax\_LLaMA}} > 0.85$$

#### RQ3 – Comparative Evaluation (Đánh giá đối chứng)
Có sự khác biệt có ý nghĩa thống kê về chất lượng ngữ nghĩa và tỷ lệ cú pháp tĩnh hợp lệ giữa LLaMA-3-8B LoRA-FT và GPT-4o zero-shot hay không?
*   *Hệ giả thuyết:*
    $$\text{H0}_{1b}: \text{Median}(\text{Similarity}_{\text{LLaMA-FT}} - \text{Similarity}_{\text{GPT-4o}}) = 0$$
    $$\text{H1}_{1b}: \text{Median}(\text{Similarity}_{\text{LLaMA-FT}} - \text{Similarity}_{\text{GPT-4o}}) \neq 0$$

### 4.3 PICO Framework

Bảng mô tả cấu trúc PICO của thực nghiệm:

| Thành phần PICO | Đặc tả chi tiết trong nghiên cứu của nhóm |
| :--- | :--- |
| **Population (P)** | 100 User Stories định dạng Connextra rút ngẫu nhiên không lặp (seed = 42) từ tập dữ liệu 500 mẫu của Rathnayake et al. (2026). |
| **Intervention (I)** | Quy trình đồng sinh kịch bản Gherkin và Step Definitions bằng mô hình LLaMA-3-8B tinh chỉnh LoRA local. |
| **Comparison (C)** | Đối chứng với sinh zero-shot của GPT-4o và kịch bản chuẩn viết tay từ chuyên gia (Ground Truth). |
| **Outcome (O)** | Điểm tương đồng ngữ nghĩa Cosine Similarity (ngưỡng $\ge 0.85$) và Tỷ lệ cú pháp tĩnh hợp lệ (ngưỡng $\ge 85\%$). |

---

## 5. Experiment Protocol

### 5.1 Dataset

Nghiên cứu sử dụng bộ dữ liệu gốc của Rathnayake et al. (2026) bao gồm:
*   500 User Stories
*   500 Requirement Descriptions
*   500 Manual BDD Scenarios

Phương pháp rút mẫu thực nghiệm:
*   **Phương pháp:** Simple Random Sampling (Rút mẫu ngẫu nhiên đơn giản).
*   **Seed:** 42 (Để đảm bảo tính tái lập).
*   **Replacement:** Rút mẫu không lặp (Without replacement).
*   **Tập thực nghiệm cuối cùng:** 100 User Stories định dạng Connextra.

Việc chọn mẫu ngẫu nhiên giúp loại bỏ hoàn toàn thiên lệch lựa chọn (selection bias), đảm bảo tập thực nghiệm 100 mẫu bao phủ đại diện cho nhiều miền nghiệp vụ khác nhau từ doanh nghiệp thực tế của tập dữ liệu gốc, hỗ trợ mạnh mẽ cho tính hợp lệ bên ngoài (external validity) và khả năng tổng quát hóa kết quả.

### 5.2 Experimental Pipeline

Quy trình thực nghiệm tuần tự được thiết kế như sau:

```
      Connextra User Story
               ↓
       LLaMA-3-8B LoRA-FT
               ↓
            Generate:
      • Gherkin Scenario
      • Python Step Definition
               ↓
       Static Validation
               ↓
      Semantic Evaluation
               ↓
      Statistical Analysis
```

Chi tiết mục đích của từng giai đoạn:
1.  **Connextra User Story:** Dữ liệu yêu cầu đầu vào chuẩn hóa làm ngữ cảnh cho LLM.
2.  **LLaMA-3-8B LoRA-FT:** Thực thi sinh tự động trên mô hình thực nghiệm (và mô hình đối chứng GPT-4o).
3.  **Generate:** Đồng sinh kịch bản Gherkin (.feature) và Step Definitions (.py) trong một lượt gọi duy nhất.
4.  **Static Validation:** Bộ lọc kép kiểm lỗi cú pháp tĩnh của kịch bản Gherkin và Step Code Python.
5.  **Semantic Evaluation:** Đánh giá độ tương hợp nghiệp vụ Cosine SBERT so với Ground Truth của chuyên gia.
6.  **Statistical Analysis:** Áp dụng các phép kiểm thống kê toán học để kết luận hệ giả thuyết ở mức ý nghĩa $\alpha = 0.05$.

### 5.3 Model Configuration

#### Experimental Model (Mô hình can thiệp)
*   **Mô hình:** LLaMA-3-8B
*   **Tối ưu:** Tinh chỉnh LoRA (QLoRA 4-bit) nhằm đánh giá khả năng của mô hình local nguồn mở.

#### Baseline Model (Mô hình đối chứng)
*   **Mô hình:** GPT-4o
*   **Cấu hình:** Zero-shot prompting để làm chuẩn so sánh với mô hình đóng thương mại hàng đầu.

#### Generation Settings (Tham số sinh)
*   **Temperature:** 0
*   **Top_p:** 1
*   *Lý do:* Cấu hình sinh tất định (deterministic generation) giúp loại bỏ tính bất định của văn bản sinh ra, đảm bảo tính tái lập cao nhất khi thực hiện lại thực nghiệm.

### 5.4 Prompt Template

Cả hai mô hình đều nhận cùng một cấu trúc Prompt chuẩn hóa nhằm loại bỏ thiên lệch cấu trúc:

```text
Generate a Gherkin Scenario and Python Step Definitions
from the following Connextra User Story.

User Story:
<USER_STORY>

Output Format:

Gherkin: <SCENARIO>

Python:
<STEP_DEFINITIONS>
```

Việc chuẩn hóa prompt đảm bảo tính khách quan tối đa cho thực nghiệm, đảm bảo sự khác biệt về hiệu năng đo lường chỉ phản ánh năng lực cốt lõi của mô hình và phương pháp tinh chỉnh.

### 5.5 Static Validation (Kiểm định tĩnh kép)

Quy trình kiểm định tĩnh được chia làm 2 giai đoạn độc lập:
*   **Gherkin Validation:** Sử dụng công cụ `Gherkin Parser` để phân tích cú pháp tệp kịch bản sinh ra, đảm bảo cấu trúc các từ khóa Given-When-Then đúng định dạng.
*   **Python Validation:** Sử dụng công cụ `Python AST Validation` (`ast.parse`) phân tích cây cú pháp tĩnh của Step Code, kiểm tra lỗi SyntaxError (thụt lề, thiếu dấu hai chấm, đóng mở ngoặc).

**Executable Syntax Rate** được định nghĩa bằng tỷ lệ tệp đạt yêu cầu ở cả hai bộ lọc cú pháp tĩnh trên:

$$\text{Executable Syntax Rate} = \frac{\text{Số lượng artifacts PASS cả hai bộ lọc}}{\text{Tổng số artifacts do mô hình sinh ra}}$$

### 5.6 Semantic Evaluation (Đánh giá ngữ nghĩa)

Tất cả các artifacts vượt qua bước static validation sẽ được so sánh trực tiếp với bộ kịch bản **Ground Truth viết tay của chuyên gia**.
*   **Độ đo:** Cosine Semantic Similarity (Tính qua mô hình nhúng SBERT `all-MiniLM-L6-v2`).
*   **Ngưỡng tối thiểu đạt:** 0.85.

Độ tương đồng ngữ nghĩa Cosine giúp đo lường mức độ bảo toàn nghiệp vụ và độ phủ yêu cầu của kịch bản sinh ra, đảm bảo kịch bản tự sinh khớp với thiết kế chuẩn mực nghiệp vụ từ con người.

### 5.7 Statistical Analysis

Quy trình ánh xạ các phép kiểm thống kê toán học tương ứng cho mỗi câu hỏi nghiên cứu:

| Research Question | Metric | Statistical Test |
| :--- | :--- | :--- |
| **RQ1** | Cosine Similarity | One-Sample Wilcoxon Signed-Rank Test |
| **RQ2** | Executable Syntax Rate | Binomial Exact Test |
| **RQ3** | Model Comparison | Paired Wilcoxon Signed-Rank Test |

*   **RQ1** dùng Wilcoxon một mẫu để so sánh giá trị trung vị Cosine của LLaMA-FT với ngưỡng kỳ vọng 0.85.
*   **RQ2** dùng phép kiểm nhị thức Binomial để so sánh tỷ lệ cú pháp tĩnh PASS thực tế với ngưỡng 85%.
*   **RQ3** dùng Wilcoxon cặp để so sánh hiệu năng trực tiếp của hai nhóm mẫu sinh ra từ LLaMA-3-8B LoRA-FT và GPT-4o.

---

## 6. Evaluation Plan

### 6.1 Hypothesis Mapping

Bảng ánh xạ câu hỏi nghiên cứu, tiêu chuẩn chất lượng và phép kiểm thống kê:

| RQ | Metric | Threshold | Statistical Test |
| :--- | :--- | :--- | :--- |
| **RQ1** | Cosine Semantic Similarity | 0.85 | One-Sample Wilcoxon |
| **RQ2** | Executable Syntax Rate | 85% | Binomial Exact Test |
| **RQ3** | So sánh hiệu năng hai mô hình | N/A | Paired Wilcoxon |

### 6.2 Decision Criteria (Quy tắc ra quyết định)

*   **RQ1:** Bác bỏ giả thuyết không $H_0$ nếu $p < 0.05$ và giá trị trung vị Cosine Similarity $\ge 0.85$.
*   **RQ2:** Bác bỏ giả thuyết không $H_0$ nếu $p < 0.05$ và tỷ lệ cú pháp tĩnh khả thi thực tế $\ge 85\%$.
*   **RQ3:** Bác bỏ giả thuyết không $H_0$ nếu $p < 0.05$, chỉ ra có sự khác biệt có ý nghĩa thống kê về hiệu năng giữa LLaMA-3-8B LoRA-FT và GPT-4o.

### 6.3 Expected Outcomes (Kịch bản kết quả dự tính)
*   **Kịch bản A (Tối ưu):** Cosine $\ge 0.85$, Cú pháp $\ge 85\%$, và không có sự khác biệt có ý nghĩa thống kê so với GPT-4o. Kết luận LLaMA-3-8B local hoàn toàn có thể thay thế mô hình đóng thương mại.
*   **Kịch bản B (Trung bình):** Đạt ngưỡng chất lượng đề ra nhưng vẫn có sự khác biệt hiệu năng có ý nghĩa thống kê so với GPT-4o. Kết luận mô hình local sử dụng tốt cho quy trình kiểm thử nhưng cần tối ưu thêm.
*   **Kịch bản C (Không đạt):** Không đạt các ngưỡng tối thiểu. Kết luận cần cải thiện tập dữ liệu huấn luyện hoặc thay đổi kiến trúc prompt.

---

## 7. Threats to Validity

### 7.1 Internal Validity (Độ chính xác nội bộ)
*   **Mối đe dọa:** Sự thiên kiến trong thiết kế prompt template có thể tạo lợi thế vô ý cho một mô hình cụ thể.
*   **Hành động giảm thiểu (Mitigation):** Nhóm áp dụng prompt template chuẩn hóa duy nhất cho cả hai mô hình và cấu hình tham số sinh tất định ($temperature = 0, top\_p = 1.0$) để loại bỏ hoàn toàn tính ngẫu nhiên của kết quả.

### 7.2 External Validity (Khả năng tổng quát hóa)
*   **Mối đe dọa:** Thực nghiệm trên một tập dữ liệu cụ thể có thể không phản ánh đúng khả năng trên các ngôn ngữ lập trình và miền nghiệp vụ khác.
*   **Hành động giảm thiểu (Mitigation):** Nhóm sử dụng tập dữ liệu thực tế đa miền của doanh nghiệp gồm 4 sản phẩm phần mềm thực tế (*Rathnayake et al. 2026*) và tiến hành rút mẫu ngẫu nhiên không lặp (seed = 42) để đảm bảo tập thực nghiệm đại diện tốt cho quần thể.

### 7.3 Construct Validity (Độ đo chính xác)
*   **Mối đe dọa:** Điểm tương đồng ngữ nghĩa Cosine có thể không phản ánh hoàn hảo đánh giá chất lượng thực tế từ kỹ sư phát triển phần mềm.
*   **Hành động giảm thiểu (Mitigation):** Sử dụng mô hình nhúng SBERT `all-MiniLM-L6-v2` đã được chứng minh có tương quan rất cao với đánh giá ngữ nghĩa của con người. Đồng thời, tích hợp bộ kiểm định tĩnh kép (Gherkin & AST) làm bộ lọc tiền xử lý để loại trừ các tệp lỗi cú pháp trước khi tính điểm Cosine, tránh hiện tượng nhiễu điểm số.

### 7.4 Conclusion Validity (Tính hợp lệ kết luận)
*   **Mối đe dọa:** Quy mô mẫu quá nhỏ hoặc vi phạm giả định phân phối dữ liệu dẫn đến kết luận sai lầm về mặt thống kê.
*   **Hành động giảm thiểu (Mitigation):** Nhóm sử dụng quy mô mẫu lớn $N = 100$ và tiến hành kiểm tra lực lượng mẫu (Power Analysis) đạt lực lượng thống kê $\beta \ge 0.80$ ở mức ý nghĩa $\alpha = 0.05$. Đồng thời, sử dụng các phép kiểm thống kê phi tham số (Wilcoxon) không phụ thuộc vào giả định phân phối chuẩn của dữ liệu.

---

## 8. Timeline & Resources

### 8.1 Phân công vai trò nhóm (Role Delegation)

Để đảm bảo tính khách quan độc lập theo quy chuẩn RBL-3, các vai trò của 5 thành viên được phân định cụ thể như sau:

| Vai trò | Thành viên đảm nhận | Trách nhiệm cụ thể trong thực nghiệm |
| :--- | :--- | :--- |
| **PL (Project Lead)** | Ngô Đình Khoa (SE196737) | Điều phối tiến độ, rà soát tính nhất quán đề cương và báo cáo walkthrough. |
| **DG (Data & Ground Truth)** | Trần Đăng Khoa (SE194398) | Rút mẫu ngẫu nhiên 100 User Stories, kiểm định dữ liệu expert baseline Ground Truth. |
| **LR (LLM Runner)** | Trịnh Phú Quốc (SE190287) | Cài đặt API key, viết mã nguồn gọi GPT-4o và huấn luyện local LLaMA-3-8B. |
| **MS (Metrics & Stats)** | Đặng Đỗ Cao Sang (SE193269) | Lập trình bộ parser kiểm định tĩnh, đo độ tương đồng Cosine, và chạy kiểm định thống kê. |
| **RW (Report Writer)** | Đào Lý Phi Hùng (SE172826) | Viết báo cáo Threats to Validity, vẽ các biểu đồ trực quan hóa số liệu và định dạng văn bản. |

*Lưu ý: LR (Trịnh Phú Quốc) và MS (Đặng Đỗ Cao Sang) là hai thành viên hoàn toàn độc lập để loại bỏ xung đột lợi ích khi đo lường kết quả thực nghiệm.*

### 8.2 Quản lý Tài nguyên (Resource Inventory)

| Tài nguyên | Trạng thái | Chủ sở hữu | Ghi chú |
| :--- | :---: | :--- | :--- |
| Dataset Rathnayake | [x] | DG | Đã tải và lưu trữ máy local thành công, verify OK. |
| OpenAI API Key | [x] | LR | Tài khoản API GPT-4o đã nạp tiền hoạt động bình thường. |
| Compute Platform | [x] | LR | Cấu hình thành công môi trường chạy GPU Google Colab Pro. |
| Thư viện thống kê | [x] | MS | Đã kiểm thử thành công các thư viện `scipy`, `ast`, `sentence-transformers`. |

### 8.3 Dự trù kinh phí API GPT-4o
*   **Input Tokens:** 100 samples $\times$ 1,500 tokens/sample = 150,000 tokens. Giá API: $2.50 / 1M tokens $\rightarrow$ **$0.38**.
*   **Output Tokens:** 100 samples $\times$ 2,500 tokens/sample = 250,000 tokens. Giá API: $10.00 / 1M tokens $\rightarrow$ **$2.50**.
*   **Tài nguyên GPU local:** Sử dụng free tier Kaggle/Colab $\rightarrow$ **$0.00**.
*   **Tổng chi phí dự tính:** **$2.88** (Được tài trợ bởi ngân quỹ nhóm).

### 8.4 Kế hoạch chi tiết theo tuần (Tuần 5-10)

| Tuần | Hoạt động thực hiện | Thành viên chịu trách nhiệm | checkpoint / Sản phẩm đầu ra |
| :--- | :--- | :--- | :--- |
| **Tuần 5-6** | Viết hoàn thiện và nộp bảo vệ Đề cương | Cả nhóm | Nộp file `proposal.md` v1.0 và slide thuyết trình. |
| **Tuần 7** | Triển khai chạy Pilot thực nghiệm (10% mẫu) | LR + MS + DG | Tệp `pilot_ground_truth.csv` và `pilot_llm_output.csv` sạch lỗi. |
| **Tuần 8** | Thực thi chạy thực nghiệm chính thức (100%) | LR | Tệp log kết quả thô `full_llm_output.csv`. |
| **Tuần 8** | Chạy đo lường và kiểm định thống kê | MS | Tệp phân tích code thống kê `full_analysis.ipynb`. |
| **Tuần 9-10** | Viết báo cáo nghiệm thu và slide thuyết trình | RW + PL | File báo cáo nghiệm thu khoa học `walkthrough.md` cuối kỳ. |

### 8.5 Kế hoạch dự phòng rủi ro (Contingency Plan)
*   **Đề cương bị từ chối duyệt:** PL chủ trì cuộc họp sửa đổi bổ sung và nộp lại bản cập nhật cho GV trong vòng 24 giờ.
*   **Lỗi Rate Limit API:** LR thiết lập cấu hình gọi chia nhỏ batch (10 mẫu/lượt) và tạo độ trễ nghỉ 60 giây giữa các lượt trong mã nguồn Python.
*   **LLaMA local bị tràn bộ nhớ VRAM:** LR chuyển đổi cấu hình sang lượng tử hóa 4-bit QLoRA hoặc chạy trên GPU Kaggle T4 kép miễn phí.
*   **Thành viên chậm tiến độ:** PL có quyền luân chuyển khẩn cấp nhiệm vụ sang thành viên khác sau 48 giờ không phản hồi.

### 8.6 Quy trình thay đổi đề cương (Amendment Process)
1.  Nếu quá trình chạy thử nghiệm Pilot ở Tuần 7 phát hiện lỗi hệ thống (ví dụ: lỗi parser tĩnh do định dạng Markdown):
2.  Nhóm ghi chép lỗi kỹ thuật và đề xuất giải pháp thay thế.
3.  Viết đề xuất thay đổi vào tệp `proposal-amendment-v1.1.md` và nộp GV phê duyệt trong vòng 24 giờ.
4.  Cập nhật mã nguồn thực nghiệm chính thức sau khi được GV đồng ý.
