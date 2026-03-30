/*
Q022: CASE（ランク付け）
- 学生ごとに平均点を出し、平均点に応じてランクを付ける
- 90以上=A, 80〜89=B, 70〜79=C, それ未満=D
- 表示列は id, last_name, first_name, avg_point, rank
- avg_point の降順、同点時は id 昇順で並べる
*/

SELECT
  s.id,
  s.last_name,
  s.first_name,
  AVG(p.point) AS avg_point,
  CASE
    WHEN AVG(p.point) >= 90 THEN 'A'
    WHEN AVG(p.point) >= 80 THEN 'B'
    WHEN AVG(p.point) >= 70 THEN 'C'
    ELSE 'D'
  END AS rank
FROM student AS s
JOIN point AS p
  ON p.student_id = s.id
GROUP BY s.id, s.last_name, s.first_name
ORDER BY avg_point DESC, s.id;

/*
Learnings:
- AVG(p.point) で学生ごとの平均点を求め、GROUP BY で学生単位に1行へまとめられる
- CASE を使うと、平均点の値に応じて A〜D のランクを同じSELECT内で付けられる
- 集計結果を基準に並べ替えるときは、ORDER BY avg_point DESC のように別名を使って見やすく書ける
*/
