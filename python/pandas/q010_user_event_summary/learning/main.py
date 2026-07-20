from pathlib import Path

import pandas as pd

# main.py があるlearningフォルダを取得する
base_dir = Path(__file__).resolve().parent

# CSVファイルの場所を指定する
csv_path = base_dir.parent / "data" / "user_events.csv"

# CSVファイルを読み込む
df = pd.read_csv(csv_path)

#　読み込めているか確認する
print(df.head())

# 行動種類別の発生件数を集計する
event_counts = df["event"].value_counts()

print("=== 行動種類別の発生件数 ===")
print(event_counts)

# ページ別・行動種類別の発生件数を集計する
page_event_counts = pd.crosstab(
    index=df["page"],
    columns=df["event"],
)

print("=== ページ別・行動種類別の発生件数 ===")
print(page_event_counts)