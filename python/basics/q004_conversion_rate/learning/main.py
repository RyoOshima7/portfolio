import csv # csvファイルを読み書きするためのモジュールをインポート
from pathlib import Path # Pathlibモジュールの中にあるPathクラスをインポート

def calculate_rates(file_path): #率を計算する関数を定義
    # それぞれのイベントの数をカウントするための変数を初期化
    view_count = 0
    click_count = 0
    purchase_count = 0

    with open(file_path, "r", encoding="utf-8") as f:  #ファイルをreadingモードで開き、UTF-8エンコーディングを指定してファイルオブジェクトfを作成
        reader = csv.DictReader(f) #列名を使って値をアクセスできるようにするために、csv.DictReaderを使用してファイルオブジェクトfからreaderオブジェクトを作成

        for row in reader: #readerの中身を1行ずつループしてrowに代入
            event = row["event"] #変数eventに、rowの中の"event"という列の値を代入

            if event == "view": #もしeventが"view"だったら、view_countを1増やす
                view_count += 1
            elif event == "click": #もしeventが"click"だったら、click_countを1増やす
                click_count += 1
            elif event == "purchase": #もしeventが"purchase"だったら、purchase_countを1増やす
                purchase_count += 1


    # もしview が0だったら、click_rateとpurchase_rateは0になるので、0を返す
    if view_count == 0:
        return {"view": view_count,
                "click": click_count,
                "purchase": purchase_count,
                "click_rate": 0,
                "purchase_rate": 0}

    # click_rate と purchase_rate を計算して返す
    click_rate = click_count / view_count
    purchase_rate = purchase_count / view_count

    # 結果を辞書形式で返す
    return {
        "view" : view_count,
        "click" : click_count,
        "purchase" : purchase_count,
        "click_rate" : click_rate,
        "purchase_rate" : purchase_rate,
    }

try: #例外処理を開始
    base_dir = Path(__file__).resolve().parent #Pathクラスを使って、現在のファイル（main.py)の絶対パスを取得し、その親ディレクトリをbase_dirに代入

    csv_path = base_dir.parent / "data" / "user_log_rate.csv" #base_dirの親ディレクトリにあるdataディレクトリの中のuser_log_rate.csvというファイルのパスをcsv_pathに代入

    result = calculate_rates(csv_path) #calculate_rates関数を呼び出して、csv_pathを引数として渡し、その結果をresultに代入

    # 結果を表示
    print(f"view数： {result['view']}")
    print(f"click数: {result['click']}")
    print(f"purchase数: {result['purchase']}")
    print(f"click率: {result['click_rate']:.2f}")
    print(f"purchase率: {result['purchase_rate']:.2f}")

except FileNotFoundError: #もしファイルが見つからなかった場合の例外処理
    print(f"ファイルが見つかりません:{csv_path}")
