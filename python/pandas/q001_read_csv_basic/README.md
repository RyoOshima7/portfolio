# q001_read_csv_basic

## 目的
pandasを使ってCSVファイルを読み込み、データの中身を確認する基本操作を学習する。

## 使用技術
- Python
- pandas
- pathlib
- CSV

## 実行方法

リポジトリのルートで以下を実行します。

```bash
python python/pandas/q001_read_csv_basic/learning/main.py
```

または、`q001_read_csv_basic` フォルダに移動してから以下を実行します。

```bash
python learning/main.py
```

## 学習内容
この課題では、以下を学習しました。

- `pd.read_csv()` でCSVファイルを読み込む方法
- `df.head()` で先頭5行を確認する方法
- `df.columns` で列名を確認する方法
- `df.info()` でデータ型や欠損値を確認する方法
- `df.describe()` で数値データの基本統計量を確認する方法
- `df.info()` はそれ自体で表示を行うため、`print(df.info())` と書くと最後に `None` が表示されること

## ファイル構成

```text
q001_read_csv_basic/
  README.md
  data/
    sales_basic.csv
  docs/
    problem.md
    requirements.md
  learning/
    main.py
  completed/
    main.py
  notes/
    learning_log.md
```

## 学び
pandasでは、まずCSVを読み込み、すぐに集計するのではなく、最初にデータの中身・列名・データ型・欠損値を確認することが重要だと学びました。

## 関連リンク
- [問題文](docs/problem.md)
- [要件](docs/requirements.md)
- [学習用コード](learning/main.py)
- [完成版コード](completed/main.py)
- [学習ログ](notes/learning_log.md)
