# Gap Statement — Automated Test Generation from BDD/Gherkin using LLMs

Evidence table: N = 5 papers

---

## Các khoảng trống phát hiện

### GAP-T (Technology)
Các nghiên cứu hiện tại chủ yếu sử dụng các dòng LLM đời cũ hoặc chung chung (như ChatGPT-3.5, GPT-4 đời đầu, Gemini, Grok, Llama) hoặc các công cụ dựa trên luật (rule-based). Chưa có nghiên cứu nào đánh giá chất lượng sinh kịch bản Gherkin của mô hình biên thế hệ mới nhất như **GPT-4o** ở chế độ zero-shot/few-shot với cấu hình nhiệt độ tối ưu (`temperature = 0`).
- **Bằng chứng:** Cột *Tool/LLM* của cả 5 bài báo (Mendoza 2026, Tiwari 2026, Santos 2026, Fernandes 2026, Patel 2026) đều không có nghiên cứu nào sử dụng hay đánh giá mô hình GPT-4o.

### GAP-M (Metric)
Các nghiên cứu hiện tại đánh giá chất lượng kịch bản dựa trên độ phủ (coverage), thời gian sinh (efficiency), độ nhất quán, hoặc độ tương đồng cấu trúc đơn giản. Chưa có bài báo nào đo lường độ tương đồng ngữ nghĩa dựa trên nhúng (**embedding-based semantic similarity**) của kịch bản Gherkin được sinh ra so với kịch bản chuẩn viết bởi chuyên gia (expert-written) với một ngưỡng cụ thể (như 0.85). Đồng thời, chưa có nghiên cứu nào đo lường tỷ lệ cú pháp thực thi được (**executable syntax rate**) của kịch bản Gherkin được sinh ra thông qua các bộ phân tích cú pháp tự động (Gherkin parser) với ngưỡng mong đợi $\ge 80\%$.
- **Bằng chứng:** Cột *Metric* của cả 5 bài báo đều không đo lường độ tương đồng ngữ nghĩa cosine (dùng Sentence-BERT) hoặc tỷ lệ cú pháp thực thi được (executable rate) của kịch bản Gherkin.

### GAP-D (Dataset)
Các nghiên cứu thường sử dụng tập dữ liệu độc quyền hoặc không chia sẻ công khai (như Tiwari 2026 dùng dữ liệu nội bộ của dự án, Patel 2026 dùng mã nguồn hiện hữu), hoặc chỉ sử dụng các prompts chuẩn hóa đơn giản mà không áp dụng cho các user stories chuẩn nghiệp vụ phần mềm (như định dạng Connextra) từ nhiều dự án thực tế.
- **Bằng chứng:** Cột *Dataset* của các bài báo chỉ ra sự thiếu hụt các tập dữ liệu user stories định dạng chuẩn nghiệp vụ như Connextra từ $\ge 3$ dự án SE thực tế để làm giàu tính tổng quát của nghiên cứu.

---

## Phát biểu GAP tổng hợp
Chưa có đánh giá toàn diện về khả năng của frontier LLM (GPT-4o) trong việc tự động sinh kịch bản Gherkin từ user stories định dạng Connextra sử dụng các độ đo chính là độ tương đồng ngữ nghĩa (embedding-based semantic similarity) và tỷ lệ cú pháp thực thi được (executable rate) đạt ngưỡng kỳ vọng.
