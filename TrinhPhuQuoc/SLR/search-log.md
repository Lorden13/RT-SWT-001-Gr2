# Phase 0 & Phase 1.1: PICO Analysis, Keywords, and Search Strings

## 1. Giai đoạn 0 — Đọc hiểu RQ ban đầu

### Bước 0.1 — Phân tích PICO

Dựa trên câu hỏi nghiên cứu (Research Question - RQ) ban đầu của nhóm:
*Đối với user stories viết theo format Connextra (P), LLM tự động sinh Gherkin scenarios + step definitions (I) so với BDD viết thủ công (C), có đạt semantic similarity >= 0.85 và executable không lỗi cú pháp không (O)?*

Dưới đây là bảng phân tích cấu trúc PICO:

| Thành phần    | Điền của nhóm                | Đáp án đúng                                                      |
| :---          | :---                         | :---                                                             |
| P             | User stories Connextra format| User stories Connextra format ("As a ... I want... So that...")   |
| I             | GPT-4o zero-shot sinh Gherkin| GPT-4o zero-shot sinh Gherkin scenarios + step definitions       |
| C             | BDD scenarios viết tay       | BDD scenarios viết tay bởi expert                                |
| O - Metric 1  | Semantic similarity >= 0.85  | Semantic similarity >= 0.85                                      |
| O - Metric 2  | Executable syntax rate       | Executable syntax rate (không lỗi parse)                         |

#### 2 điểm chưa rõ (Lý do cần thực hiện quy trình SLR với PRISMA):
1. **LLM**: Mô hình LLM cụ thể nào sẽ được sử dụng và đánh giá? (Ví dụ: GPT-4o, Gemini, Claude, hay các mô hình nguồn mở khác?).
2. **Ngưỡng >= 0.85**: Ngưỡng tương đồng ngữ nghĩa (Semantic similarity) này được tham chiếu và lấy từ công trình nghiên cứu/bài báo khoa học cụ thể nào?

---

### Bước 0.2 — Chọn Keyword Seed

Rút ra từ khung PICO, nhóm đã xác định 6 từ khóa cốt lõi (keywords) sau:
1. `user story` (Từ P)
2. `Gherkin generation` (Từ I)
3. `step definitions` (Từ I)
4. `LLM` (Từ I)
5. `semantic similarity` (Từ O)
6. `acceptance test` (Từ O)

Bảng trace từ khóa về các thành phần P/I/C/O:

| Từ khóa            | Thuộc thành phần PICO | Vai trò trong tìm kiếm                                      |
| :---               | :---:                 | :---                                                        |
| user story         | P                     | Xác định định dạng yêu cầu đầu vào                          |
| requirements       | P                     | Định nghĩa tài liệu yêu cầu hệ thống nói chung              |
| Gherkin generation | I                     | Hoạt động sinh kịch bản kiểm thử tự động                    |
| step definitions   | I                     | Kết quả đầu ra mã nguồn kiểm thử BDD                        |
| LLM                | I                     | Công nghệ/công cụ thực hiện sinh tự động                    |
| semantic similarity| O                     | Chỉ số đánh giá độ tương đồng ngữ nghĩa                     |
| acceptance test    | O                     | Lĩnh vực kiểm thử nghiệm thu mục tiêu                       |

---

## 2. Giai đoạn 1 — SLR với PRISMA

### Bước 1.1 — Xây dựng Search Strings

Để tìm kiếm các bài báo khoa học liên quan trên các cơ sở dữ liệu học thuật, nhóm đã xây dựng 2 chuỗi tìm kiếm (Search Strings) chuẩn cú pháp Boolean (AND, OR, dấu ngoặc và cụm từ trong dấu nháy kép):

#### String A
```text
("Gherkin" OR "BDD" OR "behavior-driven development") AND ("large language model" OR LLM OR GPT OR ChatGPT) AND (generate OR generation OR automated) AND ("user story" OR requirements)
```

#### String B
```text
("large language model" OR LLM OR GPT OR ChatGPT) AND ("step definition" OR "acceptance test" OR "test case generation") AND ("BDD" OR Gherkin)
```

#### Đánh giá tính hợp lệ của hai chuỗi tìm kiếm:
* **String A**: Tập trung vào quy trình sinh tự động Gherkin từ User Story/Yêu cầu bằng cách sử dụng các mô hình LLM. Chuỗi này phủ đầy đủ 4 nhánh PICO (BDD/Gherkin AND LLMs AND Automation AND User Stories/Requirements).
* **String B**: Tập trung vào việc sinh mã kiểm thử kỹ thuật (step definitions/acceptance tests) cho BDD bằng các mô hình LLM. Chuỗi này giúp bổ sung các bài báo chuyên sâu về mặt lập trình và thực thi kiểm thử.
* **Cú pháp Boolean**: Cả hai chuỗi đều sử dụng đúng cú pháp logic chuẩn, phân nhóm rõ ràng bằng dấu ngoặc đơn và sử dụng dấu nháy kép cho các cụm từ ghép (`"behavior-driven development"`, `"large language model"`, `"user story"`, `"step definition"`, `"acceptance test"`, `"test case generation"`) để đảm bảo không bị tách từ đơn lẻ khi tìm kiếm.

#### Các cơ sở dữ liệu học thuật áp dụng:
Nhóm sử dụng hai chuỗi tìm kiếm này trên các thư viện học thuật lớn bao gồm:
1. Google Scholar (`scholar.google.com`)
2. IEEE Xplore (`ieeexplore.ieee.org`)
3. ACM Digital Library (`dl.acm.org`)
4. Semantic Scholar (`semanticscholar.org`)
5. OpenAlex (`openalex.org`)
