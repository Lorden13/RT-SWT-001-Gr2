# Research Proposal: Co-generating BDD Gherkin Scenarios and Step Definitions from User Stories: A Comparative Evaluation of Fine-Tuned LLaMA-3-8B and GPT-4o

**Nhóm:** [RT-SWT-00X]
**Thành viên:**
*   [Họ tên thành viên 1] ([MSSV])
*   [Họ tên thành viên 2] ([MSSV])
*   [Họ tên thành viên 3] ([MSSV])
*   [Họ tên thành viên 4] ([MSSV])
*   [Họ tên thành viên 5] ([MSSV])

**Topic code:** [RT-SWT-00X]
**Ngày nộp:** [YYYY-MM-DD]
**Version:** 1.0
**Trạng thái:** Đang chờ phê duyệt

---

## 1. Problem Statement

### 1.1 Bối cảnh & Tầm quan trọng
Trong quy trình phát triển phần mềm hiện đại, phương pháp Phát triển hướng hành vi (Behavior-Driven Development - BDD) đóng vai trò then chốt trong việc thu hẹp khoảng cách giao tiếp giữa các bên liên quan và đội ngũ phát triển thông qua các kịch bản kiểm thử viết bằng ngôn ngữ tự nhiên Gherkin. Tuy nhiên, việc chuyển đổi thủ công các câu chuyện người dùng (User Stories) thành kịch bản Gherkin và mã kiểm thử (Step Definitions) tiêu tốn nhiều thời gian và dễ xảy ra lỗi sai lệch nghiệp vụ. Do đó, việc tự động hóa quy trình đồng sinh (co-generation) cả kịch bản và mã kiểm thử bằng các mô hình ngôn ngữ lớn (LLM) là vô cùng cần thiết để tối ưu hóa năng suất và đảm bảo chất lượng phần mềm.

### 1.2 State of the Art
Các nghiên cứu gần đây đã ứng dụng LLM trong việc tự động hóa sinh kịch bản kiểm thử BDD từ User Stories. Rathnayake et al. (2026) đã xây dựng bộ dữ liệu benchmark gồm 500 mẫu để sinh kịch bản Gherkin và đánh giá chất lượng ngữ nghĩa của chúng. Fernandes (2025) thực hiện so sánh hiệu năng các dòng LLM zero-shot cho tác vụ sinh kịch bản Gherkin bằng điểm METEOR. Tesfalidet et al. (2025) đã thử nghiệm sinh kịch bản thực thi trên framework Python Behave cho các dự án Fintech. Mặc dù đạt được những kết quả khả quan, hiệu năng cao chủ yếu vẫn phụ thuộc vào các mô hình đóng thương mại đắt đỏ như GPT-4 hay GPT-4o.

### 1.3 GAP (Khoảng trống nghiên cứu)
Dựa trên rà soát phản chứng từ bảng bằng chứng tổng hợp (N = 37 bài báo), nhóm xác định các khoảng trống nghiên cứu chính sau:
*   **GAP-T (Technology - Chính):** Chưa có nghiên cứu nào đánh giá toàn diện khả năng đồng sinh (co-generation) cả Gherkin Scenarios và Step Definitions từ Connextra User Stories bằng các mô hình nguồn mở cỡ nhỏ (8B parameters) được tinh chỉnh (fine-tuned) trên dữ liệu thực tế, nhằm thay thế các API đóng đắt đỏ và bảo mật thông tin doanh nghiệp.
*   **GAP-M (Metric - Phụ):** Thiếu sự đánh giá đồng thời, song song giữa chất lượng ngữ nghĩa (Semantic Similarity so với Ground Truth) và tính hợp lệ cú pháp tĩnh (Executable Syntax Rate qua bộ parser tĩnh kép) của mã kiểm thử sinh ra.
*   **GAP-D (Dataset - Hỗ trợ):** Thiếu một bộ dữ liệu benchmark đa miền chứa đầy đủ chuỗi vết từ Yêu cầu -> Kịch bản -> Mã kiểm thử thực thi. Nghiên cứu này sử dụng 100 mẫu ngẫu nhiên từ bộ dữ liệu thực tế của Rathnayake et al. (2026) để giải quyết hạn chế này.

### 1.4 Motivation
Nếu khoảng trống nghiên cứu này không được giải quyết, các doanh nghiệp phần mềm sẽ tiếp tục phải chịu chi phí API đắt đỏ hoặc đối mặt với nguy cơ rò rỉ dữ liệu yêu cầu nghiệp vụ khi sử dụng các LLM thương mại đóng. Đồng thời, việc thiếu bộ độ đo kép tích hợp sẽ dẫn đến việc sinh ra các test case tuy đúng cú pháp nhưng sai nghiệp vụ, hoặc đúng nghiệp vụ nhưng bị lỗi cú pháp không chạy được.

---

## 2. Related Work

### 2.1 Bảng tóm tắt các nghiên cứu liên quan (Tối đa 10 bài báo)

| Paper | Tool/LLM | Dataset (size) | Metric | Kết quả chính | Hạn chế / Gap |
|:---|:---|:---|:---|:---|:---|
| Rathnayake 2026 | GPT-4, Claude 3, Gemini | 500 User Stories thực tế | BERTScore, Cosine, Human Rating | GPT-4 đạt tương đồng ngữ nghĩa cao nhất. | Chưa sinh Step Definitions; chưa đánh giá cú pháp tĩnh kép. |
| Fernandes 2025 | GPT-4o, LLaMA-3, Gemini | 10 ca kiểm thử chọn lọc | METEOR, CV | Zero-shot đạt kết quả tốt nhất; Gemini và Phi-3 đạt điểm cao nhất. | Quy mô mẫu rất nhỏ (10 mẫu); chưa đo lỗi thực thi động. |
| Selfbehave 2026 | LLaMA-3-8B, GPT-4 | 5,000 kịch bản tự sinh | Syntax Pass Rate | Huấn luyện thành công LLaMA-3-8B đạt 99.2% cú pháp Gherkin. | Dữ liệu hoàn toàn là tự sinh (synthetic), chưa thử trên User Stories doanh nghiệp thực tế. |
| Tesfalidet 2025 | GPT-4, GPT-3.5 | 10-20 fintech stories | Compliance, Executable Step, Cosine | GPT-4 đạt 85% executable steps, Cosine = 0.81. | Cỡ mẫu nhỏ; giới hạn trong miền fintech và framework Python Behave. |
| dos Santos 2025 | GPT-4, Llama-2-13B | ~50 stories Agile | Syntax Accuracy qua gherkin-lint | Few-shot đạt 100% cú pháp với GPT-4; Llama-2 đạt 92%. | Chỉ đánh giá cú pháp tĩnh, chưa kiểm tra ngữ nghĩa và độ phủ. |
| Poth 2025 | GPT-4o, LLaMA-3-8B | 12-25 file Gherkin | UI Compilation Rate, Locator Accuracy | GPT-4o đạt 88% compilation rate; LLaMA-3-8B đạt 61.5% locator accuracy. | Phụ thuộc nặng vào chất lượng thuộc tính HTML trong context. |
| Mendoza 2024 | ChatGPT-4, Gemini, Copilot | 5 kịch bản BDD | Thang đo Likert | ChatGPT-4 và Gemini đạt điểm cao nhất 23/24. | Copilot không đáp ứng định dạng Gherkin; LLM yếu logic toán. |
| Bergsmann 2024 | GPT-4o, Gemini | 12-15 web apps | Execution Success Rate | Hệ thống Multi-Agent đạt 83-84% tỷ lệ chạy thành công. | Chi phí token rất cao; tương tác bất định giữa các agent. |
| AutoQALLMs 2026 | GPT-4, LLaMA-3-8B | 10 web apps | Selenium Executability | 86% script Selenium chạy thành công, tìm ra 11 bugs. | Sinh ra các hàm Selenium bị deprecated; cần cập nhật prompt liên tục. |
| Ferreira 2025 | LLM Pipeline | User Stories | Executability, Quality | Đề xuất pipeline sinh Gherkin -> Cypress code. | Cần validation/repair sau sinh; sinh một lần chưa ổn định. |

### 2.2 Phân tích xu hướng (Pattern Analysis)
1.  **Sự phân mảnh về độ đo:** Các nghiên cứu trước đây thường chỉ tập trung vào một khía cạnh đo lường riêng biệt: hoặc đo ngôn ngữ tĩnh (BERTScore, METEOR) hoặc đo thực thi động (Compilation Rate, Executable Steps), chưa có sự kết hợp đồng thời để đánh giá toàn diện chất lượng test.
2.  **Sự thống trị của mô hình đóng:** GPT-4/GPT-4o luôn là baseline mạnh nhất trong các nghiên cứu thực nghiệm BDD, trong khi các mô hình nguồn mở chưa qua tinh chỉnh (như LLaMA-3-8B) có hiệu năng kém hơn rõ rệt (chênh lệch từ 15-20% về độ chính xác cú pháp và định vị phần tử).
3.  **Hạn chế quy mô dữ liệu:** Đa số các nghiên cứu thực chứng sử dụng các bộ dữ liệu nhỏ lẻ tự xây dựng (<50 mẫu) hoặc dữ liệu tự sinh (synthetic) bằng AI, gây thiếu kiểm chứng về khả năng tổng quát hóa trên các dự án phần mềm đa miền thực tế.

### 2.3 GAP Mapping

| GAP Loại | Bằng chứng nghiên cứu hỗ trợ | Trạng thái xác nhận |
|:---|:---|:---|
| **GAP-T (Technology)** | Rathnayake 2026, Selfbehave 2026, Fernandes 2025 | **Confirmed** (Nhóm sẽ giải quyết bằng cách tinh chỉnh LLaMA-3-8B LoRA) |
| **GAP-M (Metric)** | Tesfalidet 2025, dos Santos 2025, Poth 2025 | **Confirmed** (Nhóm thiết lập bộ kiểm định tĩnh kép + Cosine SBERT) |
| **GAP-D (Dataset)** | Rathnayake 2026, Selfbehave 2026 | **Confirmed** (Sử dụng mẫu ngẫu nhiên 100 User Stories đa miền thực tế) |

---

## 3. Research Questions

*   **Main RQ:** Khi áp dụng trên bộ dữ liệu User Stories viết theo định dạng Connextra và mô tả yêu cầu thực tế, liệu mô hình ngôn ngữ lớn nguồn mở **LLaMA-3-8B** được tinh chỉnh bằng phương pháp **LoRA** có khả năng tự động sinh đồng thời kịch bản Gherkin và mã kiểm thử (step definitions) tương đồng ngữ nghĩa (Cosine Similarity $\ge 0.85$ so với Ground Truth) và đạt tỷ lệ cú pháp tĩnh khả thi (Executable Syntax Rate $\ge 85\%$), tương đương hoặc vượt trội so với mô hình thương mại đóng hàng đầu **GPT-4o** hay không?
*   **RQ1 (Semantic Similarity):** Mô hình LLaMA-3-8B (Fine-tuned via LoRA) có đạt độ tương đồng ngữ nghĩa trung bình (Cosine Similarity sử dụng mô hình nhúng `all-MiniLM-L6-v2`) từ **0.85 trở lên** so với bộ kịch bản kiểm thử viết tay của chuyên gia (Ground Truth) hay không?
    *   *Claim type:* Absolute threshold.
    *   *Hệ giả thuyết:*
        $$\text{H0}_{1a}: \text{Median}(\text{Similarity}_{\text{LLaMA-FT}}) \le 0.85$$
        $$\text{H1}_{1a}: \text{Median}(\text{Similarity}_{\text{LLaMA-FT}}) > 0.85$$
*   **RQ2 (Executable Syntax Rate):** Mô hình LLaMA-3-8B (Fine-tuned via LoRA) có đạt tỷ lệ hợp lệ cú pháp tĩnh (Executable Syntax Rate) từ **85% trở lên** (không xảy ra lỗi phân tích cú pháp tĩnh từ Gherkin Parser và Python AST Parser) hay không?
    *   *Claim type:* Absolute threshold.
    *   *Hệ giả thuyết:*
        $$\text{H0}_{2a}: p_{\text{syntax\_LLaMA}} \le 0.85$$
        $$\text{H1}_{2a}: p_{\text{syntax\_LLaMA}} > 0.85$$
*   **RQ3 (Comparative Evaluation):** Có sự khác biệt có ý nghĩa thống kê về độ tương đồng ngữ nghĩa và tỷ lệ cú pháp tĩnh khả thi giữa mô hình LLaMA-3-8B (LoRA-FT) và mô hình GPT-4o zero-shot hay không?
    *   *Claim type:* Comparative claim.
    *   *Hệ giả thuyết:*
        $$\text{H0}_{1b}: \text{Median}(\text{Similarity}_{\text{LLaMA-FT}} - \text{Similarity}_{\text{GPT-4o}}) = 0$$
        $$\text{H1}_{1b}: \text{Median}(\text{Similarity}_{\text{LLaMA-FT}} - \text{Similarity}_{\text{GPT-4o}}) \neq 0$$

---

## 4. Experiment Protocol

### 4.1 Quy trình thực nghiệm (Pipeline)
Quy trình thực nghiệm gồm 6 bước chi tiết:
1.  **Dữ liệu đầu vào:** Thu thập bộ dữ liệu nguồn từ Rathnayake et al. (2026), rút mẫu ngẫu nhiên 100 User Stories định dạng Connextra kèm Requirement Descriptions.
2.  **Tiền xử lý:** Chuẩn hóa cấu trúc văn bản đầu vào và đưa vào tiêu chuẩn prompt template được thiết kế sẵn.
3.  **Thực thi mô hình (LLM Run):** Chạy sinh kịch bản đồng thời bằng GPT-4o (Zero-shot) và LLaMA-3-8B (LoRA-FT).
4.  **Tách xuất dữ liệu (Extraction):** Dùng biểu thức chính quy (Regex) tách phần kịch bản Gherkin và Step Definitions Python từ kết quả của LLM.
5.  **Kiểm định tĩnh kép (Static Validation):** Chạy Gherkin Parser trên tệp kịch bản và Python AST module trên tệp Step Code. Ghi nhận kết quả PASS/FAIL cú pháp tĩnh.
6.  **Đánh giá ngữ nghĩa & Phân tích:** Đo độ tương đồng Cosine qua `all-MiniLM-L6-v2` cho các mẫu PASS tĩnh, sau đó tiến hành kiểm định thống kê trên công cụ Python.

### 4.2 Thiết kế Dataset thực nghiệm
*   **Dataset nguồn:** Bộ dữ liệu công khai từ Rathnayake et al. (2026) gồm 500 User Stories, 500 Requirement Descriptions và 500 kịch bản Gherkin thủ công (Ground Truth) được thu thập từ 4 dự án phần mềm thực tế đa miền của doanh nghiệp.
*   **Phương pháp rút mẫu:** Sử dụng phương pháp rút mẫu ngẫu nhiên đơn giản (Simple Random Sampling) không lặp bằng thư viện Pandas trong Python để chọn ra đúng **100 mẫu** thực nghiệm nhằm loại bỏ thiên kiến chọn mẫu.
*   **Dự phòng dữ liệu:** Xác nhận bộ dữ liệu nguồn đã được tải về thành công và lưu trữ trên thư mục máy cục bộ của nhóm, sẵn sàng truy cập không cần phụ thuộc mạng.

### 4.3 Cấu hình Mô hình (LLM Configuration)
*   **Mô hình Can thiệp:** LLaMA-3-8B-Instruct tinh chỉnh bằng phương pháp LoRA (QLoRA 4-bit, Rank = 8, Alpha = 16, Target Modules = `q_proj, v_proj`, Learning Rate = $2\times 10^{-4}$).
*   **Mô hình Đối chứng:** GPT-4o (`gpt-4o-2024-08-06`) gọi qua API.
*   **Siêu tham số thực thi (Inference Hyperparameters):**
    *   `temperature = 0` (Đảm bảo tính tất định).
    *   `top_p = 1.0`
    *   `max_tokens = 2048`
*   **Prompt Template mẫu nguyên văn:**
    ```text
    You are an expert QA Engineer specializing in Behavior-Driven Development (BDD).
    Your task is to generate both a Gherkin Scenario (.feature) and the corresponding Python Step Definitions (.py) using the 'behave' framework.

    Input User Story:
    {user_story}

    Input Requirement Description:
    {requirement_description}

    Output Format:
    You MUST output the Gherkin Scenario inside the `[START_GHERKIN]` and `[END_GHERKIN]` tags.
    You MUST output the Python Step Definitions inside the `[START_STEPS]` and `[END_STEPS]` tags. Do not include any other markdown code block syntax around them, just the tags.

    Example structure:
    [START_GHERKIN]
    Feature: ...
      Scenario: ...
    [END_GHERKIN]
    [START_STEPS]
    from behave import given, when, then
    ...
    [END_STEPS]
    ```

### 4.4 Kế hoạch kiểm định thống kê (Statistical Analysis Plan)
*   ** Wilcoxon Signed-Rank Test (Một mẫu, Một đuôi):** So sánh giá trị trung vị Cosine Similarity của LLaMA-FT với giá trị ngưỡng 0.85 ($\alpha = 0.05$).
*   ** Wilcoxon Signed-Rank Test (Cặp, Hai đuôi):** So sánh hiệu năng Cosine Similarity trực tiếp giữa LLaMA-FT và GPT-4o trên 100 mẫu cặp phụ thuộc.
*   ** Binomial Exact Test (Một mẫu, Một đuôi):** Đánh giá xem tỷ lệ đúng cú pháp tĩnh thực tế của từng mô hình có vượt trội hơn ngưỡng xác suất lý thuyết 85% ($\alpha = 0.05$) hay không.
*   **Phân tích lực lượng mẫu (Power Analysis):** Với cỡ mẫu $N = 100$, độ lớn ảnh hưởng kỳ vọng trung bình $d = 0.35$ (cỡ ảnh hưởng trung bình yếu), kiểm định đạt lực lượng mẫu (statistical power) $\beta \ge 0.80$ ở mức ý nghĩa $\alpha = 0.05$.

---

## 5. Evaluation Plan

### 5.1 Bảng tiêu chí đánh giá và Phép kiểm thống kê

| RQ | Metric | Ngưỡng | Phép kiểm thống kê | Điều kiện bác bỏ H0 | Biện giải kết quả âm tính (Negative Result) |
|:---|:---|:---|:---|:---|:---|
| **RQ1** | Cosine Similarity | $\ge 0.85$ | One-sample Wilcoxon (1-tailed) | p-value $< 0.05$ và Median $> 0.85$ | Nếu bác bỏ thất bại: Tinh chỉnh LoRA chưa tối ưu hóa tốt ngữ nghĩa nghiệp vụ; cần tăng kỷ nguyên huấn luyện (epochs) hoặc sử dụng Few-shot Prompting. |
| **RQ2** | Executable Syntax Rate | $\ge 85\%$ | One-sample Binomial (1-tailed) | p-value $< 0.05$ và Rate $> 85\%$ | Nếu bác bỏ thất bại: Mô hình bị ảo tưởng cú pháp; cần tối ưu lại Prompt Template hoặc bổ sung tập luật Regex sửa lỗi tự động. |
| **RQ3** | So sánh Cosine | Đối chứng | Paired Wilcoxon (2-tailed) | p-value $< 0.05$ | Nếu không có sự khác biệt (p $\ge$ 0.05): LLaMA-3-8B local đã tiệm cận hiệu năng của GPT-4o; chứng minh sự thành công lớn của phương pháp LoRA. |

### 5.2 Phân tích các kịch bản kết quả (Synthesis of Results)
*   **Kịch bản 1 (Double Positive):** LLaMA-FT vượt qua cả hai ngưỡng (Cosine $> 0.85$ và Cú pháp tĩnh $> 85\%$). Kết luận mô hình nguồn mở tinh chỉnh hoàn toàn sẵn sàng triển khai thực tế.
*   **Kịch bản 2 (Mixed):** Đạt ngưỡng cú pháp tĩnh nhưng thất bại ở tương đồng ngữ nghĩa. Kết luận mô hình viết code chuẩn nhưng bị lệch hướng nghiệp vụ (cần cải thiện tập dữ liệu tinh chỉnh).
*   **Kịch bản 3 (Double Negative):** Thất bại ở cả hai tiêu chí. Kết luận mô hình nguồn mở 8B chưa đủ khả năng giải quyết bài toán đồng sinh BDD phức tạp.

---

## 6. Threats to Validity

*   **Internal Validity (Độ chính xác nội bộ):** Sự thiên kiến trong cách viết prompt template có thể làm giảm hiệu năng của một trong hai mô hình.
    *   *Mitigation:* Sử dụng cùng một prompt template chuẩn hóa, trung lập cho cả hai mô hình và thiết lập cấu hình tham số giống nhau.
*   **External Validity (Khả năng tổng quát hóa):** Kết quả nghiên cứu có thể chỉ đúng trên bộ dữ liệu của Rathnayake mà không đúng trên dự án thực tế khác.
    *   *Mitigation:* Lựa chọn bộ dữ liệu nguồn đa miền (gồm 4 sản phẩm phần mềm thực tế khác nhau) để nâng cao tính đại diện.
*   **Construct Validity (Độ đo chính xác):** Cosine Similarity có thể không phản ánh hoàn toàn đánh giá chất lượng của lập trình viên con người.
    *   *Mitigation:* Sử dụng mô hình nhúng Sentence-BERT (`all-MiniLM-L6-v2`) đã được chứng minh có tương quan cao với đánh giá của con người trên tác vụ tương đồng văn bản.
*   **Conclusion Validity (Tính hợp lệ kết luận):** Cỡ mẫu quá nhỏ có thể dẫn đến sai lầm loại I hoặc loại II trong kết luận thống kê.
    *   *Mitigation:* Sử dụng cỡ mẫu $N = 100$ và tiến hành kiểm tra lực lượng mẫu (Power Analysis) đạt chuẩn khoa học.

---

## 7. Timeline & Resources

### 7.1 Phân công vai trò (Role Delegation)

| Vai trò | Thành viên đảm nhận | Nhiệm vụ chi tiết trong thực nghiệm |
|:---|:---|:---|
| **PL (Project Lead)** | [Họ tên PL] | Điều phối tiến độ nhóm, kiểm tra tính nhất quán của đề cương và báo cáo cuối cùng, submit sản phẩm. |
| **DG (Data & Ground Truth)** | [Họ tên DG] | Rút mẫu ngẫu nhiên 100 User Stories, kiểm định dữ liệu Ground Truth, viết Phần 2 (Related Work) của đề cương. |
| **LR (LLM Runner)** | [Họ tên LR] | Cài đặt API, viết script chạy thực nghiệm sinh code trên GPT-4o và LLaMA-3-8B local, lưu log chi phí. |
| **MS (Metrics & Stats)** | [Họ tên MS] | Lập trình bộ parser cú pháp tĩnh, tính Cosine Similarity, thực hiện kiểm định Wilcoxon và Binomial bằng thư viện Python. |
| **RW (Report Writer)** | [Họ tên RW] | Định dạng tài liệu, viết phần Threats to Validity, vẽ biểu đồ trực quan hóa dữ liệu và viết báo cáo cuối cùng. |

> [!IMPORTANT]
> Thành viên giữ vai trò **LR (LLM Runner)** và **MS (Metrics & Stats)** bắt buộc phải là hai người khác nhau để đảm bảo tính khách quan và phân rã trách nhiệm độc lập theo quy tắc RBL-3.

### 7.2 Quản lý Tài nguyên (Resource Inventory)

| Tài nguyên | Trạng thái | Chủ sở hữu | Ghi chú |
|:---|:---:|:---|:---|
| Dataset 100 mẫu | [x] | DG | Đã tải về máy cục bộ, kiểm tra truy cập OK. |
| GPT-4o API Key | [x] | LR | Đã kích hoạt tài khoản OpenAI API và nạp tiền dự phòng. |
| Compute Platform | [x] | LR | Sử dụng GPU Google Colab Pro / Kaggle P100. |
| Thư viện kiểm định | [x] | MS | Cài đặt thành công `scipy`, `gherkin-official`, `sentence-transformers`. |

### 7.3 Ước tính chi phí thực nghiệm

| Khoản mục | Số lượng | Đơn giá | Thành tiền (USD) | Ghi chú |
|:---|:---:|:---|:---|:---|
| Input Tokens (GPT-4o) | ~150,000 tokens | $2.50 / 1M tokens | $0.38 | Cho 100 mẫu đầu vào |
| Output Tokens (GPT-4o) | ~250,000 tokens | $10.00 / 1M tokens | $2.50 | Cho kịch bản sinh ra |
| Compute (Colab / Kaggle) | 10 giờ chạy | $0.00 | $0.00 | Sử dụng tài nguyên free tier |
| **Tổng chi phí dự tính** | | | **$2.88** | Rất tối ưu cho ngân sách sinh viên |

### 7.4 Kế hoạch chi tiết (Timeline Tuần 5-10)

| Tuần | Hoạt động | Người chịu trách nhiệm | checkpoint / Đầu ra cụ thể |
|:---|:---|:---|:---|
| **Tuần 5-6** | Hoàn thiện đề cương và nộp phê duyệt | Cả nhóm | Nộp file `proposal.md` đạt chuẩn chất lượng. |
| **Tuần 7** | Thực hiện chạy Pilot (10% dữ liệu) | LR + MS + DG | Tệp `pilot_ground_truth.csv`, `pilot_llm_output.csv` và log chạy không lỗi. |
| **Tuần 8** | Thực hiện chạy thực nghiệm chính thức (100%) | LR | Tệp `full_llm_output.csv` và hóa đơn chi phí API thực tế. |
| **Tuần 8** | Chạy đo lường và tính toán metrics | MS | Tệp phân tích `full_analysis.ipynb` chứa p-value kiểm định. |
| **Tuần 9-10** | Viết báo cáo hoàn chỉnh và làm slide | RW + PL | Slide thuyết trình và file báo cáo nghiệm thu `walkthrough.md`. |

### 7.5 Kế hoạch dự phòng (Contingency Plan)
*   **Trường hợp Đề cương bị phản hồi sửa đổi:** PL chịu trách nhiệm tổ chức họp nhóm ngay trong 24 giờ để điều chỉnh theo ý kiến giáo viên hướng dẫn.
*   **Trường hợp API Rate Limit:** LR sẽ cấu hình cơ chế chia batch dữ liệu nhỏ (mỗi batch 10 mẫu) và dừng nghỉ 60 giây giữa các lần gọi API.
*   **Trường hợp mô hình local LLaMA lỗi bộ nhớ:** LR chuyển sang sử dụng mô hình LLaMA-3-8B-Instruct không tinh chỉnh thông qua kỹ thuật Few-shot Prompting để đối chứng hiệu năng.
*   **Trường hợp thành viên trễ hạn:** PL sẽ kích hoạt phân phối lại công việc khẩn cấp sau 48 giờ trễ hạn không có lý do chính đáng.

### 7.6 Quy trình sửa đổi đề cương (Amendment Process)
Khi có sự thay đổi về mặt kỹ thuật phát hiện được trong quá trình chạy Pilot ở Tuần 7:
1.  Nhóm ghi nhận lỗi kỹ thuật cụ thể (ví dụ: phân phối điểm dữ liệu bimodal cần thay đổi phép kiểm thống kê).
2.  Viết đề xuất thay đổi vào tệp `proposal-amendment-v1.1.md` theo mẫu chuẩn.
3.  Nộp giáo viên phê duyệt sửa đổi trong vòng 24 giờ kể từ cuộc họp Pilot của nhóm.
4.  Cập nhật cấu hình mới vào mã nguồn thực nghiệm chính thức.
