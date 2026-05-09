# 学習ログ

## 2026-05-09

### 今日やったこと
- SQLの苦手問題を2問復習
- Pythonの苦手問題を2問再実行
- pandasでCSV読み込みの入口を作成
- Excel q011〜q020から1つ復習

### pandasで学んだこと
- pandasは、Pythonで表データを扱うためのライブラリであること
- `import pandas as pd` を使う前に、pandasのインストールが必要であること
- `python -c "import pandas as pd; print(pd.__version__)"` でpandasが使えるか確認できること
- `pd.read_csv()` でCSVファイルをDataFrameとして読み込めること
- `head()`、`columns`、`info()`、`describe()` を使ってデータの基本確認ができること
- `df.info()` はそれ自体で表示するため、`print(df.info())` と書くと最後に `None` が表示されること

### 分からなかったこと
- SQL
- Python
- Excel
- pandasの環境設定とインポートエラーへの対応

### 次にやること
毎朝通知される学習内容をもとに、今まで学習した内容の復習と、就活ロードマップ達成のための新規学習を行う。

### 次回のpandas学習候補
- q002：必要な列だけを取り出す
- `df["列名"]` と `df[["列名1", "列名2"]]` の違いを理解する
