# Quy trình sàng lọc bài báo PRISMA (PRISMA Flowchart)

Dưới đây là sơ đồ và thống kê chi tiết số lượng bài báo qua từng vòng lọc trong quy trình Systematic Literature Review (SLR) của đề tài:
LLM for Acceptance Test Automation (BDD/Gherkin).

---

## 1. Sơ đồ PRISMA Flowchart (Theo định dạng mẫu Lab)

```text
┌────────────────────────────────────────────────────────┐
│ Records từ database searching                          │
│ (N = 404)                                              │
└────────────────────────────────────────────────────────┘
                            │
                            ▼
┌────────────────────────────────────────────────────────┐
│ Sau khi xóa duplicate (N = 301)                        │
└────────────────────────────────────────────────────────┘
                            │
                            ▼
                         Vòng 1
┌───────────────────────────────┐        ┌───────────────────────────────┐
│ Screened title+abstract       ├───────►│ Excluded (N = 272)            │
│ (N = 301)                     │        │ EC1=0, EC2=0, EC3=0, EC4=272  │
└───────────────────────────────┘        └───────────────────────────────┘
                            │
                            ▼
                         Vòng 2
┌───────────────────────────────┐        ┌───────────────────────────────┐
│ Full-text assessed            ├───────►│ Excluded (N = 21)             │
│ (N = 29)                      │        │ Reasons:                      │
└───────────────────────────────┘        │ EC2=4, EC3=5, EC4=12          │
                            │        └───────────────────────────────┘
                            ▼
┌────────────────────────────────────────────────────────┐
│ Included trong Evidence Table                          │
│ (N = 8)                                                │
└────────────────────────────────────────────────────────┘
```

---

## 2. Bảng thống kê chi tiết số liệu thực tế

| Giai đoạn | Thống kê số lượng (N) | Mô tả chi tiết |
| :--- | :---: | :--- |
| Identification | 404 | Tổng số bản ghi tìm thấy từ Google Scholar:<br/>- String A: 227 bài báo<br/>- String B: 177 bài báo |
| Deduplication | 103 | Số lượng bài viết bị trùng lặp (Duplicate) bị loại bỏ dựa trên tiêu đề và năm xuất bản. |
| Vòng 1 (Screening) | 301 | Tổng số bài báo được rà soát tiêu đề (Title) và tóm tắt (Abstract). |
| Vòng 1 Excluded | 272 | Số bài bị loại do không thỏa mãn tiêu chí tuyển chọn (chủ yếu là EC4 - không bàn về sinh test tự động BDD/Gherkin hoặc không dùng LLM). |
| Vòng 2 (Eligibility) | 29 | Số bài báo được tải toàn văn PDF để đọc chi tiết (gồm 27 bài `INCLUDE` và 2 bài `UNSURE` ở vòng 1). |
| Vòng 2 Excluded | 21 | Số bài báo bị loại sau khi đọc toàn văn:<br/>- EC2 (Không tìm được PDF): 4 bài báo<br/>- EC3 (Dạng poster, extended abstract, < 4 trang): 5 bài báo<br/>- EC4 (Chỉ nói về chạy test, không sinh test tự động): 12 bài báo |
| Included | 8 | Số lượng bài viết được chọn lựa cuối cùng để đưa vào bảng bằng chứng dữ liệu (Evidence Table). |
