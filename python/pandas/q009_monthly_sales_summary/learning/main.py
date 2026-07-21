from pathlib import Path

import pandas as pd

# main.pyがあるlearningフォルダを取得する
base_dir = Path(__file__).resolve().parent

# CSVファイルの場所を指定する
csv_path = base_dir.parent / "data" / "sales_monthly.csv"

# CSVファイルを読み込む
df = pd.read_csv(csv_path)

# データの先頭とデータ型を確認する
print("【データの先頭】")
print(df.head())

print("\n【データの基本情報】")
df.info()

# date列を日付型に変換する
df["date"] = pd.to_datetime(df["date"])

# 注文ごとの売上金額を計算する
df["sales_amount"] = df["quantity"] * df["price"]

# 年月を表す列を作成する
df["month"] = df["date"].dt.to_period("M")

# 月別の合計売上を集計する
monthly_sales = (
    df.groupby("month", as_index=False)["sales_amount"].sum()
)

print("\n【月別の合計売上】")
print(monthly_sales)