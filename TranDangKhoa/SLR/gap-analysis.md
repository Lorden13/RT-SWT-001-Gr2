# GAP Analysis

## Bảng GAP

| Cột | Phát hiện | Loại GAP | Phản chứng |
|-----|-----------|----------|-----------|
| Tool/LLM (GAP‑T) | Chỉ có một nghiên cứu (Bergsmann 2024) sử dụng Multi‑agent LLM; chưa có đánh giá zero‑shot trên các LLM đơn lẻ (GPT‑4o, Claude‑2, …) | GAP‑T | Kiểm tra literature: không tìm thấy bài báo nào đánh giá zero‑shot trên LLM đơn lẻ → phản chứng không tồn tại |
| Metric (GAP‑M) | Không có đo lường độ tương đồng ngữ nghĩa so với baseline expert | GAP‑M | Các paper không báo cáo Cosine Similarity / BLEU so với expert → phản chứng không có |
| Dataset (GAP‑D) | Chỉ 12 kịch bản Gherkin, quy mô nhỏ, không đa dạng miền | GAP‑D | Không có dataset lớn hơn 50 user‑story Connextra → phản chứng không có |
| Shared Limitation (GAP‑S) | Độ trễ điều phối, tiêu token cao (được báo cáo) | GAP‑S | Các paper đồng thuận về hạn chế này → phản chứng có nhưng không giải quyết |

## GAP Chính

**GAP‑T (Technology)** – Thiếu đánh giá zero‑shot trên các LLM đơn lẻ (GPT‑4o, Claude‑2, …). Đây là GAP chính vì việc mở rộng sang các mô hình mới là yếu tố quyết định tính khả thi và đóng góp mới.

## GAP Secondary

**GAP‑M (Metric)** – Thiếu đo lường độ tương đồng ngữ nghĩa (Cosine Similarity) so với baseline expert‑written. Đây là GAP phụ, hỗ trợ cho GAP‑T.

## Feasibility Check

| Tiêu chí | Mức |
|----------|-----|
| Dataset | ✅ Có sẵn 50 user‑story Connextra (tự thu thập) → mức trung bình |
| Tool/API | ✅ GPT‑4o (zero‑shot) có sẵn qua OpenAI API → mức thấp |
| Compute | ✅ GPU/CPU tiêu chuẩn, chi phí token 1 200/token → mức trung bình |
| Ground Truth | ✅ Expert‑written baseline đã có trong literature → mức thấp |
| Skills | ✅ Nhóm có kinh nghiệm LLM & Gherkin → mức thấp |
| Thời gian | ✅ 5‑6 giờ cho thiết kế + chạy thí nghiệm → mức trung bình |
| Contribution | ✅ Đóng góp mới về zero‑shot và metric mới → mức cao |

---

## BỔ SUNG THEO RBL-2 - Phản chứng chi tiết

GAP tuyên bố: Chưa có paper nào đánh giá GPT-4o zero-shot đơn lẻ cho sinh đồng thời Gherkin scenarios và step definitions từ Connextra user stories bằng cả semantic similarity và executable syntax rate.

| Paper | Đã làm chưa? | Ghi chú |
|---|---|---|
| Bergsmann 2024 | Không | Multi-agent GPT-4, không GPT-4o zero-shot đơn lẻ. |
| Comparative Study of LLMs for Gherkin | Một phần | Có GPT-4o và cosine nhưng chưa step definitions. |
| Automated Test Generation Based on BDD | Một phần | Có compilation rate nhưng chưa expert semantic baseline. |
| Industrial Case Study | Không | GPT-4, logistics requirements, không Connextra multi-domain. |
| AutoQALLMs | Một phần | Có Selenium executability nhưng chưa đánh giá semantic similarity với expert baseline. |

**GAP chính giữ lại:** GAP-T.

**GAP secondary giữ lại:** GAP-M với metric kép cosine similarity >= 0.85 và executable syntax rate >= 80%.
