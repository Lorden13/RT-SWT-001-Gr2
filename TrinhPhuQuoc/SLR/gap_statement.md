# GAP Statement — Xác nhận khoảng trống nghiên cứu từ Evidence Table

## 1. Trả lời 4 câu hỏi rà soát từ Evidence Table

### Q1. LLM nào chưa được đánh giá?
*   Rà soát cột Tool/LLM: Các nghiên cứu trong bảng (8/8 papers) sử dụng các mô hình: GPT-3.5, GPT-4 (Mendoza 2024, Fernandes 2025, Rathnayake 2026, Matveeva 2025, Tesfalidet 2025, Bergsmann 2024), Claude 3, Gemini 1.5 Pro (Fernandes 2025), Llama 2/3 (Mendoza 2024, dos Santos 2025), và GitHub Copilot (Poth 2025, Tesfalidet 2025).
*   Ghi nhận: Hầu hết nghiên cứu dùng GPT-4 hoặc các mô hình cũ hơn. Mô hình GPT-4o zero-shot chưa được đánh giá cụ thể trong việc sinh đồng thời cả kịch bản Gherkin và mã step definition từ User stories định dạng Connextra. Do đó, nhóm lựa chọn GPT-4o làm Intervention (I) cho nghiên cứu này.

### Q2. "Semantic similarity" đã dùng chưa? - đếm papers dùng metric này
*   Rà soát cột Metric/Kết quả: **Đã dùng rồi**. Có **3 trên tổng số 8 bài báo** sử dụng độ tương đồng ngữ nghĩa làm metric đánh giá:
    1.  *Fernandes 2025* (Paper 2) sử dụng BERTScore để đo độ tương đồng ngữ nghĩa (đạt BERTScore = 0.88).
    2.  *Rathnayake 2026* (Paper 5) sử dụng ROUGE-L (tính trùng lặp từ vựng/ngữ nghĩa, đạt ROUGE-L = 0.86).
    3.  *Tesfalidet 2025* (Paper 7) sử dụng Semantic similarity chung chung (đạt 0.81).
*   Ghi nhận: Chưa có nghiên cứu nào sử dụng phương pháp Cosine Similarity kết xuất từ mô hình nhúng Sentence-Transformers để so sánh trực tiếp kịch bản sinh ra bởi LLM với baseline viết tay bởi chuyên gia (expert-written BDD). Do đó, nhóm chọn Metric 1 của Outcome (O) là Semantic Similarity sử dụng Cosine Similarity qua Sentence-Transformers.

### Q3. Executable syntax đã đo chưa? - đếm papers đo executable rate
*   Rà soát cột Metric/Kết quả: **Chưa đo trực tiếp cho cú pháp tĩnh (syntax)**. Tuy nhiên, có **3 trên tổng số 8 bài báo** đo lường tính khả thi thực thi động (executable rate) của kịch bản/code:
    1.  *Mendoza 2024* (Paper 1) đo tỷ lệ thực thi thành công (execution success rate đạt 94% với GPT-4 few-shot).
    2.  *Poth 2025* (Paper 3) đo tỷ lệ sinh kịch bản Cypress/Playwright thực thi thành công từ Gherkin (đạt 78%).
    3.  *Bergsmann 2024* (Paper 8) đo tỷ lệ thực thi thành công step code của collaborating agents (đạt 83%).
*   Ghi nhận: Các bài báo trên đều kiểm thử động (dynamic execution) trên môi trường chạy thực tế của code test UI hoặc code step, chưa có nghiên cứu nào tập trung đo lường tỷ lệ không lỗi cú pháp tĩnh (executable syntax rate) của cả kịch bản Gherkin kết hợp mã step definitions được sinh ra đồng thời. Do đó, nhóm chọn Metric 2 của Outcome (O) là Executable syntax rate (không lỗi parse).

### Q4. Hạn chế nào lặp >= 2 lần?
*   Rà soát cột Hạn chế tự nêu: Có 2 hạn chế chính lặp lại từ 2 lần trở lên:
    1.  *Kích thước dataset thử nghiệm nhỏ/giới hạn:* Lặp lại **4 lần** (Mendoza 2024 - 15 feature files; Fernandes 2025 - 50 US; Poth 2025 - 25 Gherkin specs; Tesfalidet 2025 - 20 US).
    2.  *Sự phụ thuộc vào cấu trúc prompt thủ công hoặc thiết lập hệ thống multi-agent quá phức tạp:* Lặp lại **4 lần** (Mendoza 2024, dos Santos 2025, Rathnayake 2026, Bergsmann 2024).
*   Ghi nhận: Khoảng trống nghiên cứu được cộng đồng thừa nhận rộng rãi là thiếu các đánh giá trên tập dữ liệu thực tế lớn hơn và sự phụ thuộc quá nhiều vào prompt engineering phức tạp (như few-shot hoặc multi-agent) thay vì đánh giá khả năng zero-shot thuần túy của các LLM mạnh nhất.

---

## 2. Nguồn gốc của ngưỡng tương đồng ngữ nghĩa 0.85

Nhóm lựa chọn ngưỡng đánh giá Semantic Similarity >= 0.85 dựa trên cơ sở khoa học rút ra từ các nghiên cứu thực nghiệm đi trước trong cùng lĩnh vực:
*   Theo Fernandes 2025 SBES (Paper 2), khi sử dụng mô hình ngôn ngữ lớn để sinh Gherkin từ User Stories, độ tương đồng ngữ nghĩa lớn nhất đạt được là **0.88** (đo bằng BERTScore).
*   Theo Rathnayake 2026 arXiv (Paper 5), độ tương đồng ngữ nghĩa lớn nhất đạt được là **0.86** (đo bằng ROUGE-L).
*   Theo Matveeva 2025 IEEE (Paper 6), độ chính xác ngữ nghĩa của kịch bản Gherkin do GPT-4 sinh ra đạt trung bình **0.85 (85%)**.

Vì vậy, việc đặt ngưỡng chất lượng >= 0.85 cho nghiên cứu này là hoàn toàn khả thi và có cơ sở khoa học đối chứng rõ ràng (được trích dẫn trực tiếp từ kết quả thực nghiệm tối ưu của *Fernandes 2025* và *Matveeva 2025*).

---

## 3. Phát biểu khoảng trống nghiên cứu (GAP Statement)

**Phát biểu theo cấu trúc chuẩn:**

Tất cả 8 bài báo được rà soát (papers reviewed) đều tập trung vào việc sử dụng các mô hình ngôn ngữ lớn thương mại qua API (như GPT-4, GPT-3.5, Claude 3) hoặc NLP truyền thống để sinh hoặc thực thi kịch bản kiểm thử BDD/Gherkin.

Tuy nhiên, không có bài báo nào trong số đó:
1.  Đánh giá hiệu quả của mô hình frontier LLM thế hệ mới là GPT-4o dưới dạng zero-shot để sinh đồng thời cả kịch bản Gherkin và mã step definitions từ User stories định dạng Connextra.
2.  Đo lường chất lượng kịch bản bằng độ tương đồng ngữ nghĩa Cosine Similarity (sử dụng mô hình nhúng Sentence-Transformers) đối chiếu trực tiếp với kịch bản kiểm thử viết tay bởi chuyên gia (expert-written) làm baseline.
3.  Kiểm tra tính đúng đắn về mặt tĩnh thông qua tỷ lệ không lỗi cú pháp (executable syntax rate) của cả kịch bản và step definitions được sinh ra.

*   **Khoảng trống nghiên cứu (GAP):** Chưa có nghiên cứu nào đánh giá toàn diện khả năng sinh đồng thời kịch bản Gherkin và mã step definitions từ User Stories định dạng Connextra của mô hình GPT-4o (zero-shot) sử dụng kết hợp hai chỉ số đo lường chính: độ tương đồng ngữ nghĩa Cosine Similarity (Sentence-Transformers so với expert baseline) và tính đúng đắn cú pháp tĩnh (executable syntax rate).
*   **Đóng góp của nghiên cứu này (Contribution):** Đánh giá thực nghiệm khả năng sinh zero-shot của GPT-4o trên bộ dữ liệu gồm 50 user stories định dạng Connextra, đo lường độ tương đồng ngữ nghĩa Cosine Similarity (Sentence-Transformers) so với bộ kịch bản viết tay chuẩn của chuyên gia, và kiểm tra tính hợp lệ cú pháp tĩnh (executable syntax rate) bằng công cụ parse chuyên dụng.
