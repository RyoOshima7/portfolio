# 要件

## 必須要件
- pandasを `pd` という名前でインポートすること
- `pd.read_csv()` を使ってCSVファイルを読み込むこと
- `head()` を使って先頭5行を表示すること
- `columns` を使って列名を表示すること
- `info()` を使ってデータの基本情報を表示すること
- `describe()` を使って基本統計量を表示すること

## 補足
- ファイルパスは `Path(__file__).resolve().parent` を使って指定すること
- CSVファイルは `data/sales_basic.csv` に置くこと
- `df.info()` はそれ自体で表示を行うため、`print(df.info())` ではなく `df.info()` と書くこと
