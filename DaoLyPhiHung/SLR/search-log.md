# Search Log — Automated BDD/Gherkin Test Case Generation using Large Language Models
**Thành viên:** Đào Lý Phi Hùng (SE172826)
**Ngày thực hiện:** 2026-06-02

---

## Chuỗi tìm kiếm (Query Strings)

### String A
**Query nguyên văn:**
```
("Gherkin" OR "BDD" OR "behavior-driven") AND ("LLM" OR "GPT" OR "language model") AND ("test generation" OR "test automation")
```
**Database:** IEEE Xplore, Google Scholar (ACM, Springer, ScienceDirect)  
**Bộ lọc:** Year 2018–2026, English only, Conference + Journal + Preprint  
**Ngày search:** 2026-06-02 10:15  
**Số kết quả:** 158 papers

---

### String B
**Query nguyên văn:**
```
"acceptance test" AND ("large language model" OR "GPT-4" OR "ChatGPT") AND ("user story" OR "requirements")
```
**Database:** Scopus, Google Scholar  
**Bộ lọc:** Year 2018–2026, English only, Conference + Journal  
**Ngày search:** 2026-06-02 11:30  
**Số kết quả:** 60 papers

---

## Tổng hợp trước dedup

| Database         | String   | Kết quả |
|------------------|----------|---------|
| Google Scholar / IEEE Xplore  | String A | 158     |
| Scopus / Google Scholar       | String B | 60      |
| **Tổng trước dedup**          |          | **218** |
| **Sau dedup**                 |          | **217** |
| Số bị loại (trùng lặp)        |          | 1       |

---

## Ghi chú

- Thực hiện dedup tự động bằng code Python, dựa trên tiêu đề bài viết được chuẩn hóa (loại bỏ ký tự đặc biệt, dấu câu, khoảng trắng thừa, và chuyển về chữ thường).
- Paper trùng lặp phát hiện: ID 69 ("Increasing Test Coverage by Automating BDD Tests in Proofs of Concepts (POCs) using LLM") là bản lưu trữ trên ResearchGate trùng với bản xuất bản chính thức trên ACM (ID 61).
- Quá trình search trên Google Scholar có một số tạp âm từ các ngành khoa học khác (khoa học thực phẩm, hóa học, nông nghiệp...) xuất hiện ở String B do sự trùng lặp thuật ngữ về "acceptance criteria", "user story" hoặc "requirements" trong các ngữ cảnh khác. Các tạp âm này được loại bỏ triệt để ở vòng sàng lọc Title & Abstract (Screening V1).
