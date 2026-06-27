# GAP Statement — Xác nhận khoảng trống nghiên cứu từ Evidence Table

## 1. Trả lời 4 câu hỏi rà soát từ Evidence Table

### Q1. LLM nào chưa được đánh giá?
*   **Rà soát cột Tool/LLM:** Các nghiên cứu sử dụng các mô hình: GPT-3.5, GPT-4 (Mendoza 2024, Fernandes 2025, Rathnayake 2026, Karpurapu 2024, Ferreira 2025, Tesfalidet 2025), Claude 3.5 Sonnet / Claude 3 (Rathnayake 2026, Increasing BDD PoCs 2026), Gemini (Mendoza 2024, Fernandes 2025, dos Santos 2026, Rathnayake 2026, Bergsmann 2024), Grok (dos Santos 2026), Llama 2 / Llama 3 (Karpurapu 2024, Fernandes 2025, Poth 2025, AutoQALLMs 2026), PaLM-2 (Karpurapu 2024), và GitHub Copilot (dos Santos 2026, Tesfalidet 2025, Poth 2025).
*   **Ghi nhận:** Khả năng sinh đồng thời (co-generation) zero-shot của mô hình **GPT-4o** để tạo ra cả kịch bản Gherkin và mã step definition từ User Stories định dạng Connextra chưa được đánh giá đầy đủ. Đồng thời, hiệu năng của mô hình nguồn mở cỡ nhỏ (**LLaMA-3-8B**) sau khi tinh chỉnh bằng phương pháp **LoRA** trên dữ liệu thực tế so với GPT-4o cũng là một khoảng trống công nghệ lớn cần kiểm chứng.

### Q2. "Semantic similarity" đã dùng chưa? - đếm papers dùng metric này
*   **Rà soát cột Metric/Kết quả:** **Đã dùng**. Có **3 trên tổng số 15 bài báo** thực nghiệm đo lường độ tương đồng ngữ nghĩa:
    1.  *Fernandes 2025 (Bài 2)* sử dụng METEOR để đo độ tương đồng ngữ nghĩa/từ vựng (đạt METEOR = 0.84 với Gemini).
    2.  *Rathnayake 2026 (Bài 4)* sử dụng BERTScore (91.16%) và Cosine Similarity (SBCS = 53.96%) để đo độ tương đồng ngữ nghĩa.
    3.  *Tesfalidet 2025 (Bài 8)* sử dụng Semantic Similarity (đạt 0.81 với GPT-4).
*   **Ghi nhận:** Hầu hết các nghiên cứu này chỉ sử dụng độ đo tương đồng ngữ nghĩa cho riêng kịch bản Gherkin, chưa có nghiên cứu nào sử dụng Sentence-Transformers (như model `all-MiniLM-L6-v2`) để so sánh trực tiếp cả kịch bản và step definitions với expert-written baseline với một ngưỡng chất lượng cụ thể như $\ge 0.85$.

### Q3. Executable syntax đã đo chưa? - đếm papers đo executable rate
*   **Rà soát cột Metric/Kết quả:** **Đã dùng**. Có **9 trên tổng số 15 bài báo** đo lường tính khả thi thực thi hoặc tính đúng đắn cú pháp tĩnh:
    1.  *Karpurapu 2024 (Bài 5)* đo tỷ lệ đúng cú pháp Gherkin tĩnh (Syntax Accuracy) qua `gherkin-lint` (đạt 100% ở few-shot).
    2.  *dos Santos 2026 SciTePress (Bài 3)* đo độ chính xác/khả năng chạy của mã kiểm thử (đạt 76.7% với ChatGPT).
    3.  *Ferreira 2025 (Bài 6)* đo executability của kịch bản và mã Cypress.
    4.  *Tesfalidet 2025 (Bài 8)* đo Executable Step Rate (đạt 85% với GPT-4).
    5.  *Poth 2025 (Bài 10)* đo UI Test Compilation Rate và Executable UI script rate (Playwright đạt 78% với GPT-4o).
    6.  *Selfbehave 2026 (Bài 11)* đo Gherkin Syntax Pass Rate (đạt 99.2% với mô hình tinh chỉnh).
    7.  *Bergsmann 2024 (Bài 12)* đo Execution Success Rate (đạt 83%-84% nhờ Multi-Agent).
    8.  *AutoQALLMs 2026 (Bài 13)* đo Selenium Test Script Executability (đạt 86.0%).
    9.  *Agentic BDD 2026 (Bài 14)* đo Test Generation Pass Rate (đạt 95.0% nhờ cơ chế tự sửa lỗi).
*   **Ghi nhận:** Các nghiên cứu trước đo lường tỷ lệ thực thi thành công động (dynamic execution) hoặc cú pháp tĩnh một cách riêng rẽ. Chưa có nghiên cứu nào sử dụng chỉ số kép kết hợp cả độ tương đồng ngữ nghĩa và tỷ lệ không lỗi cú pháp tĩnh (Executable Syntax Rate $\ge 80\% / 85\%$) làm chốt chặn kiểm thử tĩnh trước khi đưa vào môi trường thực thi động.

### Q4. Hạn chế nào lặp >= 2 lần?
*   Rà soát cột Hạn chế tự nêu, phát hiện 4 hạn chế chính lặp lại:
    1.  *Quy mô tập dữ liệu thử nghiệm nhỏ hoặc thiếu dự án thực tế:* Lặp lại **4 lần** (Mendoza 2024 - 5 kịch bản; Fernandes 2025 - 10 kịch bản; dos Santos 2026 - 34 stories; Tesfalidet 2025 - 10-20 stories).
    2.  *LLM gặp khó khăn khi sinh ca kiểm thử cho logic nghiệp vụ phức tạp hoặc tính toán toán học:* Lặp lại **3 lần** (Mendoza 2024, Tesfalidet 2025, Increasing BDD PoCs 2026).
    3.  *Chi phí token cao, độ trễ lớn của các hệ thống Multi-Agent hoặc prompt engineering phức tạp:* Lặp lại **3 lần** (dos Santos 2026, Bergsmann 2024, Agentic BDD 2026).
    4.  *Phụ thuộc nặng nề vào chất lượng của các UI attributes / thuộc tính HTML (ID, Class name) trong context:* Lặp lại **2 lần** (Ferreira 2025, Poth 2025).

---

## 2. Nguồn gốc của các ngưỡng chất lượng (Thresholds)

Nhóm lựa chọn các ngưỡng đánh giá dựa trên cơ sở khoa học rút ra từ các nghiên cứu thực nghiệm đi trước trong cùng lĩnh vực:
*   **Ngưỡng Cosine Similarity $\ge 0.85$ (Case 2):** Dựa trên kết quả thực nghiệm của *Fernandes 2025* (đạt BERTScore = 0.88), *Rathnayake 2026* (đạt ROUGE-L = 0.86) và *Matveeva 2025* (độ chính xác ngữ nghĩa trung bình 85%).
*   **Ngưỡng Executable Syntax Rate $\ge 80\% / 85\%$ (Case 2):** Dựa trên tỷ lệ thực thi thành công của *Poth 2025* (Playwright đạt 78%), *Tesfalidet 2025* (executable steps đạt 85%), và *Bergsmann 2024* (chạy thành công đạt 83%).

---

## 3. Phát biểu khoảng trống nghiên cứu (GAP Statement)

**Phát biểu theo cấu trúc chuẩn:**

Các bài báo khoa học được rà soát (15 papers reviewed) đều tập trung vào việc ứng dụng LLM/NLP để tự động hóa sinh kịch bản kiểm thử BDD/Gherkin hoặc mã kiểm thử.

Tuy nhiên, không có bài báo nào trong số đó:
1.  Đánh giá khả năng sinh zero-shot đồng thời cả kịch bản Gherkin và mã step definitions từ User Stories định dạng Connextra của mô hình frontier GPT-4o hoặc mô hình mã nguồn mở cỡ nhỏ LLaMA-3-8B được tinh chỉnh bằng LoRA trên dữ liệu thực tế.
2.  Sử dụng bộ độ đo kép tích hợp gồm: độ tương đồng ngữ nghĩa Cosine Similarity (dùng Sentence-Transformers so với expert-written baseline) và tỷ lệ đúng cú pháp tĩnh (Executable Syntax Rate) làm chốt chặn kiểm thử tĩnh.
3.  Đánh giá hiệu năng và tính kinh tế (tiết kiệm token, giảm chi phí API, bảo mật dữ liệu) của mô hình nhỏ tinh chỉnh so với mô hình lớn thương mại trên một bộ dữ liệu đa miền quy mô trung bình (50-100 User Stories).

*   **Khoảng trống nghiên cứu (GAP):** Chưa có nghiên cứu nào đánh giá toàn diện khả năng sinh đồng thời kịch bản Gherkin và mã step definitions từ User Stories định dạng Connextra của mô hình GPT-4o (zero-shot) và LLaMA-3-8B (LoRA-FT) sử dụng bộ độ đo kép tích hợp gồm độ tương đồng ngữ nghĩa Cosine Similarity (Sentence-Transformers so với expert baseline $\ge 0.85$) và tỷ lệ đúng cú pháp tĩnh (Executable Syntax Rate $\ge 80\%$).
*   **Đóng góp của nghiên cứu này (Contribution):** Xây dựng bộ dữ liệu benchmark gồm 50 User Stories Agile đa miền định dạng Connextra, tinh chỉnh mô hình LLaMA-3-8B qua LoRA và so sánh đối chứng hiệu năng với GPT-4o (zero-shot) bằng bộ độ đo kép tích hợp (Cosine Similarity và Executable Syntax Rate), cung cấp cơ sở dữ liệu thực nghiệm cho việc đánh giá chất lượng kiểm thử tĩnh trước khi thực hiện môi trường runtime.
