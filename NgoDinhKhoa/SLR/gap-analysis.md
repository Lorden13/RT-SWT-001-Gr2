# GAP Analysis

## Bảng GAP

| Cột | Phát hiện | Loại GAP | Phản chứng |
| --- | --------- | -------- | ---------- |
| Tool/LLM | Chưa có nghiên cứu nào đánh giá chất lượng sinh kịch bản Gherkin của mô hình frontier thế hệ mới nhất như **GPT-4o** ở chế độ zero-shot với `temperature = 0`. | **GAP-T** (Primary) | Không tìm thấy nghiên cứu nào sử dụng GPT-4o cho mục đích này. (Xem chi tiết bảng phản chứng bên dưới). |
| Metric | Chưa có nghiên cứu nào đánh giá kịch bản Gherkin dựa trên chỉ số kết hợp ngữ nghĩa (SBERT cosine similarity >= 0.85) và cú pháp thực thi được (Gherkin parser execution rate >= 80%). | **GAP-M** (Secondary) | Không tìm thấy nghiên cứu nào kết hợp hai độ đo này với ngưỡng cụ thể như trên. (Xem chi tiết bảng phản chứng bên dưới). |
| Dataset | Hầu hết các nghiên cứu sử dụng tập dữ liệu đóng, quy mô nhỏ, hoặc prompts đơn giản không mang tính chuẩn hóa nghiệp vụ phần mềm (như định dạng Connextra). | **GAP-D** | Các nghiên cứu có sử dụng tập dữ liệu nhưng chưa chuẩn hóa thành các User Stories chuẩn nghiệp vụ phần mềm quy mô lớn từ nhiều dự án thực tế. |
| Shared Limitation | Phụ thuộc nặng nề vào chất lượng viết prompt ban đầu (prompt engineering) và độ phức tạp cao của các yêu cầu làm giảm chất lượng đầu ra. | **GAP-S** | Hầu hết các nghiên cứu đều tự thừa nhận hạn chế này ở phần Threats to Validity. |

---

## GAP Chính (GAP-T)

Nghiên cứu đánh giá hiệu năng của frontier LLM thế hệ mới (**GPT-4o**) trong việc tự động sinh kịch bản Gherkin ở cấu hình tối ưu (`temperature = 0`, zero-shot prompt) từ User Stories định dạng chuẩn nghiệp vụ Connextra.

### Kiểm tra phản chứng cho GAP Chính

GAP tuyên bố: Chưa có nghiên cứu nào đánh giá chất lượng sinh kịch bản Gherkin của mô hình **GPT-4o** ở chế độ zero-shot với cấu hình nhiệt độ tối ưu (`temperature = 0`).

| Paper | Đã làm chưa? | Ghi chú |
|-------|--------------|---------|
| Mendoza 2026 | Không | Đánh giá ChatGPT-4 (phiên bản cũ) và Gemini cho việc sinh dữ liệu kiểm thử (test data) BDD. |
| Tiwari 2026 | Không | Sử dụng Generative AI/LLMs nói chung để sinh kịch bản và step definitions trong vòng đời BDD, không đánh giá GPT-4o. |
| Santos 2026 | Không | So sánh ChatGPT (GPT-3.5/GPT-4 đời đầu), Gemini, Grok, GitHub Copilot về độ phủ kiểm thử. |
| Fernandes 2026 | Không | Đánh giá độ nhất quán của cú pháp Gherkin với các dòng mô hình cũ (GPT-4 đời đầu, Llama). |
| Patel 2026 | Không | Sử dụng API GPT cũ kết hợp Cucumber để reverse-engineer legacy requirements. |

---

## GAP Secondary (GAP-M)

Đo lường chất lượng kịch bản Gherkin được sinh ra thông qua bộ chỉ số kép: độ tương đồng ngữ nghĩa dựa trên nhúng câu (**embedding-based semantic similarity** sử dụng Sentence-BERT với ngưỡng cosine similarity >= 0.85) và tỷ lệ cú pháp thực thi được (**executable syntax rate** sử dụng gherkin-parser với ngưỡng >= 80%).

### Kiểm tra phản chứng cho GAP Secondary

GAP tuyên bố: Chưa có nghiên cứu nào kết hợp đánh giá kịch bản Gherkin qua độ tương đồng ngữ nghĩa (Sentence-BERT cosine similarity >= 0.85) và tỷ lệ cú pháp thực thi được (Gherkin parser execution rate >= 80%).

| Paper | Đã làm chưa? | Ghi chú |
|-------|--------------|---------|
| Mendoza 2026 | Không | Đánh giá cấu trúc và độ đại diện dựa trên thang điểm Likert 0-4 bằng khảo sát người dùng. |
| Tiwari 2026 | Không | Đo lường tỷ lệ giảm thời gian viết test và cải thiện độ phủ kiểm thử (test coverage). |
| Santos 2026 | Không | Đo độ phủ kiểm thử trung bình (test coverage mean) và thời gian sinh của các mô hình. |
| Fernandes 2026 | Không | Đánh giá độ nhất quán của cú pháp Gherkin bằng kiểm định thống kê ANOVA và Kruskal-Wallis. |
| Patel 2026 | Không | Đo tỷ lệ tự động hóa ngược (automation rate) và chi phí tác soạn (authoring cost). |

---

## Feasibility Check

| Tiêu chí | Mức | Ghi chú |
| -------- | --- | ------- |
| Dataset | ⚠️ Trung bình | Cần chuẩn bị 50 Connextra user stories có kèm kịch bản chuẩn viết bởi chuyên gia (expert-written Gherkin scenarios) để làm Ground Truth. |
| Tool/API | ⚠️ Trung bình | Yêu cầu tài khoản OpenAI và kinh phí gọi API GPT-4o (có thể tối ưu hóa bằng cách gọi batch hoặc dùng các gói hỗ trợ học tập). |
| Compute | ✅ Cao | Tính toán SBERT cosine similarity và parse Gherkin có thể thực hiện trên máy tính cá nhân trong vài giây (sử dụng CPU với mô hình all-MiniLM-L6-v2). |
| Ground Truth | ✅ Cao | Có sẵn từ các tài liệu đặc tả của các dự án phần mềm mã nguồn mở hoặc benchmark kiểm thử có sẵn. |
| Skills | ✅ Cao | Nhóm đã có sẵn kỹ năng lập trình Python, xử lý API OpenAI, và tích hợp các thư viện NLP cơ bản. |
| Thời gian | ✅ Cao | Toàn bộ pipeline thu thập dữ liệu, gọi API, và chạy đánh giá có thể được thiết lập và hoàn tất trong vòng 5-6 giờ. |
| Contribution | ✅ Cao | Cung cấp một phương pháp đánh giá định lượng tự động, khách quan (semantic + syntax) cho các kịch bản kiểm thử sinh bởi LLM thế hệ mới. |

**Quyết định**: Số lượng mức Cảnh báo (⚠️) là 2 và không có mức Không khả thi (❌). Đề xuất này nằm trong vùng an toàn và khả thi cao để thực hiện.
