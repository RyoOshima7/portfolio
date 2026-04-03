# SQL Drills

SQLの基礎〜実務で頻出のパターンを、**1問 = 1ファイル**で整理して積み上げています。  
目的は「学習したこと」ではなく、**就活で “何ができるか” が一目で伝わる形**にすることです。

---

## ルール
- ファイル名は `q###_topic.sql`（連番 + 内容）
- 各ファイルは以下の構成
  - 問題（要件）
  - 解答SQL
  - Learnings（学びを2〜3行で要約）

---

## Logs

### 2026-02
- `q001_select_alias.sql` : SELECT / AS（別名）
- `q002_where_orderby.sql` : WHERE / ORDER BY（複数キーソート）
- `q003_in_between.sql` : IN / BETWEEN（複数候補・範囲）
- `q004_like_null.sql` : LIKE / NULL判定（前方一致・IS NULL）
- `q005_distinct_limit.sql` : DISTINCT / LIMIT（重複排除・先頭N件）
- `q006_groupby_count.sql` : GROUP BY / COUNT（都道府県ごとの件数集計）
- `q007_join_avg.sql` : JOIN / AVG（複数表の平均点集計）
- `q008_having_avg.sql` : HAVING / AVG（集計後の条件抽出）
- `q009_groupby_minmax.sql` : GROUP BY / MIN / MAX（学年ごとの最小・最大誕生日）
- `q010_inner_join_mtm.sql` : INNER JOIN（多対多の基本・文化部の所属者抽出）
- `q011_count_distinct_left_join.sql` : COUNT(DISTINCT) / LEFT JOIN（所属0件を含む部活数集計）
- `q012_club_member_count.sql` : JOIN / COUNT（部活ごとの所属人数集計）

### 2026-03
- `q013_left_join_zero_count.sql` : LEFT JOIN / COUNT（所属0人の部活も含む人数集計）
- `q014_three_table_join_points.sql` : JOIN / WHERE / ORDER BY（学生ID=1の点数明細表示）
- `q015_subquery_above_avg.sql` : サブクエリ / AVG / WHERE / ORDER BY（全体平均より高い点数の抽出）
- `q016_subquery_subject_top_score.sql` : サブクエリ / MAX / 相関サブクエリ（科目ごとの最高点の学生一覧）
- `q017_exists_under_60.sql` : EXISTS / 相関サブクエリ（60点未満が1科目でもある学生の抽出）
- `q018_left_join_no_affiliation.sql` : LEFT JOIN / IS NULL（どの部活にも所属していない学生の抽出）
- `q019_having_multiple_clubs.sql` : HAVING / COUNT(DISTINCT)（2つ以上の部活に所属している学生の抽出）
- `q020_correlated_subquery_grade_avg.sql` : 相関サブクエリ / AVG（自分の平均点と学年平均の比較）
- `q021_case_pass_fail_count.sql` : CASE / SUM / 条件付き集計（科目ごとの合格人数・不合格人数集計）
- `q022_case_rank_by_avg.sql` : CASE / AVG / GROUP BY（学生ごとの平均点とランク付け）

### 2026-04
- `q023_date_month_extract.sql` : 日付関数 / MONTH（誕生日が1月の学生を抽出）
- `q024_date_age_calc.sql` : 日付関数 / TIMESTAMPDIFF / CURDATE（学生の満年齢を計算）
- `q025_string_concat_contact.sql` : 文字列関数 / CONCAT（氏名とメールを連結して連絡先表示）
- `q026_window_rank_by_subject.sql` : ウィンドウ関数 / RANK / PARTITION BY（科目ごとの順位付け）
- `q027_window_top_subject_per_student.sql` : ウィンドウ関数 / ROW_NUMBER（学生ごとの最高点科目を1件抽出）
- `q028_groupby_club_group_student_count.sql` : GROUP BY / COUNT(DISTINCT)（部活グループごとの所属学生数集計）
- `q029_join_non_null_position.sql` : JOIN / IS NOT NULL（役職がある学生の一覧表示）
- `q030_summary_club_count_avg_point.sql` : LEFT JOIN / COUNT(DISTINCT) / AVG / GROUP BY（学生ごとの所属部活数と平均点サマリー）
