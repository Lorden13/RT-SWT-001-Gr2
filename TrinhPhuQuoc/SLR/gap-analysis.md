# Phân Tích Khoảng Trống Nghiên Cứu — GAP Analysis (Trịnh Phú Quốc)

Tài liệu này chứa nội dung chi tiết của quy trình phân tích khoảng trống nghiên cứu (GAP Analysis) được thực hiện trên bảng bằng chứng (Evidence Table) cá nhân gồm **8 bài báo khoa học** đã được tuyển chọn.

---

## 1. Bảng phân loại GAP phát hiện

| Loại GAP | Phát hiện từ bảng bằng chứng | Câu hỏi cốt lõi |
|:---|:---|:---|
| **GAP-T (Technology)** | Hầu hết các nghiên cứu sử dụng GPT-4 hoặc các mô hình cũ hơn. Khả năng zero-shot của mô hình đóng thế mới nhất **GPT-4o** để đồng sinh kịch bản Gherkin và mã step definition chưa được nghiên cứu rõ. | Công nghệ/Mô hình nào thế hệ mới chưa được đánh giá? |
| **GAP-M (Metric)** | Các nghiên cứu trước đo lường tách biệt: hoặc đo độ tương đồng ngữ nghĩa (Semantic similarity như BERTScore, ROUGE-L) hoặc đo tỷ lệ thực thi thành công của code test (execution pass rate), chưa có độ đo tích hợp đồng thời hai khía cạnh này. | Khía cạnh chất lượng/Độ đo kết hợp nào chưa được sử dụng? |
| **GAP-D (Dataset)** | Các nghiên cứu sử dụng các bộ dữ liệu nhỏ lẻ, đóng hoặc đặc thù đơn miền (ví dụ: chỉ về tài chính ngân hàng). Thiếu các thử nghiệm trên các bộ dữ liệu User Stories đa miền Agile. | Domain/Quy mô dữ liệu thực nghiệm nào còn thiếu? |
| **GAP-S (Shared Limitation)** | Nhiều nghiên cứu thừa nhận hạn chế về sự phụ thuộc vào cấu trúc prompt template thủ công phức tạp hoặc cấu trúc multi-agent có độ trễ/chi phí API quá cao. | Hạn chế chung nào được đa số nghiên cứu thừa nhận? |

---

## 2. Kiểm tra phản chứng (Counter-evidence Check)
Để đảm bảo các khoảng trống nghiên cứu đề xuất là hợp lệ và chưa từng được giải quyết bởi các công trình đi trước, nhóm tiến hành rà soát phản chứng trên cả 8 bài báo thuộc Evidence Table:

### Bảng rà soát phản chứng cho GAP-T (GPT-4o zero-shot co-generation)

| Paper | Đã làm chưa? | Ghi chú từ Evidence Table |
|:---|:---:|:---|
| 1. Mendoza 2024 SBES | **Không** | Sử dụng GPT-3.5, GPT-4, Llama 2 ở chế độ Zero-shot vs. Few-shot. |
| 2. Fernandes 2025 SBES | **Không** | Sử dụng GPT-4, Claude 3, Gemini 1.5 Pro. |
| 3. Poth 2025 Springer | **Không** | Sử dụng GPT-4o để sinh Cypress/Playwright từ kịch bản Gherkin có sẵn, không phải sinh Gherkin + step def từ User Story. |
| 4. dos Santos 2025 ICEIS | **Không** | Sử dụng GPT-3.5-turbo, Llama-3-70B. |
| 5. Rathnayake 2026 arXiv | **Không** | Sử dụng hệ thống Agentic phức tạp trên nền GPT-4 và LLaMA-3. |
| 6. Matveeva 2025 IEEE | **Không** | Sử dụng GPT-4 và so sánh với NLP truyền thống. |
| 7. Tesfalidet 2025 DiVA | **Không** | Sử dụng ChatGPT-4 và GitHub Copilot. |
| 8. Bergsmann 2024 ACM | **Không** | Sử dụng hệ thống Multi-agent phức tạp trên nền GPT-4. |

*   **Kết luận:** GAP-T hoàn toàn hợp lệ, không có paper nào sử dụng GPT-4o zero-shot để sinh đồng thời cả Gherkin và step definitions từ User stories.

### Bảng rà soát phản chứng cho GAP-M (SBERT Cosine Similarity + Executable Syntax Rate)

| Paper | Đã làm chưa? | Ghi chú từ Evidence Table |
|:---|:---:|:---|
| 1. Mendoza 2024 SBES | **Không** | Chỉ đo độ chính xác cú pháp (syntactic correctness) và tỷ lệ thực thi (không dùng Cosine). |
| 2. Fernandes 2025 SBES | **Không** | Đo tương đồng bằng BERTScore, đo biên dịch bằng Gherkin compilation (tách biệt). |
| 3. Poth 2025 Springer | **Không** | Chỉ đo tỷ lệ chạy Cypress/Playwright thành công và độ chính xác định vị selector. |
| 4. dos Santos 2025 ICEIS | **Không** | Đo độ bao phủ tiêu chí nghiệm thu (completeness) và tỷ lệ biên dịch cú pháp. |
| 5. Rathnayake 2026 arXiv | **Không** | Đo tương đồng bằng ROUGE-L, tỷ lệ khớp step-definition. |
| 6. Matveeva 2025 IEEE | **Không** | Đo tỷ lệ lỗi cú pháp Gherkin, độ chính xác ngữ nghĩa thủ công. |
| 7. Tesfalidet 2025 DiVA | **Không** | Đo tỷ lệ biên dịch cú pháp, độ tương đồng ngữ nghĩa. |
| 8. Bergsmann 2024 ACM | **Không** | Chỉ đo tỷ lệ thực thi mã step definition và độ bao phủ kiểm thử. |

*   **Kết luận:** GAP-M hoàn toàn hợp lệ. Chưa có bài báo nào kết hợp kiểm tra độ tương đồng ngữ nghĩa Cosine ( Sentence-Transformers) đối chiếu với expert baseline đồng thời với tỷ lệ hợp lệ cú pháp tĩnh (Executable Syntax Rate) của cả Gherkin và step definitions sinh ra.

---

## 3. Chốt GAP nghiên cứu chính

### GAP Chính (Primary GAP):
> **Tuyên bố GAP chính:** Các nghiên cứu hiện tại về sinh kiểm thử tự động chấp nhận (BDD/Gherkin) chủ yếu tập trung vào các mô hình cũ như GPT-4 hoặc các hệ thống Agentic phức tạp, đồng thời đánh giá tách rời khía cạnh tương đồng văn bản với khả năng thực thi. Chưa có nghiên cứu nào đánh giá toàn diện khả năng sinh zero-shot đồng thời cả kịch bản Gherkin và mã step definitions từ User Stories định dạng Connextra của mô hình GPT-4o thế hệ mới sử dụng bộ độ đo kết hợp gồm: độ tương đồng ngữ nghĩa Cosine Similarity ( Sentence-Transformers so với expert baseline) và tỷ lệ đúng cú pháp tĩnh (Executable Syntax Rate).

### GAP Phụ (Secondary GAP):
> **Tuyên bố GAP phụ:** Thiếu các đánh giá thực nghiệm trên các bộ dữ liệu yêu cầu thực tế Agile đa miền có kích thước vừa và lớn (ví dụ: 50 User Stories), thay vào đó hầu hết các nghiên cứu trước bị giới hạn ở quy mô rất nhỏ (12 đến 30 mẫu) hoặc đặc thù đơn miền.

---

## 4. Feasibility Check (Đánh giá tính khả thi)

Dưới đây là bảng tự đánh giá mức độ khả thi khi giải quyết khoảng trống nghiên cứu đã chọn:

| Tiêu chí | Mức độ | Rationale / Lý do chi tiết |
|:---|:---:|:---|
| **Dataset (Dữ liệu)** | **Medium** | Cần thu thập và chuẩn hóa bộ dữ liệu 50 User Stories định dạng Connextra đa miền. Việc này hoàn toàn khả thi bằng cách lấy từ các dự án phần mềm mẫu hoặc bài tập lớn. |
| **Tool/API (Công cụ)** | **High** | API của GPT-4o đã sẵn sàng và chi phí sử dụng cho 50 mẫu là rất thấp. Công cụ tính toán như Sentence-Transformers (`all-MiniLM-L6-v2`) và các thư viện Gherkin parser đều miễn phí và dễ cài đặt. |
| **Compute (Tài nguyên tính toán)** | **High** | Việc chạy mô hình nhúng SBERT và parser cú pháp tĩnh chỉ tốn vài giây trên một máy tính cá nhân thông thường. |
| **Ground Truth (Đáp án chuẩn)** | **High** | Bộ ca kiểm thử BDD viết tay của chuyên gia (Expert-written baseline) có thể xây dựng dựa trên bài giải mẫu của giảng viên hoặc nhờ các sinh viên xuất sắc viết. |
| **Skills (Kỹ năng)** | **High** | Sinh viên đã được trang bị kỹ năng lập trình Python, gọi API, sử dụng thư viện sentence-transformers và hiểu biết sâu sắc về BDD/Gherkin. |
| **Thời gian** | **High** | Thực nghiệm có thể chạy xong trong vòng 1-2 tuần, hoàn toàn nằm trong khung thời gian cho phép của môn học. |
| **Contribution (Đóng góp)** | **High** | Kết quả thực nghiệm sẽ cung cấp một báo cáo thực tế, có số liệu đối chứng khoa học giúp giảng viên và sinh viên các khóa sau lựa chọn mô hình/cách prompt tối ưu nhất. |

*   **Quyết định:** Không có tiêu chí nào bị đánh giá mức ❌ (Không thể thực hiện), chỉ có 1 tiêu chí ở mức ⚠️ (Medium), do đó thiết kế thực nghiệm này nằm trong **vùng an toàn** và cực kỳ khả thi.
