# Walkthrough Report — Full Experiment
**Nhóm:** RT-SWT-001-Gr2  
**Thành viên:** Đào Lý Phi Hùng (SE172826) — Vai trò RW  
**Ngày:** 2026-07-21  
**Phạm vi:** Tổng hợp kết quả Pilot + Full Run (RBL-4)

---

## 1. Tổng quan thực nghiệm

| Giai đoạn | Ngày | Model | N | Invalid |
|:---|:---:|:---:|:---:|:---:|
| Pilot | 2026-07-13 | GPT-4o | 20/strategy | 0/60 |
| Full Run | 2026-07-19 | GPT-4o | 500/strategy | 0/1500 |

**Cấu hình:** Temperature=0, 3 strategies: Zero-Shot / Few-Shot / CoT  
**Dataset:** 100 User Stories × 5 scenarios = 500 mẫu  
**Ground truth:** `data/full_ground_truth.csv` — Manual Scenario do chuyên gia viết

---

## 2. Kết quả Full Run (N=500/strategy)

### 2.1 Syntax Validity

| Chiến lược | Valid | Tỷ lệ |
|:---|:---:|:---:|
| Zero-Shot | 500/500 | **100%** |
| Few-Shot | 496/500 | **99.2%** |
| CoT | 500/500 | **100%** |

> 4 mẫu Few-Shot thiếu `When` — ghi nhận trong §4 paper, không ảnh hưởng kết luận chính.

### 2.2 Cosine Similarity (vs Ground Truth)

| Chiến lược | Avg Cosine |
|:---|:---:|
| Zero-Shot | 0.8088 |
| **Few-Shot** | **0.8218** |
| CoT | 0.7667 |

### 2.3 AST Parse Rate

| Chiến lược | Valid | Rate |
|:---|:---:|:---:|
| Zero-Shot | 499/500 | 99.8% |
| Few-Shot | 500/500 | **100%** |
| CoT | 500/500 | **100%** |

### 2.4 Statistical Tests (Wilcoxon Signed-Rank)

| Cặp | p-value | Effect Size (Cliff's δ) | Mức |
|:---|:---:|:---:|:---:|
| Zero-Shot vs Few-Shot | <0.001 | 0.291 | Small |
| Zero-Shot vs CoT | <0.001 | 0.467 | Medium |
| Few-Shot vs CoT | <0.001 | 0.617 | **Large** |

---

## 3. So sánh Pilot vs Full Run

| Metric | Pilot (N=20) | Full Run (N=500) | Cải thiện |
|:---|:---:|:---:|:---:|
| Cosine Zero-Shot | 0.6968 | 0.8088 | +16.1% |
| Cosine Few-Shot | 0.7175 | 0.8218 | +14.5% |
| Cosine CoT | 0.6960 | 0.7667 | +10.2% |
| Invalid outputs | 0/60 | 0/1500 | ✅ Ổn định |

---

## 4. Ví dụ minh họa — ID 1

**User Story:** As a user, I want to enable image tagging from the Asset Intelligence section in MCP settings.

| Strategy | Gherkin quality | Python quality |
|:---|:---|:---|
| Zero-Shot | 5 steps, rõ ràng, có `And` | URL navigation thực, tên hàm mô tả |
| Few-Shot | Then-step sát ground truth nhất | Decorator đầy đủ, tên hàm rõ |
| CoT | Chi tiết nhất (6 steps, 2× `And`) | Body trống, bị cắt ngắn |

---

## 5. Vấn đề kỹ thuật & xử lý

| # | Vấn đề | Khi nào | Xử lý |
|:---|:---|:---:|:---|
| 1 | Few-Shot `step_impl` trùng tên | Pilot | Ghi nhận, sửa trước full run |
| 2 | CoT output bị cắt | Pilot | LR tăng max_tokens |
| 3 | Few-Shot 4/500 thiếu `When` | Full Run | Báo cáo trong §4, không sửa |
| 4 | Zero-Shot 1/500 Python fail AST | Full Run | Ghi nhận, tính invalid rate |

---

## 6. Kết luận & Trả lời RQ

> **Few-Shot prompting** sinh Gherkin scenario có chất lượng ngữ nghĩa cao nhất khi dùng GPT-4o (Cosine = 0.8218), vượt trội so với Zero-Shot (p<0.001, δ=0.291) và CoT (p<0.001, δ=0.617 — large effect).

**Khuyến nghị thực tiễn:** Dùng Few-Shot với few-shot examples phản ánh writing convention của dự án. CoT tạo ra nhiều steps hơn nhưng xa ground truth hơn — không phù hợp khi ưu tiên độ sát yêu cầu.

---
*RW: Đào Lý Phi Hùng (SE172826) | MS: Đặng Đỗ Cao Sang (SE193269) | 2026-07-21*
