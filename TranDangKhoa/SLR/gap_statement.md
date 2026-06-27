# GAP Statement — Xác nhận khoảng trống nghiên cứu từ Evidence Table

Evidence table: N = 1 papers

## Các khoảng trống phát hiện

### GAP-T (Technology): Thiếu đánh giá trên các mô hình ngôn ngữ lớn khác và phương pháp Single-agent / Zero-shot
**Bằng chứng:** Trong bảng bằng chứng chỉ có duy nhất nghiên cứu **Bergsmann 2024** sử dụng hệ thống phức tạp Multi-agent chạy trên GPT-4 để sinh mã kiểm thử. Lĩnh vực hoàn toàn thiếu vắng các đánh giá thực nghiệm cho thấy hiệu quả của phương pháp tiếp cận zero-shot trên các mô hình ngôn ngữ lớn tiên tiến đơn lẻ (như GPT-4o zero-shot).

### GAP-M (Metric): Thiếu các đánh giá độ tương đồng ngữ nghĩa đối chiếu với baseline viết tay của chuyên gia
**Bằng chứng:** Nghiên cứu duy nhất **Bergsmann 2024** chỉ đo lường tỷ lệ thực thi mã step definition động và độ bao phủ kiểm thử. Chưa có đánh giá nào đo lường độ tương đồng ngữ nghĩa bằng Cosine Similarity thông qua mô hình Sentence-Transformers đối chiếu trực tiếp với bộ kiểm thử baseline viết tay bởi các chuyên gia (expert-written) làm chuẩn.

### GAP-D (Dataset): Hạn chế về quy mô và tính đa dạng miền của dữ liệu thực nghiệm
**Bằng chứng:** Thử nghiệm của **Bergsmann 2024** chỉ được thực hiện trên một bộ dữ liệu rất nhỏ gồm 12 kịch bản kiểm thử Gherkin. Quy mô này là quá nhỏ để khẳng định tính tổng quát của công nghệ và thiếu hẳn các thử nghiệm trên bộ dữ liệu thực tế lớn hơn (ví dụ: 50 User Stories định dạng Connextra).

---

## Phát biểu GAP tổng hợp

Chưa có nghiên cứu thực nghiệm nào sử dụng kết quả tìm kiếm từ ACM đánh giá khả năng sinh zero-shot đồng thời cả kịch bản Gherkin và mã step definitions từ User stories định dạng Connextra của mô hình GPT-4o thế hệ mới sử dụng chỉ số đo lường kép: độ tương đồng ngữ nghĩa Cosine Similarity (Sentence-Transformers so với expert baseline) và tính đúng đắn cú pháp tĩnh (executable syntax rate).
