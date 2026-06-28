# Cơ Sở Thiết Kế Thực Nghiệm — Design Rationale (Trịnh Phú Quốc)

Tài liệu này trình bày bảng quyết định thiết kế thực nghiệm và giải thích nguồn gốc của các ngưỡng chất lượng (thresholds) được sử dụng để đánh giá hiệu năng của mô hình.

---

## 1. Bảng quyết định thiết kế thực nghiệm

Mọi quyết định thiết kế cho thực nghiệm này đều được đối chiếu trực tiếp với các phát hiện và thực tế triển khai từ các nghiên cứu khoa học đi trước trong bảng bằng chứng (Evidence Table):

| Quyết định thiết kế | Giá trị lựa chọn | Nguồn tham chiếu / Lý do lựa chọn |
|:---|:---|:---|
| **LLM / Tool (Mô hình)** | **GPT-4o** (phiên bản `gpt-4o-2024-05-13`) | *Nguồn:* Poth 2025 (Bài 3) và Fernandes 2025 (Bài 2).<br/>*Lý do:* GPT-4o là mô hình đóng thế hệ mới nhất có khả năng sinh cú pháp và hiểu ngôn ngữ xuất sắc nhưng chưa được đánh giá zero-shot đồng thời Gherkin + step code. |
| **Dataset (Dữ liệu)** | **50 User Stories** định dạng Connextra thuộc đa miền nghiệp vụ khác nhau. | *Nguồn:* Fernandes 2025 (Bài 2) dùng 50 User Stories.<br/>*Lý do:* Khắc phục hạn chế của các tập dữ liệu nhỏ lẻ (như Bài 8 chỉ dùng 12 kịch bản, Bài 7 dùng 20 fintech stories). |
| **Metric 1 (Ngữ nghĩa)** | **Cosine Semantic Similarity** sử dụng mô hình nhúng `all-MiniLM-L6-v2`. | *Nguồn:* Fernandes 2025 (Bài 2) đo tương đồng ngữ nghĩa.<br/>*Lý do:* `all-MiniLM-L6-v2` là mô hình SBERT chuẩn công nghiệp cho độ tương quan cao với đánh giá của con người. |
| **Metric 2 (Cú pháp)** | **Executable Syntax Rate** (tỷ lệ cú pháp Gherkin và Python không có lỗi parse tĩnh). | *Nguồn:* dos Santos 2025 (Bài 4) và Matveeva 2025 (Bài 6).<br/>*Lý do:* Đảm bảo các ca kiểm thử sinh ra hợp lệ cú pháp tĩnh trước khi chuyển giao vào môi trường kiểm thử CI/CD. |
| **Baseline (Đối chứng)** | **Expert-written BDD tests** (Kịch bản kiểm thử viết tay bởi chuyên gia phần mềm). | *Nguồn:* Fernandes 2025 (Bài 2) và Matveeva 2025 (Bài 6) dùng expert baseline.<br/>*Lý do:* Kiểm chứng xem chất lượng sinh tự động của LLM đã tiệm cận năng lực của lập trình viên kiểm thử chuyên nghiệp hay chưa. |
| **Threshold (Ngưỡng)** | - Độ tương đồng ngữ nghĩa Cosine $\ge 0.85$.<br/>- Tỷ lệ đúng cú pháp tĩnh $\ge 80\%$. | Xem chi tiết giải thích nguồn gốc các ngưỡng bên dưới. |
| **Pipeline (Quy trình)** | **Zero-shot prompting** với $temperature = 0$. | *Nguồn:* Mendoza 2024 (Bài 1) và Fernandes 2025 (Bài 2).<br/>*Lý do:* Thiết lập $temperature = 0$ đảm bảo tính tái lập (reproducibility) của các kết quả thực nghiệm. Zero-shot kiểm chứng năng lực nội tại của GPT-4o. |

---

## 2. Giải thích nguồn gốc của các Thresholds

Nhóm tuân thủ nghiêm ngặt quy tắc xác lập ngưỡng của Lab, không tự đặt các con số một cách tùy tiện mà trích xuất dựa trên kết quả tối ưu từ các bài báo khoa học trong Evidence Table:

### 2.1. Ngưỡng tương đồng ngữ nghĩa Cosine $\ge 0.85$ (Case 2)
*   **Phân loại:** **Case 2** (Các paper đi trước cung cấp kết quả thực nghiệm số cụ thể nhưng chưa đề xuất một ngưỡng đánh giá cố định nào).
*   **Nguồn tham chiếu:** 
    *   *Fernandes 2025 SBES (Bài 2):* Đạt độ tương đồng ngữ nghĩa trung bình là **0.88** (đo bằng BERTScore).
    *   *Rathnayake 2026 arXiv (Bài 5):* Đạt độ tương đồng trung bình là **0.86** (đo bằng ROUGE-L).
    *   *Matveeva 2025 IEEE (Bài 6):* GPT-4 đạt độ chính xác ngữ nghĩa trung bình **85% (0.85)**.
*   **Lý do chọn:** Dựa trên kết quả thực tế từ 3 công trình trên, mức độ tương đồng ngữ nghĩa từ 0.85 trở lên là mức sàn sàn (floor value) đạt được của các mô hình dòng GPT-4. Việc chọn ngưỡng 0.85 là khả thi và có tính đối chứng khoa học mạnh mẽ.

### 2.2. Ngưỡng hợp lệ cú pháp tĩnh Executable Syntax Rate $\ge 80\%$ (Case 2)
*   **Phân loại:** **Case 2** (Các paper đi trước cung cấp kết quả thực nghiệm số cụ thể nhưng chưa đề xuất một ngưỡng đánh giá cố định nào).
*   **Nguồn tham chiếu:**
    *   *Poth 2025 Springer (Bài 3):* Đạt tỷ lệ chạy code test Cypress/Playwright thành công trung bình là **78%**.
    *   *Bergsmann 2024 ACM (Bài 8):* Đạt tỷ lệ thực thi mã step code thành công trung bình là **83%**.
    *   *Mendoza 2024 SBES (Bài 1):* GPT-4 few-shot đạt tỷ lệ chạy thành công **94%**, nhưng Llama 2 chỉ đạt **68%** độ chính xác cú pháp.
*   **Lý do chọn:** Do chúng ta sinh tĩnh đồng thời cả kịch bản Gherkin và step definitions mà không qua cơ chế tự sửa lỗi (self-repair) động, tỷ lệ thành công thường thấp hơn các pipeline agentic. Mức 80% được lựa chọn làm ngưỡng tối thiểu hợp lý, nằm giữa kết quả của Poth 2025 (78%) và Bergsmann 2024 (83%).
