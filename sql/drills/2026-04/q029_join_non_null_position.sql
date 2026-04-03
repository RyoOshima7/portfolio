/*
Q029: NULL判定＋JOIN（役職者）
- 部活で役職を持っている学生の一覧を表示する
- affiliation.position が NULL ではない行だけを抽出する
- 表示列は student_id, last_name, first_name, club_name, position
- student_id、club_id の順に並べる
*/

SELECT
  s.id AS student_id,
  s.last_name,
  s.first_name,
  c.name AS club_name,
  a.position
FROM affiliation AS a
JOIN student AS s
  ON s.id = a.student_id
JOIN club AS c
  ON c.id = a.club_id
WHERE a.position IS NOT NULL
ORDER BY s.id, c.id;

/*
Learnings:
- IS NOT NULL を使うと、値が入っている行だけを抽出できる
- affiliation を起点に student と club を JOIN すると、「誰が」「どの部活で」「どんな役職か」を同時に表示できる
- 別名（student_id, club_name）を付けると、複数表を結合した結果でも列の意味が分かりやすい
*/
