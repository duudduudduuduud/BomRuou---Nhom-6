<table>
  <thead>
    <tr style="background-color: #f8f9fa;">
      <th style="border: 1px solid #e1e4e8; padding: 12px; text-align: left; width: 30%;">Ý tưởng trong bài trình bày</th>
      <th style="border: 1px solid #e1e4e8; padding: 12px; text-align: left; width: 70%;">Ứng dụng vào dự án của nhóm</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border: 1px solid #e1e4e8; padding: 12px; vertical-align: top; font-weight: bold;">Nạp tệp dữ liệu vào công cụ</td>
      <td style="border: 1px solid #e1e4e8; padding: 12px; vertical-align: top;">Đọc <code>winequality-red.csv</code>, kiểm tra tên cột, kiểu dữ liệu và số dòng.</td>
    </tr>
    <tr>
      <td style="border: 1px solid #e1e4e8; padding: 12px; vertical-align: top; font-weight: bold;">Lọc dữ liệu theo tiêu chí</td>
      <td style="border: 1px solid #e1e4e8; padding: 12px; vertical-align: top;">Cho phép chọn rượu theo khoảng cồn, pH, axit hoặc điểm chất lượng để phân tích.</td>
    </tr>
    <tr>
      <td style="border: 1px solid #e1e4e8; padding: 12px; vertical-align: top; font-weight: bold;">Tạo nhiều cách phân tích từ một nền tảng chung</td>
      <td style="border: 1px solid #e1e4e8; padding: 12px; vertical-align: top;">Xây dựng pipeline chung cho tiền xử lý, EDA, huấn luyện và đánh giá mô hình.</td>
    </tr>
    <tr>
      <td style="border: 1px solid #e1e4e8; padding: 12px; vertical-align: top; font-weight: bold;">Hiển thị kết quả phân tích</td>
      <td style="border: 1px solid #e1e4e8; padding: 12px; vertical-align: top;">Tạo biểu đồ phân phối, tương quan, chất lượng theo đặc trưng và bảng so sánh mô hình.</td>
    </tr>
    <tr>
      <td style="border: 1px solid #e1e4e8; padding: 12px; vertical-align: top; font-weight: bold;">Mở rộng khi có nhu cầu mới</td>
      <td style="border: 1px solid #e1e4e8; padding: 12px; vertical-align: top;">Tách các bước thành hàm hoặc module để thêm mô hình, biểu đồ hay chức năng dự đoán mà không viết lại toàn bộ chương trình.</td>
    </tr>
  </tbody>
</table>

Quy trình đề xuất
1.Tải dữ liệu và kiểm tra cấu trúc. Xác nhận cột mục tiêu là quality, kiểm tra giá trị thiếu, bản ghi trùng và kiểu dữ liệu.

2.Khám phá dữ liệu. Xem phân phối từng đặc trưng, phân phối điểm quality, tương quan giữa các biến và số mẫu ở mỗi lớp.

3.Chốt cách đặt mục tiêu. Thử dự đoán điểm chất lượng bằng hồi quy, hoặc chuyển điểm thành nhóm chất lượng để phân loại. Nêu rõ quy tắc chia nhóm.

4.Tạo pipeline tiền xử lý và mô hình. Đặt các bước biến đổi dữ liệu cùng mô hình trong pipeline để quy trình huấn luyện và dự đoán nhất quán.

5.So sánh mô hình phù hợp. Dùng các chỉ số đánh giá phù hợp với bài toán. Với phân loại, xem F1-score và ma trận nhầm lẫn bên cạnh Accuracy.

6.Kiểm tra kết quả trên dữ liệu chưa dùng khi huấn luyện. Tránh để cùng một mẫu xuất hiện ở cả tập huấn luyện và tập kiểm tra.

7.Đóng gói demo. Lưu pipeline đã huấn luyện, rồi dùng Streamlit hoặc Gradio để nhận đầu vào và hiển thị dự đoán.

  Cách chia việc giữa các thành viên

Phân công ban đầu của nhóm đã có các vai trò làm sạch dữ liệu, EDA, giao diện/API và pipeline. Để tránh chồng chéo, hãy thống nhất đầu vào/đầu ra của từng phần:

Huy: làm sạch dữ liệu và bàn giao bộ dữ liệu đã kiểm tra cùng quy tắc xử lý.
Hưng và Hiếu: chia EDA thành hai phần, chẳng hạn một người xem phân phối và chất lượng, người còn lại xem tương quan và ngoại lệ.
Khôi: xây dựng giao diện gọi đúng pipeline đã lưu, không tự tiền xử lý khác với lúc huấn luyện.
Đăng Khôi: quản lý pipeline lưu trữ, kiểm tra chất lượng dữ liệu đầu vào và xác nhận kết quả tái lập được.
Mỗi phần nên bàn giao một tệp rõ ràng, chẳng hạn dữ liệu đã xử lý, hình EDA, bảng so sánh mô hình và pipeline đã lưu. Như vậy, thành viên khác có thể dùng kết quả mà không cần đoán cách bạn đã tạo ra nó.

Hai điểm quan trọng để báo cáo chính xác

Thứ nhất, hãy phân biệt “dự đoán” với “khuyến nghị”. Mô hình dự đoán chất lượng từ các đặc trưng trong dữ liệu. Nó không tự chứng minh rằng thay đổi một thành phần cụ thể sẽ làm rượu ngon hơn. Vì vậy, tính năng “khuyến nghị điều chỉnh thành phần” nên được ghi là gợi ý tham khảo dựa trên mô hình, trừ khi nhóm có thiết kế kiểm chứng riêng.

Thứ hai, đừng mặc định SMOTE là cần thiết. Trước tiên, hãy xem số mẫu của từng lớp sau khi chia nhóm chất lượng. Nếu áp dụng SMOTE, chỉ áp dụng trên tập huấn luyện trong từng lượt huấn luyện, không áp dụng trước khi chia tập.
  
Một điểm cần thống nhất trong tài liệu: mô tả của nhóm nói quality từ 0 đến 10, nhưng hãy kiểm tra các giá trị thực tế trong chính tệp CSV và báo cáo đúng phạm vi quan sát được. Tương tự, ghi rõ ngưỡng “Kém / Trung bình / Tốt” mà nhóm chọn, vì cách chia ngưỡng làm thay đổi kết quả phân loại.







