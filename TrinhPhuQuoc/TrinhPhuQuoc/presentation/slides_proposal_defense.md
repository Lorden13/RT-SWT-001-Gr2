# Slide Outline & Script: Proposal Defense (Week 6)

*   **Thời lượng thuyết trình tối đa:** 5 - 7 phút (Tổng thời gian dự tính dưới đây: ~5 phút 30 giây).
*   **Mục tiêu:** GV hỏi và phê duyệt đề cương thực nghiệm (Không thay đổi RQ/Metric/Threshold sau gate này).

---

## Slide 1: Tiêu đề & Thông tin nhóm (30 giây)
*   **Nội dung Slide:**
    *   **Research Proposal:** Co-generating BDD Gherkin Scenarios and Step Definitions from User Stories: A Comparative Evaluation of Fine-Tuned LLaMA-3-8B and GPT-4o
    *   **Nhóm:** [Tên/Mã Nhóm]
    *   **Thành viên:** [Họ tên 1], [Họ tên 2], [Họ tên 3], [Họ tên 4], [Họ tên 5]
    *   **Topic Code:** [RT-SWT-00X]
    *   **Ngày bảo vệ:** [YYYY-MM-DD]
*   **Kịch bản nói (Script):**
    "Kính chào Thầy/Cô và các bạn. Hôm nay nhóm chúng em xin phép bảo vệ đề cương nghiên cứu thực nghiệm với đề tài: 'Đồng sinh kịch bản Gherkin BDD và định nghĩa bước kiểm thử từ User Stories: Đánh giá đối chứng giữa mô hình LLaMA-3-8B tinh chỉnh và GPT-4o'."

---

## Slide 2: Problem Statement (60 giây)
*   **Nội dung Slide:**
    *   *Bối cảnh:* Viết kịch bản BDD và Step Definitions thủ công tốn thời gian, dễ lệch nghiệp vụ.
    *   *State of the art:* Các nghiên cứu (Rathnayake 2026, Fernandes 2025) đã tự động hóa sinh kịch bản nhưng phụ thuộc vào API đóng đắt đỏ (GPT-4/GPT-4o) và chưa giải quyết sinh đồng thời cả kịch bản và mã code thực thi.
    *   *GAP chính (GAP-T):* **Chưa có nghiên cứu đánh giá co-generation kịch bản Gherkin và Step Definitions bằng mô hình nguồn mở 8B tinh chỉnh trên User Stories thực tế.**
*   **Kịch bản nói (Script):**
    "Trong quy trình phát triển phần mềm hiện đại, việc sinh kiểm thử BDD thủ công từ User Stories rất tốn công sức. Các nghiên cứu đi trước tuy đã áp dụng LLM để sinh kịch bản nhưng lại phụ thuộc nặng vào API đóng đắt đỏ và chưa sinh đồng thời mã Step Definitions đi kèm. Từ đó, chúng em xác định khoảng trống công nghệ (GAP-T) là: Chưa có đánh giá về khả năng co-generation kịch bản và mã kiểm thử của mô hình nguồn mở 8B tinh chỉnh local trên User Stories thực tế để thay thế mô hình đóng bảo mật thông tin."

---

## Slide 3: Related Work - Bảng bằng chứng (45 giây)
*   **Nội dung Slide:**
    *   *Tổng quan bảng bằng chứng:* Tổng hợp từ N = 37 bài báo khoa học.

    | Paper | Tool/LLM | Dataset (size) | Metric | Kết quả chính |
    |:---|:---|:---|:---|:---|
    | **Rathnayake 2026** | GPT-4, Claude 3 | 500 Stories thực tế | Cosine SBCS, BERTScore | GPT-4 đạt tương đồng ngữ nghĩa cao nhất. |
    | **Selfbehave 2026** | LLaMA-3-8B, GPT-4 | 5,000 kịch bản tự sinh | Syntax Pass Rate | LLaMA-3-8B đạt 99.2% cú pháp Gherkin. |
    | **Fernandes 2025** | GPT-4o, Gemini | 10 ca kiểm thử | METEOR | Zero-shot cho kết quả tốt nhất. |
    | **Tesfalidet 2025** | GPT-4, GPT-3.5 | 10-20 fintech stories | Executable Step Rate | GPT-4 đạt 85% executable steps. |

*   **Kịch bản nói (Script):**
    "Để chứng minh khoảng trống nghiên cứu, nhóm đã tổng hợp bảng bằng chứng gồm 37 bài báo khoa học. Công trình của Rathnayake 2026 là nền tảng cung cấp bộ dữ liệu thực tế. Selfbehave 2026 chứng minh tính khả thi khi tinh chỉnh LLaMA-3-8B đạt 99.2% cú pháp Gherkin nhưng lại dùng dữ liệu tự sinh. Tesfalidet 2025 đạt 85% tỷ lệ thực thi trên tập mẫu fintech nhỏ."

---

## Slide 4: Research Questions & Hypotheses (60 giây) — *Slide quan trọng nhất*
*   **Nội dung Slide:**
    *   **Main RQ:** LLaMA-3-8B tinh chỉnh LoRA có khả năng đồng sinh kịch bản Gherkin và mã kiểm thử tương đồng ngữ nghĩa ($\ge 0.85$ Cosine) và đúng cú pháp tĩnh ($\ge 85\%$ Executable Rate) tương đương hoặc vượt trội GPT-4o không?
    *   **RQ1 (Semantic):** LLaMA-FT đạt Cosine Similarity $\ge 0.85$ so với Ground Truth?
        *   $H0_{1a}: \text{Median}(\text{Sim}_{\text{LLaMA-FT}}) \le 0.85$ | $H1_{1a}: \text{Median}(\text{Sim}_{\text{LLaMA-FT}}) > 0.85$
    *   **RQ2 (Syntax):** LLaMA-FT đạt Executable Syntax Rate $\ge 85\%$?
        *   $H0_{2a}: p_{\text{syntax\_LLaMA}} \le 0.85$ | $H1_{2a}: p_{\text{syntax\_LLaMA}} > 0.85$
    *   **RQ3 (Comparison):** Có sự khác biệt có ý nghĩa thống kê giữa LLaMA-FT và GPT-4o?
        *   $H0_{1b}: \text{Median}(\text{Sim}_{\text{LLaMA-FT}} - \text{Sim}_{\text{GPT-4o}}) = 0$
*   **Kịch bản nói (Script):**
    "Chúng em đặt ra 3 câu hỏi nghiên cứu. RQ1 đánh giá độ tương đồng ngữ nghĩa của LLaMA tinh chỉnh với ngưỡng 0.85 bằng phép kiểm Wilcoxon một mẫu. RQ2 đánh giá độ chính xác cú pháp tĩnh kép của mô hình tinh chỉnh với ngưỡng 85% bằng phép kiểm nhị thức Binomial Exact Test. RQ3 tiến hành so sánh đối chứng trực tiếp giữa LLaMA tinh chỉnh và GPT-4o sử dụng phép kiểm cặp Paired Wilcoxon."

---

## Slide 5: Experimental Pipeline (45 giây)
*   **Nội dung Slide:**
    *   *Sơ đồ luồng thực nghiệm:*
        User Stories (100 mẫu ngẫu nhiên) -> Prompt Template (Inference Temp = 0) -> Sinh đồng thời bằng GPT-4o vs LLaMA-3-8B (LoRA-FT) -> Regex Extraction -> Bộ kiểm định tĩnh kép (Gherkin Parser & Python AST) -> Executable Syntax Rate -> Tính Cosine Similarity bằng SBERT -> Phân tích thống kê (Wilcoxon & Binomial).
*   **Kịch bản nói (Script):**
    "Đây là sơ đồ quy trình thực nghiệm của nhóm. Dữ liệu User Stories đầu vào sau khi qua tiền xử lý sẽ được nạp vào prompt template chuẩn hóa. Cả hai mô hình sẽ thực thi sinh mã với cấu hình Temperature = 0 để đảm bảo tính tái lập. Kết quả đầu ra sẽ được tách bằng biểu thức chính quy Regex, đưa qua bộ kiểm định tĩnh kép Gherkin Parser và Python AST để tính tỷ lệ cú pháp. Chỉ các mẫu pass tĩnh mới được tiếp tục đo độ tương đồng ngữ nghĩa bằng SBERT và phân tích kiểm định."

---

## Slide 6: Dataset & Baseline (30 giây)
*   **Nội dung Slide:**
    *   **Dataset nguồn:** Bộ dữ liệu thực tế đa miền của Rathnayake et al. (2026) gồm 500 stories và kịch bản chuyên gia viết tay.
    *   **Dataset thực nghiệm:** Rút mẫu ngẫu nhiên không lặp **100 mẫu** từ tập dữ liệu nguồn.
    *   **Trạng thái truy cập:** Dataset đã được verify và lưu trữ local [x].
    *   **Baseline:** Mô hình đóng **GPT-4o** (`gpt-4o-2024-08-06`) zero-shot.
*   **Kịch bản nói (Script):**
    "Để tránh thiên kiến dữ liệu tự sinh, nhóm sử dụng bộ dữ liệu thực tế đa miền của Rathnayake 2026. Chúng em rút ngẫu nhiên không lặp 100 mẫu làm tập thực nghiệm. Bộ dữ liệu này đã được tải về máy local thành công. Baseline đối chứng là mô hình GPT-4o phiên bản mới nhất gọi qua API."

---

## Slide 7: Statistical Plan (30 giây)
*   **Nội dung Slide:**
    *   *Bảng kiểm định thống kê:*

    | Mục tiêu | Ngưỡng | Phép kiểm | Rationale |
    |:---|:---:|:---|:---|
    | **Tương đồng LLaMA-FT** | $\ge 0.85$ | One-sample Wilcoxon | Dữ liệu liên tục, phi chuẩn |
    | **Cú pháp LLaMA-FT** | $\ge 85\%$ | One-sample Binomial | Dữ liệu nhị phân PASS/FAIL |
    | **So sánh LLaMA vs. GPT** | Đối chứng | Paired Wilcoxon | Cặp mẫu phụ thuộc phi chuẩn |

    *   *Power Analysis:* Cỡ mẫu $N = 100$, độ lớn ảnh hưởng $d = 0.35$, đạt lực lượng mẫu $\beta \ge 0.80$ ở mức ý nghĩa $\alpha = 0.05$.
*   **Kịch bản nói (Script):**
    "Về mặt thống kê, nhóm sử dụng phép kiểm phi tham số Wilcoxon một mẫu để so sánh Cosine Similarity với ngưỡng 0.85, và phép kiểm nhị thức Binomial Exact Test cho Executable Syntax Rate với ngưỡng tỷ lệ 85%. Phép kiểm cặp Wilcoxon dùng để so sánh đối chứng trực tiếp hiệu năng hai mô hình. Với cỡ mẫu N = 100, chúng em đảm bảo độ tin cậy thống kê tối thiểu 80%."

---

## Slide 8: Threats to Validity (30 giây)
*   **Nội dung Slide:**
    *   **Internal Threat:** Sự khác biệt prompt template gây thiên lệch.
        *   *Mitigation:* Đồng nhất prompt template và cấu hình tham số cho cả 2 mô hình.
    *   **External Threat:** Bộ dữ liệu đơn miền không đại diện.
        *   *Mitigation:* Sử dụng dataset đa miền thực tế từ 4 dự án doanh nghiệp.
    *   **Construct Threat:** Cosine Similarity không khớp với đánh giá con người.
        *   *Mitigation:* Sử dụng mô hình nhúng SBERT đã được chứng minh có tương quan ngữ nghĩa rất cao.
*   **Kịch bản nói (Script):**
    "Đối với các mối đe dọa đến tính hợp lệ của nghiên cứu, nhóm đề xuất các hành động giảm thiểu cụ thể: đồng nhất cấu hình prompt để giảm thiểu đe dọa nội bộ; sử dụng dữ liệu đa miền thực tế cho đe dọa bên ngoài; và dùng mô hình nhúng SBERT có độ tương quan ngữ nghĩa cao để giải quyết đe dọa về độ đo."

---

## Slide 9: Timeline & Role Delegation (30 giây)
*   **Nội dung Slide:**
    *   **Phân công vai trò:**
        *   **PL (Project Lead):** [Tên PL] - Điều phối, review nhất quán đề cương.
        *   **DG (Data/Ground Truth):** [Tên DG] - Rút 100 mẫu, viết Related Work.
        *   **LR (LLM Runner):** [Tên LR] - Gọi API, chạy LLaMA local, log chi phí.
        *   **MS (Metrics/Stats):** [Tên MS] - Lập trình parser tĩnh, chạy kiểm định thống kê.
        *   **RW (Report Writer):** [Tên RW] - Viết báo cáo Threats, vẽ biểu đồ.
    *   **Timeline:**
        *   *Tuần 5-6:* Nộp Đề cương Proposal.
        *   *Tuần 7:* Chạy thực nghiệm Pilot (10% sample).
        *   *Tuần 8:* Chạy chính thức (100% sample) + Tính toán số liệu thống kê.
        *   *Tuần 9-10:* Viết báo cáo Walkthrough nghiệm thu + Slide báo cáo.
*   **Kịch bản nói (Script):**
    "Về mặt nhân sự, nhóm phân công cụ thể 5 vai trò theo chuẩn RBL-3, đảm bảo độc lập hoàn toàn giữa người chạy mô hình (LR) và người đo lường thống kê (MS). Lộ trình thực hiện dự kiến sẽ chạy Pilot thử nghiệm ở Tuần 7, chạy thực nghiệm chính thức ở Tuần 8, và hoàn thiện viết bài báo khoa học cùng slide nghiệm thu ở Tuần 9 và 10."

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
