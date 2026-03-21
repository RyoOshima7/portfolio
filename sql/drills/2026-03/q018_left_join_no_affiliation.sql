/*
Q018: LEFT JOIN + NULL（所属なし抽出）
- どの部活にも所属していない学生を抽出する
- 表示列は id, last_name, first_name
- id 昇順で並べる
*/

SELECT
  s.id,
  s.last_name,
  s.first_name
FROM student AS s
LEFT JOIN affiliation AS a
  ON a.student_id = s.id
WHERE a.student_id IS NULL
ORDER BY s.id;

/*
Learnings:
- LEFT JOIN は左側の student を全件残しつつ、対応する affiliation を結びつける
- 所属情報がない学生は、右側の a.student_id が NULL になる
- WHERE a.student_id IS NULL とすることで、どの部活にも所属していない学生だけを抽出できる
*/
