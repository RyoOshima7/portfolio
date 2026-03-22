/*
Q021: CASE（条件付き集計）
- 科目ごとに、合格(60点以上)人数と不合格(60点未満)人数を表示する
- 表示列は subject_name, pass_count, fail_count
- subject_id 昇順で並べる
*/

SELECT
  sub.name AS subject_name,
  SUM(CASE WHEN p.point >= 60 THEN 1 ELSE 0 END) AS pass_count,
  SUM(CASE WHEN p.point < 60 THEN 1 ELSE 0 END) AS fail_count
FROM subject AS sub
JOIN point AS p
  ON p.subject_id = sub.id
GROUP BY sub.id, sub.name
ORDER BY sub.id;

/*
Learnings:
- CASE WHEN ... THEN 1 ELSE 0 END を使うと、条件に合う行だけを 1 として数え上げられる
- SUM と組み合わせることで、合格人数と不合格人数を1回の集計で同時に求められる
- GROUP BY sub.id, sub.name によって、科目ごとに結果を1行へまとめられる
*/
