import os
import warnings
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from pathlib import Path
from sklearn.preprocessing import StandardScaler

warnings.filterwarnings('ignore')

# Đảm bảo đường dẫn luôn trỏ về thư mục gốc dự án
PROJECT_ROOT = Path(__file__).resolve().parent.parent
if not Path('data/raw/winequality-red.csv').exists() and (PROJECT_ROOT / 'data/raw/winequality-red.csv').exists():
    os.chdir(PROJECT_ROOT)

# ---------------------------------------------------------
# TẠO CÁC THƯ MỤC CẦN THIẾT
# ---------------------------------------------------------
os.makedirs('assets_bieu_do', exist_ok=True)
os.makedirs('data/processed', exist_ok=True)

# Cấu hình giao diện đồ thị
sns.set_theme(style="whitegrid", palette="muted")
plt.rcParams["figure.figsize"] = (10, 6)
plt.rcParams["font.size"] = 11

print("Thư viện đã được tải thành công!")

# Load dataset
data_path = 'data/raw/winequality-red.csv'

# Tải dữ liệu (kiểm tra delimiter tự động hoặc chỉ định sep=';')
try:
    df = pd.read_csv(data_path, sep=';')
    if df.shape[1] == 1: # Nếu dùng sai sep, chỉ có 1 cột gom lại
        df = pd.read_csv(data_path, sep=',')
except Exception as e:
    print(f"Lỗi tải dữ liệu: {e}")

print(f"Kích thước tập dữ liệu: {df.shape[0]} dòng, {df.shape[1]} cột.\n")
df.head()

# Thông tin tổng quan về các cột và kiểu dữ liệu
print("=== Thông tin dữ liệu (df.info()) ===")
df.info()

print("\n=== Kiểm tra giá trị khuyết thiếu (Missing Values) ===")
missing_summary = pd.DataFrame({
    'Missing_Count': df.isnull().sum(),
    'Missing_Percentage (%)': (df.isnull().sum() / len(df)) * 100
})
print(missing_summary)

df.describe().T[['mean', 'std', 'min', '25%', '50%', '75%', 'max']]

# ---------------------------------------------------------
# 1. BOXPLOTS CÁC ĐẶC TRƯNG & LƯU HÌNH 1
# ---------------------------------------------------------
features = df.columns[:-1] # Loại bỏ cột 'quality'

plt.figure(figsize=(15, 12))
for i, col in enumerate(features, 1):
    plt.subplot(4, 3, i)
    sns.boxplot(y=df[col], color='skyblue')
    plt.title(f'Boxplot: {col}')
    plt.tight_layout()

# Save Figure 1
plt.savefig('assets_bieu_do/01_feature_boxplots.png', bbox_inches='tight', dpi=300)
plt.close()

# Hàm tính số lượng Outliers theo phương pháp IQR (Interquartile Range)
def detect_outliers_iqr(data, column):
    Q1 = data[column].quantile(0.25)
    Q3 = data[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    outliers = data[(data[column] < lower_bound) | (data[column] > upper_bound)]
    return len(outliers), lower_bound, upper_bound

print("=== Thống kê Outliers theo phương pháp IQR ===")
for col in features:
    count, lb, ub = detect_outliers_iqr(df, col)
    pct = (count / len(df)) * 100
    print(f"{col:22s}: {count:3d} outliers ({pct:5.2f}%) | Ngưỡng: [{lb:.2f}, {ub:.2f}]")

# Kỹ thuật Capping Outliers (Winsorization thủ công bằng IQR)
df_capped = df.copy()

for col in features:
    Q1 = df_capped[col].quantile(0.25)
    Q3 = df_capped[col].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    
    # Clip giá trị trong phạm vi [lower_bound, upper_bound]
    df_capped[col] = np.clip(df_capped[col], lower_bound, upper_bound)

print("Đã thực hiện Capping Outliers thành công!")

# ---------------------------------------------------------
# 2. PHÂN PHỐI CỦA QUALITY & LƯU HÌNH 2
# ---------------------------------------------------------
plt.figure(figsize=(8, 5))
ax = sns.countplot(x='quality', data=df, palette='viridis')
plt.title('Phân phối Điểm số Chất lượng Rượu Vang (Quality)', fontsize=14)
plt.xlabel('Điểm số Quality (3 - 8)')
plt.ylabel('Số lượng mẫu')

# Hiển thị số lượng cụ thể trên từng cột
for p in ax.patches:
    ax.annotate(f'{int(p.get_height())}', (p.get_x() + p.get_width() / 2., p.get_height()),
                ha='center', va='baseline', fontsize=10, color='black', xytext=(0, 5),
                textcoords='offset points')

# Save Figure 2
plt.savefig('assets_bieu_do/02_quality_distribution.png', bbox_inches='tight', dpi=300)
plt.close()

# ---------------------------------------------------------
# 3. MA TRẬN TƯƠNG QUAN & LƯU HÌNH 3
# ---------------------------------------------------------
plt.figure(figsize=(12, 8))
correlation_matrix = df.corr()

sns.heatmap(correlation_matrix, annot=True, fmt='.2f', cmap='coolwarm', linewidths=0.5)
plt.title('Ma trận Tương quan Tương hỗ (Correlation Heatmap)', fontsize=14)

# Save Figure 3
plt.savefig('assets_bieu_do/03_correlation_heatmap.png', bbox_inches='tight', dpi=300)
plt.close()

# ---------------------------------------------------------
# 4. MỨC ĐỘ TƯƠNG QUAN VỚI QUALITY & LƯU HÌNH 4
# ---------------------------------------------------------
corr_with_quality = correlation_matrix['quality'].drop('quality').sort_values(ascending=False)

plt.figure(figsize=(10, 5))
corr_with_quality.plot(kind='bar', color=['g' if x > 0 else 'r' for x in corr_with_quality])
plt.title('Mức độ tương quan của các chỉ số với Quality', fontsize=14)
plt.ylabel('Hệ số tương quan Pearson')
plt.axhline(0, color='black', linewidth=0.8)

# Save Figure 4
plt.savefig('assets_bieu_do/04_correlation_with_quality.png', bbox_inches='tight', dpi=300)
plt.close()

# ---------------------------------------------------------
# 5. CÁC HÓA CHẤT CHÍNH VS QUALITY & LƯU HÌNH 5
# ---------------------------------------------------------
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Alcohol vs Quality
sns.boxplot(x='quality', y='alcohol', data=df, ax=axes[0, 0], palette='Blues')
axes[0, 0].set_title('Alcohol vs Quality')

# Volatile Acidity vs Quality
sns.boxplot(x='quality', y='volatile acidity', data=df, ax=axes[0, 1], palette='Reds')
axes[0, 1].set_title('Volatile Acidity vs Quality')

# Sulphates vs Quality
sns.boxplot(x='quality', y='sulphates', data=df, ax=axes[1, 0], palette='Greens')
axes[1, 0].set_title('Sulphates vs Quality')

# Citric Acid vs Quality
sns.boxplot(x='quality', y='citric acid', data=df, ax=axes[1, 1], palette='Oranges')
axes[1, 1].set_title('Citric Acid vs Quality')

plt.tight_layout()

# Save Figure 5
plt.savefig('assets_bieu_do/05_key_chemical_features_vs_quality.png', bbox_inches='tight', dpi=300)
plt.close()

# ---------------------------------------------------------
# CHUẨN HÓA & LƯU TẬP DỮ LIỆU ĐÃ XỬ LÝ
# ---------------------------------------------------------
df_processed = df_capped.copy()
df_processed['target'] = (df_processed['quality'] >= 7).astype(int)

print("Tỷ lệ phân phối lớp mục tiêu (Binary Target):")
print(df_processed['target'].value_counts(normalize=True) * 100)

# Chuẩn hóa thang đo các đặc trưng (Standardization)
X = df_processed.drop(columns=['quality', 'target'])
y = df_processed['target']

scaler = StandardScaler()
X_scaled = pd.DataFrame(scaler.fit_transform(X), columns=X.columns)

# Kiểm tra dữ liệu sau chuẩn hóa (Mean ~ 0, Std ~ 1)
X_scaled.describe().round(2).T[['mean', 'std']]

# Lưu tập dữ liệu đã làm sạch & chuẩn hóa ra file CSV mới
cleaned_data_path = os.path.join('data/processed', 'winequality-red-cleaned.csv')
df_processed.to_csv(cleaned_data_path, index=False)

print(f"Đã lưu thành công tập dữ liệu sạch tại: {cleaned_data_path}")
print("Tất cả hình ảnh đã được lưu vào thư mục 'assets_bieu_do/'!")
