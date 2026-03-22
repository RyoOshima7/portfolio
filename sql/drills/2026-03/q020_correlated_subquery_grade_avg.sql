/*
Q020: 相関サブクエリ（学年平均との差）
- 学生ごとに「自分の平均点」と「同じ grade の平均点」を表示する
- 自分の平均点が学年平均より高い学生だけを抽出する
- 表示列は id, last_name, first_name, my_avg, grade_avg
- my_avg の高い順、同点なら id 昇順で並べる
*/

SELECT
  s.id,
  s.last_name,
  s.first_name,
  (SELECT AVG(p1.point) FROM point AS p1 WHERE p1.student_id = s.id) AS my_avg,
  (
    SELECT AVG(p2.point)
    FROM point AS p2
    JOIN student AS s2 ON s2.id = p2.student_id
    WHERE s2.grade = s.grade
  ) AS grade_avg
FROM student AS s
WHERE (SELECT AVG(p1.point) FROM point AS p1 WHERE p1.student_id = s.id)
  >
  (
    SELECT AVG(p2.point)
    FROM point AS p2
    JOIN student AS s2 ON s2.id = p2.student_id
    WHERE s2.grade = s.grade
  )
ORDER BY my_avg DESC, s.id;

/*
Learnings:
- student の1行ごとに、相関サブクエリで「自分の平均点」と「同じ学年の平均点」を計算している
- s.id や s.grade のように外側の行を参照することで、学生ごとに比較対象が変わる
- WHERE で my_avg と grade_avg を比べることで、学年平均を上回る学生だけを抽出できる
*/
