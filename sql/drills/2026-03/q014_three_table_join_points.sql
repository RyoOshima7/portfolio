/*
Q014: 3テーブルJOIN（点数明細）
- 学生ID=1 の点数明細を表示する
- 表示列は subject_id, subject_name, point
- subject_id 昇順で並べる
*/

SELECT
  sub.id AS subject_id,
  sub.name AS subject_name,
  p.point
FROM point AS p
JOIN subject AS sub
  ON sub.id = p.subject_id
WHERE p.student_id = 1
ORDER BY sub.id;

/*
Learnings:
- point テーブルと subject テーブルを JOIN すると、科目IDだけでなく科目名つきで点数を見られる
- WHERE p.student_id = 1 で、対象の学生1人分の点数だけに絞り込める
- ORDER BY sub.id にすると、科目ID順で見やすく並べられる
*/
