import csv
from pathlib import Path

def summarize_by_product(file_path):
    # TODO:
    # product_sales = {} を作る
    product_sales = {}

    # 商品ごとに売上を足し込む
    with open(file_path, "r" ,encoding="utf-8") as f:
        reader = csv.DictReader(f)

        for row in reader:
            product = row["product"]
            quantity = int(row["quantity"])
            unit_price = int(row["unit_price"])
            sales = quantity * unit_price

            if product not in product_sales:
                product_sales[product] = 0
            
            product_sales[product] += sales

         
    # 最後に辞書を返す
    return product_sales

try:

    base_dir = Path(__file__).resolve().parent
    
    csv_path = base_dir.parent / "data" / "sales_by_product.csv"

    result = summarize_by_product(csv_path)

    # TODO:
    # result.items() を売上の大きい順に並び替えて表示する
    sorted_result = sorted(result.items(), key=lambda x: x[1], reverse=True)

    for product, sales in sorted_result:
        print(f"{product}: {sales}円")

except FileNotFoundError:
    print(f"ファイルが見つかりません: {csv_path}")
