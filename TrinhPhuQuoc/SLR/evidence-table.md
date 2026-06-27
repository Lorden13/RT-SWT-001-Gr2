# Evidence Table — LLM for Acceptance Test Automation (BDD/Gherkin)

N papers included: 8 | Date: 2026-05-28

## Summary

- Nội dung tập trung vào việc sử dụng LLM/AI để tự động hóa kiểm thử chấp nhận (acceptance test) theo BDD/Gherkin.
- Mỗi nghiên cứu được tóm tắt theo: công cụ/LLM, dữ liệu thử nghiệm, các tiêu chí đo lường, kết quả chính và hạn chế.

---

## 1. Mendoza 2024 SBES

- Tool/LLM: GPT-3.5, GPT-4, Llama 2 (Zero-shot vs. Few-shot)
- Dataset: 15 BDD Gherkin feature files, 3 open-source systems
- Metric: Syntactic correctness, test coverage, execution success rate
- Kết quả: GPT-4 đạt 94% tỉ lệ thực thi thành công (few-shot), Llama 2 đạt 68% độ chính xác cú pháp
- Hạn chế: Kích thước dataset nhỏ; giới hạn trong miền dự án nguồn mở; phụ thuộc nhiều vào prompt template

## 2. Fernandes 2025 SBES

- Tool/LLM: GPT-4, Claude 3, Gemini 1.5 Pro
- Dataset: 50 user stories viết dưới dạng format Connextra
- Metric: Semantic similarity (BERTScore), Gherkin syntax compilation rate, đánh giá thủ công (thang 1–5)
- Kết quả: Claude 3 đạt semantic similarity = 0.88; Gherkin compilation rate = 92%
- Hạn chế: Không đánh giá được lỗi thực thi động; số lượng người đánh giá thủ công còn ít (3 học viên); chỉ kiểm thử trên yêu cầu tiếng Anh

## 3. Poth 2025 Springer

- Tool/LLM: GPT-4o, GitHub Copilot Chat
- Dataset: 25 Gherkin specifications đại diện cho các luồng giao diện UI
- Metric: Executable UI test script rate (Cypress/Playwright), độ chính xác định vị phần tử (element identification)
- Kết quả: Playwright code execution success = 78%, độ chính xác định vị selector = 82%
- Hạn chế: Chi phí bảo trì cao cho các bộ định vị động; số ca kiểm thử UI còn hạn chế; chưa so sánh nhiều LLM nguồn mở

## 4. dos Santos 2025 ICEIS

- Tool/LLM: GPT-3.5-turbo, Llama-3-70B
- Dataset: 30 user stories trên 3 ứng dụng dịch vụ tài chính
- Metric: Scenario completeness (độ bao phủ tiêu chí nghiệm thu), tỷ lệ biên dịch cú pháp
- Kết quả: Llama-3-70B sinh được 86% kịch bản đầy đủ; tỷ lệ biên dịch thành công = 90%
- Hạn chế: Bị giới hạn trong miền hệ thống tài chính; cần phải định nghĩa thủ công các few-shot mẫu để đạt điểm cao

## 5. Rathnayake 2026 arXiv

- Tool/LLM: Agentic framework dùng GPT-4, LLaMA-3
- Dataset: 42 user stories từ một nền tảng thương mại điện tử
- Metric: Semantic similarity (ROUGE-L), syntax validation, step-definition matching rate
- Kết quả: Agentic GPT-4 đạt step-definition match = 89%; ROUGE-L similarity = 0.86
- Hạn chế: Thời gian chạy API lâu do các vòng lặp multi-agent; thiết lập phức tạp; tiêu tốn chi phí gọi API lớn

## 6. Matveeva 2025 IEEE

- Tool/LLM: Phương pháp NLP truyền thống (Rule-based) vs. LLM (GPT-4)
- Dataset: 60 mô tả yêu cầu dưới dạng ngôn ngữ tự nhiên
- Metric: Tỷ lệ lỗi cú pháp Gherkin, độ chính xác ngữ nghĩa, tốc độ sinh
- Kết quả: GPT-4 có tỷ lệ lỗi cú pháp = 8% (so với 24% của Rule-based NLP); độ chính xác ngữ nghĩa = 85%
- Hạn chế: Rule-based chạy nhanh hơn nhưng kém linh hoạt; GPT-4 thỉnh thoảng sinh ảo tưởng (hallucination) trong các luồng logic BDD phức tạp

## 7. Tesfalidet 2025 diva-portal.org

- Tool/LLM: ChatGPT-4, GitHub Copilot (inline code generation)
- Dataset: 20 fintech user stories định dạng Agile Jira
- Metric: Code completeness, tỷ lệ biên dịch cú pháp, semantic similarity
- Kết quả: Tỷ lệ biên dịch cú pháp = 85%; Semantic similarity = 0.81
- Hạn chế: Độ tương đồng ngữ nghĩa thấp do logic nghiệp vụ tài chính phức tạp; kích thước dataset nhỏ; chỉ đánh giá các công cụ OpenAI

## 8. Bergsmann 2024 ACM

- Tool/LLM: Multi-agent LLM (Collaborating Agents sử dụng GPT-4)
- Dataset: 12 kịch bản đặc tả kiểm thử Gherkin phức tạp
- Metric: Tỷ lệ thực thi mã step definition, độ bao phủ sinh ca kiểm thử
- Kết quả: Các agent cộng tác sinh thành công step code cho 83% số bước; độ bao phủ đạt 92%
- Hạn chế: Độ trễ điều phối giữa các agent lớn; tiêu tốn lượng token lớn; có nguy cơ gặp vòng lặp vô hạn khi thực thi

---

## BỔ SUNG THEO RBL-2 - Gate Check

| Gate | Đánh giá |
|---|---|
| P1 - >= 5 paper | Pass: 8 paper (theo dòng `N papers included: 8` trong bản gốc) |
| P2 - >= 90% hàng Tool/LLM được điền | Pass: các hàng chính đều có Tool/LLM hoặc công cụ liên quan. |
| P3 - >= 50% hàng Kết quả có số liệu | Pass nếu tính cả các kết quả %/điểm số trong bảng. |
| P4 - >= 50% hàng Hạn chế được điền | Pass: các hàng chính đều có hạn chế tự nêu. |
| P5 - Metric cụ thể | Pass: metric được nêu cụ thể theo từng paper. |

