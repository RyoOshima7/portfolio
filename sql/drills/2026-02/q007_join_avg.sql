/*
Q007: JOIN + 平均点
- 科目ごとの平均点を表示
- 表示列は subject_id, subject_name, avg_point
- avg_point の高い順に並べる
*/

SELECT
  sub.id AS subject_id,
  sub.name AS subject_name,
  AVG(p.point) AS avg_point
FROM subject AS sub
JOIN point AS p
  ON p.subject_id = sub.id
GROUP BY sub.id, sub.name
ORDER BY avg_point DESC;

/*
Learnings:
- JOIN を使うと、subject と point のような複数表をつないで集計できる
- AVG() は「平均値」を計算する集計関数
- GROUP BY を使うと、科目ごとに平均点をまとめて出せる
*/
