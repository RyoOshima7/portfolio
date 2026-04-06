import csv
from pathlib import Path

def calculate_total_sales(file_path):
    # 総売上を入れる箱を用意する
    total_sales = 0

    # UTF-8 で CSV ファイルを開く
    with open(file_path, "r", encoding="utf-8") as f:
        # 1行目の見出しを使って、列名で値を取り出せるようにする
        reader = csv.DictReader(f)

        # 1行ずつ順番に取り出して処理する
        for row in reader:
            # 文字列で読まれるので int に変換する
            quantity = int(row["quantity"])
            unit_price = int(row["unit_price"])

            # その行の売上 = 数量 × 単価
            line_sales = quantity * unit_price

            # 総売上に足す
            total_sales += line_sales

    # 最後に合計を返す
    return total_sales

try:
    # main.py があるフォルダを取得する
    base_dir = Path(__file__).resolve().parent

    # main.py の1つ上のフォルダにある data/sales_basic.csv を指定する
    csv_path = base_dir.parent / "data" / "sales_basic.csv"

    result = calculate_total_sales(csv_path)
    print(f"総売上: {result}円")
except FileNotFoundError:
    print("ファイルが見つかりません。")
except ValueError:
    print("数値の変換に失敗しました。")