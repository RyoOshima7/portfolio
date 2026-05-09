from pathlib import Path

import pandas as pd


# main.py がある learning フォルダを取得する
base_dir = Path(__file__).resolve().parent

# data/sales_basic.csv の場所を指定する
csv_path = base_dir.parent / "data" / "sales_basic.csv"

# CSVファイルを読み込む
df = pd.read_csv(csv_path)

# データの先頭5行を表示する
print("=== 先頭5行 ===")
print(df.head())

# 列名を表示する
print("=== 列名 ===")
print(df.columns)

# データの基本情報を表示する
print("=== 基本情報 ===")
df.info()

# 数値データの基本統計量を表示する
print("=== 基本統計量 ===")
print(df.describe())
