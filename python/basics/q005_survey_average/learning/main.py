import csv #csvモジュールをインポート
from pathlib import Path #pathlibモジュールからPathクラスをインポート

def calculate_average_satisfaction(file_path): #満足度の平均を計算する関数
    # total と count を作る
    total = 0 #満足度の合計
    count = 0 #満足度の件数
    #ファイルを開く
    with open(file_path, "r" , encoding="utf-8") as f: #ファイルを読み込みモードで開く。エンコードはutf-8
        reader = csv.DictReader(f) #列名をキーとする辞書形式でCSVを読み込む

        for row in reader: #readerの各行をrowに代入してループ
            value = row["satisfaction"] #satisfaction列の値をvalueに代入

        # satisfaction が空ならスキップ
            if value == "":
                continue
        # satisfaction を数値に変換して total に加算
            score = int(value) #satisfaction列の値を整数に変換してscoreに代入
            total += score #scoreをtotalに加算
            count += 1 #satisfactionの件数をカウント

    # countが0なら0を返す
    if count == 0:
        return 0
    # 平均を返す
    return total / count

try: # 例外処理を開始
    # このPythonファイルが置かれている場所を基準にする
    base_dir = Path(__file__).resolve().parent

    # 絶対パスを作る
    csv_file = base_dir.parent / "data" / "survey_basic.csv"
    
    # resultに満足度の平均を計算した結果を代入
    result = calculate_average_satisfaction(csv_file)
    # 結果を小数点以下2桁で表示
    print(f"満足度平均: {result:.2f}")

# ファイルが見つからない場合
except FileNotFoundError:
    print("csvファイルが見つかりませんでした。パスを確認してください。")
# satisfaction列に整数ではない値がある場合
except ValueError:
    print("satisfaction列に整数ではない値があります。")