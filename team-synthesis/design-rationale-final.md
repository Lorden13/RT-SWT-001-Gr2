# Cơ Sở Thiết Kế Thực Nghiệm Nhóm — Experiment Design Rationale (Final)

Tài liệu này tổng hợp bảng quyết định thiết kế thực nghiệm chính thức của nhóm, giải thích nguồn gốc các ngưỡng đánh giá (thresholds) được lựa chọn và chi tiết quá trình giải quyết xung đột (Conflict Resolution) dựa trên kết quả RBL-2 của các thành viên.

---

## 1. Bảng quyết định thiết kế thực nghiệm (Design Decision Matrix)

Các quyết định thiết kế cho thực nghiệm của nhóm được đối chiếu và trích xuất trực tiếp từ các bằng chứng khoa học trong bảng bằng chứng tổng hợp (Evidence Table):

| Quyết định | Giá trị lựa chọn | Nguồn tham chiếu / Cơ sở khoa học |
|:---|:---|:---|
| **Intervention** | Mô hình nguồn mở **LLaMA-3-8B** được tinh chỉnh bằng phương pháp **LoRA** (QLoRA 4-bit) để co-generate Gherkin scenarios và step definitions. | **Paper 11 (Selfbehave)**: Đã chứng minh tính khả thi của việc huấn luyện LLaMA-3-8B cho tác vụ BDD. |
| **Dataset** | **Dataset nguồn**:<br>- Rathnayake et al. (2026)<br>- 500 User Stories, 500 Requirement Descriptions, 500 Manual BDD Scenarios<br><br>**Dataset thực nghiệm**:<br>- Random sampling **100 samples** từ tập 500 mẫu. | **Paper 4 (Rathnayake 2026)**: Cung cấp bộ dữ liệu 500 mẫu thực tế.<br>Khắc phục hạn chế của các tập dữ liệu đóng quy mô nhỏ bằng cách rút mẫu ngẫu nhiên 100 mẫu để thực nghiệm. |
| **Metric** | Song song hai độ đo:<br>1. **Cosine Semantic Similarity** (qua mô hình nhúng `all-MiniLM-L6-v2`).<br>2. **Executable Syntax Rate** (tỷ lệ cú pháp tĩnh hợp lệ qua Static Validation kép). | **Paper 2 (Fernandes 2025)**: Sử dụng độ tương đồng ngữ nghĩa.<br>**Paper 5 (Karpurapu 2024)** & **Paper 11 (Selfbehave 2026)**: Sử dụng parser để kiểm tra tính đúng đắn của cú pháp tĩnh. |
| **Baseline** | **GPT-4o (Zero-shot)** (Baseline đối chứng hiệu năng) và **Expert-written BDD tests (Ground Truth)** làm chuẩn đối chứng chất lượng ngữ nghĩa. | **Paper 2 (Fernandes 2025)**: Cơ sở đối chứng của GPT-4o ở chế độ zero-shot.<br>**Paper 4 (Rathnayake 2026)**: Sử dụng bộ kịch bản viết tay làm chuẩn đối chứng khách quan. |
| **Threshold** | - Cosine Similarity $\ge 0.85$.<br>- Executable Syntax Rate $\ge 85\%$. | Xem chi tiết giải thích nguồn gốc các ngưỡng bên dưới. |
| **Pipeline** | Tinh chỉnh LoRA trên Hugging Face. Giai đoạn sinh mã sử dụng cấu hình **Zero-shot Prompting** với **Temperature = 0** để đảm bảo tính tất định và khả năng tái lập (reproducibility). | **Paper 11 (Selfbehave)**: Huấn luyện tinh chỉnh mô hình nguồn mở.<br>**Paper 2 & 4**: Sử dụng zero-shot prompting temp = 0 để tối ưu hóa cú pháp sinh ra. |

> [!NOTE]
> The purpose of the comparison is to determine whether a fine-tuned open-source model can achieve performance comparable to a frontier proprietary model, rather than to demonstrate superiority. (Mục đích của việc so sánh là để xác định xem mô hình mã nguồn mở tinh chỉnh có thể đạt được hiệu năng tương đương với mô hình thương mại đóng hàng đầu hay không, chứ không phải để chứng minh tính vượt trội.)


---

## 2. Giải thích nguồn gốc các Thresholds (Ngưỡng chất lượng)

### 2.1. Ngưỡng tương đồng ngữ nghĩa Cosine Similarity $\ge 0.85$ (Case 2)
*   **Phân loại:** **Case 2** (Các nghiên cứu trước cung cấp kết quả thực nghiệm số cụ thể nhưng chưa đề xuất một ngưỡng đánh giá cố định nào).
*   **Nguồn tham chiếu:** 
    *   *Fernandes 2025 SBES (Paper 2):* Đạt điểm tương đồng METEOR trung bình cao nhất là **0.84** (Gemini zero-shot).
    *   *Rathnayake 2026 arXiv (Paper 4):* GPT-4o đạt độ tương đồng ngữ nghĩa BERTScore = **91.16%** và Cosine Similarity (SBCS) = **53.96%**.
    *   *Tesfalidet 2025 (Paper 8):* GPT-4 đạt độ tương đồng ngữ nghĩa trung bình **81% (0.81)**.
*   **Lý do chọn:** Dựa trên kết quả thực nghiệm của các công trình trên, mức độ tương đồng ngữ nghĩa từ 0.85 trở lên là mức sàn (floor value) đạt được của các dòng GPT-4/GPT-4o. Việc chọn ngưỡng 0.85 là khả thi và có tính đối chứng khoa học mạnh mẽ.

### 2.2. Ngưỡng đúng cú pháp tĩnh Executable Syntax Rate $\ge 85\%$ (Case 2)
*   **Phân loại:** **Case 2** (Các paper đi trước cung cấp kết quả thực nghiệm số cụ thể).
*   **Nguồn tham chiếu:**
    *   *Exploring BDD Fintech 2025 (Paper 8):* Đạt tỷ lệ executable steps **85%** với GPT-4.
    *   *Karpurapu 2024 (Paper 5):* Đạt tỷ lệ đúng cú pháp Gherkin tĩnh (syntax accuracy) qua parser là **100%** đối với GPT-4/GPT-3.5 và **92%** đối với Llama-2 ở few-shot.
    *   *Selfbehave 2026 (Paper 11):* LLaMA-3-8B tinh chỉnh đạt tỷ lệ cú pháp tĩnh Gherkin đúng chuẩn **99.2%**.
*   **Lý do chọn:** Nhóm lựa chọn ngưỡng tối thiểu là **85%** làm giá trị sàn (floor value) đại diện cho khả năng sinh cú pháp đúng đắn tĩnh của mô hình nguồn mở sau khi tinh chỉnh, chứng minh tính khả thi của mô hình nhỏ trong việc viết code kiểm thử sạch lỗi cú pháp.

---

## 3. Đặc tả chi tiết về Static Validation và Executable Syntax Rate

### 3.1. Quy trình kiểm định tĩnh kép (Static Validation)
Quy trình Static Validation được thiết kế gồm 2 bộ lọc cú pháp tĩnh độc lập cho Gherkin và Step Definitions:

#### A. Gherkin Parser Validation
*   **Đối tượng áp dụng:** Các kịch bản Gherkin Scenarios sinh ra (`.feature` files).
*   **Nội dung kiểm tra:** Kiểm định cấu trúc cú pháp của file `.feature` bao gồm các từ khóa định nghĩa chuẩn: `Feature`, `Scenario`, `Given`, `When`, `Then`, `And`, `But`.
*   **Kết quả:**
    *   **PASS:** Gherkin Scenario parse được và hợp lệ cú pháp.
    *   **FAIL:** Gherkin Scenario có chứa lỗi cú pháp.

#### B. Python AST Validation
*   **Đối tượng áp dụng:** Các định nghĩa bước sinh ra (`step_definitions` Python files).
*   **Nội dung kiểm tra:** Sử dụng module `ast` của Python để phân tích cây cú pháp tĩnh (Abstract Syntax Tree), kiểm tra: cấu trúc hàm định nghĩa bước (Function definition), tính hợp lệ của dấu đóng mở ngoặc (Parentheses), dấu hai chấm (Colon), thụt dòng (Indentation), và các lỗi Python syntax khác thông qua hàm `ast.parse()`.
*   **Kết quả:**
    *   **PASS:** Step Definition parse được thành công bằng Python AST.
    *   **FAIL:** Step Definition gây ra lỗi `SyntaxError` (không parse được).

### 3.2. Định nghĩa Executable Syntax Rate
Executable Syntax Rate được tính trên các artifacts do mô hình sinh ra, bao gồm Gherkin Scenarios và Step Definitions. Chỉ số này không cần Ground Truth Step Definitions vì mục tiêu của nó chỉ là kiểm tra tính hợp lệ cú pháp tĩnh, không đánh giá đúng sai nghiệp vụ.

$$\text{Executable Syntax Rate} = \frac{\text{Number of PASS artifacts}}{\text{Total generated artifacts}}$$

---

## 4. Nhật ký Giải Quyết Xung Đột Nhóm (Conflict Resolution Log)

Nhóm đã áp dụng quy tắc phân xử xung đột để đưa ra quyết định thiết kế thực nghiệm tối ưu nhất:

### 4.1. Xung đột 1: Ngưỡng (Threshold) khác nhau
*   *Xung đột:* Các thành viên đề xuất ngưỡng Cosine và cú pháp khác nhau.
*   *Giải quyết:*
    *   Với Cosine Similarity: Cùng thuộc Case 2, nhóm chọn ngưỡng bảo thủ (khắt khe/cao hơn) là **$\ge 0.85$**.
    *   Với Executable Syntax Rate: Ngưỡng 100% của một số thành viên không khả thi vì LLM luôn có tỷ lệ ảo tưởng nhất định. Nhóm thống nhất chọn ngưỡng bảo thủ là **$\ge 85\%$** để đảm bảo tính nghiêm ngặt cho chốt chặn tĩnh (Parser & AST).
    *   *Loại bỏ Execution Pass Rate:* Do dataset Rathnayake 2026 không cung cấp mã nguồn test code executable hoặc HTML locator để chạy động, nhóm thống nhất loại bỏ hoàn toàn chỉ số Execution Pass Rate và các tranh luận liên quan đến ngưỡng chạy động.

### 4.2. Xung đột 2: Phép kiểm định (Statistical Test) khác nhau
*   *Xung đột:* Đề xuất kiểm định có sự khác nhau về One-sample vs. Paired-sample tùy thuộc vào mô hình đối chứng và cấu trúc dữ liệu.
*   *Giải quyết:* Nhóm ưu tiên chọn theo bản chất của loại dữ liệu:
    *   *Cosine Similarity* (Dữ liệu liên tục, phân phối phi chuẩn): Chọn **Wilcoxon Signed-Rank Test** (One-sample cho so sánh đơn với 0.85, Paired Wilcoxon cho so sánh đối chứng LLaMA-FT vs GPT-4o).
    *   *Executable Syntax Rate* (Dữ liệu tỷ lệ nhị phân độc lập): Chọn **Binomial Exact Test** để so sánh với ngưỡng kỳ vọng 85%.
    *   *Loại bỏ McNemar's Test:* Do loại bỏ chỉ số Execution Pass Rate động, phép kiểm McNemar's Test cho dữ liệu cặp nhị phân chạy động không còn được sử dụng.

### 4.3. Xung đột 3: Mô hình và Tác vụ (LLM/Tool & Task) khác nhau
*   *Xung đột:* Các đề xuất ban đầu có sự khác nhau giữa sinh Unit Test và BDD, giữa mô hình đóng và nguồn mở chạy local.
*   *Giải quyết:* Nhóm thống nhất chọn hướng **BDD/Gherkin** và sinh đồng thời (co-generation) cả kịch bản Gherkin và step definitions. Để giải quyết khoảng trống phụ thuộc API đóng nhưng vẫn đảm bảo tính đối chứng khoa học, nhóm chọn thực nghiệm so sánh: **Intervention chính là LLaMA-3-8B tinh chỉnh qua LoRA** và **Baseline đối chứng là GPT-4o (Zero-shot)**.

### 4.4. Xung đột 4: Bài báo nền tảng (Base Paper) khác nhau
*   *Xung đột:* Các thành viên đề xuất nhiều bài báo nền tảng khác nhau cho pipeline của mình.
*   *Giải quyết:* Nhóm chọn các bài báo gần nhất với RQ của nhóm để làm cơ sở:
    *   **Paper 11 (Selfbehave 2026)**: làm cơ sở khoa học cho việc tinh chỉnh LLaMA-3-8B cho tác vụ Gherkin.
    *   **Paper 2 (Fernandes 2025)**: làm cơ sở đối chứng hiệu năng của GPT-4o trên tác vụ Gherkin.
    *   **Paper 4 (Rathnayake 2026)**: làm cơ sở dữ liệu benchmark thực tế 500 mẫu.

---

## 5. Khuyến nghị cho việc Phát triển Đề cương RBL-3 (Recommendations for RBL-3 Proposal Development)

Để chuẩn bị đầy đủ cho việc bảo vệ đề cương nghiên cứu RBL-3, nhóm nghiên cứu cần bổ sung và chi tiết hóa các nội dung sau trong tài liệu đề cương chính thức (lưu ý không thay đổi thiết kế thực nghiệm cốt lõi đã thống nhất):

### 5.1. Đặc tả Prompt Template
*   **Yêu cầu:** Cần đặc tả chi tiết Prompt Template sử dụng cho cả hai mô hình (Intervention LLaMA-3-8B LoRA-FT và Baseline GPT-4o Zero-shot).
*   **Nội dung:** Prompt cần định rõ định dạng đầu vào (Connextra User Story và Requirement Description) và định dạng đầu ra mong muốn (đồng thời kịch bản Gherkin và Step Definitions bằng Python) cùng với các chỉ dẫn ràng buộc để tránh ảo tưởng cú pháp.

### 5.2. Chiến lược lấy mẫu dữ liệu (Sampling Strategy)
*   **Phương pháp:** Sử dụng **Simple Random Sampling** (Lấy mẫu ngẫu nhiên đơn giản).
*   **Tham số cố định:**
    *   Lấy mẫu **không thay thế** (Without replacement).
    *   Thiết lập **Seed = 42** để đảm bảo khả năng tái lập (reproducibility) kết quả trích xuất mẫu dữ liệu thực nghiệm (100 mẫu từ tập 500 mẫu gốc của Rathnayake et al. 2026).

### 5.3. Các mối đe dọa đối với tính hợp lệ (Threats to Validity)
Cần xây dựng mục phân tích chi tiết về 4 nhóm nguy cơ ảnh hưởng đến tính đúng đắn của thực nghiệm:
*   **Internal Validity (Tính hợp lệ nội bộ):** Các yếu tố như sự biến động trong tham số suy luận (temperature, top_p) của mô hình, chất lượng của dữ liệu huấn luyện LoRA và bias trong quá trình sinh.
*   **External Validity (Tính hợp lệ bên ngoài):** Khả năng tổng quát hóa kết quả thực nghiệm từ tập dữ liệu Connextra User Stories (Rathnayake 2026) sang các định dạng User Stories khác hoặc sang các dự án phần mềm có quy mô và miền nghiệp vụ khác.
*   **Construct Validity (Tính hợp lệ cấu trúc):** Mức độ phản ánh chính xác của các độ đo lựa chọn (Cosine Semantic Similarity qua mô hình nhúng `all-MiniLM-L6-v2` và Executable Syntax Rate qua Static Validation) đối với chất lượng kiểm thử BDD thực tế.
*   **Conclusion Validity (Tính hợp lệ kết luận):** Tính đúng đắn của các kết luận rút ra từ các phép kiểm định thống kê (Wilcoxon Signed-Rank Test và Binomial Exact Test) với cỡ mẫu 100 mẫu ở mức ý nghĩa $\alpha = 0.05$.

### 5.4. Kế hoạch thời gian và Tài nguyên (Timeline and Resource Plan)
*   **Timeline:** Phác thảo tiến trình thực hiện thực nghiệm (Chuẩn bị dữ liệu, Tinh chỉnh LoRA, Chạy mô hình sinh kết quả, Thực hiện kiểm định tĩnh kép, Tính toán độ tương đồng và Phân tích thống kê).
*   **Resource Plan:** Mô tả tài nguyên tính toán cần thiết (ví dụ: GPU Google Colab Pro / Kaggle cho LoRA Fine-tuning; API Keys cho GPT-4o) và công cụ phần mềm (Hugging Face Libraries, Python `ast`, Gherkin Parser, và thư viện phân tích thống kê `scipy.stats`).
