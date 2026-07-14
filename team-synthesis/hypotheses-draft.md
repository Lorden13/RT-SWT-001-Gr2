# Giả Thuyết Thống Kê & Phép Kiểm Định Nhóm — Hypotheses & Statistical Tests (Final)

Tài liệu này xác lập các cặp giả thuyết thống kê (H0/H1) và đề xuất các phép kiểm định thống kê tương ứng phục vụ cho việc phân tích dữ liệu thực nghiệm sau khi chạy mô hình. Nghiên cứu tập trung đánh giá hiệu quả của các kỹ thuật Prompt Engineering (Zero-Shot, Few-Shot, Chain-of-Thought) trên mô hình GPT-4o thông qua OpenAI Responses API.

---

## 1. Hệ thống các cặp giả thuyết thống kê (H0 & H1)

Để trả lời các câu hỏi nghiên cứu, nhóm thiết lập các giả thuyết thống kê như sau (ở mức ý nghĩa $\alpha = 0.05$):

### 1.1. RQ1: Độ tương đồng ngữ nghĩa (Semantic Similarity)
Đánh giá xem điểm tương đồng ngữ nghĩa Cosine Similarity của các kịch bản BDD sinh ra bởi từng kỹ thuật prompting có vượt qua ngưỡng chất lượng kỳ vọng 0.80 hay không. Phép kiểm định được sử dụng là **One-Sample Wilcoxon Signed-Rank Test** (một đuôi), so khớp với ngưỡng 0.80, và báo cáo kích cỡ hiệu ứng bằng **Rank-Biserial Correlation**.

#### Giả thuyết 1a: Đánh giá kỹ thuật Zero-Shot
*   **H0 (Giả thuyết không):** Trung vị độ tương đồng ngữ nghĩa Cosine Similarity của các kịch bản do GPT-4o sinh ra bằng kỹ thuật Zero-Shot **nhỏ hơn hoặc bằng 0.80**.
    $$\text{H0}_{1a}: \text{Median}(\text{Similarity}_{\text{Zero-Shot}}) \le 0.80$$
*   **H1 (Giả thuyết đối):** Trung vị độ tương đồng ngữ nghĩa Cosine Similarity của các kịch bản do GPT-4o sinh ra bằng kỹ thuật Zero-Shot **lớn hơn 0.80**.
    $$\text{H1}_{1a}: \text{Median}(\text{Similarity}_{\text{Zero-Shot}}) > 0.80$$

#### Giả thuyết 1b: Đánh giá kỹ thuật Few-Shot
*   **H0 (Giả thuyết không):** Trung vị độ tương đồng ngữ nghĩa Cosine Similarity của các kịch bản do GPT-4o sinh ra bằng kỹ thuật Few-Shot **nhỏ hơn hoặc bằng 0.80**.
    $$\text{H0}_{1b}: \text{Median}(\text{Similarity}_{\text{Few-Shot}}) \le 0.80$$
*   **H1 (Giả thuyết đối):** Trung vị độ tương đồng ngữ nghĩa Cosine Similarity của các kịch bản do GPT-4o sinh ra bằng kỹ thuật Few-Shot **lớn hơn 0.80**.
    $$\text{H1}_{1b}: \text{Median}(\text{Similarity}_{\text{Few-Shot}}) > 0.80$$

#### Giả thuyết 1c: Đánh giá kỹ thuật Chain-of-Thought (CoT)
*   **H0 (Giả thuyết không):** Trung vị độ tương đồng ngữ nghĩa Cosine Similarity của các kịch bản do GPT-4o sinh ra bằng kỹ thuật Chain-of-Thought **nhỏ hơn hoặc bằng 0.80**.
    $$\text{H0}_{1c}: \text{Median}(\text{Similarity}_{\text{CoT}}) \le 0.80$$
*   **H1 (Giả thuyết đối):** Trung vị độ tương đồng ngữ nghĩa Cosine Similarity của các kịch bản do GPT-4o sinh ra bằng kỹ thuật Chain-of-Thought **lớn hơn 0.80**.
    $$\text{H1}_{1c}: \text{Median}(\text{Similarity}_{\text{CoT}}) > 0.80$$

---

### 1.2. RQ2: Tỷ lệ cú pháp tĩnh khả thi (Executable Syntax Rate)
Đánh giá xem tỷ lệ đúng cú pháp tĩnh của các kịch bản và mã code sinh ra có vượt qua ngưỡng chấp nhận tối thiểu 85% hay không (kiểm định kép bằng Gherkin Parser và Python AST). Phép kiểm định được sử dụng là **One-Sample Binomial Exact Test** (một đuôi) so với ngưỡng 85%.

#### Giả thuyết 2a: Đánh giá kỹ thuật Zero-Shot
*   **H0 (Giả thuyết không):** Tỷ lệ đúng cú pháp tĩnh (Executable Syntax Rate) của kỹ thuật Zero-Shot **nhỏ hơn hoặc bằng 85%**.
    $$\text{H0}_{2a}: p_{\text{syntax\_Zero-Shot}} \le 0.85$$
*   **H1 (Giả thuyết đối):** Tỷ lệ đúng cú pháp tĩnh (Executable Syntax Rate) của kỹ thuật Zero-Shot **lớn hơn 85%**.
    $$\text{H1}_{2a}: p_{\text{syntax\_Zero-Shot}} > 0.85$$

#### Giả thuyết 2b: Đánh giá kỹ thuật Few-Shot
*   **H0 (Giả thuyết không):** Tỷ lệ đúng cú pháp tĩnh (Executable Syntax Rate) của kỹ thuật Few-Shot **nhỏ hơn hoặc bằng 85%**.
    $$\text{H0}_{2b}: p_{\text{syntax\_Few-Shot}} \le 0.85$$
*   **H1 (Giả thuyết đối):** Tỷ lệ đúng cú pháp tĩnh (Executable Syntax Rate) của kỹ thuật Few-Shot **lớn hơn 85%**.
    $$\text{H1}_{2b}: p_{\text{syntax\_Few-Shot}} > 0.85$$

#### Giả thuyết 2c: Đánh giá kỹ thuật Chain-of-Thought (CoT)
*   **H0 (Giả thuyết không):** Tỷ lệ đúng cú pháp tĩnh (Executable Syntax Rate) của kỹ thuật Chain-of-Thought **nhỏ hơn hoặc bằng 85%**.
    $$\text{H0}_{2c}: p_{\text{syntax\_CoT}} \le 0.85$$
*   **H1 (Giả thuyết đối):** Tỷ lệ đúng cú pháp tĩnh (Executable Syntax Rate) của kỹ thuật Chain-of-Thought **lớn hơn 85%**.
    $$\text{H1}_{2c}: p_{\text{syntax\_CoT}} > 0.85$$

---

### 1.3. RQ3: Đánh giá đối chứng các kỹ thuật Prompting (Comparative Evaluation)
So sánh đối chứng chéo giữa ba kỹ thuật Prompt Engineering (Zero-Shot, Few-Shot, Chain-of-Thought) để tìm ra kỹ thuật hiệu quả nhất.

#### A. So sánh đối chứng về Độ tương đồng ngữ nghĩa (Semantic Similarity)
Sử dụng **Paired Wilcoxon Signed-Rank Test** (hai đuôi) để so sánh từng cặp mô hình độc lập phụ thuộc trên 100 mẫu, đồng thời đo lường kích cỡ hiệu ứng (Effect Size) bằng chỉ số **Rank-Biserial Correlation**.

*   **Cặp so sánh 1: Zero-Shot vs. Few-Shot**
    *   **H0 (Giả thuyết không):** Không có sự khác biệt có ý nghĩa thống kê về điểm trung vị độ tương đồng giữa Few-Shot và Zero-Shot.
        $$\text{H0}_{3a}: \text{Median}(\text{Similarity}_{\text{Few-Shot}} - \text{Similarity}_{\text{Zero-Shot}}) = 0$$
    *   **H1 (Giả thuyết đối):** Có sự khác biệt có ý nghĩa thống kê về điểm trung vị độ tương đồng giữa Few-Shot và Zero-Shot.
        $$\text{H1}_{3a}: \text{Median}(\text{Similarity}_{\text{Few-Shot}} - \text{Similarity}_{\text{Zero-Shot}}) \neq 0$$

*   **Cặp so sánh 2: Few-Shot vs. Chain-of-Thought**
    *   **H0 (Giả thuyết không):** Không có sự khác biệt có ý nghĩa thống kê về điểm trung vị độ tương đồng giữa Chain-of-Thought và Few-Shot.
        $$\text{H0}_{3b}: \text{Median}(\text{Similarity}_{\text{CoT}} - \text{Similarity}_{\text{Few-Shot}}) = 0$$
    *   **H1 (Giả thuyết đối):** Có sự khác biệt có ý nghĩa thống kê về điểm trung vị độ tương đồng giữa Chain-of-Thought và Few-Shot.
        $$\text{H1}_{3b}: \text{Median}(\text{Similarity}_{\text{CoT}} - \text{Similarity}_{\text{Few-Shot}}) \neq 0$$

*   **Cặp so sánh 3: Zero-Shot vs. Chain-of-Thought**
    *   **H0 (Giả thuyết không):** Không có sự khác biệt có ý nghĩa thống kê về điểm trung vị độ tương đồng giữa Chain-of-Thought và Zero-Shot.
        $$\text{H0}_{3c}: \text{Median}(\text{Similarity}_{\text{CoT}} - \text{Similarity}_{\text{Zero-Shot}}) = 0$$
    *   **H1 (Giả thuyết đối):** Có sự khác biệt có ý nghĩa thống kê về điểm trung vị độ tương đồng giữa Chain-of-Thought và Zero-Shot.
        $$\text{H1}_{3c}: \text{Median}(\text{Similarity}_{\text{CoT}} - \text{Similarity}_{\text{Zero-Shot}}) \neq 0$$

#### B. So sánh đối chứng về Tỷ lệ cú pháp tĩnh hợp lệ (Executable Syntax Rate)
Sử dụng phép kiểm **McNemar Test** để so sánh chéo tỷ lệ PASS cú pháp tĩnh giữa các cặp kỹ thuật trên cùng tập dữ liệu mẫu phụ thuộc.

*   **Cặp so sánh 1: Zero-Shot vs. Few-Shot**
    *   **H0 (Giả thuyết không):** Không có sự khác biệt có ý nghĩa thống kê về tỷ lệ đúng cú pháp tĩnh giữa Zero-Shot và Few-Shot.
    *   **H1 (Giả thuyết đối):** Có sự khác biệt có ý nghĩa thống kê về tỷ lệ đúng cú pháp tĩnh giữa Zero-Shot và Few-Shot.
*   **Cặp so sánh 2: Few-Shot vs. Chain-of-Thought**
    *   **H0 (Giả thuyết không):** Không có sự khác biệt có ý nghĩa thống kê về tỷ lệ đúng cú pháp tĩnh giữa Few-Shot và Chain-of-Thought.
    *   **H1 (Giả thuyết đối):** Có sự khác biệt có ý nghĩa thống kê về tỷ lệ đúng cú pháp tĩnh giữa Few-Shot và Chain-of-Thought.
*   **Cặp so sánh 3: Zero-Shot vs. Chain-of-Thought**
    *   **H0 (Giả thuyết không):** Không có sự khác biệt có ý nghĩa thống kê về tỷ lệ đúng cú pháp tĩnh giữa Zero-Shot và Chain-of-Thought.
    *   **H1 (Giả thuyết đối):** Có sự khác biệt có ý nghĩa thống kê về tỷ lệ đúng cú pháp tĩnh giữa Zero-Shot và Chain-of-Thought.

---

## 2. Bảng tóm tắt các phép kiểm định thống kê lựa chọn

| Mục tiêu nghiên cứu | Loại dữ liệu đầu ra | Ngưỡng so sánh | Phép kiểm định thống kê | Chỉ số Kích cỡ hiệu ứng (Effect Size) | Lý do lựa chọn (Rationale) |
|:---|:---|:---|:---|:---|:---|
| **Semantic Similarity (RQ1)** | Liên tục phi chuẩn (Cosine) | Ngưỡng $\ge 0.80$ | **One-sample Wilcoxon Signed-Rank Test** | Rank-Biserial Correlation | So sánh giá trị trung vị của từng kỹ thuật prompt so với ngưỡng chất lượng kỳ vọng 0.80. |
| **Executable Syntax Rate (RQ2)** | Nhị phân (PASS / FAIL) | Ngưỡng $\ge 85\%$ | **One-sample Binomial Exact Test** | N/A | So sánh tỷ lệ cú pháp tĩnh PASS của từng kỹ thuật prompt so với ngưỡng xác suất kỳ vọng 85%. |
| **So sánh ngữ nghĩa (RQ3 - Semantic)** | Liên tục phi chuẩn theo cặp | So sánh chéo | **Paired Wilcoxon Signed-Rank Test** | Rank-Biserial Correlation | So sánh sự khác biệt điểm tương đồng ngữ nghĩa trung vị giữa các cặp kỹ thuật prompt phụ thuộc. |
| **So sánh cú pháp (RQ3 - Syntax)** | Nhị phân theo cặp (PASS / FAIL) | So sánh chéo | **McNemar Test** | N/A | So sánh sự khác biệt về tỷ lệ cú pháp tĩnh hợp lệ giữa các cặp kỹ thuật prompt phụ thuộc. |

---

## 3. Quy tắc ra quyết định và Giải thích ý nghĩa p-value

Tất cả các phép kiểm định thống kê được thực hiện ở mức ý nghĩa (mức độ chấp nhận sai lầm loại I) $\alpha = 0.05$.
*   **Nếu p-value $< 0.05$:** Bác bỏ giả thuyết không $H_0$, chấp nhận giả thuyết đối $H_1$. Kết quả thực nghiệm đạt ý nghĩa thống kê (ở mức tin cậy 95%). Kích cỡ hiệu ứng (Rank-Biserial Correlation) sẽ được sử dụng để đánh giá mức độ ảnh hưởng thực tế (lớn, trung bình hay nhỏ).
*   **Nếu p-value $\ge 0.05$:** Chưa đủ bằng chứng bác bỏ giả thuyết không $H_0$. Sự vượt trội (nếu có) có thể do biến động ngẫu nhiên của tập mẫu và chưa có ý nghĩa thống kê.
