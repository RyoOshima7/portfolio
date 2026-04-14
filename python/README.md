# Python

分析に必要な範囲に絞って、**小さく作って積む** フォルダです。

- `basics/`：関数 / 例外 / ファイル入出力 / CSV読み込み など
- `data_analysis/`：pandas / 可視化 / 簡易ETL など

各テーマは、`README.md`（目的/手順/学び）を必ず付けます。

## 現在の追加内容
- [`basics/q001_sales_total/`](basics/q001_sales_total/)：CSVの総売上計算（関数・for文・DictReader・例外処理）
- [`basics/q002_sales_by_product/`](basics/q002_sales_by_product/)：商品別売上集計（辞書・集計・sorted・CSV読み込み）
- [`basics/q003_user_event_count/`](basics/q003_user_event_count/)：ユーザー行動ログのイベント件数集計（辞書・条件分岐・関数・CSV読み込み）
- [`basics/q004_conversion_rate/`](basics/q004_conversion_rate/)：コンバージョン率計算（関数・条件分岐・CSV読み込み・割合計算・例外処理）
- [`basics/q005_survey_average/`](basics/q005_survey_average/)：アンケート満足度平均の計算（関数・条件分岐・CSV読み込み・平均計算・例外処理）
- [`basics/q006_survey_by_age/`](basics/q006_survey_by_age/)：年代別の満足度平均を計算（辞書・集計・CSV読み込み・平均計算・例外処理）
- [`basics/q007_inventory_total/`](basics/q007_inventory_total/)：在庫一覧と合計金額の表示（リスト・for文・関数・計算）
- [`basics/q008_inventory_order/`](basics/q008_inventory_order/)：在庫・注文管理CLI（input・if文・関数・例外処理・在庫更新）
- [`basics/q009_file_error_handling/`](basics/q009_file_error_handling/)：ファイル読み込みと例外処理（Path・CSV読み込み・try/except・ValueError・FileNotFoundError）


## 学習の見方
- `learning/`：自力で取り組む途中版
- `completed/`：完成版
- `docs/`：課題文・要件
- `data/`：CSVなどの入力データ（ある場合）
