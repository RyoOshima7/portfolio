import csv
from pathlib import Path

def count_events(file_path):
    # 最初に各イベントの件数を 0 にしておく
    event_counts = {"view": 0, "click": 0, "purchase": 0}

    with open(file_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        for row in reader:
            event = row["event"]

            # 想定しているイベントだけを数える
            if event in event_counts:
                event_counts[event] += 1

    return event_counts

try:
    # このPythonファイルが置かれている場所を基準にする
    base_dir = Path(__file__).resolve().parent

    # 絶対パスを作る
    csv_path = base_dir.parent / "data" / "user_log_basic.csv"

    result = count_events(csv_path)

    print("イベント件数")
    for event_name, count in result.items():
        print(f"{event_name}: {count}")
except FileNotFoundError:
    print(f"ファイルが見つかりません: {csv_path}")
