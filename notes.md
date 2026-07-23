# Notes & Technical Decisions — RT-SWT-001-Gr2

## Thông tin thực nghiệm

| Tham số | Giá trị |
|:---|:---|
| Model | GPT-4o (OpenAI API) |
| Temperature | 0 |
| Dataset | 100 User Stories × 5 scenarios = 500 mẫu |
| Ngày chạy Pilot | 2026-07-13 |
| Ngày chạy Full Run | 2026-07-19 |
| Random seed Pilot | [TBD — hỏi DG] |

## Quyết định kỹ thuật

### Pilot (Tuần 7)
- **2026-07-13:** Chạy pilot 20 mẫu × 3 strategies = 60 calls. Status: SUCCESS, Invalid: 0.
- **Quyết định sau pilot:** Tiến hành full run — syntax validity 100%, Cosine ≥ 0.69 trên cả 3 strategies.
- **Vấn đề phát hiện:** Few-Shot dùng `step_impl` trùng tên cho mọi step → cần sửa few-shot example trước full run.
- **Vấn đề phát hiện:** Một số CoT output bị cắt ngắn → LR kiểm tra max_tokens.
- **Phân phối data:** Như dự kiến → giữ nguyên Wilcoxon signed-rank test đã chọn trong proposal.

### Full Run (Tuần 8)
- **2026-07-19:** Chạy full 500 mẫu × 3 strategies = 1,500 calls. Status: SUCCESS, Invalid: 0.
- **Few-Shot syntax:** 4/500 mẫu thiếu `When` (99.2%) — ghi nhận, không ảnh hưởng RQ chính.
- **AST:** Zero-Shot có 1/500 Python không parse được (99.8%) — không đáng kể.
- **Statistical test:** Wilcoxon signed-rank — tất cả 3 cặp p < 0.001, giữ α = 0.05.
- **Effect size:** Few-Shot vs CoT = 0.617 (large) — sự khác biệt thực tiễn rõ ràng.

## Error Log

| Ngày | Loại lỗi | Xử lý |
|:---|:---|:---|
| 2026-07-13 | Few-Shot step_impl trùng tên | Ghi nhận, sửa trước full run |
| 2026-07-13 | CoT output bị cắt 2/20 mẫu | LR tăng max_tokens cho full run |
| 2026-07-19 | Few-Shot 4/500 thiếu When | Ghi nhận trong paper §4 |
| 2026-07-19 | Zero-Shot 1/500 Python fail AST | Ghi nhận, tính invalid rate |

## Kết quả tóm tắt Full Run

| Metric | Zero-Shot | Few-Shot | CoT |
|:---|:---:|:---:|:---:|
| Avg Cosine | 0.8088 | 0.8218 | 0.7667 |
| Syntax Valid | 500/500 (100%) | 496/500 (99.2%) | 500/500 (100%) |
| AST Parse Rate | 499/500 (99.8%) | 500/500 (100%) | 500/500 (100%) |
| Wilcoxon p-value | <0.001 vs FS | — | <0.001 vs FS |
| Effect size vs FS | 0.291 (small) | — | 0.617 (large) |

**Kết luận:** Few-Shot > Zero-Shot > CoT về Cosine Similarity, tất cả significant (p<0.001).
