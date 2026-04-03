/*
Q030: 総合（サマリーテーブル風）
- 学生ごとに所属部活数と平均点をまとめて表示する
- 所属が0件の学生も表示するため、affiliation は LEFT JOIN を使う
- 部活数は重複なしで数え、点数は student ごとに平均を求める
- 表示列は id, last_name, first_name, club_count, avg_point
- avg_point の降順、同点なら id 昇順で並べる
*/

SELECT
  s.id,
  s.last_name,
  s.first_name,
  COUNT(DISTINCT a.club_id) AS club_count,
  AVG(p.point) AS avg_point
FROM student AS s
LEFT JOIN affiliation AS a
  ON a.student_id = s.id
JOIN point AS p
  ON p.student_id = s.id
GROUP BY s.id, s.last_name, s.first_name
ORDER BY avg_point DESC, s.id;

/*
Learnings:
- LEFT JOIN affiliation にすることで、部活に所属していない学生も落とさず集計できる
- COUNT(DISTINCT a.club_id) は、同じ部活が重複して数えられるのを防げる
- AVG(p.point) と部活数を同じクエリでまとめると、学生単位のサマリー表を作れる
*/
