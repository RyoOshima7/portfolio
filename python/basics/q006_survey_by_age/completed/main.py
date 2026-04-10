import csv
from pathlib import Path

def summarize_by_age(file_path):
    # 年代ごとの合計点
    age_totals = {}
    # 年代ごとの件数
    age_counts = {}

    with open(file_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        for row in reader:
            age_group = row["age_group"]
            value = row["satisfaction"]

            if value == "":
                continue

            score = int(value)

            if age_group not in age_totals:
                age_totals[age_group] = 0
                age_counts[age_group] = 0

            age_totals[age_group] += score
            age_counts[age_group] += 1

    age_averages = {}

    for age_group in age_totals:
        age_averages[age_group] = age_totals[age_group] / age_counts[age_group]

    return age_averages

try:
    # このPythonファイルが置かれている場所を基準にする
    base_dir = Path(__file__).resolve().parent

    # 絶対パスを作る
    csv_path = base_dir.parent / "data" / "survey_by_age.csv"

    result = summarize_by_age(csv_path)

    for age_group, avg_score in result.items():
        print(f"{age_group}: {avg_score:.2f}")
except FileNotFoundError:
    print(f"ファイルが見つかりません: {csv_path}")
except ValueError:
    print("satisfaction列に整数ではない値があります。")
