# Bảng Kết Quả Pilot — RT-SWT-001-Gr2

## Bảng 1: Syntax Validity

| Chiến lược | N | Feature | Scenario | Given | When | Then | Valid (tất cả) | Tỷ lệ |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Zero-Shot | 20 | 20 | 20 | 20 | 20 | 20 | 20 | 100% |
| Few-Shot | 20 | 20 | 20 | 20 | 20 | 20 | 20 | 100% |
| CoT | 20 | 20 | 20 | 20 | 20 | 20 | 20 | 100% |

## Bảng 2: Độ phong phú nội dung

| Chiến lược | Avg Steps | Avg Scenarios | Có And (%) | Avg Words | Avg Lines | Steps Min–Max |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|
| Zero-Shot | 3.70 | 1.00 | 30% | 129.4 | 23.7 | 3–6 |
| Few-Shot | 4.60 | 1.30 | 45% | 119.5 | 21.6 | 3–12 |
| CoT | 4.60 | 1.00 | 45% | 109.0 | 21.3 | 3–12 |

## Bảng 3: Metric chính (chờ MS)

| Metric | Zero-Shot | Few-Shot | CoT | Threshold | Đạt? |
|:---|:---:|:---:|:---:|:---:|:---:|
| Cosine Similarity | 0.7786 | 0.8280 | 0.8284 | ≥ 0.80 | Few/CoT Đạt |
| AST Parse Rate | 100% | 100% | 80% | ≥ 85% | Zero/Few Đạt |
| p-value (vs Few-Shot) | 0.0007 | — | 0.0049 | < 0.05 | Có ý nghĩa |

## Bảng 4: Vấn đề kỹ thuật

| # | Vấn đề | Ảnh hưởng | Mức độ |
|:---|:---|:---:|:---:|
| 1 | Python step body trống (pass) | Zero-Shot, Few-Shot | ⚠️ |
| 2 | Thiếu decorator @when | Few-Shot | ⚠️ |
| 3 | URL hardcode trong CoT | CoT | ℹ️ |
| 4 | Không có Scenario Outline | Tất cả | ℹ️ |
| 5 | Steps range rộng (3–12) | Few-Shot, CoT | ℹ️ |

