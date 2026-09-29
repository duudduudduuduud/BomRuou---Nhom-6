# Nhóm 6 - Dự Án Phân Loại Và Dự Đoán Chất Lượng Rượu Vang (Wine Quality Prediction)

## 1. Thành Viên Nhóm

| STT | Họ và Tên | Mã Sinh Viên | Vai trò / Nhiệm vụ chính |
| :---: | :--- | :---: | :--- |
| 1 | [Hoàng Trường Huy] | [BIT250172] | Trưởng nhóm, Xây dựng mô hình Machine Learning |
| 2 | [Khúc Đình Hưng] | [BIT253642] | Tiền xử lý dữ liệu & Phân tích khám phá (EDA) |
| 3 | [Nguyễn Minh Hiếu] | [BIT250135] | Đánh giá, kiểm thử tối ưu hóa mô hình & Viết tài liệu |
| 4 | [Hoàng Nguyên Khôi] | [BIT250199] | Phát triển giao diện Demo / API triển khai |
| 5 | [Trần Đăng Khôi] | [BIT250201] | Chuyên viên Dữ liệu rượu & Giải thích mô hình (XAI / Domain Specialist) |

---

## 2. Giới Thiệu & Mục Tiêu Triển Khai

* **Tên đề tài**: Phân loại và dự đoán chất lượng các loại rượu vang của Việt Nam nói riêng và thế giới nói chung.
* **Mục tiêu**:
  * Ứng dụng các thuật toán Học máy (Machine Learning) để nhận diện mối tương quan giữa các thành phần hóa lý và đánh giá cảm quan chất lượng rượu.
  * Dự đoán chính xác điểm số chất lượng hoặc phân loại hạng rượu (Kém, Trung bình, Thượng hạng), hỗ trợ các cơ sở sản xuất rượu vang tối ưu hóa quy trình lên men và phối trộn.
  * Mở rộng đối sánh giữa các dòng vang tiêu chuẩn quốc tế và các dòng vang đặc trưng của Việt Nam (vang Đà Lạt, vang nho Ninh Thuận...).

---

## 3. Mô Tả Dữ Liệu

Tập dữ liệu nền tảng sử dụng trong nghiên cứu khởi tạo được trích xuất từ tệp `winequality-red.csv` gồm 12 thuộc tính hóa lý đo lường trên các mẫu rượu vang đỏ:

* **Biến mục tiêu (Target)**:
  * `quality`: Điểm đánh giá chất lượng cảm quan của chuyên gia (thang điểm nguyên từ 0 đến 10).
* **Các đặc trưng hóa lý đầu vào (Features)**:
  * `fixed acidity`: Độ axit cố định (hàm lượng axit tartaric).
  * `volatile acidity`: Hàm lượng axit dễ bay hơi (axit axetic).
  * `citric acid`: Lượng axit xitric giúp tăng độ tươi mát của vang.
  * `residual sugar`: Lượng đường dư còn sót lại sau quá trình lên men.
  * `chlorides`: Hàm lượng muối clorua trong rượu.
  * `free sulfur dioxide`: Lượng lưu huỳnh dioxit tự do (chống oxy hóa và vi khuẩn).
  * `total sulfur dioxide`: Tổng lượng lưu huỳnh dioxit.
  * `density`: Khối lượng riêng / tỷ trọng của dung dịch rượu.
  * `pH`: Độ pH đo độ kiềm/axit của rượu vang.
  * `sulphates`: Hàm lượng sunfat (chất phụ gia bảo quản).
  * `alcohol`: Nồng độ cồn (% thể tích).

---

## 4. Tech Stack Đề Xuất

* **Ngôn ngữ lập trình**: Python 3.9+
* **Thư viện xử lý & phân tích dữ liệu**:
  * `pandas`, `numpy`: Đọc, làm sạch và biến đổi ma trận dữ liệu.
* **Thư viện trực quan hóa dữ liệu**:
  * `matplotlib`, `seaborn`: Vẽ biểu đồ phân phối, ma trận tương quan (Correlation Matrix) và biểu đồ phân tán (Scatter Matrix).
* **Machine Learning & Modeling**:
  * `scikit-learn`: Xử lý chuẩn hóa (`StandardScaler`), chia tách dữ liệu, huấn luyện các thuật toán (Random Forest, SVM, Logistic Regression, Decision Tree).
  * `xgboost`, `lightgbm`: Các thuật toán Gradient Boosting nâng cao hiệu năng dự đoán.
* **Giao diện & Triển khai (Deployment)**:
  * `Streamlit` hoặc `Gradio`: Xây dựng Dashboard tương tác nhanh cho người dùng nhập thông số và nhận kết quả dự đoán.
  * `FastAPI` / `Flask` (tùy chọn): Đóng gói mô hình thành dịch vụ RESTful API.

---

## 5. Kế Hoạch Triển Khai Dự Án

1. **Khám phá và Tiền xử lý dữ liệu (Data Preprocessing & EDA)**:
   * Kiểm tra giá trị rỗng (NaN/Missing values), phát hiện và xử lý ngoại lai (Outliers).
   * Trực quan hóa tương quan giữa nồng độ cồn, độ pH, độ axit với điểm số chất lượng (`quality`).
   * Chuẩn hóa thang đo các thuộc tính bằng `StandardScaler`.
2. **Kỹ thuật đặc trưng (Feature Engineering)**:
   * Chuyển bài toán dự đoán điểm số liên tục (Regression) sang bài toán phân loại nhị phân/đa lớp (Classification: Ví dụ: `quality < 5` là Kém, `5 - 6` là Trung bình, `>= 7` là Tốt).
   * Cân bằng tập dữ liệu bằng kỹ thuật SMOTE nếu có hiện tượng mất cân bằng lớp.
3. **Huấn luyện và Tối ưu mô hình**:
   * Thử nghiệm nhiều thuật toán phân loại và hồi quy.
   * Tinh chỉnh siêu tham số (Hyperparameter Tuning) thông qua `GridSearchCV` hoặc `RandomizedSearchCV` với phương pháp K-Fold Cross-Validation.
4. **Đánh giá và Đối sánh**:
   * Đánh giá hiệu suất phân loại qua Accuracy, Precision, Recall, F1-Score và ROC-AUC.
   * Phân tích mức độ quan trọng của đặc trưng (Feature Importance) để rút ra các chỉ số ảnh hưởng lớn nhất đến vị giác rượu vang.
5. **Đóng gói và Triển khai**:
   * Lưu trữ mô hình tối ưu bằng `joblib` hoặc `pickle`.
   * Xây dựng giao diện web cho phép nhập các chỉ số hóa lý và trả về dự đoán tức thì.

---

## 6. Chức Năng Chính Của Hệ Thống

* **Phân tích thăm dò tự động**: Hiển thị biểu đồ phân phối đặc trưng và bản đồ nhiệt độ tương quan của các chỉ số hóa lý.
* **Dự đoán chất lượng theo mẫu**: Người dùng nhập thủ công 11 chỉ số hóa lý của một chai rượu bất kỳ để hệ thống xếp loại chất lượng tương ứng.
* **Dự đoán hàng loạt (Batch Prediction)**: Hỗ trợ tải lên tệp CSV/Excel chứa danh sách nhiều lô rượu để xuất kết quả phân loại đồng loạt.
* **Khuyến nghị điều chỉnh thành phần**: Đưa ra nhận xét các thành phần cần cải thiện (ví dụ: giảm độ axit bay hơi, điều chỉnh nồng độ cồn) để nâng hạng chất lượng sản phẩm.

---

## 7. Cấu Trúc Thư Mục Dự Án

```text
├── data/
│   ├── raw/                   # Dữ liệu gốc (winequality-red.csv, dữ liệu vang Việt Nam bổ sung)
│   └── processed/             # Dữ liệu đã làm sạch và chuẩn hóa
├── notebooks/
│   ├── 01_exploratory_data_analysis.ipynb   # Phân tích EDA, biểu đồ tương quan
│   └── 02_model_training.ipynb              # Huấn luyện và đánh giá mô hình
├── src/
│   ├── __init__.py
│   ├── data_loader.py         # Module đọc và tải dữ liệu
│   ├── preprocessor.py        # Module xử lý dữ liệu và scaling
│   └── train.py               # Script huấn luyện và lưu trữ mô hình
├── models/
│   └── best_model.pkl         # Tệp mô hình tốt nhất sau khi tinh chỉnh
├── app/
│   ├── app.py                 # File chạy ứng dụng giao diện (Streamlit/Gradio)
│   └── utils.py               # Hàm phụ trợ dự đoán cho giao diện
├── requirements.txt           # Danh mục thư viện và phiên bản cần thiết
├── .gitignore
└── README.md
