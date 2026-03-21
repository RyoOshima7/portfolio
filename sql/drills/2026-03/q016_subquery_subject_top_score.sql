/*
Q016: サブクエリ（科目ごとの最高点）
- 科目ごとに最高点を取った学生の一覧を表示する
- 同点が複数いる場合は全員表示する
- 表示列は subject_name, student_id, last_name, first_name, point
- subject_id 昇順、同点時は student_id 昇順で並べる
*/

SELECT
  sub.name AS subject_name,
  s.id AS student_id,
  s.last_name,
  s.first_name,
  p.point
FROM point AS p
JOIN subject AS sub
  ON sub.id = p.subject_id
JOIN student AS s
  ON s.id = p.student_id
WHERE p.point = (
    SELECT MAX(p2.point)
    FROM point AS p2
    WHERE p2.subject_id = p.subject_id
)
ORDER BY sub.id, s.id;

/*
Learnings:
- 相関サブクエリで「今見ている科目」と同じ subject_id の中から最高点を求められる
- WHERE p.point = (...) とすることで、その科目の最高点と一致する行だけを残せる
- 同点者も同じ最高点に一致するため、複数人いる場合は全員表示される
*/
