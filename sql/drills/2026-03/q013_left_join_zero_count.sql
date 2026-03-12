/*
Q013: LEFT JOIN（0件も含める）
- 部活一覧を、所属人数つきで全て表示する
- 所属0人の部活も表示する
- 表示列は club_id, club_name, member_count
- member_count の多い順、同数なら club.id 昇順で並べる
*/

SELECT 
  c.id AS club_id,
  c.name AS club_name,
  COUNT(a.student_id) AS member_count
FROM club AS c
LEFT JOIN affiliation AS a
  ON a.club_id = c.id
GROUP BY c.id, c.name
ORDER BY member_count DESC, c.id;

/*
Learnings:
- LEFT JOIN を使うと、所属者が0人の部活も一覧に残したまま集計できる
- COUNT(a.student_id) は NULL を数えないため、所属がない部活は 0 件として表示される
- GROUP BY に club 側の列をそろえると、部活ごとに1行へまとめて人数を集計できる
*/
