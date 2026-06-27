# Phát Biểu Khoảng Trống Nghiên Cứu Nhóm — Gap Statement (Final)

**Bảng bằng chứng tổng hợp (Evidence Table):** N = 37 bài báo khoa học.

Sau khi tổng hợp và đối chiếu bảng bằng chứng từ 5 thành viên, nhóm xác định 3 khoảng trống nghiên cứu chính (GAP-T, GAP-M, GAP-D) và đưa ra phát biểu khoảng trống tổng hợp làm cơ sở thiết kế thực nghiệm.

---

## 1. Các khoảng trống nghiên cứu phát hiện

### GAP-T (Technology - Công nghệ): Sự phụ thuộc vào các API đóng thương mại và thiếu nghiên cứu tinh chỉnh (fine-tuning) các mô hình mã nguồn mở quy mô nhỏ trên dữ liệu BDD thực tế
*   **Bằng chứng thực tế từ Evidence Table:** 
    *   Hầu hết các nghiên cứu đạt hiệu năng cao trong việc sinh kịch bản và mã kiểm thử chấp nhận BDD/Gherkin đều phụ thuộc hoàn toàn vào các mô hình thương mại đóng đắt đỏ như **GPT-4, GPT-4o, Claude 3.5 Sonnet** (Xem Bài 17, 19, 20, 22, 23, 26, 29).
    *   Các mô hình mã nguồn mở chưa qua tinh chỉnh (như LLaMA-3-8B ở Bài 21 hay LLaMA-3-70B ở Bài 18, 23) chỉ đạt tỷ lệ biên dịch/chạy thành công rất thấp (khoảng từ **61.5% đến 78%**), chưa thể đưa vào vận hành tự động.
    *   Chỉ có duy nhất Bài 27 (Selfbehave) thực hiện tinh chỉnh (fine-tuning) mô hình mã nguồn mở LLaMA-3-8B, nhưng lại thực hiện trên tập dữ liệu kịch bản Gherkin tự sinh (synthetic) bằng phương pháp Self-Instruct chứ chưa kiểm chứng trên các yêu cầu (User Stories) đa miền thực tế của doanh nghiệp.
*   **Ý nghĩa:** Có một khoảng trống công nghệ lớn về việc xây dựng và đánh giá hiệu năng của quy trình tinh chỉnh (fine-tuning qua LoRA) mô hình mã nguồn mở cỡ nhỏ (8B parameters) trên dữ liệu BDD thực tế để đạt hiệu năng tương đương GPT-4o, nhằm bảo mật dữ liệu yêu cầu của doanh nghiệp và giảm chi phí vận hành.

### GAP-M (Metric - Độ đo): Thiếu sự đánh giá đồng thời, song song giữa tính đúng đắn ngữ nghĩa (Semantic Alignment) và tính hợp lệ cú pháp tĩnh (Executable Syntax Rate) của mã kiểm thử sinh ra
*   **Bằng chứng thực tế từ Evidence Table:** 
    *   Các nghiên cứu hiện tại bị chia rẽ sâu sắc về khía cạnh đo lường chất lượng.
    *   Nhóm nghiên cứu về ngôn ngữ (như Bài 19, 24, 27, 32) chỉ đo chất lượng đặc tả ở mức văn bản bằng BLEU, BERTScore hoặc Cosine Similarity, đạt điểm số rất cao nhưng không kiểm tra xem mã kiểm thử (step definitions) có biên dịch và chạy được hay không.
    *   Ngược lại, nhóm nghiên cứu thực hành (như Bài 17, 21, 26, 29, 31) chỉ đo tỷ lệ chạy thành công của mã kiểm thử (execution pass rate) trên Selenium, Playwright, Cypress hay Appium mà hoàn toàn bỏ qua việc đánh giá xem mã nguồn sinh ra có khớp chính xác với nghiệp vụ ban đầu mô tả trong User Story hay không.
*   **Ý nghĩa:** Chưa có nghiên cứu nào thiết lập một bộ độ đo kép tích hợp để đánh giá đồng thời cả **Độ tương đồng ngữ nghĩa (Cosine Similarity dựa trên nhúng của Sentence-Transformers)** và **Tỷ lệ đúng cú pháp tĩnh (Executable Syntax Rate bằng bộ parser)** nhằm đảm bảo ca kiểm thử sinh ra vừa đúng yêu cầu vừa chạy được ngay.

### GAP-D (Dataset - Dữ liệu): Sự khan hiếm của các bộ dữ liệu chuẩn (Benchmark Datasets) đa miền chứa đầy đủ chuỗi vết từ Yêu cầu -> Kịch bản -> Mã kiểm thử thực thi
*   **Bằng chứng thực tế từ Evidence Table:** 
    *   Ngoại trừ Bài 27 tạo ra bộ dataset 5,000 kịch bản Gherkin tự sinh nhưng không đi kèm mã test code thực thi, các nghiên cứu còn lại đều sử dụng bộ dữ liệu đóng, quy mô nhỏ và đơn miền (Bài 17 dùng 15 web app PoC, Bài 20 dùng 35 user stories ngân hàng đóng, Bài 22 dùng 18 tài liệu logistics nội bộ, Bài 11 dùng 10-20 fintech stories).
*   **Ý nghĩa:** Thiếu hụt một bộ dữ liệu benchmark mã nguồn mở chất lượng cao, bao phủ nhiều miền nghiệp vụ (multi-domain), tích hợp đầy đủ chuỗi từ User Story định dạng Connextra -> kịch bản Gherkin -> mã kiểm thử (step definitions) để cộng đồng khoa học có thể so sánh chéo hiệu năng giữa các mô hình LLM một cách khách quan.

---

## 2. Phát biểu khoảng trống nghiên cứu tổng hợp (GAP tổng hợp)

> [!IMPORTANT]
> **GAP Tổng Hợp:** Các nghiên cứu hiện nay về tự động hóa sinh ca kiểm thử chấp nhận (BDD/Gherkin) bị phụ thuộc nặng nề vào các mô hình thương mại đóng (GPT-4, Claude 3.5) để đạt tỷ lệ thực thi tốt, đồng thời thiếu hụt một quy trình tối ưu hóa các mô hình ngôn ngữ lớn mã nguồn mở cỡ nhỏ (8B) bằng phương pháp tinh chỉnh (fine-tuning) trên dữ liệu thực tế nhằm bảo mật thông tin doanh nghiệp. Bên cạnh đó, việc đánh giá chất lượng kiểm thử tự động sinh ra vẫn chưa có sự đồng bộ giữa tính đúng ngữ nghĩa (Semantic Similarity so với expert baseline) và tính khả thi cú pháp tĩnh (Executable Syntax Rate) của mã kiểm thử sinh ra.
>
> **Đóng góp của nhóm (Team Contribution):** Nhóm sẽ thực hiện một nghiên cứu thực nghiệm nhằm đánh giá và so sánh khả năng sinh zero-shot của GPT-4o (mô hình đóng thế hệ mới) và mô hình mã nguồn mở LLaMA-3-8B-Instruct được tinh chỉnh bằng LoRA trên bộ dữ liệu 100 User Stories đa miền (định dạng Connextra), sử dụng bộ độ đo kép tích hợp gồm Độ tương đồng ngữ nghĩa Cosine (mô hình nhúng Sentence-Transformers so với expert baseline) và Tỷ lệ cú pháp tĩnh khả thi (Executable Syntax Rate).
