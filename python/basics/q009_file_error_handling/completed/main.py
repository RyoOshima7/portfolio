import csv
from pathlib import Path

def read_scores(file_path):
    scores = []

    with open(file_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        for row in reader:
            # score は文字列なので int に変換する
            score = int(row["score"])
            scores.append(score)

    return scores

try:
    # このPythonファイルが置かれている場所を基準にする
    base_dir = Path(__file__).resolve().parent

    # 絶対パスを作る
    csv_path = base_dir.parent / "data" / "score_with_error.csv"

    result = read_scores(csv_path)
    print("読み込み成功")
    print(result)
except FileNotFoundError:
    print(f"ファイルが見つかりません: {csv_path}")
except ValueError:
    print("score列に整数ではない値があります。")
