/*
Q009: グループ別 MIN/MAX
- grade ごとに、誕生日(birthday)が最も早い学生と最も遅い学生の日付を出す
- 表示列は grade, min_birthday, max_birthday
- grade 昇順に並べる
*/

SELECT
  grade,
  MIN(birthday) AS min_birthday,
  MAX(birthday) AS max_birthday
FROM student
GROUP BY grade
ORDER BY grade ASC;

/*
Learnings:
- MIN() と MAX() を使うと、各グループの最小値・最大値をまとめて取得できる
- GROUP BY を組み合わせると、grade ごとの最も早い日付と遅い日付を出せる
- 日付データでも、文字列ではなく「最小・最大」の集計ができる
*/
