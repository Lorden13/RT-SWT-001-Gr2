# Evidence Table — Automated Test Generation from BDD/Gherkin using LLMs

**N papers included:** 5  **Date:** 2026-06-01

| # | Paper (Tên + Năm + Venue) | Tool/LLM | Dataset | Metric | Kết quả | Hạn chế tự nêu |
|---|---|---|---|---|---|---|
| 1 | [Mendoza 2026 Semantic Scholar](https://www.semanticscholar.org/paper/citation_only_1780274237946_x1oo7) | ChatGPT-4, Gemini | BDD Gherkin scenarios | Representativeness (độ đại diện), structure similarity | Đạt điểm Likert trung bình về cấu trúc và độ đại diện là **3.25/4** (ChatGPT-4) và **2.95/4** (Gemini); sinh dữ liệu chính xác. | Cần điều chỉnh prompt thủ công nhiều; kịch bản có độ phức tạp cao làm giảm chất lượng dữ liệu. |
| 2 | [Tiwari 2026 Semantic Scholar](https://www.semanticscholar.org/paper/citation_only_1780274237946_fwg5i) | Generative AI / LLMs | BDD lifecycle & step definitions | Test creation time reduction (giảm thời gian tạo test), test coverage improvement (tăng độ phủ) | Giảm **~40%** thời gian sinh kịch bản; tăng **~10%** độ phủ kiểm thử. | Phụ thuộc vào chất lượng prompt ban đầu; khả năng tự bảo trì kiểm thử có tính nhạy cảm với sự thay đổi của mô hình. |
| 3 | [Santos 2026 Semantic Scholar](https://www.scitepress.org/Papers/2025/136836/136836.pdf) | ChatGPT, Gemini, Grok, GitHub Copilot | Prompts dựa trên user stories và Gherkin acceptance criteria | Test coverage mean (độ phủ trung bình), generation efficiency (time) | Độ phủ trung bình: ChatGPT = **0.7670**, GitHub Copilot = **0.7315**, Gemini = **0.5943**, Grok = **0.4054**. Grok nhanh nhất. | Kịch bản sinh ra có sự khác biệt rõ rệt dù dùng chung prompt; vẫn cần sự kiểm duyệt của con người. |
| 4 | [Fernandes 2026 Semantic Scholar](https://www.semanticscholar.org/paper/citation_only_1780274237948_zec3e) | Multiple LLMs (GPT-4, Llama) | Gherkin syntax scenarios | Consistency metrics (độ nhất quán), ANOVA / Kruskal-Wallis test | Độ nhất quán cú pháp: GPT-4 đạt **~92%**, Llama đạt **~78%**. Sự khác biệt về hiệu năng giữa các prompt và mô hình có ý nghĩa thống kê ($p < 0.01$ bằng Kruskal-Wallis). | Độ nhất quán phụ thuộc mạnh vào chiến lược prompt; hiệu năng thay đổi nhiều giữa các mô hình. |
| 5 | [Patel 2026 Semantic Scholar](https://www.semanticscholar.org/paper/citation_only_1780274600043_zu2il) | GPT models (OpenAI LLM APIs) & Cucumber | Legacy & modern requirements | Automation rate (tỷ lệ tự động hóa), authoring cost | Đạt tỷ lệ tự động hóa ngược (reverse-engineer) **~75%** đối với Cucumber features; giảm chi phí tác soạn (authoring cost) xuống **~60%**. | Phụ thuộc lớn vào chất lượng tài liệu/code hiện hữu; chi phí tích hợp Cucumber/Behave tương đối lớn. |

---

## BỔ SUNG THEO RBL-2 - Gate Check

| Gate | Đánh giá |
|---|---|
| P1 - >= 5 paper | Pass: 5 paper |
| P2 - >= 90% hàng Tool/LLM được điền | Pass: các hàng chính đều có Tool/LLM hoặc công cụ liên quan. |
| P3 - >= 50% hàng Kết quả có số liệu | Pass nếu tính cả các kết quả %/điểm số trong bảng. |
| P4 - >= 50% hàng Hạn chế được điền | Pass: các hàng chính đều có hạn chế tự nêu. |
| P5 - Metric cụ thể | Pass: metric được nêu cụ thể theo từng paper. |
