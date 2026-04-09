# Portfolio

BtoB SaaS領域の **データアナリスト / プロダクトアナリスト** を目指し、  
SQL・分析・（必要に応じて）Web実装までを **「成果物 + 改善履歴」** として残すリポジトリです。

---

## Highlights（30秒で分かること）
- **SQL Drills**：問題定義 → 実装 → 振り返り（learnings）を **1問1ファイル** で継続蓄積（`sql/drills/`）
- **分析の土台づくり**：集計・JOIN・サブクエリ・相関サブクエリ・CASE集計まで段階的に拡張
- **継続運用**：READMEと更新ログを残し、学習の量だけでなく **積み上げ方** も見える形に整理

---

## リンク集（Proofの入口）
- **SQL Drills（最新）**：[`sql/drills/2026-04/`](sql/drills/2026-04/)
- **SQL Drills（一覧）**：[`sql/drills/`](sql/drills/)
- **Python Basics（最新）**：[`python/basics/q005_survey_average/`](python/basics/q005_survey_average/)
- **ロードマップ原本**：[`roadmap/`](roadmap/)
- **学習メモ（Notes）**：[`notes/`](notes/)
- **分析（準備中）**：[`analysis/`](analysis/)

## 結論（1行）
- **SQL drills に加えて、Pythonでは q001〜q005 を追加し、CSV読み込み・関数・条件分岐・辞書・平均計算・例外処理まで基礎課題を成果物化できた。**

## 次のアクション（1行）
- **次は Python基礎課題を q006 以降も追加しつつ、SQLと同じように「何を学んだか」をREADMEで説明できる形に整える。**

---

## Roadmapとの対応（Proofを増やす設計）
- ロードマップ原本：[`roadmap/`](roadmap/)（master / monthly plan / gantt）
- 方針：ロードマップの **各IDのProofを、GitHub内のリンクで提示できる形** にしていきます。

| ロードマップカテゴリ | GitHubの置き場所 | 代表的なProof |
|---|---|---|
| 資格：基本情報 | `learning/fe_exam/` | 弱点TOP10＋型＋改善ログ |
| 数学/前提 | `learning/math/` | まとめ＋例題（手計算→Python再現） |
| SQL | `sql/drills/` | 問題→解答→解説（learnings） |
| Python | `python/` | 小課題＋README（目的/手順/学び） |
| 統計/検定・A/B | `analysis/ab_testing/` + `learning/statistics/` | 1枚説明メモ＋演習 |
| 統計/因果 | `analysis/causal_inference/` | 用語整理＋ミニ演習＋1枚 |
| プロダクト/分析 | `analysis/product_analytics/` | ファネル/継続/解約のミニPJ |
| BI/可視化 | `bi/` | ダッシュボード設計＋指標定義 |
| データモデリング | `dwh/modeling/` | 粒度設計＋図＋期待クエリ |
| データ品質 | `data_quality/` | テスト例＋再発防止メモ |
| 実務/案件・インターン | `work/case_studies/` | ケーススタディ（公開/架空データ） |
| 就活 | `career/` | 職務要約/STAR/企業研究 |

---

## 成果物（採用担当が見る場所）
| Category | Title | 内容 | Link |
|---|---|---|---|
| SQL Drills | 2026-02 drills | q001〜q012（SELECT / WHERE / IN / LIKE / DISTINCT / GROUP BY / JOIN / HAVING / MIN/MAX / LEFT JOIN） | [sql/drills/2026-02/](sql/drills/2026-02/) |
| SQL Drills | 2026-03 drills | q013〜q022（LEFT JOIN / 3テーブルJOIN / サブクエリ / EXISTS / 相関サブクエリ / CASE集計 / CASEランク付け） | [sql/drills/2026-03/](sql/drills/2026-03/) |
| SQL Drill | q019_having_multiple_clubs.sql | HAVING + COUNT(DISTINCT)（2つ以上の部活に所属している学生の抽出） | [sql/drills/2026-03/q019_having_multiple_clubs.sql](sql/drills/2026-03/q019_having_multiple_clubs.sql) |
| SQL Drill | q020_correlated_subquery_grade_avg.sql | 相関サブクエリ + AVG（自分の平均点と学年平均の比較） | [sql/drills/2026-03/q020_correlated_subquery_grade_avg.sql](sql/drills/2026-03/q020_correlated_subquery_grade_avg.sql) |
| SQL Drill | q021_case_pass_fail_count.sql | CASE + SUM（科目ごとの合格人数・不合格人数集計） | [sql/drills/2026-03/q021_case_pass_fail_count.sql](sql/drills/2026-03/q021_case_pass_fail_count.sql) |
| SQL Drill | q022_case_rank_by_avg.sql | CASE + AVG（学生ごとの平均点とランク付け） | [sql/drills/2026-03/q022_case_rank_by_avg.sql](sql/drills/2026-03/q022_case_rank_by_avg.sql) |
| Python Basics | q001_sales_total | CSV読み込み + DictReader + 関数 + 例外処理で総売上を計算 | [python/basics/q001_sales_total/](python/basics/q001_sales_total/) |
| Python Basics | q005_survey_average | CSV読み込み + DictReader + 関数 + 条件分岐 + 平均計算 + 例外処理で満足度平均を計算 | [python/basics/q005_survey_average/](python/basics/q005_survey_average/) |
| Analysis | （準備中） | ファネル / 継続率 / 解約率などのミニ分析 | [analysis/](analysis/) |
| Web | （準備中） | 最小限の可視化 / アプリ | [web/](web/) |
| Notes | 学習メモ | 設計 / 学びの蓄積 | [notes/](notes/) |

---

## リポジトリ構成
- `sql/`：SQLドリル・分析用クエリ
- `python/`：Python基礎課題・データ処理の練習
- `analysis/`：分析ミニプロジェクト（問い / 仮説 / 指標 / 結果 / 示唆）
- `web/`：簡易アプリ・UI（必要な範囲で）
- `notes/`：学習メモ、設計メモ、振り返り

---

## 技術スタック
### 現在
- SQL
- Git / GitHub

### 今後（必要に応じて）
- Python（データ処理）
- Flask（簡易Web）
- HTML / CSS / JavaScript（可視化 / UI）

---

## 次に追加する予定（短期）
- `analysis/` に **分析ミニPJ** を1本追加（問い→仮説→指標→検証→示唆）
- SQL drills を「問い→SQL→解釈→学び」まで一段強くする
- 各成果物フォルダの README を「目的 / 手順 / 学び」で統一する

---

## 今週やったこと／学び／次週やること（2026-03-16〜2026-03-22）

- **今週やったこと**：SQL drills を q019〜q022 まで追加し、HAVING・相関サブクエリ・CASEを使った条件付き集計とランク付けまで拡張した
- **学び**：単純な抽出だけでなく、**「集計後に絞る」「自分の行に応じて比較先を変える」「条件ごとに件数を分ける」「集計結果を区分で表現する」** といった実務で頻出の考え方が見えてきた
- **次週やること**：CASE / HAVING / 相関サブクエリの違いを1行で説明できるよう整理し、各SQLに「どんな場面で使うか」の観点を足す

---

## 更新ログ
- 2026-04-09: `python/basics/q005_survey_average` を追加（CSV読み込み, DictReader, 関数, 条件分岐, 平均計算, 例外処理）
- 2026-04-05: `python/basics/q001_sales_total` を追加（CSV読み込み, DictReader, 関数, for文, 例外処理）
- 2026-04-05: Python README / Basics README / ルート README を更新
- 2026-03-22: ルート README を現在の学習状況に合わせて更新（最新リンク / 成果物 / 学び / 更新ログを修正）
- 2026-03-30: SQL drills（2026-03）に q022 を追加（CASE, AVG, GROUP BY によるランク付け）
- 2026-03-22: SQL drills（2026-03）に q019〜q021 を追加（HAVING, 相関サブクエリ, CASE集計）
- 2026-03-21: SQL drills（2026-03）に q017〜q018 を追加（EXISTS, LEFT JOIN / IS NULL）
- 2026-03-21: SQL drills（2026-03）に q015〜q016 を追加（サブクエリ, MAX, 相関サブクエリ）
- 2026-03-12: SQL drills（2026-03）に q013〜q014 を追加（LEFT JOIN, 3テーブルJOIN）
- 2026-02-28: SQL drills（2026-02）に q011〜q012 を追加（COUNT(DISTINCT), LEFT JOIN, JOIN / COUNT）
- 2026-02-27: SQL drills（2026-02）に q009〜q010 を追加（GROUP BY/MIN/MAX, INNER JOIN）
- 2026-02-26: SQL drills（2026-02）に q007〜q008 を追加（JOIN/AVG, HAVING）
- 2026-02-25: SQL drills（2026-02）に q005〜q006 を追加（DISTINCT/LIMIT, GROUP BY/COUNT）
- 2026-02-22: SQL drills（2026-02）に q003〜q004 を追加（IN/BETWEEN, LIKE/NULL）
- 2026-02-17: リポジトリ作成、README初版作成
- 2026-02-17: SQL drills（2026-02）に q001〜q002 を追加（SELECT/AS, WHERE/ORDER BY）
