# Search Log — LLM for Acceptance Test Automation (BDD/Gherkin)
**Thành viên:** Đăng Khoa
**Ngày thực hiện:** 2026-06-02

---

## Chuỗi tìm kiếm (Query Strings)

### String A
**Query nguyên văn:**
```
("Gherkin" OR "BDD" OR "behavior-driven development") AND ("large language model" OR LLM OR GPT OR ChatGPT) AND (generate OR generation OR automated) AND ("user story" OR requirements)
```
**Database:** ACM Digital Library
**Bộ lọc:** Year 2018–2026, English only, Peer-reviewed / Conference + Journal
**Ngày search:** 2026-06-02
**Số kết quả:** 159 papers

---

### String B
**Query nguyên văn:**
```
("large language model" OR LLM OR GPT OR ChatGPT) AND ("step definition" OR "acceptance test" OR "test case generation") AND ("BDD" OR Gherkin)
```
**Database:** ACM Digital Library
**Bộ lọc:** Year 2018–2026, English only, Peer-reviewed / Conference + Journal
**Ngày search:** 2026-06-02
**Số kết quả:** 47 papers

---

## Tổng hợp trước dedup

| Database / Source | Search String | Kết quả |
|-------------------|---------------|---------|
| ACM Digital Library | String A | 159 |
| ACM Digital Library | String B | 47 |
| **Tổng trước dedup** | | **206** |
| **Sau dedup** | | **160** |
| Số bị loại (trùng lặp) | | 46 |

---

## Ghi chú

- Thực hiện loại bỏ trùng lặp (deduplication) thông qua sự kết hợp của phần mềm quản lý trích dẫn **Zotero** và các hàm xử lý dữ liệu chuẩn hóa trong **Excel** dựa trên so khớp tiêu đề (`Title`) và năm xuất bản (`Year`).
