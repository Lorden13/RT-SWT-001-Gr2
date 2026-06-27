# Quy trình sàng lọc bài báo PRISMA (PRISMA Flowchart)

Dưới đây là sơ đồ và thống kê chi tiết số lượng bài báo qua từng vòng lọc trong quy trình Systematic Literature Review (SLR) của đề tài:
**LLM for Acceptance Test Automation (BDD/Gherkin)**.

---

## 1. Sơ đồ PRISMA Flowchart (Theo định dạng mẫu Lab - myLab3)

```text
┌────────────────────────────────────────────────────────┐
│ Records từ database searching (myLab3 search)          │
│ (N = 206) (String A: 159, String B: 47)                │
└────────────────────────────────────────────────────────┘
                            │
                            ▼
┌────────────────────────────────────────────────────────┐
│ Sau khi xóa duplicate (N = 160)                        │
│ (Loại bỏ 46 bài trùng)                                 │
└────────────────────────────────────────────────────────┘
                            │
                            ▼
                         Vòng 1 (Sàng lọc Title + Abstract)
┌───────────────────────────────┐        ┌───────────────────────────────┐
│ Screened title+abstract       ├───────►│ Excluded (N = 155)            │
│ (N = 160)                     │        │ EC4=155                       │
└───────────────────────────────┘        └───────────────────────────────┘
                            │
                            ▼
                         Vòng 2 (Sàng lọc Toàn văn PDF - Eligibility)
┌───────────────────────────────┐        ┌───────────────────────────────┐
│ Full-text assessed            ├───────►│ Excluded (N = 4)              │
│ (N = 5)                       │        │ Reasons:                      │
└───────────────────────────────┘        │ EC2=4                         │
                            │        └───────────────────────────────┘
                            ▼
┌────────────────────────────────────────────────────────┐
│ Included trong Evidence Table                          │
│ (N = 1)                                                │
└────────────────────────────────────────────────────────┘
```

---

## 2. Bảng thống kê chi tiết số liệu thực tế

| Giai đoạn | Thống kê số lượng (N) | Mô tả chi tiết |
| :--- | :---: | :--- |
| **Identification** | **206** | Tổng số bản ghi tìm thấy từ ACM Digital Library:<br/>- **String A**: 159 bài báo<br/>- **String B**: 47 bài báo |
| **Deduplication** | **46** | Số lượng bài viết bị trùng lặp (Duplicate) bị loại bỏ dựa trên tiêu đề và năm xuất bản. |
| **Vòng 1 (Screening)** | **160** | Tổng số bài báo được rà soát tiêu đề (Title) và tóm tắt (Abstract). |
| **Vòng 1 Excluded** | **155** | Số bài bị loại do không thỏa mãn tiêu chí tuyển chọn (chủ yếu là **EC4** - không bàn về sinh test tự động BDD/Gherkin hoặc không dùng LLM). |
| **Vòng 2 (Eligibility)** | **5** | Số bài báo được tải toàn văn PDF để đọc chi tiết (gồm 4 bài `INCLUDE` và 1 bài `UNSURE` ở vòng 1). |
| **Vòng 2 Excluded** | **4** | Số bài báo bị loại sau khi đọc toàn văn:<br/>- **EC2** (Không tìm được PDF): **4** bài báo |
| **Included** | **1** | Số lượng bài viết được chọn lựa cuối cùng để đưa vào bảng bằng chứng dữ liệu (Evidence Table). |
