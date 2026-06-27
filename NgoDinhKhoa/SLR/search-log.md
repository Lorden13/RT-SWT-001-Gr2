# Search Log — Automated Test Generation from BDD/Gherkin using LLMs

**Thành viên:** Nguyễn Thành Ty  
**Ngày thực hiện:** 2026-06-01  

---

## Chuỗi tìm kiếm (Query Strings)

### String A
**Query nguyên văn:**
```sql
("Gherkin" OR "BDD" OR "behavior-driven development") AND ("large language model" OR "LLM" OR "GPT" OR "ChatGPT") AND ("generate" OR "generation" OR "automated") AND ("user story" OR "requirements")
```
**Database:** Semantic Scholar  
**Bộ lọc:** Year 2018–2026, English only  
**Ngày search:** 2026-06-01 10:00  
**Số kết quả:** 9 papers

---

### String B
**Query nguyên văn:**
```sql
("large language model" OR "LLM" OR "GPT" OR "ChatGPT") AND ("step definition" OR "acceptance test" OR "test case generation") AND ("BDD" OR "Gherkin")
```
**Database:** Semantic Scholar  
**Bộ lọc:** Year 2018–2026, English only  
**Ngày search:** 2026-06-01 10:30  
**Số kết quả:** 6 papers

---

## Tổng hợp trước dedup

| Database         | String   | Kết quả |
|------------------|----------|---------|
| Semantic Scholar | String A | 9       |
| Semantic Scholar | String B | 6       |
| **Tổng trước dedup** |      | **15**  |
| **Sau dedup**    |          | **14**  |
| Số bị loại (trùng lặp) |    | 1       |

---

## Ghi chú

- Thực hiện dedup bằng Excel / tay dựa trên tiêu đề bài báo.
- Bài báo trùng lặp: *"Automating Behavior-Driven Development with Generative AI: Enhancing Efficiency in Test Automation"* của tác giả Sujeet Kumar Tiwari xuất hiện ở cả hai chuỗi tìm kiếm của Semantic Scholar.
