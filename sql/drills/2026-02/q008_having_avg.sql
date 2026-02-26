/*
Q008: HAVING（集計後の条件）
- 科目ごとの平均点が 80 以上の科目だけを表示
- 表示列は subject_name, avg_point
- avg_point の高い順に並べる
*/

SELECT
  sub.name AS subject_name,
  AVG(p.point) AS avg_point
FROM subject AS sub
JOIN point AS p
  ON p.subject_id = sub.id
GROUP BY sub.id, sub.name
HAVING AVG(p.point) >= 80
ORDER BY avg_point DESC;

/*
Learnings:
- HAVING は、GROUP BY で集計したあとの結果に条件をかける
- WHERE は集計前、HAVING は集計後に使うのが基本
- 「平均点が80以上」のような条件付き集計でよく使う
*/
