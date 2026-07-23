# Full Run Walkthrough Report
**Nhóm:** RT-SWT-001-Gr2  
**Thành viên thực hiện:** Đào Lý Phi Hùng (SE172826) — Vai trò RW  
**Ngày:** 2026-07-19  
**Giai đoạn:** RBL-4 Full Run (Tuần 8) - N=500

---

## 1. Tổng quan Thực nghiệm
### Mục tiêu
Chạy thực nghiệm chính thức trên toàn bộ **500 mẫu (N=500)** để kiểm tra khả năng sinh Gherkin scenario + Selenium/Behave step definitions từ User Story bằng LLM, so sánh hiệu quả của 3 chiến lược prompting:

| Chiến lược | File kết quả |
|:---|:---|
| Zero-Shot | `results/full_zero_shot_500.csv` |
| Few-Shot | `results/full_few_shot_500.csv` |
| Chain-of-Thought (CoT) | `results/full_cot_500.csv` |

### Cấu hình thực nghiệm
- **Model:** `Qwen2.5-7B-Instruct`
- **Temperature:** `0` (deterministic — đảm bảo tái hiện kết quả)
- **Top_p:** `1`
- **Invalid outputs:** 0 / 1500 calls
- **Input:** User Story (plain text)
- **Output mong đợi:** Gherkin scenario + Python step definitions (Behave/Selenium)
- **Dataset:** `data/full_ground_truth.csv` (random seed: 42)

---

## 2. Kết quả Phân tích Thực nghiệm

### 2.1 Syntax Validity (Tính hợp lệ cú pháp Gherkin)
Kiểm tra sự hiện diện đầy đủ của 5 từ khóa bắt buộc: `Feature`, `Scenario`, `Given`, `When`, `Then`.

| Chiến lược | Valid Syntax | Tỷ lệ |
|:---|:---:|:---:|
| Zero-Shot | 500/500 | **100.00%** |
| Few-Shot | 500/500 | **100.00%** |
| CoT | 500/500 | **100.00%** |

> ✅ **Nhận xét:** Cả 3 chiến lược đều đạt 100% cú pháp Gherkin hợp lệ, chứng minh khả năng tuân thủ định dạng BDD rất tốt của mô hình Qwen2.5-7B-Instruct.

---

### 2.2 Metric chính (tính từ kết quả so khớp Gherkin-only)

| Metric | Zero-Shot | Few-Shot | CoT | Threshold | Đạt? |
|:---|:---:|:---:|:---:|:---:|:---:|
| Avg Cosine Similarity | 0.8088 | **0.8218** | **0.8168** | ≥ 0.80 | Tất cả Đạt |
| AST Parse Rate | 99.80% | 100.00% | 100.00% | ≥ 85% | Tất cả Đạt |
| Wilcoxon p-value vs Few-Shot | 0.0000 ✅ | — | 0.0105 ✅ | < 0.05 | Có ý nghĩa (Few-Shot tốt nhất) |
| Wilcoxon p-value Zero vs CoT | — | — | 0.0002 ✅ | < 0.05 | Có ý nghĩa (CoT tốt hơn Zero) |

> **Nhận xét kết quả:**
> - **Cả 3 kỹ thuật** đều đạt điểm tương đồng ngữ nghĩa trung bình vượt mốc chất lượng tối thiểu $0.80$ có ý nghĩa thống kê ($p = 0.0000$). Khi cỡ mẫu tăng từ $N=100$ lên $N=500$, sức mạnh thống kê tăng lên giúp khẳng định Zero-Shot cũng vượt ngưỡng một cách đáng tin cậy.
> - **Few-Shot** đạt điểm tương đồng ngữ nghĩa cao nhất ($0.8218$, $p = 0.0000$) và tỷ lệ AST pass tuyệt đối ($100.00\%$).
> - **CoT** đạt điểm ngữ nghĩa rất tốt ($0.8168$) và cũng đạt tỷ lệ AST pass tuyệt đối ($100.00\%$) trên 500 mẫu.
> - Phép kiểm định so sánh cặp (RQ3) chứng minh **Few-Shot hoạt động hiệu quả hơn rõ rệt so với cả Zero-Shot ($p = 0.0000$) và CoT ($p = 0.0105$)** với ý nghĩa thống kê.

---

## 3. Quyết định & Bài học kinh nghiệm
- **Chiến lược tối ưu**: **Few-Shot prompting** tiếp tục là lựa chọn số 1 vì nó tối ưu chất lượng ngữ nghĩa ($0.8218$), cú pháp tuyệt đối ($100\%$) và tiết kiệm chi phí token/thời gian chạy so với CoT.
- **Xử lý hậu kỳ**: Với Zero-Shot, mô hình thỉnh thoảng (1/500 mẫu) bị cắt cụt (truncation) do giới hạn max tokens, gây lỗi cú pháp. Do đó, việc áp dụng Few-Shot giúp kiểm soát cấu trúc đầu ra tốt hơn, ngăn ngừa hiện tượng cắt cụt này.
- **Hạn chế**: Các hàm Python Step Definitions sinh ra có body rỗng (\texttt{pass}), do đó cần nghiên cứu thêm các giải pháp tự động sinh Selenium locator trong tương lai.

---

*Tài liệu này được tổng hợp bởi RW từ kết quả thực nghiệm chính thức. Model: Qwen2.5-7B-Instruct. Seed: 42, IAA = 0.85 (DG).*
