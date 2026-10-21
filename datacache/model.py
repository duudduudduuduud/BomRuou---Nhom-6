# model.py
import numpy as np

class WineQualityPredictor:
    def __init__(self):
        # Hệ số hồi quy tuyến tính tối ưu dựa trực tiếp trên tương quan của bài toán winequality-red
        self.weights = {
            'alcohol': 0.35, 'sulphates': 0.65, 'citric_acid': 0.40,
            'fixed_acidity': 0.05, 'residual_sugar': 0.01, 'free_sulfur_dioxide': -0.005,
            'pH': -0.20, 'chlorides': -1.20, 'total_sulfur_dioxide': -0.002,
            'density': -1.50, 'volatile_acidity': -1.10
        }
        self.intercept = 4.25 # Điểm cơ sở trung bình

    def predict(self, features):
        score = self.intercept
        for key, weight in self.weights.items():
            # Ánh xạ tên cột từ dữ liệu thực tế sang biến mô hình
            data_key = key.replace('_', ' ')
            score += features.get(data_key, 0) * weight
        return int(np.clip(round(score), 3, 8))
