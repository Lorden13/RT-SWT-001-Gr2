# Giả thuyết thống kê — H0 và H1

Trong phần nghiên cứu thực nghiệm này, nhóm thiết lập các giả thuyết thống kê cho hai khía cạnh chất lượng (tương đồng ngữ nghĩa và tính khả thi cú pháp) để kiểm chứng hiệu quả thực tế của GPT-4o zero-shot.

---

## 1. Cặp giả thuyết cho RQ1 (Semantic Similarity)

*   **H0 (Giả thuyết không):** Trung bình độ tương đồng ngữ nghĩa Cosine Similarity của các kịch bản do GPT-4o sinh ra so với kịch bản viết tay của chuyên gia nhỏ hơn hoặc bằng 0.85.
    $$\text{H0}_1: \mu_{\text{similarity}} \le 0.85 \quad \text{(GPT-4o chưa đạt ngưỡng kỳ vọng)}$$
*   **H1 (Giả thuyết đối):** Trung bình độ tương đồng ngữ nghĩa Cosine Similarity của các kịch bản do GPT-4o sinh ra so với kịch bản viết tay của chuyên gia lớn hơn 0.85.
    $$\text{H1}_1: \mu_{\text{similarity}} > 0.85 \quad \text{(GPT-4o đạt ngưỡng kỳ vọng)}$$
*   **Phương pháp kiểm định:** Kiểm định Wilcoxon signed-rank test (một đuôi - one-tailed) vì đây là kiểm định phi tham số phù hợp cho so sánh cặp mẫu (paired samples) có phân phối không chuẩn.
*   **Mức ý nghĩa thống kê:** $\alpha = 0.05$

---

## 2. Cặp giả thuyết cho RQ2 (Executable Syntax)

*   **H0 (Giả thuyết không):** Tỷ lệ không lỗi cú pháp tĩnh (executable rate) của các kịch bản và mã step definitions do GPT-4o sinh ra nhỏ hơn hoặc bằng 80%.
    $$\text{H0}_2: \text{executable\_rate} \le 0.80 \quad \text{(GPT-4o chưa đạt ngưỡng kỳ vọng)}$$
*   **H1 (Giả thuyết đối):** Tỷ lệ không lỗi cú pháp tĩnh (executable rate) của các kịch bản và mã step definitions do GPT-4o sinh ra lớn hơn 80%.
    $$\text{H1}_2: \text{executable\_rate} > 0.80 \quad \text{(GPT-4o đạt ngưỡng kỳ vọng)}$$
*   **Phương pháp kiểm định:** Kiểm định nhị thức Binomial test (một đuôi - one-tailed, với tham số tỷ lệ giả định $p_0 = 0.80$) vì biến kết quả là nhị phân (hợp lệ cú pháp / lỗi cú pháp).
*   **Mức ý nghĩa thống kê:** $\alpha = 0.05$

---

## 3. Giải thích ý nghĩa kết quả kiểm định (Trường hợp p-value = 0.03)

Giả sử sau khi thực hiện chạy thực nghiệm trên tập mẫu và áp dụng các kiểm định thống kê trên, phần mềm tính toán ra chỉ số **p-value = 0.03**:

### Nguyên tắc ra quyết định:
*   So sánh p-value với mức ý nghĩa $\alpha = 0.05$.
*   Quy tắc: Nếu $\text{p-value} < \alpha$, ta bác bỏ giả thuyết không H0 và chấp nhận giả thuyết đối H1.

### Kết luận thực tế với p-value = 0.03:
Vì $0.03 < 0.05$ (p-value nhỏ hơn mức ý nghĩa $\alpha$ đã thiết lập), ta thực hiện **bác bỏ giả thuyết không H0** và **chấp nhận giả thuyết đối H1** cho cả hai trường hợp kiểm định:
1.  **Về Semantic Similarity (RQ1):** Ta có đủ bằng chứng thống kê để kết luận rằng độ tương đồng ngữ nghĩa Cosine trung bình của kịch bản Gherkin do GPT-4o sinh ra lớn hơn 0.85 một cách có ý nghĩa thống kê (ở mức tin cậy 95%).
2.  **Về Executable Syntax (RQ2):** Ta có đủ bằng chứng thống kê để kết luận rằng tỷ lệ không lỗi cú pháp tĩnh của các kịch bản và step definitions do GPT-4o sinh ra lớn hơn 80% một cách có ý nghĩa thống kê (ở mức tin cậy 95%).

Điều này chứng minh hiệu quả thực tế của mô hình GPT-4o zero-shot đã vượt qua các ngưỡng chất lượng mong đợi đặt ra bởi giảng viên hướng dẫn.
