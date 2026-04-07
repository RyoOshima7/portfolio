import csv #csvを読み込むためのモジュールをインポート
from pathlib import Path #絶対パスを取得するためのモジュールをインポート

def calculate_total_sales(file_path): #合計金額を計算する関数を定義
    # TODO:
    # 1. total_sales = 0 を作る
    total_sales = 0 #合計金額を保存する変数を初期化

    # 2. csv.DictReader でファイルを読む
    with open(file_path, 'r' , encoding='utf-8') as f: #csvファイルを開く
      
      reader = csv.DictReader(f) #列名をキーとする辞書形式でcsvを読み込む

      for row in reader: #1行ずつ処理するためのループ   
    # 3. quantity と unit_price を int に変換する
        quantity = int(row['quantity']) #文字型から整数に変換して数値をquantityに代入

        unit_price = int(row['unit_price']) #文字型から整数に変換して数値をunit_priceに代入

    # 4. quantity * unit_price を total_sales に足す
        line_sales = quantity * unit_price #1行の売上を計算

        total_sales += line_sales #合計金額に1行の売上を加算
        
        print(f"行の売上: {line_sales}円, 現在の総売上: {total_sales}円") #デバッグ用に1行の売上と現在の総売上を表示

    # 5. total_sales を返す
    return total_sales

try: #エラー処理のためのtry-exceptブロックを開始
    base_dir = Path(__file__).resolve().parent #現在のファイルの絶対パスを取得し、その親ディレクトリをbase_dirに代入

    csv_path = base_dir.parent / "data" / "sales_basic.csv" #base_dirの親ディレクトリにあるdataフォルダ内のsales_basic.csvのパスをcsv_pathに代入
    
    result = calculate_total_sales(csv_path) #calculate_total_sales関数を呼び出し、結果をresultに代入

    print(f"総売上: {result}円")

except FileNotFoundError: #ファイルが見つからない場合のエラー処理
    print("ファイルが見つかりません。")
except ValueError: #数値の変換に失敗した場合のエラー処理
    print("数値の変換に失敗しました。")