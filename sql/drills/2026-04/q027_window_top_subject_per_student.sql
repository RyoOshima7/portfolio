/*
Q027: ウィンドウ関数（学生の最高科目）
- 各学生について、最高点の科目を1つだけ表示する
- 同点がある場合は subject_id が小さい科目を採用する
- ROW_NUMBER() を使って学生ごとに1位の行を選ぶ
- 表示列は student_id, last_name, first_name, subject_name, point
*/

SELECT
  t.student_id,
  s.last_name,
  s.first_name,
  t.subject_name,
  t.point
FROM (
  SELECT
    p.student_id,
    p.subject_id,
    sub.name AS subject_name,
    p.point,
    ROW_NUMBER() OVER (
      PARTITION BY p.student_id
      ORDER BY p.point DESC, p.subject_id ASC
    ) AS rn
  FROM point AS p
  JOIN subject AS sub
    ON sub.id = p.subject_id
) AS t
JOIN student AS s
  ON s.id = t.student_id
WHERE t.rn = 1
ORDER BY t.student_id;

/*
Learnings:
- ROW_NUMBER() を使うと、学生ごとに「何番目の行か」を1行ずつ振れるため、1位だけを取り出せる
- ORDER BY p.point DESC, p.subject_id ASC とすることで、「高得点優先、同点なら subject_id が小さい方」を表現できる
- まずサブクエリで順位を付け、外側で WHERE t.rn = 1 とするのが定番パターンである
*/
