# Search Log — LLM for Acceptance Test Automation (BDD/Gherkin)
**Thành viên:** Trịnh Phú Quốc
**Ngày thực hiện:** 2026-05-28

---

## Chuỗi tìm kiếm (Query Strings)

### String A
**Query nguyên văn:**
```text
("Gherkin" OR "BDD" OR "behavior-driven development") AND ("large language model" OR LLM OR GPT OR ChatGPT) AND (generate OR generation OR automated) AND ("user story" OR requirements)
```
**Database:** Google Scholar
**Bộ lọc:** Year 1999–2026, English only, Conference + Journal + Preprint
**Ngày search:** 2026-05-28 09:30
**Số kết quả:** 227 papers

---

### String B
**Query nguyên văn:**
```text
("large language model" OR LLM OR GPT OR ChatGPT) AND ("step definition" OR "acceptance test" OR "test case generation") AND ("BDD" OR Gherkin)
```
**Database:** Google Scholar
**Bộ lọc:** Year 1999–2026, English only, Conference + Journal + Preprint
**Ngày search:** 2026-05-28 10:15
**Số kết quả:** 177 papers

---

## Tổng hợp trước dedup

| Database | String | Kết quả |
|---------|--------|---------|
| Google Scholar | String A | 227 |
| Google Scholar | String B | 177 |
| **Tổng trước dedup** | | **404** |
| **Sau dedup** | | **301** |
| Số bị loại (trùng lặp) | | 103 |

---

## Ghi chú

- Thực hiện dedup bằng: Tính năng lọc trùng tự động của Chrome Extension SLR Assistant kết hợp rà soát thủ công trên Microsoft Excel.
- Paper trùng nhau nhiều nhất: Các bài báo nghiên cứu về sinh Gherkin kịch bản từ User Story sử dụng mô hình GPT xuất hiện đồng thời trong cả hai kết quả tìm kiếm của String A và String B.
- Không có bất kỳ bất thường nào khác được ghi nhận trong quá trình tìm kiếm.
