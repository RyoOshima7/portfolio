# Portfolio

BtoB SaaS領域の **データアナリスト / プロダクトアナリスト** を目指し、  
SQL・分析・（必要に応じて）Web実装までを **「成果物 + 改善履歴」** として残すリポジトリです。

---

## Highlights（30秒で分かること）
- **SQL Drills**：問題定義 → 実装 → 振り返り（notes）を統一フォーマットで蓄積（`sql/drills/`）
- **分析ミニPJ**：問い → 仮説 → 指標 → 検証 → 示唆 の型で整理（`analysis/`）
- **継続運用**：更新ログを残し、学習と品質改善のプロセスを可視化

---

## Roadmapとの対応（Proofを増やす設計）
- ロードマップ原本：[`roadmap/`](roadmap/)（master / monthly plan / gantt）
- 方針：ロードマップの **各IDのProofを、GitHub内のリンクで提示できる形** にしていきます。

| ロードマップカテゴリ | GitHubの置き場所 | 代表的なProof |
|---|---|---|
| 資格：基本情報 | `learning/fe_exam/` | 弱点TOP10＋型＋改善ログ |
| 数学/前提 | `learning/math/` | まとめ＋例題（手計算→Python再現） |
| SQL | `sql/drills/` | 問題→解答→解説（notes） |
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
| SQL Drills | 2026-02 drills | 2問（SELECT/AS / WHERE/ORDER BY） | [sql/drills/2026-02/](sql/drills/2026-02/) |
| SQL Drill | q001_select_alias.sql | SELECT + AS（別名） | [sql/drills/2026-02/q001_select_alias.sql](sql/drills/2026-02/q001_select_alias.sql) |
| SQL Drill | q002_where_orderby.sql | WHERE + ORDER BY（複数キー） | [sql/drills/2026-02/q002_where_orderby.sql](sql/drills/2026-02/q002_where_orderby.sql) |
| Analysis | （準備中） | ファネル/継続率などのミニ分析 | [analysis/](analysis/) |
| Web | （準備中） | 最小限の可視化/アプリ | [web/](web/) |
| Notes | 学習メモ | 設計/学びの蓄積 | [notes/](notes/) |

---

## リポジトリ構成
- `sql/`：SQLドリル・分析用クエリ
- `analysis/`：分析ミニプロジェクト（問い/仮説/指標/結果/示唆）
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
- HTML / CSS / JavaScript（可視化/UI）

---

## 次に追加する予定（短期）
- `analysis/` に **分析ミニPJ** を1本追加（問い→仮説→指標→検証→示唆）
- SQL drills を「問い→SQL→解釈」まで一段強くする（notes の示唆を増やす）
- 各成果物フォルダの README を「目的/手順/学び」で統一

---

## 更新ログ
- 2026-02-17: リポジトリ作成、README初版作成
- 2026-02-13: SQL drills（2026-02）に q001〜q003 を追加（問題/解答/notes）
