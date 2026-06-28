# BẢNG GHI CHÚ CHÚ GIẢI VÀ HIGHLIGHT CHI TIẾT (15 PAPERS)
**Học phần:** SWT301 — Kiểm thử phần mềm (Software Testing)  
**Sinh viên:** Trịnh Phú Quốc (MSSV: SE190287)  
**Mục tiêu:** Lưu trữ thông tin chi tiết và phần văn bản bôi đậm (highlight) của 15 bài báo khoa học làm bằng chứng phân tích GAP và thiết kế thực nghiệm.

---

## TỔNG QUAN THƯ MỤC PDF TẢI VỀ (DOWNLOADED PAPERS)
Hiện tại, thư mục [downloaded_papers](file:///c:/FPTU/S5/SWT301/SLR/PhuQuoc/SLR/downloaded_papers/) chứa **8 tệp PDF gốc** đã tải thành công và có sẵn:
1.  `Mendoza_2024_SBES_highlighted.pdf` (Bài 1)
2.  `Fernandes_2025_SBES_highlighted.pdf` (Bài 2)
3.  `dos_Santos_2026_SciTePress_highlighted.pdf` (Bài 3)
4.  `Rathnayake_2026_arXiv_highlighted.pdf` (Bài 4)
5.  `dos Santos 2025 ICEIS _highlighted.pdf` (Bài 5)
6.  `Ferreira_2025_arXiv.pdf` (Bài 6)
7.  `Hasan_2025_arXiv.pdf` (Bài 7)
8.  `Mobile_Acceptance_Testing_2026_arXiv.pdf` (Bài 9)

Đối với các bài báo còn lại nằm sau tường lửa trả phí của các nhà xuất bản lớn (IEEE, ACM, Springer), tài liệu này cung cấp **đầy đủ ghi chú học thuật (notes) và các đoạn trích dẫn cốt lõi (quotes/highlights)** để phục vụ nghiệm thu.

---

## CHI TIẾT HIGHLIGHT & NOTE CỦA 15 BÀI BÁO

### BÀI 1: Mendoza 2024 SBES
*   **Tên bài báo:** *Comparative analysis of large language model tools for automated test data generation from BDD*
*   **Trạng thái PDF:** Đã tải (`Mendoza_2024_SBES_highlighted.pdf`)
*   **Tóm tắt nội dung:** Đánh giá so sánh ChatGPT-4, ChatGPT-3.5, Gemini, và Copilot trong việc sinh dữ liệu kiểm thử từ 5 kịch bản Gherkin BDD có độ phức tạp tăng dần.
*   **Tool/LLM:** ChatGPT-4, ChatGPT-3.5, Gemini (LaMDA), Copilot.
*   **Dataset:** 5 kịch bản BDD (S1 đến S5). Quy mô: **Cực nhỏ (5 mẫu)**.
*   **Metric:** Thang đo Likert (0-4) đánh giá tính rõ ràng, cấu trúc, độ bao phủ.
*   **Kết quả:** ChatGPT-4 và Gemini đạt 23/24 điểm; ChatGPT-3.5 đạt 22/24 điểm; Copilot đạt 17/24 điểm.
*   **Hạn chế:** Quy mô tập mẫu quá nhỏ; Copilot không duy trì được cấu trúc Gherkin; gặp khó khăn khi xử lý toán học phức tạp (S5).
*   **[HIGHLIGHT / NOTE CHI TIẾT]:**
    *   *Trích dẫn sử dụng:* `"ChatGPT-4 and Gemini reached the highest completeness scores, but all models struggled with mathematical and logical rules in scenario S5 (Inner product)..."` (Section 4.2).
    *   *Ý nghĩa viết GAP:* Cung cấp bằng chứng về sự thất bại của các LLM trước logic nghiệp vụ phức tạp (GAP-S) và hạn chế về kích thước tập dữ liệu cực nhỏ (GAP-D).

---

### BÀI 2: Fernandes 2025 SBES
*   **Tên bài báo:** *A Comparative Study of LLMs for Gherkin Generation*
*   **Trạng thái PDF:** Đã tải (`Fernandes_2025_SBES_highlighted.pdf`)
*   **Tóm tắt nội dung:** So sánh hiệu năng sinh kịch bản Gherkin từ đặc tả ca kiểm thử dạng tự do giữa 7 mô hình LLM thương mại và nguồn mở.
*   **Tool/LLM:** GPT-3.5, GPT-4, GPT-4o Mini, LLaMA-3-70B, Phi-3 Mini, Gemini 1.5 Pro, DeepSeek R1.
*   **Dataset:** 10 mô tả ca kiểm thử từ tập 1.286 ca. Quy mô: **Nhỏ (10 mẫu)**.
*   **Metric:** Điểm tương đồng ngữ nghĩa (METEOR), Hệ số biến thiên (CV) đo độ ổn định.
*   **Kết quả:** Zero-shot đạt kết quả tốt nhất. Gemini (0.84) và Phi-3 Mini (0.81) đạt điểm METEOR cao nhất. LLaMA 3 đạt 0.75.
*   **Hạn chế:** Kích thước mẫu nhỏ; METEOR không phản ánh tính khả thi thực thi động của code kiểm thử sinh ra.
*   **[HIGHLIGHT / NOTE CHI TIẾT]:**
    *   *Trích dẫn sử dụng:* `"Zero-shot prompting yielded superior and more consistent Gherkin scenarios than few-shot prompting... A limitation of automatic metrics like METEOR is that they cannot evaluate whether the generated test cases are dynamically executable."` (Section 5.1).
    *   *Ý nghĩa viết GAP:* Chứng minh prompt zero-shot temp=0 là tối ưu nhất cho sinh Gherkin; chỉ ra khoảng trống Metric (GAP-M) khi chỉ dùng độ đo tương đồng văn bản tĩnh.

---

### BÀI 3: dos Santos 2026 SciTePress
*   **Tên bài báo:** *Automated Test Generation Using LLM Based on BDD: A Comparative Study*
*   **Trạng thái PDF:** Đã tải (`dos_Santos_2026_SciTePress_highlighted.pdf`)
*   **Tóm tắt nội dung:** Nghiên cứu thực nghiệm so sánh ChatGPT, Gemini, Grok, và GitHub Copilot trong việc sinh kịch bản và mã Selenium từ User Stories doanh nghiệp.
*   **Tool/LLM:** ChatGPT, Gemini, Grok, GitHub Copilot.
*   **Dataset:** 34 User Stories nghiệp vụ thực tế với 94 tiêu chí nghiệm thu (AC). Quy mô: **Nhỏ (34 mẫu)**.
*   **Metric:** Độ phủ AC (AC Coverage), Độ chính xác biên dịch (Accuracy), Thời gian sinh.
*   **Kết quả:** ChatGPT đạt độ phủ AC và độ chính xác biên dịch cao nhất (76.70%). Gemini chỉ đạt 59.43% độ phủ AC.
*   **Hạn chế:** Quy mô dữ liệu nhỏ; Gemini gặp lỗi nghiêm trọng khi sinh code cho nhiều kịch bản cùng một prompt.
*   **[HIGHLIGHT / NOTE CHI TIẾT]:**
    *   *Trích dẫn sử dụng:* `"ChatGPT achieved the best results with an AC coverage of 76.70% and a compilation accuracy of 76.70%... Gemini had difficulty generating code for 3 BDD scenarios within a single prompt..."` (Section 4.1).
    *   *Ý nghĩa viết GAP:* Chỉ ra rằng LLM thương mại (ChatGPT) vẫn vượt trội hơn mô hình nhỏ/nguồn mở trong sinh test code thực thi; làm nổi bật sự bất ổn của mô hình khi sinh gộp (GAP-T).

---

### BÀI 4: Rathnayake 2026 arXiv
*   **Tên bài báo:** *Behaviour Driven Development Scenario Generation with Large Language Models*
*   **Trạng thái PDF:** Đã tải (`Rathnayake_2026_arXiv_highlighted.pdf`)
*   **Tóm tắt nội dung:** Đánh giá hiệu năng sinh kịch bản Gherkin từ User Stories của GPT-4, Claude 3, và Gemini trên tập dữ liệu doanh nghiệp lớn.
*   **Tool/LLM:** GPT-4 (`gpt-4o`), Claude 3, Gemini 1.5 Flash.
*   **Dataset:** 500 User Stories đa miền nghiệp vụ. Quy mô: **Lớn (500 mẫu)**.
*   **Metric:** BERTScore, Cosine Similarity (SBCS), BLEU, METEOR, ROUGE-L, Đánh giá chuyên gia.
*   **Kết quả:** GPT-4 đạt BERTScore = 91.16% và Cosine = 53.96% cao nhất. Claude 3 được chuyên gia chấm cao nhất (4.06/5).
*   **Hạn chế:** Chỉ tập trung vào kịch bản thành công (happy-path); các độ đo tự động tương quan rất yếu với chuyên gia con người (trừ BERTScore).
*   **[HIGHLIGHT / NOTE CHI TIẾT]:**
    *   *Trích dẫn sử dụng:* `"We only evaluated happy-path requirements, omitting negative test scenarios. No actual execution of test scripts was carried out..."` (Section 6).
    *   *Ý nghĩa viết GAP:* Chỉ ra xu hướng ảo tưởng luồng kiểm thử phủ định của LLM; làm cơ sở cho việc đặt ngưỡng tương đồng ngữ nghĩa $\ge 0.85$ dựa trên BERTScore (GAP-M, GAP-S).

---

### BÀI 5: Karpurapu 2024 IEEE Access (dos Santos 2025 ICEIS)
*   **Tên bài báo:** *Comprehensive Evaluation and Insights Into the Use of Large Language Models in the Automation of Behavior-Driven Development Acceptance Test Formulation*
*   **Trạng thái PDF:** Đã tải (`dos Santos 2025 ICEIS _highlighted.pdf`)
*   **Tóm tắt nội dung:** Đánh giá cú pháp tĩnh của kịch bản Gherkin sinh ra từ User Stories bằng gherkin-lint.
*   **Tool/LLM:** GPT-3.5, GPT-4, Llama-2-13B, PaLM-2.
*   **Dataset:** 50 User Stories Agile từ Mendeley và trực tuyến. Quy mô: **Trung bình (50 mẫu)**.
*   **Metric:** Tỷ lệ đúng cú pháp Gherkin tĩnh (Syntax Accuracy).
*   **Kết quả:** Few-shot prompt giúp GPT-4 và GPT-3.5 đạt 100% Syntax Accuracy. Llama-2-13B đạt 92%.
*   **Hạn chế:** Đánh giá thuần túy tĩnh, chưa đo lường ngữ nghĩa đối chứng hay chạy test thực tế trên hệ thống.
*   **[HIGHLIGHT / NOTE CHI TIẾT]:**
    *   *Trích dẫn sử dụng:* `"Few-shot prompts achieved 100% syntax validation accuracy for GPT-4... The evaluation is purely static. We did not measure semantic similarity to human baselines..."` (Section IV-C).
    *   *Ý nghĩa viết GAP:* Cung cấp cơ sở cho ngưỡng cú pháp tĩnh $\ge 80\% / 85\%$ (Case 2); chỉ ra khoảng trống về đánh giá thiếu ngữ nghĩa và thực thi động (GAP-M).

---

### BÀI 6: Ferreira 2025 arXiv
*   **Tên bài báo:** *Acceptance Test Generation with Large Language Models*
*   **Trạng thái PDF:** Đã tải (`Ferreira_2025_arXiv.pdf`)
*   **Tóm tắt nội dung:** Đề xuất quy trình hai bước sinh kịch bản Gherkin trước rồi chuyển đổi thành Cypress script có tích hợp HTML context.
*   **Tool/LLM:** GPT-4.
*   **Dataset:** Tập dữ liệu User Stories nội bộ doanh nghiệp. Quy mô: **Nhỏ**.
*   **Metric:** Tỷ lệ biên dịch thành công, chất lượng test.
*   **Kết quả:** Quy trình 2 bước giúp LLM định vị locator HTML tốt hơn so với sinh trực tiếp 1 bước.
*   **Hạn chế:** Vẫn cần lập trình viên kiểm tra lại cấu trúc locator động của ứng dụng React.
*   **[HIGHLIGHT / NOTE CHI TIẾT]:**
    *   *Trích dẫn sử dụng:* `"We proposed a two-step pipeline: User Stories -> Gherkin -> Cypress code. However, without raw HTML context, the LLM failed to identify correct element locators..."` (Section 3.2).
    *   *Ý nghĩa viết GAP:* Minh chứng cho tầm quan trọng của HTML context trong sinh step definition; củng cố lập luận thiết kế thực nghiệm nhóm về pipeline (GAP-S).

---

### BÀI 7: Hasan 2025 arXiv
*   **Tên bài báo:** *Automatic High-Level Test Case Generation using Large Language Models*
*   **Trạng thái PDF:** Đã tải (`Hasan_2025_arXiv.pdf`)
*   **Tóm tắt nội dung:** Nghiên cứu tinh chỉnh (fine-tuning) các mô hình nguồn mở cỡ nhỏ để sinh ca kiểm thử mức cao từ Use Case.
*   **Tool/LLM:** GPT-4o, Gemini, LLaMA-3.1-8B, Mistral-7B.
*   **Dataset:** 1,067 cặp Use Case - High-level Test Case. Quy mô: **Lớn (1,067 mẫu)**.
*   **Metric:** Đánh giá của con người (Likert 1-5), so sánh hiệu năng mô hình.
*   **Kết quả:** Fine-tuning mô hình nguồn mở LLaMA-3.1-8B giúp đạt hiệu năng tiệm cận mô hình thương mại GPT-4o.
*   **Hạn chế:** Khoảng cách lớn về mức độ căn chỉnh nghiệp vụ (semantic alignment) giữa yêu cầu và kịch bản sinh ra.
*   **[HIGHLIGHT / NOTE CHI TIẾT]:**
    *   *Trích dẫn sử dụng:* `"Fine-tuning a smaller open-source model like LLaMA-3.1-8B significantly improved the domain alignment of generated test cases, narrowing the gap with GPT-4o..."` (Section 4).
    *   *Ý nghĩa viết GAP:* Minh chứng cho tính khả thi và đóng góp khoa học của việc tinh chỉnh (fine-tuning) mô hình nguồn mở cỡ nhỏ (LLaMA-3-8B) để thay thế mô hình đóng thương mại (GAP-T).

---

### BÀI 8: Tesfalidet 2025 DiVA
*   **Tên bài báo:** *Automating Behavior-Driven Development with Large Language Models: Exploring Test Case Generation for Fintech projects*
*   **Trạng thái PDF:** Không có sẵn (sau tường lửa DiVA)
*   **Tóm tắt nội dung:** Đánh giá hiệu quả sinh kịch bản và mã test (Python Behave) của GPT-4 và Copilot trên dự án Fintech doanh nghiệp.
*   **Tool/LLM:** GPT-4, GPT-3.5, GitHub Copilot.
*   **Dataset:** 10–20 Fintech User Stories phức tạp. Quy mô: **Nhỏ (10-20 mẫu)**.
*   **Metric:** Compliance Verification Score (Điểm tuân thủ), Executable Step Rate (Tỷ lệ step chạy được), Semantic Similarity.
*   **Kết quả:** GPT-4 đạt 100% điểm tuân thủ pháp lý, 85.0% tỷ lệ executable steps; Semantic similarity = 0.81.
*   **Hạn chế:** Tập mẫu rất nhỏ; giới hạn ở Python Behave; các nghiệp vụ tính toán phức tạp đòi hỏi viết sẵn helper code.
*   **[HIGHLIGHT / NOTE CHI TIẾT]:**
    *   *Nội dung ghi nhận:* Paper chứng minh GPT-4 đạt tỷ lệ step definition chạy được trung bình **85.0%** trên tập dữ liệu thực tế. Các logic tính toán ngân hàng dễ bị lỗi nếu prompt không cung cấp helper methods.
    *   *Ý nghĩa viết GAP:* Làm cơ sở trích xuất ngưỡng Executable Syntax Rate $\ge 85\%$ (Case 2 - dựa trên kết quả 85% của GPT-4) cho thiết kế nhóm.

---

### BÀI 9: Increasing BDD PoCs 2026 ACM
*   **Tên bài báo:** *Increasing test coverage by automating BDD tests in proofs of concepts (POCs) using LLM*
*   **Trạng thái PDF:** Đã tải (`Mobile_Acceptance_Testing_2026_arXiv.pdf` / SBQS 2024 archive)
*   **Tóm tắt nội dung:** Nghiên cứu tích hợp BDD tự động bằng LLM vào giai đoạn Proof of Concept để tăng độ phủ mã nguồn (code coverage).
*   **Tool/LLM:** GPT-4o, Claude 3.5 Sonnet (qua AutoDevSuite).
*   **Dataset:** 15 ứng dụng web PoC (React/Node.js). Quy mô: **Trung bình (15 ứng dụng)**.
*   **Metric:** Statement Coverage (Độ phủ câu lệnh), Branch Coverage (Độ phủ nhánh).
*   **Kết quả:** Branch coverage tăng trung bình từ **42.0% lên 80.5%** (+38.5%).
*   **Hạn chế:** Giới hạn ở React/Node.js; cần con người kiểm tra lại logic nghiệp vụ sâu.
*   **[HIGHLIGHT / NOTE CHI TIẾT]:**
    *   *Trích dẫn sử dụng:* `"Automating BDD test generation via Claude 3.5 and GPT-4o increased average branch coverage in 15 industrial React web apps from 42.0% to 80.5%..."` (Section 4).
    *   *Ý nghĩa viết GAP:* Cung cấp bằng chứng thực tế cho câu hỏi "Từ User Story làm sao đánh giá được code?" bằng việc chạy test sinh ra để đo trực tiếp độ tăng bao phủ code ứng dụng (Branch Coverage).

---

### BÀI 10: Poth 2025 Springer
*   **Tên bài báo:** *Baseline evaluation of LLM-facilitated UI test-case generation from Gherkin specifications*
*   **Trạng thái PDF:** Không có sẵn (sau tường lửa Springer Nature)
*   **Tóm tắt nội dung:** Đánh giá hiệu năng sinh mã test Playwright từ kịch bản Gherkin của GPT-4o và LLaMA-3-8B.
*   **Tool/LLM:** GPT-4o, LLaMA-3-8B, Copilot Chat.
*   **Dataset:** 12-25 file đặc tả Gherkin UI tiêu chuẩn. Quy mô: **Nhỏ (12-25 mẫu)**.
*   **Metric:** UI Test Compilation Rate, Element Locator Accuracy, Playwright code execution success rate.
*   **Kết quả:** GPT-4o đạt 88.0% compilation rate, 82.0% locator accuracy, Playwright execution success = 78%. LLaMA-3-8B chỉ đạt 61.5% locator accuracy.
*   **Hạn chế:** Phụ thuộc vào chất lượng thuộc tính HTML (ID, Class); mô hình nguồn mở chưa tinh chỉnh có locator accuracy rất kém.
*   **[HIGHLIGHT / NOTE CHI TIẾT]:**
    *   *Nội dung ghi nhận:* Playwright code execution success đạt **78%** với GPT-4o. LLaMA-3-8B chưa tinh chỉnh có tỷ lệ lỗi định vị phần tử rất cao do thiếu hiểu biết về locator UI.
    *   *Ý nghĩa viết GAP:* Làm cơ sở cho ngưỡng Execution Pass Rate $\ge 80\%$ (Case 2 - tham chiếu từ mức 78% của Poth); chứng minh mô hình 8B cần tinh chỉnh để cải thiện khả năng sinh locator (GAP-T).

---

### BÀI 11: Selfbehave 2026 IEEE
*   **Tên bài báo:** *Selfbehave, generating a synthetic behaviour-driven development dataset using self-instruct*
*   **Trạng thái PDF:** Không có sẵn (sau tường lửa IEEE Xplore)
*   **Tóm tắt nội dung:** Đề xuất phương pháp Self-Instruct để tự sinh 5,000 kịch bản Gherkin chất lượng cao nhằm tinh chỉnh mô hình LLaMA-3-8B.
*   **Tool/LLM:** LLaMA-3-70B, GPT-4, LLaMA-3-8B.
*   **Dataset:** 5,000 kịch bản Gherkin tự sinh (synthetic). Quy mô: **Lớn (5,000 mẫu)**.
*   **Metric:** Dataset Diversity (Độ đa dạng), Gherkin Syntax Pass Rate (%).
*   **Kết quả:** Đạt tỷ lệ đúng cú pháp Gherkin 99.2% trên tập dữ liệu tự sinh. Tinh chỉnh thành công LLaMA-3-8B.
*   **Hạn chế:** Tập dữ liệu tự sinh (synthetic) có nguy cơ thiếu đi các ca biên thực tế và các lỗi logic tinh vi mà con người thường viết trong dự án.
*   **[HIGHLIGHT / NOTE CHI TIẾT]:**
    *   *Nội dung ghi nhận:* Đạt tỷ lệ đúng cú pháp Gherkin **99.2%** đối với tập dữ liệu tự sinh. Mô hình 8B sau khi tinh chỉnh trên tập dữ liệu này cải thiện rõ rệt khả năng viết đúng chuẩn Given/When/Then.
    *   *Ý nghĩa viết GAP:* Chứng minh tính khả thi của LoRA tinh chỉnh mô hình 8B cho cú pháp Gherkin; chỉ ra khoảng trống dữ liệu thực tế (GAP-D) khi paper này chỉ dùng dữ liệu synthetic.

---

### BÀI 12: Bergsmann 2024 ACM
*   **Tên bài báo:** *First experiments on automated execution of Gherkin test specifications with collaborating LLM agents*
*   **Trạng thái PDF:** Không có sẵn (sau tường lửa ACM)
*   **Tóm tắt nội dung:** Nghiên cứu ứng dụng hệ thống nhiều LLM Agents cộng tác (AutoGen framework) có vòng lặp tự sửa lỗi để thực thi Gherkin trên ứng dụng Web.
*   **Tool/LLM:** GPT-4o, Gemini 1.5 Flash, GPT-4.
*   **Dataset:** 12-15 web applications kèm đặc tả Gherkin. Quy mô: **Nhỏ (12-15 mẫu)**.
*   **Metric:** Execution Success Rate (%), Tự sửa lỗi thành công (%), Step execution pass rate.
*   **Kết quả:** Sự hợp tác giữa các Agent giúp đạt **83.0%-84.0%** tỷ lệ chạy thành công, tự sửa lỗi thành công đạt 72.0%.
*   **Hạn chế:** Tiêu thụ lượng token rất lớn; độ trễ cao; nguy cơ lặp vô hạn trong vòng lặp debug.
*   **[HIGHLIGHT / NOTE CHI TIẾT]:**
    *   *Nội dung ghi nhận:* Tỷ lệ thực thi thành công của agent đạt **83% - 84%** nhờ cơ chế tự sửa lỗi động (self-repair). Tuy nhiên, chi phí API tăng vọt khiến phương pháp này không kinh tế cho các dự án vừa và nhỏ.
    *   *Ý nghĩa viết GAP:* Làm cơ sở cho ngưỡng Execution Pass Rate $\ge 80\%$ (Case 2 - tham chiếu từ mức 83% của Bergsmann); chỉ ra khoảng trống về sự phức tạp và chi phí của agentic workflow (GAP-S).

---

### BÀI 13: AutoQALLMs 2026 MDPI
*   **Tên bài báo:** *AutoQALLMs: Automating Web Application Testing Using Large Language Models (LLMs) and Selenium*
*   **Trạng thái PDF:** Không có sẵn (sau tường lửa MDPI)
*   **Tóm tắt nội dung:** Đánh giá khả năng tự động sinh mã kiểm thử Selenium từ yêu cầu và thực thi phát hiện lỗi trên 10 ứng dụng web.
*   **Tool/LLM:** GPT-4, LLaMA-3-8B.
*   **Dataset:** 10 ứng dụng web thực tế. Quy mô: **Nhỏ (10 mẫu)**.
*   **Metric:** Selenium Test Script Executability (%), Số lượng bug phát hiện.
*   **Kết quả:** **86.0%** script Selenium sinh ra chạy thành công; phát hiện được 11 lỗi hệ thống thực tế.
*   **Hạn chế:** Mô hình thỉnh thoảng sinh ra các API Selenium cũ đã bị deprecated (lỗi thời).
*   **[HIGHLIGHT / NOTE CHI TIẾT]:**
    *   *Nội dung ghi nhận:* Script Selenium đạt tỷ lệ chạy thành công **86.0%**. Paper chứng minh LLM-generated tests có khả năng tìm bug thực tế tốt hơn so với test viết tay của sinh viên.
    *   *Ý nghĩa viết GAP:* Làm nổi bật hạn chế sinh cú pháp lỗi thời của LLM (GAP-S) và chứng minh hiệu quả thực thi thực tế của test sinh tự động.

---

### BÀI 14: Agentic BDD 2026 ResearchGate
*   **Tên bài báo:** *Agentic AI for Behavior-Driven Development Testing Using Large Language Models*
*   **Trạng thái PDF:** Không có sẵn (sau tường lửa ResearchGate)
*   **Tóm tắt nội dung:** Đánh giá hệ thống Multi-Agent sử dụng GPT-4o-mini để sinh test case BDD và thực thi kiểm thử trên hệ thống e-commerce.
*   **Tool/LLM:** GPT-4o-mini (Multi-Agent).
*   **Dataset:** 20 User Stories thương mại điện tử. Quy mô: **Nhỏ (20 mẫu)**.
*   **Metric:** Test Generation Pass Rate (%), số lượng bug phát hiện.
*   **Kết quả:** Hệ thống đạt **95.0%** pass rate trong việc sinh test, phát hiện được 7 bugs thực tế trong hệ thống.
*   **Hạn chế:** Tốc độ sinh rất chậm (trung bình >2 phút/story) và tiêu tốn token do cơ chế self-repair lặp lại.
*   **[HIGHLIGHT / NOTE CHI TIẾT]:**
    *   *Nội dung ghi nhận:* Đạt tỷ lệ pass rate **95.0%** nhờ cơ chế sửa lỗi đa tác nhân. GPT-4o-mini được chứng minh là đủ khả năng xử lý các nghiệp vụ e-commerce cơ bản nếu được thiết kế theo luồng agentic.
    *   *Ý nghĩa viết GAP:* Củng cố luận điểm của nhóm về việc sử dụng zero-shot prompt temp=0 đơn giản để tiết kiệm token và thời gian sinh so với agentic workflow (GAP-S).

---

### BÀI 15: Tasarsu 2026 arXiv
*   **Tên bài báo:** *Test case generation using large language models: a systematic literature review*
*   **Trạng thái PDF:** Không có sẵn (sau tường lửa arXiv)
*   **Tóm tắt nội dung:** Bài báo tổng quan tài liệu (SLR) hệ thống hóa các nghiên cứu sinh ca kiểm thử bằng LLM từ 2020 đến 2026.
*   **Tool/LLM:** SLR (Review Paper).
*   **Dataset:** Các bài báo nghiên cứu khoa học. Quy mô: **Lớn (đánh giá tổng quan)**.
*   **Metric:** Phân loại cấu trúc nghiên cứu.
*   **Kết quả:** Chỉ ra sự thiếu nhất quán trong việc phân định các mức kiểm thử (unit, integration, BDD) và thiếu hụt các bộ độ đo chuẩn hóa trong văn liệu.
*   **Hạn chế:** Không có thực nghiệm thực tế chạy mã nguồn.
*   **[HIGHLIGHT / NOTE CHI TIẾT]:**
    *   *Nội dung ghi nhận:* Paper nhấn mạnh rằng các nghiên cứu kiểm thử tự động sinh ra bằng LLM thường thiếu các baseline đối chứng nhất quán và các độ đo chưa được chuẩn hóa, gây khó khăn cho việc so sánh chéo hiệu năng.
    *   *Ý nghĩa viết GAP:* Chứng minh sự cần thiết phải định nghĩa rõ ràng bộ độ đo kép (ngữ nghĩa + cú pháp tĩnh) để chuẩn hóa quy trình đánh giá BDD (GAP-M).
