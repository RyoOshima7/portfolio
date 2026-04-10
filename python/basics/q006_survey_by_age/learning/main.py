import csv 
from pathlib import Path

def summarize_by_age(file_path):
    # 年代ごとの満足度の合計を入れる辞書
    age_totals = {} 

    # 年代ごとの件数を入れる辞書
    age_counts = {} 

    # CSVファイルを開く
    with open(file_path, "r" , encoding="utf-8") as f:
        # 1行を辞書として読む
        reader = csv.DictReader(f)

        #1行ずつ処理する
        for row in reader:
            age_group = row["age_group"]    # 年代
            value = row["satisfaction"]     # 満足度

            #　満足度が空欄ならスキップ
            if value == "":
                continue

            # 文字列を整数に変換
            score = int(value)

            # 初めて出てきた年代なら0で初期化
            if age_group not in age_totals:
                age_totals[age_group] = 0
                age_counts[age_group] = 
                
            # 合計と件数を更新
            age_totals[age_group] += score
            age_counts[age_group] += 1

    # 年代ごとの平均を入れる辞書        
    age_averages = {}

    # 平均 = 合計　÷　件数
    for age_group in age_totals:
        age_averages[age_group] = age_totals[age_group] / age_counts[age_group]

    return age_averages

try:
    # このPythonファイルがあるフォルダ
    base_dir = Path(__file__).resolve().parent

    # 1つ上のフォルダにある data/survey_by_age.csvを指定
    csv_path = base_dir.parent / "data" / "survey_by_age.csv"

    # 関数を実行して結果を受け取る
    result = summarize_by_age(csv_path)

    # 結果を表示
    for age_group, avg_score in result.items():
        print(f"{age_group}: {avg_score:.2f}")
        
except FileNotFoundError:
    print(f"ファイルが見つかりません: {csv_path}")
except ValueError:
    print("satisfaction列に整数ではない値があります。")
