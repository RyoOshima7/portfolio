products = [
    ["Apple", 120, 10],
    ["Banana", 80, 15],
    ["Orange", 100, 8],
]

def calculate_inventory_total(product_list):
    # 合計在庫金額を入れる変数
    total_value = 0
    
    # 1商品ずつ取り出す
    for product in product_list:
        # 商品情報を取り出す
        name = product[0]
        price = product[1]
        stock = product[2]

        # 1つの商品について在庫金額を計算
        item_total = price * stock

        # 合計に足す
        total_value += item_total
    
    # 最終的な合計金額を返す
    return total_value

# 商品一覧を表示
print("商品一覧")
for product in products:
    print(f"商品名: {product[0]}, 単価: {product[1]}, 在庫数: {product[2]}")

# 合計在庫金額を計算して表示
result = calculate_inventory_total(products)
print(f"合計在庫金額: {result}円") 