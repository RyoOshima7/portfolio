/*
Q012: 部活ごとの人数
- 部活ごとの所属人数を表示する
- 表示列は club_id, club_name, member_count
- member_count の多い順、同数なら club.id 昇順で並べる
*/

SELECT 
  c.id AS club_id,
  c.name AS club_name,
  COUNT(a.student_id) AS member_count
FROM club AS c
JOIN affiliation AS a
  ON a.club_id = c.id 
GROUP BY c.id, c.name
ORDER BY member_count DESC, c.id;

/*
Learnings:
- COUNT(a.student_id) を使うと、部活ごとの所属人数を数えられる
- JOIN で club と affiliation をつなぐと、どの部活に何人所属しているか集計できる
- GROUP BY に部活IDと部活名を入れることで、部活ごとに1行へまとめられる
*/
