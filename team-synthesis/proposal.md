# Research Proposal

## 1. Tiêu đề & Thông tin nhóm

*   **Tên đề tài:** Đánh giá các kỹ thuật Prompt Engineering trong sinh tự động BDD Test từ Connextra User Stories (Evaluating Prompt Engineering Techniques for Automated BDD Test Generation from Connextra User Stories)
*   **Nhóm:** Group 2  
*   **Thành viên:**  
    1. Ngô Đình Khoa (SE196737)  
    2. Trịnh Phú Quốc (SE190287)  
    3. Trần Đăng Khoa (SE194398)  
    4. Đặng Đỗ Cao Sang (SE193269)  
    5. Đào Lý Phi Hùng (SE172826)  
*   **Topic Code:** RT-SWT-SE1905  
*   **Ngày nộp:** 2026-06-18  
*   **Version:** 2.4
*   **Trạng thái:** Đang chờ phê duyệt

---

## 2. Problem Statement

### 2.1 Bối cảnh & Tầm quan trọng

Behavior-Driven Development (BDD) là một phương pháp phát triển phần mềm Agile giúp tăng cường sự hợp tác giữa lập trình viên, kiểm thử viên và các bên liên quan bằng cách đặc tả yêu cầu hệ thống dưới dạng kịch bản Gherkin dễ đọc (`Given-When-Then`). Bằng cách kết nối giữa yêu cầu ngôn ngữ tự nhiên và kiểm thử thực thi, BDD đảm bảo phần mềm hoạt động đúng nghiệp vụ. Tuy nhiên, việc viết kịch bản Gherkin và chuyển đổi thủ công chúng thành mã kiểm thử (Step Definitions) tiêu tốn nhiều thời gian và dễ xảy ra lỗi nghiệp vụ (Fernandes et al. 2025).

Để tối ưu hóa, tự động hóa sinh kiểm thử BDD từ User Stories là một hướng nghiên cứu then chốt. Việc sử dụng các mô hình ngôn ngữ lớn (LLM) để sinh kịch bản và Step Definitions từ User Stories định dạng Connextra (`As a [role], I want [feature], so that [benefit]`) hứa hẹn tăng tốc quy trình kiểm thử và đảm bảo tính nhất quán giữa tài liệu và mã nguồn (Rathnayake et al. 2026).

Đánh giá các kỹ thuật Prompt Engineering trên mô hình ngôn ngữ lớn (LLM) là rất quan trọng để tối ưu hóa quy trình sinh tự động BDD. Trong thực tế, mặc dù các mô hình ngôn ngữ lớn có năng lực sinh mã nguồn và kịch bản kiểm thử mạnh mẽ, hiệu năng của chúng phụ thuộc rất lớn vào cách thiết kế chỉ dẫn (Prompt Design). Các kỹ thuật Prompt Engineering khác nhau như Zero-Shot, Few-Shot và Chain-of-Thought (CoT) mang lại những cấu trúc thông tin và định hướng suy luận khác nhau cho mô hình. Tuy nhiên, hiện tại vẫn chưa có nhiều nghiên cứu thực nghiệm đánh giá và so sánh một cách hệ thống ảnh hưởng của các kỹ thuật prompt khác nhau đến chất lượng sinh các tài liệu BDD (bao gồm kịch bản Gherkin và mã Step Definitions) từ User Stories thực tế. Việc thực hiện nghiên cứu này trên một mô hình nguồn mở như Qwen2.5-7B-Instruct sẽ giúp các đội ngũ phát triển hiểu rõ hiệu quả thực tế và giới hạn của từng kỹ thuật prompting, từ đó áp dụng giải pháp tự động hóa kiểm thử BDD local tối ưu và tiết kiệm chi phí.

### 2.2 State of the Art

Nhiều nghiên cứu gần đây đã ứng dụng LLM cho tự động hóa sinh ca kiểm thử:

Fernandes et al. (2025) đánh giá các mô hình như GPT-4, LLaMA-3, Gemini, DeepSeek R1 trên 34 User Stories miền FinTech bằng điểm tương đồng ngữ nghĩa METEOR. Gemini zero-shot đạt điểm cao nhất (0.84). Tuy nhiên, nghiên cứu chỉ giới hạn ở sinh kịch bản Gherkin (chưa sinh Step Definitions) và quy mô mẫu nhỏ.

Rathnayake et al. (2026) đóng góp bộ dữ liệu benchmark 500 User Stories thực tế kèm kịch bản BDD viết tay. GPT-4o zero-shot đạt tương đồng ngữ nghĩa BERTScore 91.16% và Cosine Similarity 53.96%. Tuy nhiên, nghiên cứu này mới chỉ dừng lại ở sinh kịch bản Gherkin mà chưa giải quyết bài toán sinh mã Step Definitions thực thi.

Karpurapu et al. (2024) tập trung vào độ chính xác cú pháp Gherkin tĩnh qua `gherkin-lint`, báo cáo tỷ lệ đúng 100% cho GPT-4 và 92% cho Llama-2 ở few-shot. Tuy nhiên, nghiên cứu chưa kiểm tra cú pháp Step Definitions đi kèm và chưa đánh giá tương đồng ngữ nghĩa với Ground Truth.

Selfbehave et al. (2026) tinh chỉnh LLaMA-3-8B bằng LoRA, đạt tỷ lệ biên dịch cú pháp Gherkin 99.2%. Hạn chế lớn nhất là nghiên cứu chỉ thực nghiệm trên dữ liệu tự sinh (synthetic) bằng self-instruct thay vì User Stories thực tế đa miền của doanh nghiệp.

### 2.3 GAP (Khoảng trống nghiên cứu)

Dựa trên tổng hợp các bài báo khoa học chính thức, nhóm xác định 3 khoảng trống nghiên cứu chính:
*   **GAP-T (Technology - Chính):** Chưa có nhiều nghiên cứu thực nghiệm đánh giá và so sánh các kỹ thuật Prompt Engineering như Zero-Shot, Few-Shot và Chain-of-Thought trong bài toán đồng sinh Gherkin Scenarios và Python Step Definitions từ Connextra User Stories trên mô hình nguồn mở chạy cục bộ (Hỗ trợ bởi: Fernandes et al. 2025, Rathnayake et al. 2026, dos Santos et al. 2026).
*   **GAP-M (Metric - Phụ):** Các nghiên cứu hiện tại còn thiếu một cơ chế kiểm định tĩnh kép (kết hợp gherkin-official parser và Python AST Parser) làm bộ lọc chất lượng trước khi tiến hành đo độ tương đồng ngữ nghĩa Cosine Similarity với kịch bản chuẩn, tránh việc đo lường trên các đoạn mã lỗi cú pháp (Hỗ trợ bởi: Karpurapu et al. 2024, Tesfalidet et al. 2025).
*   **GAP-D (Dataset - Hỗ trợ):** Các thực nghiệm còn hạn chế trên các tập dữ liệu benchmark đa miền thực tế quy mô lớn, phần lớn chỉ tập trung vào dữ liệu tự sinh hoặc tập dữ liệu nhỏ từ 5 đến 34 mẫu (Hỗ trợ bởi: Rathnayake et al. 2026).

### 2.4 Motivation

Nếu các khoảng trống này không được giải quyết, các doanh nghiệp và đội ngũ kỹ sư sẽ thiếu cơ sở khoa học để lựa chọn kỹ thuật hướng dẫn mô hình (prompting) hiệu quả nhất, dẫn đến chất lượng mã nguồn sinh ra không tối ưu. Sinh kịch bản Gherkin thiếu Step Definitions chỉ giải quyết được một nửa bài toán tự động hóa. Hơn nữa, việc đánh giá thiếu bộ lọc tĩnh kép sẽ dẫn đến rủi ro triển khai mã nguồn lỗi cú pháp, gây lãng phí tài nguyên thực thi và giảm lòng tin của kỹ sư phát triển. Nghiên cứu thực nghiệm này nhằm cung cấp bằng chứng thực nghiệm rõ ràng về hiệu quả của Zero-Shot, Few-Shot và Chain-of-Thought trên mô hình nguồn mở Qwen2.5-7B-Instruct chạy cục bộ, giúp các tổ chức xây dựng quy trình tự động hóa kiểm thử BDD local an toàn, khả thi và tối ưu nhất.

---

## 3. Related Work

### 3.1 Overview

Bảng dưới đây tóm tắt các công trình liên quan trực tiếp nhất đến tác vụ sinh kịch bản Gherkin và Step Definitions:

| Công trình nghiên cứu | Công cụ / LLM | Tập dữ liệu (Quy mô) | Độ đo | Kết quả tốt nhất | Hạn chế |
|:---|:---|:---|:---|:---|:---|
| **Rathnayake et al. 2026** | GPT-4o (Zero-shot) | 500 User Stories | BERTScore, Cosine Semantic Similarity | BERTScore = 91.16%, Cosine = 53.96% | Loại trừ sinh step definitions; không có kiểm định tĩnh kép. |
| **Fernandes et al. 2025** | GPT-3.5, GPT-4, LLaMA-3, Gemini, DeepSeek R1 | 34 User Stories | METEOR Score | METEOR = 0.84 (Gemini zero-shot) | Chỉ sinh kịch bản Gherkin; cỡ mẫu nhỏ, đơn miền. |
| **Selfbehave et al. 2026** | LLaMA-3-8B (LoRA-FT) | Tập dữ liệu tự sinh | Tỷ lệ cú pháp tĩnh | 99.2% đúng cú pháp Gherkin | Hoàn toàn phụ thuộc vào dữ liệu tự sinh bằng AI. |
| **Karpurapu et al. 2024** | GPT-3.5, GPT-4, Llama-2 | Cỡ mẫu nhỏ | Cú pháp qua `gherkin-lint` | 100% đúng cú pháp (GPT-4) | Không sinh Step Definitions; không đánh giá ngữ nghĩa. |
| **Tesfalidet et al. 2025** | GPT-4 | 10–20 User Stories | Cosine Similarity, Behave run rate | Similarity = 0.81, Executable rate = 85% | Cỡ mẫu nhỏ; giới hạn miền FinTech; thiếu bộ kiểm định tĩnh kép. |
| **dos Santos et al. 2026** | ChatGPT, Gemini, Grok, Copilot | 34 User Stories | Độ phủ tiêu chí nghiệm thu | Độ phủ cao cho ChatGPT | Quy mô dữ liệu nhỏ; chỉ sinh kịch bản Gherkin. |
| **Mendoza et al. 2024** | ChatGPT-4, Gemini, Copilot | 5 User Stories | Thang đo Likert (đánh giá người) | Điểm chấp nhận người cao | Cỡ mẫu cực nhỏ (5 mẫu); đánh giá cảm quan. |
| **Bergsmann et al. 2024** | Multi-Agent LLMs | 12-15 web apps | Tỷ lệ chạy test thành công | Tỷ lệ thành công cao | Dựa trên hệ thống multi-agent độ trễ cao, tốn token. |

### 3.2 Pattern Analysis

*   **Observation 1:** Các nghiên cứu đánh giá chất lượng ngôn ngữ chủ yếu dùng các độ đo tương đồng ngữ nghĩa như METEOR, BERTScore, Cosine Similarity so với Ground Truth (Fernandes et al. 2025, Rathnayake et al. 2026).
*   **Observation 2:** Đa số nghiên cứu thực nghiệm bị giới hạn bởi cỡ mẫu rất nhỏ (<50 stories), ngoại trừ Rathnayake et al. (2026) đóng góp 500 mẫu, gây ảnh hưởng đến tính hợp lệ bên ngoài.
*   **Observation 3:** Hầu hết nghiên cứu bỏ qua tính thực thi đồng thời của BDD. Các nghiên cứu sinh Step Definitions (Tesfalidet et al. 2025) chưa tích hợp quy trình lọc tĩnh kép trước khi đo ngữ nghĩa.
*   **Observation 4:** Nghiên cứu thực nghiệm so sánh hiệu năng giữa các kỹ thuật Prompt Engineering khác nhau (Zero-Shot, Few-Shot, Chain-of-Thought) để đồng sinh kịch bản Gherkin và Step Definitions trên các mô hình nguồn mở cỡ trung chạy cục bộ vẫn còn rất hạn chế theo rà soát hiện tại.

### 3.3 GAP Mapping

Bảng ánh xạ các GAP nghiên cứu phát hiện được từ tài liệu rà soát:

| GAP | Bằng chứng tài liệu | Trạng thái |
|:---|:---|:---|
| **GAP-T (Technology)** | 15 nghiên cứu; chưa có nghiên cứu nào trong các tài liệu được rà soát đánh giá quy trình so sánh các kỹ thuật Prompt Engineering (Zero-Shot, Few-Shot, Chain-of-Thought) cho tác vụ đồng sinh kịch bản Gherkin và Step Definitions | Xác nhận |
| **GAP-M (Metric)** | 15 nghiên cứu; chưa có nghiên cứu nào trong các tài liệu được rà soát triển khai quy trình kiểm định tĩnh kép | Xác nhận |
| **GAP-D (Dataset)** | 13/15 nghiên cứu sử dụng tập dữ liệu tự sinh hoặc cỡ mẫu nhỏ dưới 50 mẫu | Xác nhận |

---

## 4. Research Questions & PICO

### 4.1 Câu hỏi nghiên cứu chính (Main RQ)

Liệu có sự khác biệt có ý nghĩa thống kê về Semantic Similarity và Executable Syntax Rate giữa các kỹ thuật Prompt Engineering (Zero-Shot, Few-Shot, Chain-of-Thought) khi áp dụng trên mô hình Qwen2.5-7B-Instruct hay không?

### 4.2 Các câu hỏi nghiên cứu phụ (Sub-RQs)

#### RQ1 – Semantic Similarity (Độ tương đồng ngữ nghĩa)
Kỹ thuật Prompt Engineering nào tạo ra độ tương đồng ngữ nghĩa Cosine Similarity cao nhất so với Ground Truth?
*   *Cơ sở khoa học cho ngưỡng 0.80:* Ngưỡng 0.80 được lựa chọn dựa trên các nghiên cứu đi trước về so khớp ngữ nghĩa trong kiểm thử phần mềm (ví dụ: Fernandes et al. 2025 đạt điểm tương đồng trung bình 0.84 với Gemini; Tesfalidet et al. 2025 đạt 0.81 với GPT-4). Điểm số từ 0.80 trở lên biểu thị kịch bản BDD sinh ra giữ được các tiêu chí chấp nhận nghiệp vụ cốt lõi và ánh xạ đúng cấu trúc tham số của Ground Truth, giúp giảm thiểu đáng kể nỗ lực chỉnh sửa thủ công của kỹ sư.
*   *Hệ giả thuyết cho Zero-Shot:*
    $$\text{H0}_{1a}: \text{Median}(\text{Similarity}_{\text{Zero-Shot}}) \le 0.80$$
    $$\text{H1}_{1a}: \text{Median}(\text{Similarity}_{\text{Zero-Shot}}) > 0.80$$
*   *Hệ giả thuyết cho Few-Shot:*
    $$\text{H0}_{1b}: \text{Median}(\text{Similarity}_{\text{Few-Shot}}) \le 0.80$$
    $$\text{H1}_{1b}: \text{Median}(\text{Similarity}_{\text{Few-Shot}}) > 0.80$$
*   *Hệ giả thuyết cho Chain-of-Thought (CoT):*
    $$\text{H0}_{1c}: \text{Median}(\text{Similarity}_{\text{CoT}}) \le 0.80$$
    $$\text{H1}_{1c}: \text{Median}(\text{Similarity}_{\text{CoT}}) > 0.80$$

#### RQ2 – Executable Syntax Rate (Tỷ lệ cú pháp tĩnh khả thi)
Kỹ thuật Prompt Engineering nào tạo ra tỷ lệ cú pháp tĩnh hợp lệ Executable Syntax Rate tối thiểu 85% cao nhất sau khi qua bộ lọc kép Gherkin Parser và Python AST Validation?
*   *Hệ giả thuyết cho Zero-Shot:*
    $$\text{H0}_{2a}: p_{\text{syntax\_Zero-Shot}} \le 0.85$$
    $$\text{H1}_{2a}: p_{\text{syntax\_Zero-Shot}} > 0.85$$
*   *Hệ giả thuyết cho Few-Shot:*
    $$\text{H0}_{2b}: p_{\text{syntax\_Few-Shot}} \le 0.85$$
    $$\text{H1}_{2b}: p_{\text{syntax\_Few-Shot}} > 0.85$$
*   *Hệ giả thuyết cho Chain-of-Thought (CoT):*
    $$\text{H0}_{2c}: p_{\text{syntax\_CoT}} \le 0.85$$
    $$\text{H1}_{2c}: p_{\text{syntax\_CoT}} > 0.85$$

#### RQ3 – Comparative Evaluation (Đánh giá đối chứng)
Có sự khác biệt có ý nghĩa thống kê về chất lượng ngữ nghĩa và tỷ lệ cú pháp tĩnh hợp lệ giữa Zero-Shot, Few-Shot và Chain-of-Thought prompting khi áp dụng trên mô hình Qwen2.5-7B-Instruct hay không?
*   *Hệ giả thuyết so sánh độ tương đồng ngữ nghĩa (Paired Wilcoxon Signed-Rank Test):*
    - Zero-Shot vs Few-Shot:
      $$\text{H0}_{3a}: \text{Median}(\text{Similarity}_{\text{Few-Shot}} - \text{Similarity}_{\text{Zero-Shot}}) = 0$$
      $$\text{H1}_{3a}: \text{Median}(\text{Similarity}_{\text{Few-Shot}} - \text{Similarity}_{\text{Zero-Shot}}) \neq 0$$
    - Few-Shot vs Chain-of-Thought:
      $$\text{H0}_{3b}: \text{Median}(\text{Similarity}_{\text{CoT}} - \text{Similarity}_{\text{Few-Shot}}) = 0$$
      $$\text{H1}_{3b}: \text{Median}(\text{Similarity}_{\text{CoT}} - \text{Similarity}_{\text{Few-Shot}}) \neq 0$$
    - Zero-Shot vs Chain-of-Thought:
      $$\text{H0}_{3c}: \text{Median}(\text{Similarity}_{\text{CoT}} - \text{Similarity}_{\text{Zero-Shot}}) = 0$$
      $$\text{H1}_{3c}: \text{Median}(\text{Similarity}_{\text{CoT}} - \text{Similarity}_{\text{Zero-Shot}}) \neq 0$$
*   *Hệ giả thuyết so sánh tỷ lệ đúng cú pháp tĩnh (McNemar's Test):*
    - Zero-Shot vs Few-Shot:
      - $\text{H0}_{3d}$: Không có sự khác biệt có ý nghĩa thống kê về tỷ lệ đúng cú pháp tĩnh giữa Zero-Shot và Few-Shot.
      - $\text{H1}_{3d}$: Có sự khác biệt có ý nghĩa thống kê về tỷ lệ đúng cú pháp tĩnh giữa Zero-Shot và Few-Shot.
    - Few-Shot vs Chain-of-Thought:
      - $\text{H0}_{3e}$: Không có sự khác biệt có ý nghĩa thống kê về tỷ lệ đúng cú pháp tĩnh giữa Few-Shot và Chain-of-Thought.
      - $\text{H1}_{3e}$: Có sự khác biệt có ý nghĩa thống kê về tỷ lệ đúng cú pháp tĩnh giữa Few-Shot và Chain-of-Thought.
    - Zero-Shot vs Chain-of-Thought:
      - $\text{H0}_{3f}$: Không có sự khác biệt có ý nghĩa thống kê về tỷ lệ đúng cú pháp tĩnh giữa Zero-Shot và Chain-of-Thought.
      - $\text{H1}_{3f}$: Có sự khác biệt có ý nghĩa thống kê về tỷ lệ đúng cú pháp tĩnh giữa Zero-Shot và Chain-of-Thought.

### 4.3 Khung phân tích PICO (PICO Framework)

Bảng mô tả cấu trúc PICO của thực nghiệm:

| Thành phần PICO | Đặc tả chi tiết trong nghiên cứu của nhóm |
| :--- | :--- |
| **Population (P)** | 100 User Stories định dạng Connextra rút ngẫu nhiên không lặp (seed = 42) từ tập dữ liệu 500 mẫu của Rathnayake et al. (2026). |
| **Intervention (I)** | Áp dụng các kỹ thuật Prompt Engineering (Zero-Shot, Few-Shot, Chain-of-Thought) trên mô hình nguồn mở Qwen2.5-7B-Instruct. |
| **Comparison (C)** | So sánh đối chứng chéo giữa 3 kỹ thuật Prompting với nhau và so sánh với kịch bản chuẩn viết tay từ chuyên gia (Ground Truth). |
| **Outcome (O)** | Điểm tương đồng ngữ nghĩa Cosine Similarity (ngưỡng $\ge 0.80$) và Tỷ lệ cú pháp tĩnh hợp lệ Executable Syntax Rate (ngưỡng $\ge 85\%$). |

### 4.4 Variables Definition (Đặc tả biến nghiên cứu)

Để đảm bảo tính hợp lệ về mặt thực nghiệm, các biến trong nghiên cứu được phân loại rõ ràng như sau:
*   **Independent Variable (Biến độc lập - IV):** Kỹ thuật Prompt Engineering được áp dụng (Zero-Shot, Few-Shot, Chain-of-Thought).
*   **Dependent Variables (Biến phụ thuộc - DV):**
    1.  Độ tương đồng ngữ nghĩa Cosine Similarity (đo bằng mô hình nhúng SBERT `all-MiniLM-L6-v2` so với Ground Truth).
    2.  Tỷ lệ cú pháp tĩnh hợp lệ Executable Syntax Rate (xác định qua bộ lọc kép gherkin-official parser và Python AST Parser).

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

*Lý do chọn quy mô mẫu N = 100:* Quy mô mẫu N = 100 được lựa chọn nhằm cân bằng giữa chi phí tính toán thực nghiệm, thời gian thực thi và độ tin cậy thống kê.

*Lý do chọn Simple Random Sampling:* Đảm bảo mọi User Story trong tập dữ liệu gốc 500 mẫu đều có xác suất được chọn như nhau, giúp giảm thiểu tối đa thiên lệch lựa chọn (selection bias) và nâng cao khả năng tổng quát hóa kết quả (external validity) trên các miền nghiệp vụ khác nhau của tập dữ liệu gốc.

### 5.2 Experimental Pipeline

Quy trình thực nghiệm tuần tự được thiết kế như sau:

```
      User Story định dạng Connextra
                 ↓
        Qwen2.5-7B-Instruct
                 ↓
   [Zero-Shot / Few-Shot / CoT] Prompt
                 ↓
             Đồng sinh:
       • Kịch bản Gherkin (.feature)
       • Mã Python Step Definition (.py)
                 ↓
       Kiểm định cú pháp tĩnh (Parser & AST)
                 ↓
       Đánh giá ngữ nghĩa (SBERT Cosine)
                 ↓
       Phân tích thống kê (Wilcoxon, Binomial, McNemar)
```

Chi tiết mục đích của từng giai đoạn:
1.  **Connextra User Story:** Dữ liệu yêu cầu đầu vào chuẩn hóa làm ngữ cảnh cho LLM.
2.  **Qwen2.5-7B-Instruct:** Mô hình ngôn ngữ lớn nguồn mở thực thi suy luận cục bộ.
3.  **Prompt Configuration:** Cung cấp prompt tương ứng với 3 kỹ thuật thực nghiệm: Zero-Shot, Few-Shot, hoặc Chain-of-Thought.
4.  **Generate:** Đồng sinh kịch bản Gherkin (.feature) và Step Definitions (.py) sử dụng framework Behave trong một lượt suy luận duy nhất.
5.  **Static Validation:** Bộ lọc kép kiểm lỗi cú pháp tĩnh của kịch bản Gherkin (qua gherkin parser) và Step Code Python (qua AST).
6.  **Semantic Evaluation:** Đánh giá độ tương hợp nghiệp vụ Cosine SBERT so với Ground Truth của chuyên gia.
7.  **Statistical Analysis:** Áp dụng các phép kiểm thống kê toán học để kết luận hệ giả thuyết ở mức ý nghĩa $\alpha = 0.05$.

### 5.3 Model Configuration

#### Experimental Model (Mô hình thực nghiệm)
*   **Mô hình:** Qwen2.5-7B-Instruct
*   **Lý do lựa chọn:** 
    *   Là mô hình mã nguồn mở thế hệ mới với khả năng tuân thủ chỉ dẫn (instruction-following) và sinh mã nguồn (Code Generation) vượt trội trong nhóm mô hình quy mô dưới 10 tỷ tham số.
    *   Model có thể chạy thông qua Ollama local hoặc môi trường miễn phí như Kaggle Notebook tùy điều kiện phần cứng của nhóm.
    *   Không yêu cầu fine-tuning hay huấn luyện lại mô hình, loại bỏ hoàn toàn các rủi ro kỹ thuật liên quan đến việc huấn luyện (như tràn bộ nhớ, mất ổn định hàm loss) và chi phí chuẩn bị tập dữ liệu train.

#### Generation Settings (Tham số sinh)
*   **Temperature:** 0
*   **Top_p:** 1
*   *Lý do:* Thiết lập temperature = 0 và top_p = 1 đưa mô hình về chế độ sinh tất định (deterministic generation). Điều này triệt tiêu tính ngẫu nhiên của văn bản đầu ra, đảm bảo tính tái lập (reproducibility) cao nhất cho các kịch bản kiểm thử sinh ra khi thực thi lại thực nghiệm.

### 5.4 Prompt Templates

Nhóm xây dựng ba Prompt Template tương ứng với ba kỹ thuật Prompt Engineering bằng tiếng Anh học thuật để thực nghiệm trên Qwen2.5-7B-Instruct:

#### A. Zero-Shot Prompt Template
```text
You are an expert BDD engineer. Given a Connextra User Story, automatically generate a structured Gherkin Scenario and its corresponding Python Step Definitions (using the behave framework).

User Story:
{USER_STORY}

Requirements:
1. Ensure the Gherkin Scenario follows the standard Given-When-Then syntax.
2. Ensure the Python Step Definitions are syntactically valid and directly implement the steps in the Gherkin Scenario.
3. Output the results strictly in the format shown below, using 'Gherkin:' and 'Python:' delimiters. Do not include any other conversational filler.

Output Format:

Gherkin:
[Gherkin Scenario]

Python:
[Python Step Definitions]
```

#### B. Few-Shot Prompt Template
```text
You are an expert BDD engineer. Given a Connextra User Story, automatically generate a structured Gherkin Scenario and its corresponding Python Step Definitions (using the behave framework).

Here are two representative examples:

### Example 1
User Story:
As a registered user, I want to log in with my credentials, so that I can access my dashboard.

Gherkin:
Feature: User Login
  Scenario: Successful login with valid credentials
    Given the user is on the login page
    When the user enters a valid username "john_doe" and password "secure123"
    And clicks the login button
    Then they should be redirected to the dashboard

Python:
from behave import given, when, then

@given('the user is on the login page')
def step_impl(context):
    context.page = "login"

@when('the user enters a valid username "{username}" and password "{password}"')
def step_impl(context, username, password):
    context.username = username
    context.password = password

@when('clicks the login button')
def step_impl(context):
    context.logged_in = True

@then('they should be redirected to the dashboard')
def step_impl(context):
    assert context.logged_in is True
    context.page = "dashboard"


### Example 2
User Story:
As a shopper, I want to add an item to my shopping cart, so that I can purchase it later.

Gherkin:
Feature: Shopping Cart
  Scenario: Add product to cart
    Given the user has an empty shopping cart
    When the user views the product page for "Wireless Mouse"
    And clicks "Add to Cart"
    Then the shopping cart should contain 1 item of "Wireless Mouse"

Python:
from behave import given, when, then

@given('the user has an empty shopping cart')
def step_impl(context):
    context.cart = []

@when('the user views the product page for "{product_name}"')
def step_impl(context, product_name):
    context.current_product = product_name

@when('clicks "Add to Cart"')
def step_impl(context):
    context.cart.append(context.current_product)

@then('the shopping cart should contain {count:d} item of "{product_name}"')
def step_impl(context, count, product_name):
    assert len(context.cart) == count
    assert product_name in context.cart


Now, generate the BDD artifacts for the following user story. Follow the same output format.

User Story:
{USER_STORY}

Output Format:

Gherkin:
[Gherkin Scenario]

Python:
[Python Step Definitions]
```

#### C. Chain-of-Thought Prompt Template
```text
You are an expert BDD engineer. Given a Connextra User Story, you must automatically generate a structured Gherkin Scenario and its corresponding Python Step Definitions (using the behave framework).

Use step-by-step reasoning internally before generating the final answer. Do not reveal your reasoning process. Output only the final Gherkin Scenario and Python Step Definitions.

Structure your response strictly as follows, using 'Gherkin:' and 'Python:' delimiters:

Gherkin:
[Gherkin Scenario]

Python:
[Python Step Definitions]

User Story:
{USER_STORY}
```

---

### 5.5 Static Validation (Kiểm định tĩnh kép)

Quy trình kiểm định tĩnh được chia làm 2 giai đoạn độc lập:
*   **Gherkin Validation:** Sử dụng thư viện `gherkin-official` parser của Python để phân tích cú pháp tệp kịch bản `.feature` sinh ra và xác định các lỗi cú pháp Gherkin, đảm bảo cấu trúc các từ khóa Given-When-Then đúng định dạng.
*   **Python Validation:** Sử dụng module `ast` của Python để phân tích cây cú pháp tĩnh (Abstract Syntax Tree) của Step Code Python sinh ra thông qua hàm `ast.parse()`, kiểm tra lỗi `SyntaxError` (thụt lề, thiếu dấu hai chấm, đóng mở ngoặc, cú pháp sai).

**Executable Syntax Rate** được định nghĩa bằng tỷ lệ tệp đạt yêu cầu ở cả hai bộ lọc cú pháp tĩnh trên và được tính bằng công thức:

$$\text{Executable Syntax Rate} = \frac{N_{\text{pass}}}{N_{\text{total}}} \qquad (1)$$

Trong đó:
*   $N_{\text{pass}}$ là số lượng artifacts (cặp kịch bản Gherkin và mã Step Definitions) vượt qua cả bộ lọc gherkin parser và Python AST Validation.
*   $N_{\text{total}}$ là tổng số artifacts do mô hình sinh ra ($N_{\text{total}} = 100$).

### 5.6 Semantic Evaluation (Đánh giá ngữ nghĩa)

Tất cả các artifacts vượt qua bước static validation sẽ được so sánh trực tiếp với bộ kịch bản **Ground Truth viết tay của chuyên gia**.
*   **Độ đo:** Cosine Semantic Similarity (Tính qua mô hình nhúng SBERT `all-MiniLM-L6-v2`).
*   **Ngưỡng tối thiểu đạt:** 0.80.

Độ tương đồng ngữ nghĩa Cosine Similarity giữa hai vector biểu diễn nhúng $\vec{A}$ (Gherkin/Step Definitions sinh ra) và $\vec{B}$ (Ground Truth tương ứng) được tính bằng công thức:

$$\text{Cosine Similarity}(\vec{A}, \vec{B}) = \frac{\vec{A} \cdot \vec{B}}{\|\vec{A}\| \|\vec{B}\|} = \frac{\sum_{i=1}^{n} A_i B_i}{\sqrt{\sum_{i=1}^{n} A_i^2} \sqrt{\sum_{i=1}^{n} B_i^2}} \qquad (2)$$

*Lý do sử dụng Cosine Similarity qua SBERT:* Mô hình `all-MiniLM-L6-v2` là mô hình nhúng câu được tối ưu hóa cho tác vụ so khớp ngữ nghĩa. Việc sử dụng Cosine Similarity trên không gian nhúng của SBERT giúp phản ánh chính xác ngữ nghĩa nghiệp vụ của các kịch bản kiểm thử, khắc phục nhược điểm của các độ đo dựa trên từ vựng (như BLEU, ROUGE) vốn nhạy cảm với việc thay đổi từ đồng nghĩa nhưng vẫn đúng nghiệp vụ.

### 5.7 Statistical Analysis

Quy trình ánh xạ các phép kiểm thống kê toán học tương ứng cho mỗi câu hỏi nghiên cứu:

| Câu hỏi nghiên cứu | Độ đo | Phép kiểm thống kê |
| :--- | :--- | :--- |
| **RQ1** | Cosine Similarity | One-Sample Wilcoxon Signed-Rank Test (cho từng kỹ thuật so với ngưỡng 0.80) |
| **RQ2** | Executable Syntax Rate | One-Sample Binomial Exact Test (cho từng kỹ thuật so với ngưỡng 85%) |
| **RQ3 (Semantic)** | Cosine Similarity | Paired Wilcoxon Signed-Rank Test (so sánh cặp giữa các kỹ thuật) |
| **RQ3 (Syntax)** | Executable Syntax Rate | McNemar's Test (so sánh tỷ lệ cặp giữa các kỹ thuật) |

*Lý do sử dụng Wilcoxon Signed-Rank Test:* Đây là phép kiểm phi tham số phù hợp để so sánh các mẫu liên tục (điểm Cosine Similarity). Do điểm số tương đồng ngữ nghĩa thường không tuân theo phân phối chuẩn và bị giới hạn trong đoạn $[0, 1]$, việc sử dụng Wilcoxon Signed-Rank Test (One-sample cho RQ1, Paired cho RQ3) giúp tránh lỗi Type I khi các giả định của phép kiểm tham số bị vi phạm.

*Lý do sử dụng Binomial Exact Test (cho RQ2):* Phép kiểm này được áp dụng cho biến nhị phân (PASS/FAIL cú pháp tĩnh) để so sánh tỷ lệ thành công của mẫu với một tỷ lệ xác suất kỳ vọng cố định (85%), phù hợp tuyệt đối với cỡ mẫu hữu hạn $N = 100$.

*Lý do sử dụng McNemar's Test (cho RQ3 - Syntax):* Đây là phép kiểm phi tham số phù hợp để so sánh tỷ lệ của hai mẫu nhị phân phụ thuộc (cặp dữ liệu sinh ra từ cùng 100 User Stories đầu vào dưới các kỹ thuật prompt khác nhau).

---

## 6. Evaluation Plan

### 6.1 Hypothesis Mapping

Bảng ánh xạ câu hỏi nghiên cứu, tiêu chuẩn chất lượng và phép kiểm thống kê:

| RQ | Độ đo | Ngưỡng cắt (Threshold) | Phép kiểm thống kê |
| :--- | :--- | :--- | :--- |
| **RQ1** | Cosine Semantic Similarity | 0.80 | One-Sample Wilcoxon |
| **RQ2** | Executable Syntax Rate | 85% | Binomial Exact Test |
| **RQ3** | So sánh chéo các kỹ thuật | N/A | Paired Wilcoxon (ngữ nghĩa) & McNemar (cú pháp) |

### 6.2 Decision Criteria (Quy tắc ra quyết định)

*   **RQ1:** Bác bỏ giả thuyết không $H_0$ nếu $p < 0.05$ và giá trị trung vị Cosine Similarity của kỹ thuật tương ứng đạt $\ge 0.80$.
*   **RQ2:** Bác bỏ giả thuyết không $H_0$ nếu $p < 0.05$ và tỷ lệ cú pháp tĩnh khả thi thực tế của kỹ thuật tương ứng đạt $\ge 85\%$.
*   **RQ3:** Bác bỏ giả thuyết không $H_0$ nếu $p < 0.05$, chỉ ra sự khác biệt có ý nghĩa thống kê về chất lượng ngữ nghĩa và tỷ lệ cú pháp giữa các kỹ thuật Prompting (Zero-Shot, Few-Shot, Chain-of-Thought).

#### 6.2.1 Đo lường Kích cỡ Hiệu ứng (Effect Size)
Đối với phép kiểm Wilcoxon (RQ1 và RQ3), bên cạnh giá trị $p$, nhóm nghiên cứu sẽ báo cáo kích cỡ hiệu ứng (Effect Size) bằng chỉ số **Rank-Biserial Correlation** để đo lường mức độ ảnh hưởng thực tế của các kỹ thuật prompt.

### 6.3 Expected Outcomes (Kịch bản kết quả dự tính)

*   **Kịch bản A (Tối ưu):** Ít nhất một kỹ thuật prompt (thường dự kiến là Few-Shot hoặc Chain-of-Thought) đạt điểm Cosine Similarity $\ge 0.80$, Executable Syntax Rate $\ge 85\%$, và có sự vượt trội rõ rệt có ý nghĩa thống kê so với Zero-Shot. Kết luận kỹ thuật Prompt Engineering nâng cao (Few-Shot/CoT) là giải pháp hiệu quả giúp nâng cao chất lượng sinh BDD artifacts trên mô hình nguồn mở chạy cục bộ.
*   **Kịch bản B (Trung bình):** Các kỹ thuật prompt đều vượt qua ngưỡng kỳ vọng nhưng không có sự khác biệt có ý nghĩa thống kê rõ rệt giữa Few-Shot và Chain-of-Thought. Kết luận Few-Shot là đủ tốt để triển khai thực tế vì có độ trễ và số lượng token thấp hơn CoT.
*   **Kịch bản C (Không đạt):** Không có kỹ thuật prompt nào đạt các ngưỡng tối thiểu. Kết luận cần thiết kế lại cấu trúc ví dụ mẫu (few-shot examples) hoặc bổ sung thêm hướng dẫn ngữ cảnh chuyên sâu.

---

## 7. Threats to Validity

### 7.1 Internal Validity (Độ chính xác nội bộ)
*   **Mối đe dọa từ thiên kiến thiết kế Prompt (Prompt Design Bias):** Sự thiên kiến trong thiết kế prompt template có thể ảnh hưởng không mong muốn đến kết quả sinh ra của Qwen2.5-7B-Instruct. Nhóm giảm thiểu rủi ro này bằng cách xây dựng prompt dựa trên các tài liệu chuẩn hóa của behave, được rà soát chéo giữa các thành viên và cố định hoàn toàn prompt khung cho mọi lượt chạy.
*   **Mối đe dọa từ ví dụ mẫu (Few-Shot Example Selection Bias):** Việc lựa chọn 2 ví dụ mẫu trong Few-Shot prompt có thể khiến mô hình bị "quá khớp" (overfit) vào phong cách hoặc từ vựng của ví dụ. Nhóm giảm thiểu rủi ro này bằng cách chọn các ví dụ mẫu đa dạng từ các miền nghiệp vụ khác nhau (Login, Shopping Cart) và viết chuẩn mực theo đúng hướng dẫn.
*   **Mối đe dọa từ lập luận Chain-of-Thought (Reasoning Variability):** Yêu cầu mô hình lập luận trước khi sinh code (CoT) có thể dẫn đến việc lập luận sai nhưng code vẫn đúng, hoặc ngược lại. Nhóm giảm thiểu bằng cách hướng dẫn mô hình chỉ suy luận nội bộ và không xuất lập luận ra ngoài output (chỉ xuất các BDD artifacts đã qua xử lý), giúp triệt tiêu hoàn toàn nhiễu lập luận trong kết quả thô.

### 7.2 External Validity (Khả năng tổng quát hóa)
*   **Mối đe dọa:** Thực nghiệm trên một tập dữ liệu cụ thể có thể không phản ánh đúng khả năng trên các ngôn ngữ lập trình và miền nghiệp vụ khác.
*   **Hành động giảm thiểu (Mitigation):** Nhóm sử dụng tập dữ liệu thực tế đa miền của doanh nghiệp gồm 4 sản phẩm phần mềm thực tế (*Rathnayake et al. 2026*) và tiến hành rút mẫu ngẫu nhiên không lặp (seed = 42) để đảm bảo tập thực nghiệm đại diện tốt cho quần thể.

### 7.3 Construct Validity (Độ đo chính xác)
*   **Mối đe dọa:** Điểm tương đồng ngữ nghĩa Cosine có thể không phản ánh hoàn hảo chất lượng kiểm thử thực tế từ kỹ sư phát triển phần mềm.
*   **Hành động giảm thiểu (Mitigation):** Sử dụng mô hình nhúng SBERT `all-MiniLM-L6-v2` đã được chứng minh có tương quan rất cao với đánh giá ngữ nghĩa của con người. Đồng thời, tích hợp bộ kiểm định tĩnh kép (Gherkin & AST) làm bộ lọc tiền xử lý để loại trừ các tệp lỗi cú pháp trước khi tính điểm Cosine, tránh hiện tượng nhiễu điểm số.

### 7.4 Conclusion Validity (Tính hợp lệ kết luận)
*   **Mối đe dọa:** Quy mô mẫu quá nhỏ hoặc vi phạm giả định phân phối dữ liệu dẫn đến kết luận sai lầm về mặt thống kê.
*   **Hành động giảm thiểu (Mitigation):** Nhóm sử dụng quy mô mẫu lớn $N = 100$ để đảm bảo độ tin cậy thống kê. Đồng thời, sử dụng các phép kiểm thống kê phi tham số (Wilcoxon) không phụ thuộc vào giả định phân phối chuẩn của dữ liệu.

### 7.5 Dataset Validity (Mối đe dọa từ bộ dữ liệu thực nghiệm)
*   **Mối đe dọa:** Bộ dữ liệu từ Rathnayake et al. (2026) mặc dù đa miền nhưng có thể vẫn chưa bao phủ hết tất cả các cấu trúc User Story phức tạp hoặc các miền đặc thù khác.
*   **Hành động giảm thiểu (Mitigation):** Nhóm thừa nhận giới hạn này và định hướng nghiên cứu tiếp theo sẽ mở rộng kiểm thử trên các bộ dữ liệu chuyên biệt khác. Trong nghiên cứu này, việc rút mẫu ngẫu nhiên từ 4 hệ thống phần mềm doanh nghiệp thực tế giúp giảm thiểu tính đơn miền.

### 7.6 Ground Truth Bias (Thiên lệch trong kịch bản chuẩn)
*   **Mối đe dọa:** Kịch bản Ground Truth do chuyên gia viết tay có thể mang tính chủ quan của cá nhân người viết, dẫn đến việc mô hình sinh ra một kịch bản hoàn toàn đúng đắn nhưng lại bị chấm điểm thấp do khác biệt về phong cách viết.
*   **Hành động giảm thiểu (Mitigation):** Bộ dữ liệu Ground Truth được rà soát chéo độc lập bởi thành viên DG (Ngô Đình Khoa) và đối chiếu với các hướng dẫn viết BDD tiêu chuẩn để đảm bảo tính khách quan và chuẩn hóa cao nhất trước khi đưa vào so sánh.

---

## 8. Timeline & Resources

### 8.1 Phân công vai trò nhóm (Role Delegation)

Để đảm bảo tính độc lập khách quan và phân định rõ đóng góp học thuật của từng thành viên theo yêu cầu của giảng viên hướng dẫn, nhóm thống nhất cơ cấu trách nhiệm chi tiết như sau:

*   **Trần Đăng Khoa (PL - Project Lead):**
    *   *Đóng góp viết tài liệu:* Viết mục Bối cảnh & Tầm quan trọng (Section 2.1), GAP nghiên cứu (Section 2.3), Motivation (Section 2.4), và Related Work (Section 3).
    *   *Đóng góp kỹ thuật & quản lý:* Chịu trách nhiệm tổng hợp proposal, soát lỗi chính tả/định dạng, kiểm tra tính nhất quán học thuật toàn bộ tài liệu đề cương và quản lý tiến độ thực hiện dự án của các thành viên.
*   **Trịnh Phú Quốc (LR - LLM Runner):**
    *   *Đóng góp viết tài liệu:* Viết mục Thiết kế cấu hình mô hình (Section 5.3) và đặc tả các Prompt Templates (Section 5.4) cho Zero-Shot, Few-Shot, và Chain-of-Thought.
    *   *Đóng góp kỹ thuật & quản lý:* Phụ trách thiết kế chi tiết 3 loại prompts (bao gồm 2 ví dụ mẫu cho Few-Shot và hướng dẫn suy luận nội bộ cho CoT), cấu hình môi trường suy luận cục bộ Qwen2.5-7B-Instruct, thực thi chạy mô hình và thu thập dữ liệu đầu ra thô của thực nghiệm.
*   **Ngô Đình Khoa (DG - Data & Ground Truth):**
    *   *Đóng góp viết tài liệu:* Viết mục Đặc tả dữ liệu thực nghiệm (Section 5.1).
    *   *Đóng góp kỹ thuật & quản lý:* Chịu trách nhiệm nghiên cứu tập dữ liệu Rathnayake (2026), thực hiện quy trình lấy mẫu ngẫu nhiên đơn giản (Simple Random Sampling với seed = 42, không lặp) để trích xuất 100 mẫu, rà soát và kiểm định dữ liệu đối chứng Ground Truth. Hỗ trợ chuẩn hóa dữ liệu đầu ra, hỗ trợ quản lý và lưu trữ kết quả thực nghiệm, và hỗ trợ kiểm tra tính nhất quán giữa Output của mô hình và Ground Truth.
*   **Đặng Đỗ Cao Sang (MS - Metrics & Stats):**
    *   *Đóng góp viết tài liệu:* Viết mục Kiểm định tĩnh kép (Section 5.5), Đánh giá ngữ nghĩa (Section 5.6) và Quy trình phân tích thống kê (Section 5.7).
    *   *Đóng góp kỹ thuật & quản lý:* Xây dựng và thực thi bộ công cụ parser kiểm định cú pháp tĩnh (Gherkin parser và Python AST validation), lập trình tính toán điểm Cosine Semantic Similarity qua SBERT, thực hiện các phép kiểm thống kê toán học (One-Sample Wilcoxon, Binomial Exact, Paired Wilcoxon, McNemar), và viết báo cáo phân tích kết quả thực nghiệm.
*   **Đào Lý Phi Hùng (RW - Report Writer):**
    *   *Đóng góp viết tài liệu:* Viết mục Câu hỏi nghiên cứu (Section 4.1 & 4.2), Khung PICO (Section 4.3), Định nghĩa biến (Section 4.4), Kế hoạch đánh giá (Section 6.1 & 6.2), và Threats to Validity (Section 7). Viết phần Thảo luận (Discussion) và Kết luận (Conclusion) trong báo cáo cuối kỳ.
    *   *Đóng góp kỹ thuật & quản lý:* Thiết kế slide thuyết trình đề cương/slide nghiệm thu, hỗ trợ tổng hợp kết quả thực nghiệm, hỗ trợ chuẩn bị nội dung trả lời phản biện (Q&A Prep), và tổng hợp tài liệu báo cáo nghiệm thu khoa học cuối kỳ.

Bảng phân công chi tiết đóng góp học thuật và vai trò thực nghiệm:

| Thành viên | Trách nhiệm viết tài liệu | Trách nhiệm kỹ thuật thực nghiệm | Vai trò chính |
| :--- | :--- | :--- | :---: |
| **Trần Đăng Khoa** | Problem Statement, Motivation, Related Work, Soát lỗi tính nhất quán | Tổng hợp proposal, Quản lý tiến độ | PL |
| **Trịnh Phú Quốc** | Model Config, Prompt Templates (Zero, Few, CoT) | Thiết kế prompt, Cài đặt & chạy mô hình Qwen local | LR |
| **Ngô Đình Khoa** | Dataset Specification | Nghiên cứu dữ liệu, Random Sampling, Quản lý Ground Truth, Chuẩn hóa đầu ra, Lưu trữ kết quả thực nghiệm, Kiểm tra tính nhất quán Output vs Ground Truth | DG |
| **Đặng Đỗ Cao Sang**| Static Validation, Semantic Evaluation, Statistical Analysis | Xây dựng bộ lọc tĩnh parser/AST, Đo Cosine SBERT, Chạy code phân tích thống kê | MS |
| **Đào Lý Phi Hùng** | Research Questions, PICO, Threats to Validity, Timeline, Discussion & Conclusion, Slide | Thiết kế Slide, Hỗ trợ tổng hợp kết quả, chuẩn bị phản biện, hoàn thiện walkthrough | RW |

### 8.1.1 Danh mục Sản phẩm bàn giao cá nhân (Individual Deliverables)

Để phục vụ cho việc đánh giá đóng góp cá nhân của giảng viên hướng dẫn, dưới đây là bảng chi tiết các sản phẩm bàn giao chính (Deliverables) do từng thành viên chịu trách nhiệm độc lập hoặc phụ trách chính:

| Thành viên | Sản phẩm bàn giao chính (Primary Deliverables) |
| :--- | :--- |
| **Trần Đăng Khoa** | Đề cương proposal hoàn chỉnh (tổng hợp), Phần viết Problem Statement & Motivation (Section 2), Phần viết Related Work (Section 3), Kế hoạch quản lý tiến độ nhóm. |
| **Trịnh Phú Quốc** | Tài liệu đặc tả Prompt Templates (Section 5.4), Cấu hình mô hình Qwen local (Section 5.3), Bộ dữ liệu thô kết quả chạy thực nghiệm (Raw Outputs CSV). |
| **Ngô Đình Khoa** | Gói dữ liệu đầu vào chuẩn hóa (Dataset Package), Báo cáo kiểm định dữ liệu chuẩn (Ground Truth Validation Report), Bộ dữ liệu đầu ra đã chuẩn hóa và làm sạch (Cleaned Outputs). |
| **Đặng Đỗ Cao Sang**| Mã nguồn script kiểm định cú pháp tĩnh (Validation Scripts), Notebook lập trình phân tích thống kê (Statistical Notebook), Báo cáo kết quả phân tích số liệu (Analysis Report). |
| **Đào Lý Phi Hùng** | Báo cáo nghiệm thu kết quả cuối kỳ (Final walkthrough.md), Phần viết Thảo luận (Discussion) & Kết luận (Conclusion), Slide bảo vệ đề cương và nghiệm thu dự án. |

### 8.2 Quản lý Tài nguyên (Resource Inventory)

| Tài nguyên | Trạng thái | Chủ sở hữu | Ghi chú |
| :--- | :---: | :--- | :--- |
| Dataset Rathnayake | [Planned] | DG | Đã xác định nguồn dữ liệu, sẵn sàng tải và tiền xử lý. |
| Inference Environment | [Planned] | LR | Lập kế hoạch cài đặt Ollama chạy Qwen2.5-7B-Instruct cục bộ trên thiết bị của nhóm. |
| Thư viện kiểm định tĩnh | [Planned] | MS | Chuẩn bị mã nguồn tích hợp `ast` và package `gherkin-official`. |
| Thư viện thống kê | [Planned] | MS | Chuẩn bị tích hợp các thư viện `scipy.stats`, `statsmodels` và `sentence-transformers`. |

### 8.3 Dự trù kinh phí thực nghiệm
*   Ước tính chi phí thực nghiệm trực tiếp là khoảng 0 USD do mô hình Qwen2.5-7B-Instruct được chạy hoàn toàn cục bộ (local inference) trên phần cứng sẵn có của nhóm và sử dụng các thư viện phân tích thống kê mã nguồn mở (không yêu cầu thêm cơ sở hạ tầng đám mây hoặc API trả phí).

### 8.4 Kế hoạch thực hiện chi tiết theo tuần (Work Breakdown Timeline)

Nhóm phân chia lộ trình thực hiện dự án từ Tuần 5 đến Tuần 10 thành các đầu việc cụ thể với vai trò phân định rõ ràng giữa người phụ trách chính, người hỗ trợ và sản phẩm đầu ra tương ứng:

#### Tuần 5-6: Hoàn thiện proposal và slide bảo vệ đề cương
*   **Công việc thực hiện:**
    *   Viết và hoàn thiện các mục trong proposal (Problem Statement, Related Work, RQs, PICO, Methodology, Timeline, Threats).
    *   Thiết kế slide trình bày bảo vệ đề cương.
*   **Người phụ trách chính:** Trần Đăng Khoa (PL).
*   **Người hỗ trợ:** Toàn bộ thành viên trong nhóm (Trịnh Phú Quốc, Ngô Đình Khoa, Đặng Đỗ Cao Sang, Đào Lý Phi Hùng).
*   **Sản phẩm đầu ra (Deliverables):**
    *   Tệp đề cương nghiên cứu khoa học hoàn chỉnh `proposal.md` v2.4.
    *   Slide thuyết trình bảo vệ đề cương (Proposal defense slide deck).

#### Tuần 7: Chuẩn bị dataset, thiết kế prompt và chạy thử nghiệm Pilot
*   **Công việc thực hiện:**
    *   Tải tập dữ liệu gốc, viết script trích xuất 100 mẫu ngẫu nhiên không lặp (seed = 42) và chuẩn bị Ground Truth.
    *   Thiết kế cấu trúc prompt và viết các ví dụ mẫu cho kỹ thuật Few-Shot.
    *   Chạy thực nghiệm pilot trên 10 mẫu để kiểm thử tính khả thi của hệ thống và bộ parser.
*   **Người phụ trách chính:** Ngô Đình Khoa (DG) - chuẩn bị dữ liệu; Trịnh Phú Quốc (LR) - thiết kế prompt & chạy mô hình.
*   **Người hỗ trợ:** Đặng Đỗ Cao Sang (MS) - tích hợp parser tĩnh.
*   **Sản phẩm đầu ra (Deliverables):**
    *   Tập dữ liệu thực nghiệm đã chuẩn hóa (100 mẫu) kèm Ground Truth kiểm định.
    *   Tệp prompt templates hoàn chỉnh (Zero-Shot, Few-Shot, Chain-of-Thought).
    *   Kết quả pilot thô và logs chạy thử nghiệm trên 10 mẫu (Pilot results).

#### Tuần 8: Triển khai chạy thực nghiệm chính thức trên 100 mẫu
*   **Công việc thực hiện:**
    *   Chạy suy luận cục bộ Qwen2.5-7B-Instruct trên 100 mẫu đối với cả 3 kỹ thuật prompt (Zero-Shot, Few-Shot, Chain-of-Thought).
    *   Thu thập logs chạy thực nghiệm và xuất dữ liệu thô.
    *   Phân tách và lưu trữ kết quả thực nghiệm thô của từng mô hình.
*   **Người phụ trách chính:** Trịnh Phú Quốc (LR), Ngô Đình Khoa (DG).
*   **Người hỗ trợ:** Đặng Đỗ Cao Sang (MS).
*   **Sản phẩm đầu ra (Deliverables):**
    *   Tệp dữ liệu thô kết quả sinh của mô hình `prompt_experiment_outputs.csv` (100 mẫu $\times$ 3 cấu hình prompt).
    *   Bộ artifacts (kịch bản Gherkin và Python step definitions) đã được phân tách và lưu trữ có cấu trúc.

#### Tuần 9: Thực hiện Static Validation, Semantic Evaluation và Statistical Analysis
*   **Công việc thực hiện:**
    *   Chạy script phân tích cú pháp tĩnh (Gherkin parser và Python AST).
    *   Tính toán điểm Cosine Semantic Similarity bằng mô hình nhúng SBERT.
    *   Thực hiện các phép kiểm định thống kê toán học bằng scipy (Wilcoxon, Binomial, McNemar).
    *   Vẽ biểu đồ và tổng hợp kết quả phân tích số liệu.
*   **Người phụ trách chính:** Đặng Đỗ Cao Sang (MS).
*   **Người hỗ trợ:** Trịnh Phú Quốc (LR) - trích xuất logs và xử lý định dạng tệp lỗi.
*   **Sản phẩm đầu ra (Deliverables):**
    *   Tệp phân tích thống kê chi tiết chứa mã nguồn thực thi `statistical_analysis_results.ipynb`.
    *   Bảng tổng hợp kết quả kiểm định tĩnh và điểm Cosine (Validation & statistical results report).

#### Tuần 10: Hoàn thiện báo cáo cuối kỳ và thuyết trình nghiệm thu
*   **Công việc thực hiện:**
    *   Tổng hợp kết quả thực nghiệm và viết báo cáo nghiệm thu walkthrough cuối kỳ.
    *   Thiết kế slide thuyết trình nghiệm thu kết quả nghiên cứu.
    *   Tập duyệt bảo vệ kết quả trước hội đồng.
*   **Người phụ trách chính:** Đào Lý Phi Hùng (RW) - tổng hợp báo cáo và slide; Trần Đăng Khoa (PL) - rà soát chất lượng.
*   **Người hỗ trợ:** Toàn bộ thành viên trong nhóm (Trịnh Phú Quốc, Ngô Đình Khoa, Đặng Đỗ Cao Sang).
*   **Sản phẩm đầu ra (Deliverables):**
    *   Tệp báo cáo nghiệm thu kết quả dự án cuối kỳ hoàn chỉnh `walkthrough.md`.
    *   Slide trình bày bảo vệ kết quả cuối kỳ (Final defense slide deck).
    *   Bộ tài liệu nghiệm thu đóng gói (Presentation package bao gồm mã nguồn và dữ liệu sạch).

### 8.5 Kế hoạch dự phòng rủi ro (Contingency Plan)
*   **Mô hình Qwen chạy cục bộ bị lỗi tràn bộ nhớ (OOM):** LR chuyển sang sử dụng phiên bản lượng tử hóa 4-bit (Q4_K_M) của Qwen2.5-7B-Instruct qua Ollama để giảm dung lượng bộ nhớ RAM/VRAM yêu cầu hoặc chuyển sang chạy trên môi trường miễn phí như Kaggle Notebook với GPU T4 kép.
*   **Lỗi định dạng đầu ra của mô hình:** Thêm chỉ dẫn định dạng nghiêm ngặt (Markdown code block delimiters) vào hệ thống prompt và viết script regex parser mạnh mẽ hơn để tách biệt thành công phần kịch bản Gherkin và mã Python.
*   **Thành viên chậm tiến độ:** PL có quyền phân bổ lại nhiệm vụ hoặc yêu cầu họp khẩn cấp để xử lý nghẽn tiến độ sau 24 giờ không phản hồi.

### 8.6 Quy trình thay đổi đề cương (Amendment Process)
1.  Nếu quá trình thực nghiệm Pilot ở Tuần 7 phát hiện các vấn đề kỹ thuật nghiêm trọng (ví dụ: mô hình hoàn toàn không hiểu prompt template):
2.  Nhóm lập tài liệu ghi chép chi tiết lỗi và đề xuất phương án điều chỉnh prompt.
3.  Viết đề xuất thay đổi vào tệp `proposal-amendment.md` và nộp giảng viên hướng dẫn phê duyệt trong vòng 24 giờ trước khi chạy chính thức.
