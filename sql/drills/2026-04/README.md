# 2026-04 SQL Drills

## 目的
その月に取り組んだSQL演習をまとめ、どの構文や考え方を練習したかを把握しやすくすることを目的としています。

## 使用技術
SQL, SELECT, JOIN, 集計関数, サブクエリ, ウィンドウ関数, Markdown

## 実行方法
1. このフォルダ内の `.sql` ファイルを上から順に確認します。
2. 各ファイルで、問題、解答SQL、Learnings を読みます。
3. 似た構文や集計パターンを比較しながら復習します。

## 学び
- 1か月分をまとめて見ることで、どのSQLパターンを学習したかを整理しやすくなります。

## 収録内容
- `q023_date_month_extract.sql`
- `q024_date_age_calc.sql`
- `q025_string_concat_contact.sql`
- `q026_window_rank_by_subject.sql`
- `q027_window_top_subject_per_student.sql`
- `q028_groupby_club_group_student_count.sql`
- `q029_join_non_null_position.sql`
- `q030_summary_club_count_avg_point.sql`

## 次に改善するなら
- `q027_window_top_subject_per_student.sql` では、学生ごとに最高点の科目を1件だけ取り出す処理を練習しました。次に改善するなら、顧客ごとの最新利用日や企業ごとの最も利用された機能など、BtoB SaaSの利用ログ分析に近いデータ例でも同じパターンを再現します。

- `q028_groupby_club_group_student_count.sql` では、クラブのグループごとの所属学生数を重複なしで集計しました。BtoB SaaSでは、プラン別・業種別・部署別の顧客数や利用者数を集計し、顧客分析やカスタマーサクセスの優先順位付けに活用できます。