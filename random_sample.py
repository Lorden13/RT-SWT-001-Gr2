import pandas as pd

# Đọc file Excel
df = pd.read_excel("Requirements.xlsx")

# Random 100 mẫu theo proposal
sample_df = df.sample(
    n=100,
    random_state=42,
    replace=False
)

# Xuất file
sample_df.to_excel("sample_100.xlsx", index=False)
sample_df.to_csv("sample_100.csv", index=False)

print(f"Đã tạo {len(sample_df)} mẫu")