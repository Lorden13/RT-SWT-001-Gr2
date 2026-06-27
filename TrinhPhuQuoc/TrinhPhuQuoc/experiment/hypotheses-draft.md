# Thiết Kế Giả Thuyết Thống Kê — Hypotheses Draft (Trịnh Phú Quốc)

Tài liệu này trình bày các câu hỏi nghiên cứu (RQ), khung phân tích PICO, các giả thuyết thống kê định lượng và phép kiểm định thống kê được lựa chọn cho thực nghiệm.

---

## 1. Tinh chỉnh Câu hỏi nghiên cứu (RQ) theo PICO

Dựa trên kết quả rà soát từ SLR (RBL-1) và phân tích khoảng trống nghiên cứu (RBL-2), nhóm tinh chỉnh câu hỏi nghiên cứu chính thức như sau:

### Câu hỏi nghiên cứu chính (Main RQ)
> **Main RQ:** Liệu mô hình ngôn ngữ lớn đóng thế hệ mới **GPT-4o** ở chế độ **zero-shot** (temperature = 0) có khả năng sinh kịch bản đặc tả Gherkin và mã step definitions tự động từ User Stories Agile (định dạng Connextra) đạt độ tương đồng ngữ nghĩa Cosine Similarity $\ge 0.85$ so với expert baseline viết tay và đạt tỷ lệ hợp lệ cú pháp tĩnh (Executable Syntax Rate) $\ge 80\%$ hay không?

### Khung phân tích PICO chính thức
*   **P — Population (Đối tượng):** 50 Agile User Stories viết theo định dạng Connextra ("As a... I want... So that...") thuộc các dự án phần mềm thực tế.
*   **I — Intervention (Can thiệp):** Mô hình GPT-4o zero-shot (temperature = 0) tự động sinh kịch bản Gherkin và mã step definitions.
*   **C — Comparison (Đối chứng):** Kịch bản kiểm thử BDD và step definitions tương ứng viết tay bởi chuyên gia phần mềm (**Expert-written baseline**).
*   **O — Outcome (Đầu ra đo lường):**
    *   *Metric 1 (Ngữ nghĩa):* Độ tương đồng ngữ nghĩa Cosine Similarity ( Sentence-Transformers `all-MiniLM-L6-v2`) $\ge 0.85$ so với expert baseline.
    *   *Metric 2 (Cú pháp):* Tỷ lệ cú pháp tĩnh khả thi (Executable Syntax Rate) $\ge 80\%$ (không xảy ra lỗi parser).

---

## 2. Thiết lập giả thuyết thống kê (H0 & H1)

Để kiểm chứng hiệu năng thực tế của mô hình, nhóm thiết lập các giả thuyết thống kê cho hai biến kết quả đo lường (mức ý nghĩa $\alpha = 0.05$):

### 2.1. Cặp giả thuyết cho RQ1 (Semantic Similarity - Độ tương đồng ngữ nghĩa)
*   **H0 (Giả thuyết không - Null Hypothesis):** Trung bình độ tương đồng ngữ nghĩa Cosine Similarity của các kịch bản do GPT-4o sinh ra so với expert baseline viết tay nhỏ hơn hoặc bằng 0.85.
    $$\text{H0}_1: \mu_{\text{similarity}} \le 0.85 \quad \text{(GPT-4o chưa đạt ngưỡng chất lượng)}$$
*   **H1 (Giả thuyết đối - Alternative Hypothesis):** Trung bình độ tương đồng ngữ nghĩa Cosine Similarity của các kịch bản do GPT-4o sinh ra so với expert baseline viết tay lớn hơn 0.85.
    $$\text{H1}_1: \mu_{\text{similarity}} > 0.85 \quad \text{(GPT-4o đạt ngưỡng chất lượng)}$$
*   **Phép kiểm định đề xuất:** **One-sample Wilcoxon Signed-Rank Test (một đuôi - one-tailed)**.
*   **Rationale (Cơ sở lựa chọn):** Điểm Cosine Similarity là biến liên tục nằm trong khoảng $[0, 1]$, phân phối điểm số trong thực nghiệm thường không tuân theo phân phối chuẩn. Phép kiểm định phi tham số Wilcoxon một mẫu là lựa chọn thích hợp nhất để so sánh trung vị mẫu thực nghiệm với một ngưỡng tham chiếu cố định ($0.85$).

---

### 2.2. Cặp giả thuyết cho RQ2 (Executable Syntax Rate - Tỷ lệ hợp lệ cú pháp tĩnh)
*   **H0 (Giả thuyết không - Null Hypothesis):** Tỷ lệ hợp lệ cú pháp tĩnh (executable rate) của các kịch bản và step definitions do GPT-4o sinh ra nhỏ hơn hoặc bằng 80%.
    $$\text{H0}_2: p_{\text{syntax}} \le 0.80 \quad \text{(GPT-4o chưa đạt ngưỡng cú pháp)}$$
*   **H1 (Giả thuyết đối - Alternative Hypothesis):** Tỷ lệ hợp lệ cú pháp tĩnh (executable rate) của các kịch bản và step definitions do GPT-4o sinh ra lớn hơn 80%.
    $$\text{H1}_2: p_{\text{syntax}} > 0.80 \quad \text{(GPT-4o đạt ngưỡng cú pháp)}$$
*   **Phép kiểm định đề xuất:** **One-sample Binomial Exact Test (một đuôi - one-tailed)**.
*   **Rationale (Cơ sở lựa chọn):** Kết quả phân tích cú pháp của mỗi ca kiểm thử là biến nhị phân độc lập (Thành công/Parser lỗi). Phép kiểm định nhị thức chính xác (Binomial Exact Test) là phù hợp nhất để so sánh tỷ lệ thành công của mẫu với một tỷ lệ xác suất kỳ vọng lý thuyết ($p_0 = 0.80$).

---

## 3. Quy tắc ra quyết định với p-value (Mức ý nghĩa $\alpha = 0.05$)

Sau khi chạy thực nghiệm và áp dụng các phép kiểm định thống kê trên bằng phần mềm/thư viện (ví dụ `scipy.stats` trong Python):
*   **Nếu p-value $< 0.05$:** Thực hiện **bác bỏ giả thuyết không $H_0$** và **chấp nhận giả thuyết đối $H_1$**.
    *   *Ý nghĩa thực tế:* GPT-4o zero-shot đạt được ngưỡng chất lượng đề ra (độ tương đồng Cosine trung vị $> 0.85$ hoặc tỷ lệ cú pháp tĩnh $> 80\%$) một cách có ý nghĩa thống kê (ở mức tin cậy 95%).
*   **Nếu p-value $\ge 0.05$:** **Chưa đủ bằng chứng bác bỏ giả thuyết không $H_0$**.
    *   *Ý nghĩa thực tế:* Kết quả thực nghiệm chưa đủ cơ sở để khẳng định GPT-4o đạt ngưỡng yêu cầu một cách ổn định, sự vượt trội (nếu có) có thể do biến động ngẫu nhiên của tập mẫu.
