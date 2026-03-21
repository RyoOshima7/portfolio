/*
Q017: EXISTS（存在チェック）
- いずれか1科目でも 60点未満の学生を抽出する
- 表示列は id, last_name, first_name
- id 昇順で並べる
*/

SELECT
  s.id,
  s.last_name,
  s.first_name
FROM student AS s
WHERE EXISTS (
    SELECT 1
    FROM point AS p
    WHERE p.student_id = s.id
      AND p.point < 60
)
ORDER BY s.id;

/*
Learnings:
- EXISTS は「条件に合う行が1件でも存在するか」を判定するときに使う
- p.student_id = s.id によって、外側の student と内側の point を結びつけている
- 60点未満の科目が1つでもあれば真になるため、その学生だけを抽出できる
*/
