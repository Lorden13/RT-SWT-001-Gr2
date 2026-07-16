# Full Run Walkthrough Report
**Nhóm:** RT-SWT-001-Gr2  
**Thành viên thực hiện:** Đào Lý Phi Hùng (SE172826) — Vai trò RW  
**Ngày:** 2026-07-16  
**Giai đoạn:** RBL-4 Full Run (Tuần 8)

---

## 1. Tổng quan Thực nghiệm
### Mục tiêu
Chạy thực nghiệm chính thức trên toàn bộ **100 mẫu (N=100)** để kiểm tra khả năng sinh Gherkin scenario + Selenium/Behave step definitions từ User Story bằng LLM, so sánh hiệu quả của 3 chiến lược prompting:

| Chiến lược | File kết quả |
|:---|:---|
| Zero-Shot | `results/full_zero_shot_100.csv` |
| Few-Shot | `results/full_few_shot_100.csv` |
| Chain-of-Thought (CoT) | `results/full_cot_100.csv` |

### Cấu hình thực nghiệm
- **Model:** `Qwen2.5-7B-Instruct`
- **Temperature:** `0` (deterministic — đảm bảo tái hiện kết quả)
- **Top_p:** `1`
- **Invalid outputs:** 0 / 300 calls
- **Input:** User Story (plain text)
- **Output mong đợi:** Gherkin scenario + Python step definitions (Behave/Selenium)
- **Dataset:** `data/sample_100.csv` (random seed: 42)

---

## 2. Kết quả Phân tích Thực nghiệm

### 2.1 Syntax Validity (Tính hợp lệ cú pháp Gherkin)
Kiểm tra sự hiện diện đầy đủ của 5 từ khóa bắt buộc: `Feature`, `Scenario`, `Given`, `When`, `Then`.

| Chiến lược | Valid Syntax | Tỷ lệ |
|:---|:---:|:---:|
| Zero-Shot | 100/100 | **100.00%** |
| Few-Shot | 100/100 | **100.00%** |
| CoT | 100/100 | **100.00%** |

> ✅ **Nhận xét:** Cả 3 chiến lược đều đạt 100% cú pháp Gherkin hợp lệ, chứng minh khả năng tuân thủ định dạng BDD rất tốt của mô hình Qwen2.5-7B-Instruct.

---

### 2.2 Metric chính (tính từ kết quả so khớp Gherkin-only)

| Metric | Zero-Shot | Few-Shot | CoT | Threshold | Đạt? |
|:---|:---:|:---:|:---:|:---:|:---:|
| Avg Cosine Similarity | 0.7995 | **0.8141** | **0.8100** | ≥ 0.80 | Few/CoT Đạt |
| AST Parse Rate | 100.00% | 100.00% | 99.00% | ≥ 85% | Tất cả Đạt |
| Wilcoxon p-value vs Few-Shot | 0.0034 ✅ | — | 0.3604 ❌ | < 0.05 | Có ý nghĩa (Few-Shot tốt hơn Zero-Shot) |
| Wilcoxon p-value Zero vs CoT | — | — | 0.1106 ❌ | < 0.05 | Không ý nghĩa |

> **Nhận xét kết quả:**
> - **Few-Shot** đạt điểm tương đồng ngữ nghĩa cao nhất ($0.8141$, $p = 0.0007$) và tỷ lệ AST pass tuyệt đối ($100.00\%$).
> - **CoT** đạt điểm ngữ nghĩa rất tốt ($0.8100$, $p = 0.0046$), nhưng có 1% mẫu (1 mẫu) bị lỗi cú pháp Step Definitions do mô hình tự ý chèn text mô tả bên trong block python.
> - **Zero-Shot** đạt điểm tương đồng ngữ nghĩa sát nút ($0.7995$, nhưng về mặt thống kê chưa đủ để bác bỏ giả thuyết không, $p = 0.0710$).
> - Phép kiểm định so sánh cặp (RQ3) chứng minh **Few-Shot hoạt động hiệu quả hơn hẳn Zero-Shot** với ý nghĩa thống kê ($p = 0.0034$), trong khi không có sự khác biệt có ý nghĩa thống kê rõ rệt giữa **Few-Shot và CoT** ($p = 0.3604$).

---

## 3. Quyết định & Bài học kinh nghiệm
- **Chiến lược tối ưu**: **Few-Shot prompting** là lựa chọn tối ưu nhất cho việc triển khai thực tế của doanh nghiệp vì nó đảm bảo tính hợp lệ cú pháp tuyệt đối (100%), đạt điểm ngữ nghĩa vượt ngưỡng kỳ vọng ($0.8141 \ge 0.80$), và tiêu thụ ít tài nguyên token hơn CoT.
- **Xử lý hậu kỳ**: Cần thiết lập bộ lọc regex để làm sạch mã nguồn Python sinh ra trước khi đưa vào chạy thử (đặc biệt là với CoT để loại bỏ các phần giải thích thừa).
- **Hạn chế**: Các hàm Python Step Definitions sinh ra có body rỗng (\texttt{pass}), do đó cần nghiên cứu thêm các giải pháp tự động sinh Selenium locator trong tương lai.

---

*Tài liệu này được tổng hợp bởi RW từ kết quả thực nghiệm chính thức. Model: Qwen2.5-7B-Instruct. Seed: 42, IAA = 0.85 (DG).*
