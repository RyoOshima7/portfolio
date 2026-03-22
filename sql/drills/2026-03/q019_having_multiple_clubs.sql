/*
Q019: HAVING（複数所属）
- 2つ以上の部活に所属している学生を抽出する
- 表示列は id, last_name, first_name, club_count
- club_count の多い順、同数なら id 昇順で並べる
*/

SELECT
  s.id,
  s.last_name,
  s.first_name,
  COUNT(DISTINCT a.club_id) AS club_count
FROM student AS s
JOIN affiliation AS a
  ON a.student_id = s.id
GROUP BY s.id, s.last_name, s.first_name
HAVING COUNT(DISTINCT a.club_id) >= 2
ORDER BY club_count DESC, s.id;

/*
Learnings:
- GROUP BY で学生ごとにまとめると、所属している部活数を集計できる
- COUNT(DISTINCT a.club_id) を使うと、同じ部活の重複を除いて正しく部活数を数えられる
- HAVING は集計後の結果に条件をかけるため、2つ以上所属している学生だけを抽出できる
*/
