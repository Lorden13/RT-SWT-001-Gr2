# Tiêu chí Tuyển chọn và Loại trừ (IC/EC Criteria)

Bộ tiêu chí YES/NO dùng để quyết định giữ lại hay loại bỏ các bài báo trong nghiên cứu Systematic Literature Review (SLR).

---

## 1. Tiêu chí tuyển chọn (Inclusion Criteria - IC)
Để được giữ lại, bài nghiên cứu phải thỏa mãn tất cả các tiêu chí sau:

- **IC1 (Language):** Viết bằng tiếng Anh.
  - *Ví dụ:* Các bài báo khoa học xuất bản trên các tạp chí quốc tế viết hoàn toàn bằng tiếng Anh sẽ được nhận. Bài báo viết bằng tiếng Bồ Đào Nha hoặc tiếng Trung sẽ bị loại bỏ.
- **IC2 (Timeline):** Xuất bản từ năm 2018 trở về sau (đảm bảo tính cập nhật công nghệ trong lĩnh vực LLM và BDD).
  - *Ví dụ:* Các bài báo xuất bản từ 2018, 2024, 2025, 2026 sẽ được giữ lại. Các bài báo từ 2017 trở về trước sẽ bị loại bỏ.
- **IC3 (Peer-reviewed):** Được xuất bản thông qua các kênh có phản biện khoa học (Peer-reviewed như các Journal, Conference thuộc IEEE, ACM, Springer, ScienceDirect, hoặc các bản preprint học thuật uy tín trên arXiv).
  - *Ví dụ:* Bài báo đăng tại hội nghị IEEE/ACM International Conference on Software Engineering (ICSE) sẽ được giữ lại. Bài viết trên blog công nghệ cá nhân hoặc LinkedIn sẽ bị loại bỏ.
- **IC4 (Context):** Nội dung về ứng dụng LLM/NLP để tự động sinh kịch bản kiểm thử (Automated Test Generation), sinh kịch bản Gherkin, hoặc phát triển dựa trên hành vi BDD.
  - *Ví dụ:* Nghiên cứu sử dụng GPT-4 để sinh kịch bản kiểm thử Gherkin từ user stories.
- **IC5 (Empirical):** Có kết quả thực nghiệm rõ ràng bằng con số cụ thể (không chỉ đơn thuần là bài khảo sát ý kiến hoặc bài thảo luận lý thuyết).
  - *Ví dụ:* Nghiên cứu báo cáo tỷ lệ thực thi thành công của kịch bản sinh ra đạt 94%.

---

## 2. Tiêu chí loại trừ (Exclusion Criteria - EC)
Bài nghiên cứu sẽ bị loại ngay lập tức nếu thỏa mãn bất kỳ tiêu chí nào sau đây:

- **EC1 (Duplicate):** Bài nghiên cứu bị trùng lặp với các bài báo khác đã được đưa vào danh sách trước đó.
  - *Ví dụ:* Bài báo xuất hiện cả trong kết quả tìm kiếm của String A và String B sẽ bị loại bỏ bản sao trùng lặp, chỉ giữ lại một bản ghi duy nhất.
- **EC2 (Access):** Không tải được toàn văn tài liệu (No PDF / Full-text) dưới dạng công khai hoặc thông qua các tài khoản học thuật liên kết.
  - *Ví dụ:* Bài báo yêu cầu trả phí để đọc toàn văn và không thể truy cập qua thư viện trường học hoặc ResearchGate.
- **EC3 (Short):** Thuộc dạng Poster, bản tóm tắt mở rộng (Extended Abstract), hoặc có dung lượng quá ngắn (dưới 4 trang), thiếu thông tin chi tiết về phương pháp thực nghiệm.
  - *Ví dụ:* Extended abstract dài 2 trang trình bày ý tưởng sơ bộ tại một hội thảo khoa học sẽ bị loại bỏ.
- **EC4 (Scope):** Nội dung chỉ bàn về chạy test/bảo trì test (Test execution / Test maintenance), không đề cập hoặc phân tích về việc sinh ca kiểm thử tự động (Test generation) từ User Stories hoặc đặc tả yêu cầu.
  - *Ví dụ:* Bài báo nghiên cứu cách tối ưu hóa tốc độ chạy các kịch bản Gherkin sẵn có trong hệ thống CI/CD mà không nói về cách tự động tạo ra chúng sẽ bị loại bỏ.
