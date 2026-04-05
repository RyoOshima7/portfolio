import csv
from pathlib import Path

def calculate_total_sales(file_path):
    # TODO:
    # 1. total_sales = 0 を作る
    total_sales = 0

    # 2. csv.DictReader でファイルを読む
    with open(file_path, 'r' , encoding='utf-8') as f:
      
      reader = csv.DictReader(f)

      for row in reader:
    # 3. quantity と unit_price を int に変換する
        quantity = int(row['quantity'])
        unit_price = int(row['unit_price'])

    # 4. quantity * unit_price を total_sales に足す
        line_sales = quantity * unit_price

        total_sales += line_sales
        

    # 5. total_sales を返す
    return total_sales

try:
    base_dir = Path(__file__).resolve().parent

    csv_path = base_dir.parent / "data" / "sales_basic.csv"
    
    result = calculate_total_sales(csv_path)
    print(f"総売上: {result}円")
except FileNotFoundError:
    print("ファイルが見つかりません。")
except ValueError:
    print("数値の変換に失敗しました。")