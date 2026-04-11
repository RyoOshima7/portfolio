products = [
    ["Apple", 120, 10],
    ["Banana", 80, 15],
    ["Orange", 100, 8],
]

def calculate_inventory_total(product_list):
    total_value = 0

    # 1商品ずつ取り出して計算する
    for product in product_list:
        name = product[0]
        price = product[1]
        stock = product[2]

        # 在庫金額 = 単価 × 在庫数
        item_total = price * stock
        total_value += item_total

    return total_value

print("商品一覧")
for product in products:
    print(f"商品名: {product[0]}, 単価: {product[1]}円, 在庫数: {product[2]}")

result = calculate_inventory_total(products)
print(f"合計在庫金額: {result}円")
