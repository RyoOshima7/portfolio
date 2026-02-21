/*
Q002: WHEREとORDER BY
- student から grade が 2 以上の学生を抽出
- grade 降順 → id 昇順で表示
- 表示列: id, last_name, first_name, grade
*/

SELECT
  id,
  last_name,
  first_name,
  grade
FROM student
WHERE grade >= 2
ORDER BY grade DESC, id ASC;

/*
Learnings:
- ORDER BY は左から優先して並ぶ（gradeで並べ、同点はidで並べる）
- DESC=降順 / ASC=昇順（ASCは省略されることも多い）
*/
