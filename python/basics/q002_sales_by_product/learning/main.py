import csv #csvを読み込むためのモジュールをインポート
from pathlib import Path #絶対パスを取得するためのモジュールをインポート

def summarize_by_product(file_path): #商品ごとの売上を計算する関数を定義
    # TODO:
    # product_sales = {} を作る
    product_sales = {} #空の辞書を作成して、商品ごとの売上を保存するための変数を初期化

    # 商品ごとに売上を足し込む
    with open(file_path, "r" ,encoding="utf-8") as f:#csvファイルを読み込むためにファイルを開く
        reader = csv.DictReader(f) #変数readerにcsv.DictReaderを使って列名をキーとする辞書形式でcsvを読み込む

        for row in reader: #1行ずつ処理するためのループを開始
            product = row["product"] #商品名をproduct変数に代入
            quantity = int(row["quantity"]) #文字型から整数に変換して数値をquantityに代入
            unit_price = int(row["unit_price"]) #文字型から整数に変換して数値をunit_priceに代入
            sales = quantity * unit_price #1行の売上を計算してsales変数に代入

            if product not in product_sales: #productがproduct_salesのキーに存在しない場合
                product_sales[product] = 0 #product_salesのキーにproductを追加して、値を0に初期化
            
            product_sales[product] += sales #product_salesのproductの値にsalesを加算して更新

         
    # 最後に辞書を返す
    return product_sales

try: #エラー処理のためのtry-exceptブロックを開始

    base_dir = Path(__file__).resolve().parent #現在のファイルの絶対パスを取得し、その親ディレクトリをbase_dirに代入
    
    csv_path = base_dir.parent / "data" / "sales_by_product.csv" #base_dirの親ディレクトリにあるdataフォルダ内のsales_by_product.csvのパスをcsv_pathに代入

    result = summarize_by_product(csv_path) #summarize_by_product関数を呼び出し、結果をresultに代入

    # TODO:
    # result.items() を売上の大きい順に並び替えて表示する
    sorted_result = sorted(result.items(), key=lambda x: x[1], reverse=True) #result.items()でキーと値のペアを配列として取得し、key=lambda x: x[1]で値を基準にして、sorted(...,...,reverse=True)で降順に並び替える

    print(sorted_result) #デバッグ用に並び替えた結果を表示

    for product, sales in sorted_result: #並び替えた結果を1行ずつ処理するためのループを開始 (sorted_resultは配列なので、productとsalesに商品と売上をそれぞれ代入してループする)
        print(f"{product}: {sales}円") #商品名と売上をフォーマットして表示
except FileNotFoundError: #ファイルが見つからない場合のエラー処理
    print(f"ファイルが見つかりません: {csv_path}")
