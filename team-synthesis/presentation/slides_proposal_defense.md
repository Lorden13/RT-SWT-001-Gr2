# Slide Outline & Script: Proposal Defense (Week 6)

*   **Thời lượng thuyết trình tối đa:** 5 - 7 phút (Tổng thời gian dự tính dưới đây: ~5 phút 30 giây).
*   **Mục tiêu:** GV hỏi và phê duyệt đề cương thực nghiệm (Không thay đổi RQ/Metric/Threshold sau gate này).

---

## Slide 1: Tiêu đề & Thông tin nhóm (30 giây)
*   **Nội dung Slide:**
    *   **Research Proposal:** Evaluating Prompt Engineering Techniques for Automated BDD Test Generation from Connextra User Stories
    *   **Nhóm:** Group 2
    *   **Thành viên:** 
        1. Ngô Đình Khoa (SE196737)
        2. Trịnh Phú Quốc (SE190287)
        3. Trần Đăng Khoa (SE194398)
        4. Đặng Đỗ Cao Sang (SE193269)
        5. Đào Lý Phi Hùng (SE172826)
    *   **Topic Code:** RT-SWT-SE1905
    *   **Ngày bảo vệ:** 2026-06-18
*   **Kịch bản nói (Script):**
    "Kính chào Thầy/Cô và các bạn. Hôm nay nhóm chúng em xin phép bảo vệ đề cương nghiên cứu thực nghiệm với đề tài: 'Đánh giá các kỹ thuật Prompt Engineering trong sinh tự động BDD Test từ Connextra User Stories'."

---

## Slide 2: Problem Statement (60 giây)
*   **Nội dung Slide:**
    *   *Bối cảnh:* Viết kịch bản BDD và Step Definitions thủ công tốn thời gian, dễ xảy ra lỗi nghiệp vụ.
    *   *State of the art:* Các nghiên cứu (Rathnayake 2026, Fernandes 2025) đã tự động sinh kịch bản nhưng phụ thuộc vào API đóng đắt đỏ (GPT-4o) và chưa giải quyết bài toán sinh đồng thời cả kịch bản và mã code thực thi đi kèm.
    *   *GAP chính (GAP-T):* **Chưa có nhiều nghiên cứu đánh giá và so sánh các kỹ thuật Prompt Engineering (Zero-Shot, Few-Shot, Chain-of-Thought) trong bài toán đồng sinh Gherkin Scenarios và Python Step Definitions trên mô hình nguồn mở chạy cục bộ.**
*   **Kịch bản nói (Script):**
    "Trong quy trình phát triển phần mềm Agile, việc sinh kiểm thử BDD thủ công từ User Stories rất tốn công sức. Các nghiên cứu đi trước tuy đã áp dụng LLM để sinh kịch bản nhưng lại phụ thuộc nặng vào API đóng đắt đỏ và chưa sinh đồng thời mã Step Definitions thực thi. Từ đó, chúng em xác định khoảng trống công nghệ (GAP-T) là: Chưa có đánh giá so sánh hệ thống về các kỹ thuật Prompt Engineering như Zero-Shot, Few-Shot, và Chain-of-Thought cho tác vụ đồng sinh kịch bản và mã kiểm thử trên mô hình nguồn mở cục bộ."

---

## Slide 3: Related Work - Bảng bằng chứng (45 giây)
*   **Nội dung Slide:**
    *   *Tổng quan bảng bằng chứng:* Tổng hợp từ N = 37 bài báo khoa học liên quan.

    | Paper | Tool/LLM | Dataset (size) | Metric | Kết quả chính / Hạn chế |
    |:---|:---|:---|:---|:---|
    | **Rathnayake 2026** | GPT-4o (Zero-shot) | 500 Stories thực tế | Cosine, BERTScore | Đạt tương đồng ngữ nghĩa cao nhưng không sinh step definitions. |
    | **Fernandes 2025** | GPT-4, Llama-3, Gemini | 34 stories | METEOR | Chỉ sinh kịch bản Gherkin; cỡ mẫu nhỏ, đơn miền. |
    | **Selfbehave 2026** | LLaMA-3-8B (LoRA-FT) | Dữ liệu tự sinh | Tỷ lệ cú pháp tĩnh | Đạt 99.2% cú pháp Gherkin; phụ thuộc dữ liệu tự sinh. |
    | **Tesfalidet 2025** | GPT-4 | 10-20 stories | Executable Step Rate | Đạt 85% executable steps; thiếu bộ kiểm định tĩnh kép. |

*   **Kịch bản nói (Script):**
    "Để làm rõ khoảng trống nghiên cứu, nhóm đã tổng hợp bảng bằng chứng từ 37 bài báo khoa học. Công trình của Rathnayake 2026 cung cấp bộ dữ liệu thực tế lớn nhưng chưa sinh Step Definitions. Selfbehave 2026 chứng minh tính khả thi khi tinh chỉnh mô hình nguồn mở nhưng dùng dữ liệu tự sinh. Tesfalidet 2025 đạt 85% thực thi trên tập mẫu fintech rất nhỏ. Nhóm đề xuất nghiên cứu giải quyết các hạn chế này bằng cách đánh giá các kỹ thuật prompt trên mô hình nguồn mở chạy cục bộ."

---

## Slide 4: Research Questions & Hypotheses (60 giây) — *Slide quan trọng nhất*
*   **Nội dung Slide:**
    *   **Main RQ:** Liệu có sự khác biệt có ý nghĩa thống kê về Semantic Similarity và Executable Syntax Rate giữa các kỹ thuật Prompt Engineering (Zero-Shot, Few-Shot, Chain-of-Thought) khi áp dụng trên mô hình Qwen2.5-7B-Instruct hay không?
    *   **RQ1 (Semantic):** Kỹ thuật nào đạt Cosine Similarity $\ge 0.80$ so với Ground Truth?
        *   $H0_{1a/b/c}: \text{Median}(\text{Similarity}_{\text{Technique}}) \le 0.80$ | $H1_{1a/b/c}: \text{Median}(\text{Similarity}_{\text{Technique}}) > 0.80$
    *   **RQ2 (Syntax):** Kỹ thuật nào đạt Executable Syntax Rate $\ge 85\%$?
        *   $H0_{2a/b/c}: p_{\text{syntax\_Technique}} \le 0.85$ | $H1_{2a/b/c}: p_{\text{syntax\_Technique}} > 0.85$
    *   **RQ3 (Comparison):** Có sự khác biệt có ý nghĩa thống kê chéo giữa các kỹ thuật (Zero-Shot, Few-Shot, CoT)?
        *   *Ngữ nghĩa:* Phép kiểm Paired Wilcoxon ($H0_{3a/b/c}: \text{Median}(\Delta \text{Similarity}) = 0$).
        *   *Cú pháp:* Phép kiểm McNemar's Test ($H0_{3d/e/f}$: Không có sự khác biệt tỷ lệ).
*   **Kịch bản nói (Script):**
    "Chúng em đặt ra 3 câu hỏi nghiên cứu. RQ1 đánh giá độ tương đồng ngữ nghĩa của từng kỹ thuật prompt với ngưỡng 0.80 bằng phép kiểm Wilcoxon một mẫu. RQ2 đánh giá tỷ lệ đúng cú pháp tĩnh kép của từng kỹ thuật với ngưỡng 85% bằng phép kiểm nhị thức Binomial Exact Test. RQ3 tiến hành so sánh đối chứng chéo trực tiếp giữa các kỹ thuật prompt với nhau bằng phép kiểm cặp Wilcoxon cho ngữ nghĩa và phép kiểm McNemar cho cú pháp."

---

## Slide 5: Experimental Pipeline (45 giây)
*   **Nội dung Slide:**
    *   *Sơ đồ luồng thực nghiệm:*
        User Stories (100 mẫu ngẫu nhiên) -> Prompt Templates (Zero-Shot / Few-Shot / CoT) -> Qwen2.5-7B-Instruct (Temp = 0, Top_p = 1) -> Sinh đồng thời Gherkin (.feature) & Python Step-Defs (.py) -> Bộ kiểm định tĩnh kép (Gherkin Parser & Python AST) -> Executable Syntax Rate -> Đo Cosine Similarity bằng SBERT (`all-MiniLM-L6-v2`) -> Phân tích thống kê (Wilcoxon, Binomial, McNemar).
*   **Kịch bản nói (Script):**
    "Quy trình thực nghiệm của nhóm bắt đầu bằng việc nạp 100 User Stories đã lấy mẫu vào 3 template prompt tương ứng với 3 kỹ thuật. Mô hình Qwen2.5-7B-Instruct sẽ thực thi suy luận cục bộ với tham số Temperature = 0 để sinh đồng thời kịch bản Gherkin và Step Definitions. Đầu ra được đưa qua bộ lọc cú pháp kép Gherkin Parser và Python AST để tính tỷ lệ cú pháp khả thi. Các mẫu vượt qua bộ lọc cú pháp sẽ được đo độ tương đồng ngữ nghĩa bằng SBERT so với Ground Truth của chuyên gia và chạy kiểm định thống kê."

---

## Slide 6: Dataset & Model Configuration (30 giây)
*   **Nội dung Slide:**
    *   **Dataset nguồn:** Bộ dữ liệu thực tế đa miền của Rathnayake et al. (2026) gồm 500 stories và kịch bản chuyên gia viết tay.
    *   **Dataset thực nghiệm:** Rút mẫu ngẫu nhiên không lặp **100 mẫu** (seed = 42).
    *   **Mô hình thực nghiệm:** **Qwen2.5-7B-Instruct** chạy local qua Ollama.
    *   **Tham số cấu hình:** Temperature = 0, Top_p = 1 (Sinh tất định để đảm bảo tính tái lập).
*   **Kịch bản nói (Script):**
    "Để đảm bảo tính khách quan và khả năng tổng quát hóa, nhóm sử dụng bộ dữ liệu thực tế đa miền của Rathnayake 2026. Chúng em thực hiện rút mẫu ngẫu nhiên đơn giản không lặp 100 mẫu với seed = 42 để đảm bảo tính tái lập. Mô hình thực nghiệm được chọn là Qwen2.5-7B-Instruct chạy local, cấu hình temperature bằng 0 và top_p bằng 1 nhằm triệt tiêu tính bất định của văn bản sinh ra."

---

## Slide 7: Statistical Plan (30 giây)
*   **Nội dung Slide:**
    *   *Bảng kiểm định thống kê:*

    | Mục tiêu | Ngưỡng | Phép kiểm | Rationale |
    |:---|:---:|:---|:---|
    | **Tương đồng ngữ nghĩa (RQ1)** | $\ge 0.80$ | One-sample Wilcoxon | So sánh trung vị phân phối phi chuẩn với ngưỡng |
    | **Cú pháp khả thi (RQ2)** | $\ge 85\%$ | Binomial Exact Test | Kiểm định tỷ lệ nhị phân PASS/FAIL trên cỡ mẫu hữu hạn |
    | **So sánh cặp ngữ nghĩa (RQ3)** | Đối chứng | Paired Wilcoxon | So sánh cặp dữ liệu liên tục phi chuẩn từ cùng 100 mẫu |
    | **So sánh cặp cú pháp (RQ3)** | Đối chứng | McNemar's Test | So sánh tỷ lệ của hai mẫu nhị phân phụ thuộc |

    *   *Kích cỡ hiệu ứng (Effect Size):* Đo bằng Rank-Biserial Correlation cho các phép kiểm Wilcoxon.
*   **Kịch bản nói (Script):**
    "Về kế hoạch phân tích thống kê, chúng em sử dụng phép kiểm Wilcoxon một mẫu để so sánh điểm Cosine Similarity của từng kỹ thuật prompt với ngưỡng 0.80, và phép kiểm Binomial Exact Test để so sánh tỷ lệ cú pháp tĩnh với ngưỡng 85%. Để so sánh chéo giữa các kỹ thuật, phép kiểm Paired Wilcoxon được áp dụng cho ngữ nghĩa và phép kiểm McNemar cho cú pháp. Nhóm cũng sẽ báo cáo chỉ số Rank-Biserial Correlation để đo kích cỡ hiệu ứng thực tế."

---

## Slide 8: Threats to Validity (30 giây)
*   **Nội dung Slide:**
    *   **Internal Threat:** Thiên lệch trong thiết kế prompt và chọn ví dụ mẫu Few-Shot.
        *   *Mitigation:* Cố định prompt template chuẩn hóa; chọn ví dụ mẫu đa miền chuẩn BDD (Login, Cart).
    *   **External Threat:** Độ bao phủ của tập dữ liệu trên các miền nghiệp vụ khác.
        *   *Mitigation:* Sử dụng dataset thực tế đa miền từ 4 dự án doanh nghiệp lớn.
    *   **Construct Threat:** Độ đo ngữ nghĩa Cosine không phản ánh chính xác đánh giá của con người.
        *   *Mitigation:* Sử dụng SBERT `all-MiniLM-L6-v2` có tương quan ngữ nghĩa cao với con người; chạy bộ lọc cú pháp tĩnh trước khi tính tương đồng ngữ nghĩa.
*   **Kịch bản nói (Script):**
    "Đối với các mối đe dọa đến tính hợp lệ, nhóm đề xuất các biện pháp giảm thiểu tương ứng: Cố định template prompt và chọn ví dụ Few-Shot đa dạng để giảm đe dọa nội bộ; dùng dữ liệu đa miền thực tế từ doanh nghiệp cho đe dọa bên ngoài; và dùng mô hình nhúng SBERT kết hợp bộ lọc cú pháp tĩnh trước để giải quyết đe dọa về độ đo."

---

## Slide 9: Timeline & Role Delegation (30 giây)
*   **Nội dung Slide:**
    *   **Phân công vai trò:**
        *   **PL (Trần Đăng Khoa):** Project Lead - Điều phối tiến độ, rà soát tính nhất quán tài liệu.
        *   **DG (Ngô Đình Khoa):** Data & Ground Truth - Rút 100 mẫu, verify Ground Truth và Cleaned Outputs.
        *   **LR (Trịnh Phú Quốc):** LLM Runner - Cài đặt Qwen local, thiết kế prompt và chạy mô hình.
        *   **MS (Đặng Đỗ Cao Sang):** Metrics & Stats - Lập trình parser tĩnh kép, tính SBERT và chạy statistical test.
        *   **RW (Đào Lý Phi Hùng):** Report Writer - Viết Threats, vẽ chart, slide bảo vệ & nghiệm thu.
    *   **Timeline:**
        *   *Tuần 5-6:* Bảo vệ đề cương Proposal.
        *   *Tuần 7:* Thực nghiệm Pilot trên 10 mẫu (10%).
        *   *Tuần 8:* Thực nghiệm chính thức trên 100 mẫu.
        *   *Tuần 9:* Phân tích thống kê & kiểm định.
        *   *Tuần 10:* Viết báo cáo Walkthrough nghiệm thu và chuẩn bị bảo vệ cuối kỳ.
*   **Kịch bản nói (Script):**
    "Về mặt nhân sự, nhóm phân công cụ thể 5 vai trò theo chuẩn RBL-3, đảm bảo tính độc lập tuyệt đối giữa người chạy mô hình (LR) và người chạy thống kê (MS). Lộ trình thực hiện dự kiến sẽ chạy thử nghiệm Pilot trên 10 mẫu ở Tuần 7, chạy thực nghiệm chính thức ở Tuần 8, tiến hành phân tích thống kê ở Tuần 9 và hoàn thiện báo cáo walkthrough nghiệm thu cùng slide thuyết trình ở Tuần 10."

---

## Slide 10: Expected Contributions (20 giây)
*   **Nội dung Slide:**
    *   Chứng minh tính khả thi của mô hình local 8B tinh chỉnh LoRA trong tác vụ đồng sinh Gherkin và Step Definitions BDD bảo mật dữ liệu doanh nghiệp.
    *   Đóng góp một bộ độ đo kép tích hợp (Parser tĩnh + SBERT Cosine) để kiểm nghiệm đồng thời tính đúng đắn ngữ nghĩa và cú pháp của kịch bản sinh ra.
    *   Tạo tiền đề mở rộng nghiên cứu sang các mô hình local mới hơn hoặc quy trình tự sửa lỗi tự động (self-repair).
*   **Kịch bản nói (Script):**
    "Chúng em kỳ vọng nghiên cứu sẽ chứng minh được mô hình local 8B tinh chỉnh là giải pháp thay thế hoàn hảo cho API đóng thương mại, đồng thời đóng góp bộ độ đo kép tích hợp chuẩn hóa cho việc đánh giá tự động hóa kiểm thử BDD."

---

## Slide 11: Q&A (Trang trống)
*   **Kịch bản nói (Script):**
    "Em xin kết thúc phần thuyết trình bảo vệ đề cương của nhóm tại đây. Kính mong nhận được các câu hỏi chất vấn và ý kiến góp ý của Thầy/Cô để nhóm em hoàn thiện thiết kế nghiên cứu này. Em xin chân thành cảm ơn."
