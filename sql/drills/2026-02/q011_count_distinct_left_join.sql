/*
Q011: COUNT(DISTINCT)（JOINで増える対策）
- 学生ごとに所属している部活数を表示する
- 所属0件の学生も出す
- 表示列は id, last_name, first_name, club_count
- club_count の多い順、同数なら student.id 昇順で並べる
*/

SELECT
  s.id,
  s.last_name,
  s.first_name,
  COUNT(DISTINCT a.club_id) AS club_count
FROM student AS s
LEFT JOIN affiliation AS a
  ON a.student_id = s.id
GROUP BY s.id, s.last_name, s.first_name
ORDER BY club_count DESC, s.id;

/*
Learnings:
- LEFT JOIN を使うと、部活に所属していない学生も含めて一覧にできる
- COUNT(DISTINCT a.club_id) にすると、JOIN による重複を避けながら部活数を数えられる
- 集計するときは、学生ごとにまとめるために GROUP BY に student 側の列をそろえる
*/
