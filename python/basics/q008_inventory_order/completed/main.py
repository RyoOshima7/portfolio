products = [
    ["Apple", 120, 10],
    ["Banana", 80, 15],
    ["Orange", 100, 8],
]

def order_product(product_list, target_name, order_quantity):
    # 商品一覧を順番に確認する
    for product in product_list:
        name = product[0]
        price = product[1]
        stock = product[2]

        # 入力された商品名と一致するか確認する
        if name == target_name:
            # 在庫が足りるか先に確認する
            if stock >= order_quantity:
                # 在庫を減らす
                product[2] -= order_quantity

                # 合計金額を計算する
                total_price = price * order_quantity
                return total_price
            else:
                return "在庫不足"

    # 最後まで見つからなければ商品なし
    return None

print("注文できる商品")
for product in products:
    print(f"{product[0]} / 単価:{product[1]}円 / 在庫:{product[2]}")

product_name = input("商品名を入力してください: ")

try:
    quantity = int(input("注文数を入力してください: "))
    result = order_product(products, product_name, quantity)

    if result == "在庫不足":
        print("在庫が足りません。")
    elif result is None:
        print("商品が見つかりません。")
    else:
        print(f"合計金額: {result}円")
        print("注文後の在庫")
        for product in products:
            print(f"{product[0]} / 在庫:{product[2]}")
except ValueError:
    print("注文数は整数で入力してください。")
