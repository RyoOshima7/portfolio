# Portfolio

BtoB SaaS領域の **データアナリスト / プロダクトアナリスト** を目指して、
学習内容を **「何を作ったか」「何を学んだか」「次に何を伸ばすか」** が分かる形で整理したポートフォリオです。

このリポジトリでは、SQL・Python・スプレッドシート・分析の基礎学習を、
**成果物 + README + 学習ログ** として積み上げています。

---

## このリポジトリで分かること
- SQL、Python、Excelの基礎をどこまで学習したか
- 各課題で **何を目的に取り組み、何を使い、何を学んだか**
- 今後どの分野を伸ばして、実務に近い成果物へつなげる予定か

---

## まず見てほしい場所
初めて見る方は、**BtoB SaaSのデータ分析職でどう活かせるか** が分かりやすいように、以下の順番で読むことを想定しています。

1. **BtoB SaaS分析ミニ成果物**
   - [`analysis/product_analytics/user_event_funnel_mini/`](analysis/product_analytics/user_event_funnel_mini/)
   - ユーザー行動ログをもとに、イベント件数・CVR・改善仮説を整理しています。
2. **Pythonによるログ集計・CVR計算**
   - [`python/basics/q003_user_event_count/`](python/basics/q003_user_event_count/)
   - [`python/basics/q004_conversion_rate/`](python/basics/q004_conversion_rate/)
   - BtoB SaaSの利用ログ分析、ファネル分析、KPI集計につながる基礎課題です。
3. **pandasによるデータ確認**
   - [`python/pandas/q001_read_csv_basic/`](python/pandas/q001_read_csv_basic/)
   - 分析前のデータ確認、欠損値確認、EDAにつながる基礎です。
4. **BI / KPIダッシュボード設計**
   - [`bi/dashboards/btob_saas_kpi_dashboard_design/`](bi/dashboards/btob_saas_kpi_dashboard_design/)
   - 誰が何を判断するための画面かを意識して、KPIの見せ方を整理しています。
5. **SQL・Python・Excelの基礎ログ**
   - [`sql/drills/`](sql/drills/)
   - [`python/basics/`](python/basics/)
   - [`learning/spreadsheets/`](learning/spreadsheets/)

---

## おすすめ閲覧順
「BtoB SaaSの分析テーマ」→「その土台になる基礎スキル」→「今後の伸ばし方」の順で見ると、理解しやすいです。

1. **BtoB SaaS分析ミニ成果物**
   - [`analysis/product_analytics/user_event_funnel_mini/`](analysis/product_analytics/user_event_funnel_mini/)
   - 課題、指標、集計結果、改善提案までを1ページで確認できます。
2. **Pythonログ集計・CVR計算**
   - [`python/basics/q003_user_event_count/`](python/basics/q003_user_event_count/)
   - [`python/basics/q004_conversion_rate/`](python/basics/q004_conversion_rate/)
   - プロダクト分析の土台になるイベント件数集計と割合計算を確認できます。
3. **SQLの基礎〜集計練習**
   - [`sql/drills/2026-04/`](sql/drills/2026-04/)
   - 日付関数、ウィンドウ関数、要約集計など、KPI集計に必要なSQLの基礎を確認できます。
4. **pandas / Excel / BIの基礎**
   - [`python/pandas/q001_read_csv_basic/`](python/pandas/q001_read_csv_basic/)
   - [`learning/spreadsheets/excel-roadmap-q011-q020/`](learning/spreadsheets/excel-roadmap-q011-q020/)
   - [`bi/dashboards/btob_saas_kpi_dashboard_design/`](bi/dashboards/btob_saas_kpi_dashboard_design/)
5. **ロードマップ・学習ログ**
   - [`roadmap/`](roadmap/)
   - [`notes/`](notes/)
   - 今後、学習内容をどのように成果物へつなげるかを確認できます。

---

## 代表的な成果物

### BtoB SaaS分析ミニ成果物
- [`analysis/product_analytics/user_event_funnel_mini/`](analysis/product_analytics/user_event_funnel_mini/)
  - ユーザー行動ログから view / click / purchase を集計し、CVRと改善仮説を整理
  - 活用場面: ファネル分析、オンボーディング改善、機能利用率分析、プロダクト改善提案

### Python / pandas
- [`python/basics/q003_user_event_count/`](python/basics/q003_user_event_count/)
  - イベント件数集計
  - 活用場面: ログイン数、クリック数、機能利用回数、アクティブ率の基礎集計
- [`python/basics/q004_conversion_rate/`](python/basics/q004_conversion_rate/)
  - click率・purchase率の計算
  - 活用場面: CVR、トライアル転換率、商談化率、オンボーディング完了率の計算
- [`python/pandas/q001_read_csv_basic/`](python/pandas/q001_read_csv_basic/)
  - pandasによるCSV読み込み、データ確認の基礎
  - 活用場面: 分析前のデータ確認、欠損値・データ型確認、EDA

### SQL
- [`sql/drills/2026-02/`](sql/drills/2026-02/)
  - SELECT、WHERE、GROUP BY、JOIN などの基礎
- [`sql/drills/2026-03/`](sql/drills/2026-03/)
  - サブクエリ、EXISTS、CASE、相関サブクエリなど
- [`sql/drills/2026-04/`](sql/drills/2026-04/)
  - 日付関数、文字列関数、ウィンドウ関数、要約集計など
  - 活用場面: 月次KPI、ユーザー別ランキング、継続率、顧客セグメント別集計

### BI / Dashboard
- [`bi/dashboards/btob_saas_kpi_dashboard_design/`](bi/dashboards/btob_saas_kpi_dashboard_design/)
  - BtoB SaaSのKPIダッシュボード設計メモ
  - 活用場面: PM、CS、BizOpsが見るKPI整理と意思決定支援

### Spreadsheets / Excel
- [`learning/spreadsheets/excel-roadmap-q001-q010/`](learning/spreadsheets/excel-roadmap-q001-q010/)
  - 基本関数、表操作の基礎
- [`learning/spreadsheets/excel-roadmap-q011-q020/`](learning/spreadsheets/excel-roadmap-q011-q020/)
  - IF、VLOOKUP、ピボットテーブルなど

---

## リポジトリ構成
```text
portfolio/
├─ sql/                  # SQLドリル
├─ python/               # Python基礎課題・データ処理
├─ learning/             # 試験・数学・スプレッドシート学習
├─ analysis/             # 分析メモ・分析ミニプロジェクト
├─ bi/                   # ダッシュボード・計測設計
├─ dwh/                  # データモデリング・dbt学習
├─ data_quality/         # データ品質・テスト観点
├─ roadmap/              # 学習計画・月次計画
├─ career/               # 就活用メモ・面接準備
├─ notes/                # 学習メモ・振り返り
├─ web/                  # Web実装関連
└─ work/                 # ケーススタディ
```

---

## 各フォルダの見方
- **README.md**
  - そのフォルダで何に取り組んでいるかを説明
- **docs/**
  - 問題文や要件
- **learning/**
  - 学習途中のコードや試行錯誤
- **completed/**
  - 完成版コード
- **notes/**
  - 学んだこと、つまずいたこと、改善点
- **workbook/**
  - Excelファイル本体

---

## このポートフォリオの目的
このリポジトリの目的は、単に課題を保存することではなく、
**「基礎を理解しながら継続的に改善していること」を第三者に伝えること**です。

そのため、できるだけ以下が分かる形を目指しています。
- 何のための課題か
- どの技術を使っているか
- どこまでできるようになったか
- 次に何を強化する予定か

---

## 現在の学習範囲
### 学習済み
- SQL基礎〜中級手前
  - SELECT / WHERE / GROUP BY / JOIN / HAVING / サブクエリ / EXISTS / CASE / ウィンドウ関数
- Python基礎
  - 変数、条件分岐、繰り返し、関数、リスト、辞書、CSV読み込み、例外処理、簡単なFlaskアプリ
- pandas入門
  - CSV読み込み、先頭行確認、列名確認、データ型確認、基本統計量確認
- Excel基礎
  - IF、VLOOKUP、ピボットテーブルなど

### 今後強化したい内容
- Pythonでのデータ分析処理
- 分析ミニプロジェクトの追加
- BI / ダッシュボード設計
- 仮説設定 → 指標設計 → 集計 → 示唆出し の一連の流れ

---

## 採用担当者の方へ
このリポジトリでは、派手な成果物よりも、**SQL・Python・pandas・BIの基礎を、BtoB SaaSのデータ分析にどう活かすか** を見える形にすることを重視しています。

現時点では学習途中の内容も含みますが、各課題で以下を残すようにしています。
- 何のために取り組んだか
- どの処理を使ったか
- BtoB SaaSのKPI集計、ユーザー行動分析、ファネル分析、ダッシュボード作成にどうつながるか

特に以下を見ていただくと、データ分析職に向けた学習の方向性が分かりやすいです。
- BtoB SaaS分析ミニ成果物: [`analysis/product_analytics/user_event_funnel_mini/`](analysis/product_analytics/user_event_funnel_mini/)
- Pythonログ集計: [`python/basics/q003_user_event_count/`](python/basics/q003_user_event_count/)
- CVR計算: [`python/basics/q004_conversion_rate/`](python/basics/q004_conversion_rate/)
- pandas: [`python/pandas/`](python/pandas/)
- SQL: [`sql/drills/`](sql/drills/)
- BI設計: [`bi/dashboards/`](bi/dashboards/)

---

## 次のアクション
- `q003_user_event_count` と `q004_conversion_rate` を発展させ、ユーザー行動分析のミニ成果物を増やす
- 各成果物フォルダの README を **「目的 / 使用技術 / 実行方法 / 学び / BtoB SaaSでどう活かせるか」** の形式に統一する
- `analysis/` に、ファネル分析・コホート分析・解約リスク分析のミニプロジェクトを追加する
- `bi/` に、KPIダッシュボードの設計メモとスクリーンショットを追加する
- GitHub上で、初見の人でも「分析テーマ → 使用技術 → 示唆」が追いやすい導線に改善する

---

## 更新ログ
- 2026-07-03: BtoB SaaSデータ分析職向けに、ルートREADMEの導線と代表成果物の見せ方を調整
- 2026-07-03: `analysis/product_analytics/user_event_funnel_mini/` と `bi/dashboards/btob_saas_kpi_dashboard_design/` を追加
- 2026-05-09: `python/pandas/q001_read_csv_basic/` を追加。pandasでCSV読み込みとデータ確認の基礎を学習
- 2026-05-09: `notes/2026-05-09_learning_log.md` を追加。SQL・Python・pandas・Excelの学習ログを記録
- 2026-04-15: ルート README を全面見直し。成果物の説明、読み方、構成、導線を改善
- 2026-04-15: `learning/spreadsheets/excel-roadmap-q011-q020/` を追加
- 2026-04-15: `python/basics/q010_flask_summary_app/` を追加
- 2026-04-14: `python/basics/q009_file_error_handling/` を追加
- 2026-04-13: `python/basics/q008_inventory_order/` を追加
- 2026-04-11: `python/basics/q007_inventory_total/` を追加
- 2026-04-10: `python/basics/q006_survey_by_age/` を追加
- 2026-04-09: `python/basics/q005_survey_average/` を追加
- 2026-03-30: SQL drills（2026-04）を追加
- 2026-03-22: SQL drills（2026-03）を追加
- 2026-02-17: リポジトリ作成、SQL drills（2026-02）を追加
