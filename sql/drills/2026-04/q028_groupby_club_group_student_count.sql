/*
Q028: グループ別集計（culture / sports）
- club.group_name ごとに所属学生数を集計する
- 同じ学生が同じ group_name 内で複数部活に所属していても、重複せず1人として数える
- 表示列は group_name, student_count
- 所属学生数の降順、同数なら group_name 昇順で並べる
*/

SELECT
  c.group_name,
  COUNT(DISTINCT a.student_id) AS student_count
FROM club AS c
JOIN affiliation AS a
  ON a.club_id = c.id
GROUP BY c.group_name
ORDER BY student_count DESC, c.group_name;

/*
Learnings:
- GROUP BY c.group_name により、部活の分類ごとに集計できる
- COUNT(DISTINCT a.student_id) を使うと、同じ学生の重複所属を除いて人数を数えられる
- JOIN で club と affiliation を結ぶことで、部活名や分類と所属情報を一緒に扱える
*/
