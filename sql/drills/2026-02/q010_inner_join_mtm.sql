/*
Q010: INNER JOIN（多対多の基本）
- group_name = 'culture' の部活動に所属する学生を表示
- 表示列は 姓(last_name), 名(first_name), 部活名(club.name)
- student.id, club.id の順で並べる
*/

SELECT
  s.last_name AS 姓,
  s.first_name AS 名,
  c.name AS 部活名
FROM student AS s
JOIN affiliation AS a
  ON a.student_id = s.id
JOIN club AS c
  ON c.id = a.club_id
WHERE c.group_name = 'culture'
ORDER BY s.id, c.id;

/*
Learnings:
- 多対多の関係は、中間テーブル（ここでは affiliation）をはさんで JOIN する
- student と club を直接つながず、student → affiliation → club の順につなぐのが基本
- WHERE で club 側の条件を指定すると、特定グループの所属者だけを取り出せる
*/
