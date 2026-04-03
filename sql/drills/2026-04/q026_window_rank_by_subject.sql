/*
Q026: ウィンドウ関数（科目内順位）
- 各科目ごとに、点数の高い順で順位を付けて表示する
- RANK() OVER(PARTITION BY ... ORDER BY ...) を使って科目ごとの順位を求める
- 表示列は subject_id, subject_name, student_id, point, rnk
- 科目ごと、順位順、学生ID順で並べる
*/

SELECT
  p.subject_id,
  sub.name AS subject_name,
  p.student_id,
  p.point,
  RANK() OVER (
    PARTITION BY p.subject_id
    ORDER BY p.point DESC
  ) AS rnk
FROM point AS p
JOIN subject AS sub
  ON sub.id = p.subject_id
ORDER BY p.subject_id, rnk, p.student_id;

/*
Learnings:
- PARTITION BY p.subject_id を使うと、「科目ごと」にグループを分けた順位付けができる
- RANK() は同点なら同じ順位を付け、次の順位を飛ばす順位関数である
- GROUP BY と違い、ウィンドウ関数は元の行を残したまま順位や集計値を追加できる
*/
