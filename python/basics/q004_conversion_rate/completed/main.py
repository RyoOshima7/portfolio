import csv
from pathlib import Path

def calculate_rates(file_path):
    view_count = 0
    click_count = 0
    purchase_count = 0

    with open(file_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        for row in reader:
            event = row["event"]

            if event == "view":
                view_count += 1
            elif event == "click":
                click_count += 1
            elif event == "purchase":
                purchase_count += 1

    # view が 0 だと割り算エラーになるので先に確認する
    if view_count == 0:
        return {"click_rate": 0, "purchase_rate": 0}

    click_rate = click_count / view_count
    purchase_rate = purchase_count / view_count

    return {
        "view": view_count,
        "click": click_count,
        "purchase": purchase_count,
        "click_rate": click_rate,
        "purchase_rate": purchase_rate,
    }

try:
    # このPythonファイルが置かれている場所を基準にする
    base_dir = Path(__file__).resolve().parent

    # 絶対パスを作る
    csv_path = base_dir.parent / "data" / "user_log_rate.csv"

    result = calculate_rates(csv_path)

    print(f"view数: {result['view']}")
    print(f"click数: {result['click']}")
    print(f"purchase数: {result['purchase']}")
    print(f"click率: {result['click_rate']:.2f}")
    print(f"purchase率: {result['purchase_rate']:.2f}")
except FileNotFoundError:
    print(f"ファイルが見つかりません: {csv_path}")
