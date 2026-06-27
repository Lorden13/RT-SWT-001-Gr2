# GAP Analysis
**Thành viên:** Lê Huy Đạt (SE172826)
**Ngày thực hiện:** 2026-06-04

---

## Bảng GAP

| Cột | Phát hiện | Loại GAP | Phản chứng |
|:---|:---|:---|:---|
| **Tool/LLM** | Phần lớn các nghiên cứu đạt hiệu năng cao (>80%) đều phụ thuộc hoàn toàn vào mô hình thương mại đóng (GPT-4, Claude 3.5). Các nghiên cứu dùng mô hình nguồn mở chưa tinh chỉnh (LLaMA-3-8B/70B base) có kết quả rất thấp (61% - 78%). Thiếu quy trình fine-tuning mô hình nguồn mở quy mô nhỏ (8B) bằng dữ liệu BDD thực tế. | **GAP-T** | **Không có phản chứng đầy đủ.** Chỉ có duy nhất Paper 12 (Selfbehave) tinh chỉnh LLaMA-3-8B nhưng là trên dữ liệu tự sinh (synthetic data) bằng Self-instruct, không phải dữ liệu thực tế của doanh nghiệp. |
| **Metric** | Các nghiên cứu bị phân mảnh đo lường: hoặc chỉ đo cú pháp Gherkin ở mức văn bản (BLEU, Cosine Similarity), hoặc chỉ đo thực thi script (Selenium/Appium execution rate). Thiếu một bộ metric kép đồng bộ đánh giá cả tính đúng đắn cú pháp và tính thực thi kỹ thuật. | **GAP-M** | **Không có phản chứng.** Không có paper nào trong 16 paper thiết lập bộ metric kép đồng bộ kết hợp cả hai khía cạnh này một cách hệ thống. |
| **Dataset** | Thiếu các bộ dữ liệu benchmark mở, đa miền (multi-domain) tích hợp đầy đủ chuỗi: Yêu cầu -> Gherkin -> Mã kiểm thử Selenium thực tế. Hầu hết dùng dữ liệu nội bộ nhỏ lẻ (10 - 30 mẫu). | **GAP-D** | **Có phản chứng.** Paper 12 cung cấp bộ dữ liệu 5,000 kịch bản Gherkin nhưng lại thiếu mã nguồn kiểm thử thực tế. Paper 8 sử dụng 100 User Stories từ Github nhưng đóng. |
| **Hạn chế tự nêu** | Hầu hết các paper đều thừa nhận mô hình dễ gặp hiện tượng ảo ảnh (hallucinations) khi định vị UI element (locators) trong giao diện web động hoặc khi xử lý logic nghiệp vụ phức tạp. | **GAP-S** | **Có phản chứng rộng rãi.** Tất cả các paper thực hành UI testing (Paper 1, 5, 10, 13, 14, 16) đều thừa nhận đây là hạn chế lớn nhất và đề xuất hướng xử lý động. |

---

## GAP Chính

GAP tuyên bố: Sự phụ thuộc hoàn toàn của các nghiên cứu sinh mã kiểm thử BDD vào các mô hình thương mại đóng đắt đỏ (GPT-4, Claude 3.5) để đạt được tỷ lệ chạy thành công tốt, và sự thiếu hụt nghiên cứu về phương pháp tinh chỉnh (fine-tuning) các mô hình ngôn ngữ lớn nguồn mở quy mô nhỏ (như LLaMA-3-8B) bằng dữ liệu thực tế của doanh nghiệp nhằm bảo mật tuyệt đối thông tin yêu cầu và tiết kiệm chi phí.

### Kiểm tra phản chứng

GAP tuyên bố: Chưa có nghiên cứu nào thực hiện tinh chỉnh (fine-tuning) mô hình nguồn mở quy mô nhỏ (≤ 8B) bằng dữ liệu thực tế của doanh nghiệp để sinh mã kiểm thử Selenium từ BDD đạt pass rate cao tương đương GPT-4.

| Paper | Đã làm chưa? | Ghi chú |
|:---|:---|:---|
| **Paper 1** | Không | Sử dụng GPT-4o và Claude 3.5 Sonnet trực tiếp (Pre-trained). |
| **Paper 2** | Không | So sánh mô hình pre-trained: GPT-4, LLaMA-3-70B, Gemini 1.5 Pro. |
| **Paper 3** | Không | Đánh giá GPT-4o, GPT-3.5, Claude 3 Opus dạng pre-trained. |
| **Paper 4** | Không | Đánh giá GPT-4, GPT-3.5, Gemini 1.0 Ultra pre-trained. |
| **Paper 5** | Không | Đánh giá baseline GPT-4o và LLaMA-3-8B pre-trained (Base). |
| **Paper 6** | Không | Nghiên cứu tình huống công nghiệp (Case study) dùng GPT-4 pre-trained. |
| **Paper 7** | Không | So sánh Claude 3.5 Sonnet, GPT-4o, LLaMA-3-70B pre-trained. |
| **Paper 8** | Không | Dùng GPT-4 và DeepSeek-Coder-33B pre-trained kết hợp RAG. |
| **Paper 9** | Không | Dịch ngược Gherkin dùng GPT-4o và Claude 3.5 pre-trained. |
| **Paper 10** | Không | Xây dựng Agentic workflow dùng GPT-4o-mini pre-trained. |
| **Paper 11** | Không | Sử dụng GPT-4 và GPT-3.5-turbo pre-trained. |
| **Paper 12** | Có một phần | Tinh chỉnh LLaMA-3-8B nhưng sử dụng dữ liệu tự sinh (synthetic data) bằng phương pháp Self-instruct, không phải dữ liệu thực tế và không đi kèm mã Selenium thực thi. |
| **Paper 13** | Không | Sinh Appium test cho mobile bằng GPT-4o và Claude 3.5 pre-trained. |
| **Paper 14** | Không | Sinh mã bằng Multi-agent cộng tác dùng GPT-4o và Gemini 1.5. |
| **Paper 15** | Không | Tích hợp GPT-4 và LLaMA-3-70B pre-trained vào công cụ AutomTest 3.0. |
| **Paper 16** | Không | Tích hợp GPT-4 và LLaMA-3-8B pre-trained vào công cụ AutoQALLMs. |

---

## GAP Secondary

GAP tuyên bố: Thiếu một hệ thống đo lường kép đồng thời phản ánh cả chất lượng văn bản đặc tả Gherkin (Semantic Alignment) và chất lượng mã nguồn thực thi (Selenium script compilation/execution pass rate) để đánh giá toàn diện năng lực sinh mã kiểm thử từ BDD.

---

## Feasibility Check

| Tiêu chí | Mức | Ghi chú |
|:---|:---|:---|
| **Dataset** | ⚠️ Trung bình | Cần thu thập khoảng 100 User Stories kèm kịch bản Gherkin và Selenium script ground truth. Có thể giải quyết bằng cách khai thác các kho mã nguồn mở trên GitHub. |
| **Tool / API** | Green | LLaMA-3-8B-Instruct là mô hình nguồn mở miễn phí. GPT-4o đối chứng có thể dùng API hạn mức học thuật. |
| **Compute** | ⚠️ Trung bình | Cần GPU (VRAM ≥ 16GB) để tinh chỉnh. Giải quyết bằng cách sử dụng cấu hình QLoRA 4-bit giúp giảm tải VRAM xuống dưới 10GB (chạy được trên Google Colab / Kaggle miễn phí). |
| **Ground Truth** | Green | Các mã kiểm thử Selenium WebDriver tương ứng với Gherkin được viết tay bởi các chuyên gia hoặc lấy từ các dự án thực tế làm chuẩn so sánh. |
| **Skills** | Green | Sinh viên có kiến thức về Python, Hugging Face Transformers và thư viện PEFT để cấu hình LoRA fine-tuning. |
| **Thời gian** | Green | Thời gian chạy thực nghiệm ước tính khoảng 30 - 40 giờ máy, hoàn toàn nằm trong quỹ thời gian môn học. |
| **Contribution** | Green | Đóng góp giải pháp tự chủ công nghệ, tiết kiệm chi phí và bảo mật tuyệt đối cho doanh nghiệp. |
