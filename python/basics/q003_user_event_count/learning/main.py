import csv #csvを扱うためのモジュールをインポート
from pathlib import Path #ファイルパスを扱うためのモジュールをインポート

def count_events(file_path): #イベントの件数を数える関数を定義
    # TODO:
    # 件数を数えるための辞書を用意する
    event_counts = {"view": 0, "click": 0, "purchase": 0} 
    # CSV を読んで event ごとに件数を増やす
    with open(file_path, "r" , encoding="utf-8") as f: #csvファイルを読み込むためにファイルを開く

        reader = csv.DictReader(f) #列名をキーとする辞書形式でCSVを読み込む

        for row in reader: #1行ずつ処理する
            event = row["event"] #event列の値を取得する

            if event in event_counts: #event_countsのキーにeventが存在するか確認する
                event_counts[event] += 1 #event_countsの該当するキーの値を1増やす
    # 最後に event_counts を返す
    return event_counts

try: #エラーが発生する可能性のあるコードをtryブロックに入れる
    base_dir = Path(__file__).resolve().parent #現在のファイルのディレクトリを取得する

    csv_path = base_dir.parent / "data" / "user_log_basic.csv" #データファイルのパスを作成する

    result = count_events(csv_path) #イベントの件数を数える関数を呼び出して結果を取得する

    print(result) #デバッグ用に結果を表示する

    print("イベント件数")
    for event_name, count in result.items(): #resultのキーと値をevent_nameとcountに代入してループする
        print(f"{event_name}: {count}") #イベント名と件数をフォーマットして表示する

except FileNotFoundError: #ファイルが見つからない場合のエラーをキャッチする
    print(f"ファイルが見つかりません: {csv_path}")
