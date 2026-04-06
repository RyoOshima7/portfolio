import csv
from pathlib import Path

def summarize_by_product(file_path):
    # 商品ごとの売上を保存する辞書
    product_sales = {}

    with open(file_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        for row in reader:
            product = row["product"]
            quantity = int(row["quantity"])
            unit_price = int(row["unit_price"])
            sales = quantity * unit_price

            # まだ辞書に商品名がなければ 0 で初期化する
            if product not in product_sales:
                product_sales[product] = 0

            # 同じ商品の売上を足していく
            product_sales[product] += sales

    return product_sales

try:
    # このPythonファイルが置かれている場所を基準にする
    base_dir = Path(__file__).resolve().parent

    # 絶対パスを作る
    csv_path = base_dir.parent / "data" / "sales_by_product.csv"

    result = summarize_by_product(csv_path)

    # 辞書.items() は (key, value) の組になる
    # value を基準にして、売上の大きい順に並び替える
    sorted_result = sorted(result.items(), key=lambda x: x[1], reverse=True)

    for product, sales in sorted_result:
        print(f"{product}: {sales}円")

except FileNotFoundError:
    print(f"ファイルが見つかりません: {csv_path}")