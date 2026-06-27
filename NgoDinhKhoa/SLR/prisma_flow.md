# Sơ đồ quy trình sàng lọc PRISMA (PRISMA Flowchart)

Tài liệu này mô tả chi tiết các bước sàng lọc tài liệu hệ thống theo quy trình PRISMA. Các con số thống kê dưới đây khớp hoàn toàn với các tệp dữ liệu CSV đi kèm.

```
[Records từ database searching (N = 15)]   ← Tổng số kết quả từ search-log.md
↓
[Sau khi xóa duplicate (N = 14)]            ← Số dòng trong 01_all_records.csv
↓
┌─────────────────────────────────────────┐
│  Screened title + abstract (N = 14)     │
│  └── Excluded (N = 7):                  │
│       - IC1 (Không tiếng Anh): 1        │
│       - EC4 (Không về test gen): 6      │
└─────────────────────────────────────────┘
↓ 7 papers pass                             ← Số bài INCLUDE + Unsure trong 02_after_screening_v1.csv
┌─────────────────────────────────────────┐
│  Full-text assessed (N = 7)             │
│  └── Excluded (N = 2):                  │
│       - EC4 (Không về BDD test gen): 2  │
└─────────────────────────────────────────┘
↓
[Final included (N = 5)]                   ← Số bài Include trong 03_final_included.csv
```

### Bảng đối chiếu tính nhất quán của dữ liệu:
*   **Tổng số dòng trong `01_all_records.csv`:** 14 dòng (khớp với $N$ sau khi xóa trùng).
*   **Số lượng bài bị loại ở Vòng 1 trong `02_after_screening_v1.csv` (`EXCLUDE`):** 7 bài (khớp với số lượng Excluded vòng 1).
*   **Số lượng bài đi tiếp vào Vòng 2 trong `02_after_screening_v1.csv` (`INCLUDE` + `Unsure`):** 7 bài (khớp với số lượng Full-text assessed).
*   **Số lượng bài được chọn cuối cùng ở Vòng 2 trong `03_final_included.csv` (`Include`):** 5 bài (khớp với $N$ Final included).
