import os
import sys
import pandas as pd
from model import WineQualityPredictor

def load_processed_data(file_path):
    if not os.path.exists(file_path):
        print(f"[!] Không tìm thấy file dữ liệu sạch tại: {file_path}")
        print("[*] Vui lòng chạy file notebook EDA trước hoặc kiểm tra lại đường dẫn.")
        return None
    return pd.read_csv(file_path)

def main():
    print("=============================================================")
    print("     HỆ THỐNG PHÂN TÍCH & BƠM RƯỢU VANG TỰ ĐỘNG (NHÓM 6)     ")
    print("=============================================================\n")
    
    # Đường dẫn file dữ liệu sau khi chạy xong EDA
    processed_file = "../data/processed/winequality-red-cleaned.csv"
    
    # Giả lập đọc dữ liệu sạch (nếu có) để lấy mẫu test ngẫu nhiên
    df = load_processed_data(processed_file)
    
    # Khởi tạo mô hình dự đoán từ dữ liệu phân tích hóa học
    predictor = WineQualityPredictor()
    
    # Thiết lập mẫu kiểm thử mặc định từ thống kê EDA (nếu không load được file)
    sample_wine = {
        'fixed_acidity': 7.4,
        'volatile_acidity': 0.70,
        'citric_acid': 0.00,
        'residual_sugar': 1.9,
        'chlorides': 0.076,
        'free_sulfur_dioxide': 11.0,
        'total_sulfur_dioxide': 34.0,
        'density': 0.9978,
        'pH': 3.51,
        'sulphates': 0.56,
        'alcohol': 9.4
    }
    
    if df is not None:
        print(f"[✓] Tải thành công dữ liệu sạch. Tổng số mẫu khả dụng: {len(df)}")
        # Lấy ngẫu nhiên 1 mẫu trong tập dữ liệu để test hệ thống bơm rượu
        random_row = df.sample(n=1).iloc[0]
        sample_wine = {
            'fixed_acidity': random_row['fixed acidity'],
            'volatile_acidity': random_row['volatile acidity'],
            'citric_acid': random_row['citric acid'],
            'residual_sugar': random_row['residual sugar'],
            'chlorides': random_row['chlorides'],
            'free_sulfur_dioxide': random_row['free sulfur dioxide'],
            'total_sulfur_dioxide': random_row['total sulfur dioxide'],
            'density': random_row['density'],
            'pH': random_row['pH'],
            'sulphates': random_row['sulphates'],
            'alcohol': random_row['alcohol']
        }
        print("[*] Đã trích xuất ngẫu nhiên một mẫu rượu từ bộ dữ liệu đã xử lý để chạy thử.")
    else:
        print("[!] Không có file dữ liệu thực tế. Hệ thống chuyển sang chế độ GIẢ LẬP với mẫu chuẩn EDA.")

    print("\n--- THÔNG SỐ HÓA HỌC CỦA MẪU RƯỢU ĐANG KIỂM TRA ---")
    for key, val in sample_wine.items():
        print(f" • {key.replace('_', ' ').title():<22}: {val}")
        
    print("\n--- BẮT ĐẦU QUY TRÌNH PHÂN TÍCH CHẤT LƯỢNG ---")
    predicted_quality = predictor.predict(sample_wine)
    print(f"[✓] Dự đoán điểm chất lượng (Quality Score): {predicted_quality}/8")
    
    # Dựa vào điểm chất lượng để đưa ra hành động điều khiển van bơm rượu
    print("\n--- KẾT QUẢ ĐIỀU KHIỂN HỆ THỐNG BƠM RƯỢU ---")
    if predicted_quality >= 7:
        print(f" ĐÁNH GIÁ: Rượu Thượng Hạng (Chất lượng cao).")
        print(f" HÀNH ĐỘNG : Kích hoạt [VAN SỐ 1] -> Bơm vào thùng đóng chai Cao Cấp (Premium Export).")
    elif predicted_quality >= 5:
        print(f" ĐÁNH GIÁ: Rượu Tiêu Chuẩn (Chất lượng đạt chuẩn phổ thông).")
        print(f" HÀNH ĐỘNG : Kích hoạt [VAN SỐ 2] -> Bơm vào thùng đóng chai Phổ Thông (Standard Commercial).")
    else:
        print(f" ĐÁNH GIÁ: Rượu Kém Chất Lượng / Lỗi Men (Nồng độ Axit bay hơi cao hoặc thiếu Cồn).")
        print(f" HÀNH ĐỘNG : Kích hoạt [VAN SỐ 3] -> Chuyển hướng sang bể lọc lại hoặc làm Giấm (Reject/Reprocess).")
        
    print("\n=============================================================")
    print(" Quy trình hoàn tất an toàn. Hệ thống sẵn sàng cho mẫu tiếp theo.")
    print("=============================================================")

if __name__ == '__main__':
    main()
