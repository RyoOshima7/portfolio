import csv
from pathlib import Path

def calculate_average_satisfaction(file_path):
    total = 0
    count = 0

    with open(file_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        for row in reader:
            value = row["satisfaction"]

            # 空文字なら未入力として飛ばす
            if value == "":
                continue

            score = int(value)
            total += score
            count += 1

    # 有効なデータが 0 件なら 0 を返す
    if count == 0:
        return 0

    return total / count

try:
    # このPythonファイルが置かれている場所を基準にする
    base_dir = Path(__file__).resolve().parent

    # 絶対パスを作る
    csv_path = base_dir.parent / "data" / "survey_basic.csv"

    result = calculate_average_satisfaction(csv_path)
    print(f"満足度平均: {result:.2f}")
except FileNotFoundError:
    print(f"ファイルが見つかりません: {csv_path}")
except ValueError:
    print("satisfaction列に整数ではない値があります。")
