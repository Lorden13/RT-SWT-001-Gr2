# Giả Thuyết Thống Kê & Phép Kiểm Định Nhóm — Hypotheses & Statistical Tests (Final)

Tài liệu này xác lập các cặp giả thuyết thống kê (H0/H1) và đề xuất các phép kiểm định thống kê tương ứng phục vụ cho việc phân tích dữ liệu thực nghiệm sau khi chạy mô hình.

---

## 1. Hệ thống các cặp giả thuyết thống kê (H0 & H1)

Để trả lời các câu hỏi nghiên cứu, nhóm thiết lập các giả thuyết thống kê như sau (ở mức ý nghĩa $\alpha = 0.05$):

### 1.1. Nhóm giả thuyết H1: Độ tương đồng ngữ nghĩa (Semantic Similarity)

Nhóm giả thuyết này đánh giá độ khớp nối nghiệp vụ giữa kịch bản BDD do mô hình sinh ra và Ground Truth viết tay từ tập dữ liệu thực nghiệm 100 mẫu.

#### Giả thuyết 1a: Đánh giá chất lượng của mô hình tinh chỉnh (LLaMA-3-8B LoRA-FT)
*   **H0 (Giả thuyết không):** Trung vị độ tương đồng ngữ nghĩa Cosine Similarity của các kịch bản do LLaMA-3-8B LoRA-FT sinh ra so với Ground Truth **nhỏ hơn hoặc bằng 0.85**.
    $$\text{H0}_{1a}: \text{Median}(\text{Similarity}_{\text{LLaMA-FT}}) \le 0.85 \quad \text{(Chất lượng LLaMA-FT chưa đạt kỳ vọng)}$$
*   **H1 (Giả thuyết đối):** Trung vị độ tương đồng ngữ nghĩa Cosine Similarity của các kịch bản do LLaMA-3-8B LoRA-FT sinh ra so với Ground Truth **lớn hơn 0.85**.
    $$\text{H1}_{1a}: \text{Median}(\text{Similarity}_{\text{LLaMA-FT}}) > 0.85 \quad \text{(Chất lượng LLaMA-FT đạt kỳ vọng)}$$
*   **Phép kiểm định đề xuất:** **One-sample Wilcoxon Signed-Rank Test (một đuôi - one-tailed)**.
*   **Rationale:** Điểm Cosine Similarity là biến liên tục nằm trong khoảng $[0, 1]$, phân phối điểm số thực nghiệm thường lệch trái (không chuẩn). Để so sánh giá trị trung vị của mẫu với một ngưỡng cố định ($0.85$) trên 100 mẫu thực nghiệm, phép kiểm định phi tham số Wilcoxon một mẫu là lựa chọn tối ưu nhất.

#### Giả thuyết 1b: So sánh đối chứng LLaMA-3-8B LoRA-FT vs. GPT-4o (Zero-shot)
*   **H0 (Giả thuyết không):** Không có sự khác biệt có ý nghĩa thống kê về điểm tương đồng ngữ nghĩa trung vị giữa LLaMA-3-8B LoRA-FT và GPT-4o.
    $$\text{H0}_{1b}: \text{Median}(\text{Similarity}_{\text{LLaMA-FT}} - \text{Similarity}_{\text{GPT-4o}}) = 0$$
*   **H1 (Giả thuyết đối):** Có sự khác biệt có ý nghĩa thống kê về điểm tương đồng ngữ nghĩa trung vị giữa LLaMA-3-8B LoRA-FT và GPT-4o.
    $$\text{H1}_{1b}: \text{Median}(\text{Similarity}_{\text{LLaMA-FT}} - \text{Similarity}_{\text{GPT-4o}}) \neq 0$$
*   **Phép kiểm định đề xuất:** **Paired Wilcoxon Signed-Rank Test (hai đuôi - two-tailed)**.
*   **Rationale:** Dữ liệu dạng cặp mẫu phụ thuộc (cùng sinh test từ 100 User Stories đầu vào). Phép kiểm định phi tham số cặp Wilcoxon giúp so sánh sự khác biệt về chất lượng ngữ nghĩa giữa mô hình nguồn mở tinh chỉnh chạy local và mô hình đóng thương mại lớn.

---

### 1.2. Nhóm giả thuyết H2: Tỷ lệ cú pháp tĩnh hợp lệ (Executable Syntax Rate)

Nhóm giả thuyết này đánh giá tính khả thi cú pháp của kịch bản Gherkin và step definitions sinh ra (được kiểm định kép bằng Gherkin Parser và Python AST Parser).

#### Giả thuyết 2a: Đánh giá chất lượng của mô hình tinh chỉnh (LLaMA-3-8B LoRA-FT)
*   **H0 (Giả thuyết không):** Tỷ lệ đúng cú pháp tĩnh (Executable Syntax Rate) của các artifacts do LLaMA-3-8B LoRA-FT sinh ra **nhỏ hơn hoặc bằng 85%**.
    $$\text{H0}_{2a}: p_{\text{syntax\_LLaMA}} \le 0.85 \quad \text{(Cú pháp LLaMA-FT chưa đạt kỳ vọng)}$$
*   **H1 (Giả thuyết đối):** Tỷ lệ đúng cú pháp tĩnh (Executable Syntax Rate) của các artifacts do LLaMA-3-8B LoRA-FT sinh ra **lớn hơn 85%**.
    $$\text{H1}_{2a}: p_{\text{syntax\_LLaMA}} > 0.85 \quad \text{(Cú pháp LLaMA-FT đạt kỳ vọng)}$$
*   **Phép kiểm định đề xuất:** **One-sample Binomial Exact Test (một đuôi - one-tailed)**.
*   **Rationale:** Đầu ra kiểm định cú pháp tĩnh của mỗi cặp artifacts là biến nhị phân độc lập (PASS/FAIL). Phép kiểm định nhị thức chính xác (Binomial Exact Test) là phù hợp nhất để so sánh tỷ lệ thành công của mẫu với một tỷ lệ xác suất kỳ vọng lý thuyết ($p_0 = 0.85$).

#### Giả thuyết 2b: Đánh giá mô hình đối chứng GPT-4o (Zero-shot)
*   **H0 (Giả thuyết không):** Tỷ lệ đúng cú pháp tĩnh (Executable Syntax Rate) của các artifacts do GPT-4o sinh ra **nhỏ hơn hoặc bằng 85%**.
    $$\text{H0}_{2b}: p_{\text{syntax\_GPT}} \le 0.85 \quad \text{(Cú pháp GPT-4o chưa đạt kỳ vọng)}$$
*   **H1 (Giả thuyết đối):** Tỷ lệ đúng cú pháp tĩnh (Executable Syntax Rate) của các artifacts do GPT-4o sinh ra **lớn hơn 85%**.
    $$\text{H1}_{2b}: p_{\text{syntax\_GPT}} > 0.85 \quad \text{(Cú pháp GPT-4o đạt kỳ vọng)}$$
*   **Phép kiểm định đề xuất:** **One-sample Binomial Exact Test (một đuôi - one-tailed)**.
*   **Rationale:** Tương tự như trên, dùng Binomial Test để kiểm chứng xem GPT-4o ở cấu hình zero-shot có vượt qua ngưỡng cú pháp tĩnh kỳ vọng 85% hay không.

---

## 2. Bảng tóm tắt các phép kiểm định thống kê lựa chọn

| Mục tiêu nghiên cứu | Loại dữ liệu đầu ra | Ngưỡng so sánh | Phép kiểm định thống kê | Lý do lựa chọn (Rationale) |
|:---|:---|:---|:---|:---|
| **Độ tương đồng ngữ nghĩa (LLaMA-FT)** | Liên tục phi chuẩn (Cosine) | Ngưỡng $\ge 0.85$ | **One-sample Wilcoxon Signed-Rank Test** | So sánh trung vị độ tương đồng của LLaMA-FT với ngưỡng chất lượng 0.85. |
| **Tỷ lệ đúng cú pháp tĩnh (LLaMA-FT)** | Nhị phân (PASS / FAIL) | Ngưỡng $\ge 85\%$ | **One-sample Binomial Exact Test** | So sánh tỷ lệ PASS cú pháp của LLaMA-FT với ngưỡng xác suất lý thuyết 85%. |
| **So sánh độ tương đồng (LLaMA-FT vs. GPT-4o)** | Liên tục phi chuẩn theo cặp | So sánh trực tiếp | **Paired Wilcoxon Signed-Rank Test** | So sánh chất lượng ngữ nghĩa giữa hai nhóm mẫu phụ thuộc sinh ra từ cùng 100 User Stories. |
| **Tỷ lệ đúng cú pháp tĩnh (GPT-4o)** | Nhị phân (PASS / FAIL) | Ngưỡng $\ge 85\%$ | **One-sample Binomial Exact Test** | Kiểm chứng xem mô hình đối chứng GPT-4o có đạt tỷ lệ đúng cú pháp trên 85% hay không. |

---

## 3. Quy tắc ra quyết định và Giải thích ý nghĩa p-value

Tất cả các phép kiểm định thống kê được thực hiện ở mức ý nghĩa (mức độ chấp nhận sai lầm loại I) $\alpha = 0.05$.
*   **Nếu p-value $< 0.05$:** Bác bỏ giả thuyết không $H_0$, chấp nhận giả thuyết đối $H_1$. Kết quả thực nghiệm đạt ý nghĩa thống kê (ở mức tin cậy 95%).
    *   *Ví dụ:* Nếu kiểm định độ tương đồng ngữ nghĩa cho ra p-value $= 0.03 < 0.05$, ta kết luận LLaMA-FT đạt độ tương đồng ngữ nghĩa lớn hơn 0.85 một cách có ý nghĩa thống kê.
*   **Nếu p-value $\ge 0.05$:** Chưa đủ bằng chứng bác bỏ giả thuyết không $H_0$. Sự vượt trội (nếu có) có thể do biến động ngẫu nhiên của tập mẫu và chưa có ý nghĩa thống kê.
