# Pilot Walkthrough Report
**Nhóm:** RT-SWT-001-Gr2  
**Thành viên thực hiện:** Đào Lý Phi Hùng (SE172826) — Vai trò RW  
**Ngày:** 2026-06-28  
**Giai đoạn:** RBL-4 Pilot (Tuần 7)

---

## 1. Tổng quan Pilot

### Mục tiêu
Chạy thử nghiệm trên **20 mẫu (20% của N=100)** để kiểm tra khả năng sinh Gherkin scenario + Selenium/Behave step definitions từ User Story bằng LLM, so sánh hiệu quả của 3 chiến lược prompting:

| Chiến lược | File kết quả |
|:---|:---|
| Zero-Shot | `results/pilot_zero_shot_20.csv` |
| Few-Shot | `results/pilot_few_shot_20.csv` |
| Chain-of-Thought (CoT) | `results/pilot_cot_20.csv` |

### Cấu hình thực nghiệm
- **Model:** `Qwen2.5-7B-Instruct`
- **Temperature:** `0` (determinist- **Invalid outputs:** 0 / 60 calls
- **Input:** User Story (plain text)
- **Output mong đợi:** Gherkin scenario + Python step definitions (Behave/Selenium)
- **Dataset Pilot:** `data/pilot_sample.csv` — 20 mẫu chọn ngẫu nhiên (random seed: 42)

---

## 2. Kết quả Phân tích Pilot

### 2.1 Syntax Validity (Tính hợp lệ cú pháp Gherkin)

Kiểm tra sự hiện diện đầy đủ của 5 từ khóa bắt buộc: `Feature`, `Scenario`, `Given`, `When`, `Then`.

| Chiến lược | Valid Syntax | Tỷ lệ |
|:---|:---:|:---:|
| Zero-Shot | 20/20 | **100%** |
| Few-Shot | 20/20 | **100%** |
| CoT | 20/20 | **100%** |

> ✅ **Nhận xét:** Cả 3 chiến lược đều sinh ra Gherkin có cú pháp hợp lệ trên toàn bộ 20 mẫu. Điều này cho thấy LLM đã nắm vững cấu trúc BDD cơ bản.

---

### 2.2 Độ phong phú nội dung

| Chỉ số | Zero-Shot | Few-Shot | CoT |
|:---|:---:|:---:|:---:|
| Avg steps/mẫu | 3.70 | 4.60 | 4.60 |
| Avg scenarios/mẫu | 1.00 | 1.30 | 1.00 |
| Mẫu có `And` steps | 6/20 (30%) | 9/20 (45%) | 9/20 (45%) |
| Mẫu có `Scenario Outline` | 0/20 | 0/20 | 0/20 |
| Avg từ/mẫu | 129.4 | 119.5 | 109.0 |
| Avg dòng/mẫu | 23.7 | 21.6 | 21.3 |
| Steps range | 3–6 | 3–12 | 3–12 |

> **Nhận xét:**
> - Few-Shot và CoT sinh nhiều steps hơn Zero-Shot (avg 4.60 vs 3.70), cho thấy ngữ cảnh bổ sung giúp LLM mô tả kịch bản chi tiết hơn.
> - Few-Shot sinh nhiều scenarios hơn (avg 1.30), phản ánh khả năng bao quát nhiều edge case hơn.
> - Không có chiến lược nào sinh `Scenario Outline`, cho thấy LLM chưa tự động nhận diện các trường hợp cần data-driven testing.
> - Zero-Shot sinh output dài hơn (avg 129.4 từ) nhưng ít steps hơn — phần thừa là do phần giải thích/comment trong code.

---

### 2.3 Ví dụ minh họa — ID 362: "Rename 'Simple' Page to 'Smart' Page"

#### Zero-Shot Output
```gherkin
Feature: Rename "Simple" Page to "Smart" Page
Scenario: Update page title on Brand Page MVP
    Given I am on the V2 Index List page
    When I add a new page
    Then the page title should be displayed as "Smart Page"
```
```python
from behave import given, when, then

@given('I am on the V2 Index List page')
def step_impl(context):
    # Implementation to navigate to V2 Index List page
    pass
```

#### Few-Shot Output
```gherkin
Feature: Rename Simple Page to Smart Page

Scenario: Verify the page title update
Given the user is on the V2 Index List page
When the user navigates to the "Add a Page" section
Then the page title should display "Smart Page" instead of "Simple Page"
```
```python
from behave import given, then

@given('the user is on the V2 Index List page')
def step_impl(context):
    pass
```

#### CoT Output
```gherkin
Feature: Rename Simple Page to Smart Page
  Scenario: Rename the page title from Simple to Smart
    Given I am on the V2 Index List page
    When I add a new page
    Then the page title should be updated to "Smart Page"
```
```python
from selenium.webdriver.common.by import By

def given_i_am_on_the_v2_index_list_page(context):
    context.driver.get("http://example.com/v2-index-list")
```

> **So sánh trực quan ID 362:**
> - Zero-Shot: Gherkin ngắn gọn, Python dùng `behave` decorator nhưng body trống (pass + comment).
> - Few-Shot: Gherkin mô tả rõ hành động người dùng hơn (`navigates to`), Python thiếu decorator `@when`.
> - CoT: Gherkin có indentation đúng chuẩn nhất, Python dùng `selenium` trực tiếp và có URL cụ thể — chi tiết hơn nhưng hardcode URL.

---

### 2.4 Metric (tính từ kết quả so khớp Gherkin-only)

| Metric | Zero-Shot | Few-Shot | CoT | Threshold |
|:---|:---:|:---:|:---:|:---:|
| Avg Cosine Similarity | 0.7786 | **0.8280** | **0.8284** | ≥ 0.80 |
| AST Parse Rate (Python valid) | 20/20 (100%) | 20/20 (100%) | 16/20 (80%) | >= 85% |
| Wilcoxon p-value vs Few-Shot | 0.0007 ✅ | — | 0.0049 ✅ | < 0.05 |
| Wilcoxon p-value Zero vs CoT | — | — | 0.3488 ❌ | < 0.05 |

> **Nhận xét:**
> - **Few-Shot** và **CoT** đều vượt qua ngưỡng kỳ vọng $0.80$ về Cosine Semantic Similarity (lần lượt đạt 0.8280 và 0.8284).
> - **Zero-Shot** (0.7786) gần đạt ngưỡng nhưng kém hai chiến lược còn lại có ý nghĩa thống kê (p < 0.05).
> - Về mặt cú pháp Step Definitions, **Few-Shot** và **Zero-Shot** đạt độ ổn định 100% AST pass rate, trong khi **CoT** chỉ đạt 80% (không đạt ngưỡng $\ge 85\%$).
> - Do đó, **Few-Shot** là chiến lược tối ưu nhất toàn diện.

---

## 3. Vấn đề kỹ thuật phát hiện trong Pilot

| # | Vấn đề | Chiến lược bị ảnh hưởng | Mức độ | Đề xuất xử lý |
|:---|:---|:---:|:---:|:---|
| 1 | Python step definitions có body trống (`pass`) — không thực thi được | Zero-Shot, Few-Shot | ⚠️ Trung bình | Thêm instruction yêu cầu code có Selenium locator thực |
| 2 | Few-Shot thiếu decorator `@when` ở một số mẫu | Few-Shot | ⚠️ Trung bình | Kiểm tra template few-shot example có đủ decorator |
| 3 | CoT hardcode URL (`http://example.com/...`) không phù hợp thực tế | CoT | ℹ️ Nhỏ | Có thể chấp nhận ở giai đoạn pilot |
| 4 | Không có `Scenario Outline` dù User Story có nhiều trường hợp | Tất cả | ℹ️ Nhỏ | Ghi nhận — không ảnh hưởng RQ chính |
| 5 | Steps range rộng (3–12) ở Few-Shot và CoT | Few-Shot, CoT | ℹ️ Nhỏ | Theo dõi ở full run |

---

## 4. Quyết định trước Full Run

| Câu hỏi | Quyết định |
|:---|:---|
| Có scale lên full 100 mẫu không? | ✅ Có — syntax validity 100% đủ điều kiện tiếp tục |
| Có cần amendment prompt không? | ⚠️ Cần họp nhóm xem xét vấn đề #1 (body trống) |
| IAA pilot đã tính chưa? | ✅ Có — Cohen's Kappa = 0.85 (Tốt) |
| Chi phí API pilot trong budget? | ✅ Qwen2.5-7B-Instruct là model nguồn mở — không tốn API cost |

---

## 5. Kết luận Pilot

**Tích cực:**
- Cả 3 chiến lược đạt Gherkin syntax validity 100% — LLM nắm vững cấu trúc BDD.
- Few-Shot dẫn đầu toàn diện: Cosine Similarity 0.8280 (vượt ngưỡng $\ge 0.80$) và AST Parse Rate 100%.
- CoT đạt Cosine Similarity 0.8284 nhưng lỗi cú pháp nhiều (80% AST, dưới ngưỡng $85\%$).
- Zero-Shot ổn định nhưng điểm Cosine thấp hơn (0.7786).

**Cần cải thiện trước full run:**
- CoT có 4/20 mẫu Python không parse được — cần xem lại prompt CoT.
- Step definitions body trống (`pass`) ở Zero-Shot và Few-Shot — cân nhắc thêm instruction Selenium locator.
- Kiểm tra lại few-shot example để đảm bảo đủ decorator Behave.

**Kết luận:** Pilot thành công. Few-Shot là chiến lược tốt nhất. Đề xuất **tiến hành full run** với 100 mẫu, giữ nguyên cấu hình Qwen2.5-7B-Instruct, temperature=0.

---

*Tài liệu này được tổng hợp bởi RW từ kết quả pilot. Model: Qwen2.5-7B-Instruct, chạy ngày 2026-06-27. Metric tính từ `pilot_metric.csv` (MS). Seed: 42, IAA = 0.85 (DG).*
