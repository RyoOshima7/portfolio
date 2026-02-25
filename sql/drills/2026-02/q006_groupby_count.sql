/*
Q006: GROUP BY と COUNT
- 都道府県（pref）ごとの学生数を表示
- 表示列は pref, student_count
- student_count の多い順、同数なら pref 昇順
*/

SELECT
  pref,
  COUNT(*) AS student_count
FROM student
GROUP BY pref
ORDER BY student_count DESC, pref ASC;

/*
Learnings:
- GROUP BY は「同じ値ごとにまとめる」ために使う
- COUNT(*) は「各グループの件数」を数える
- 集計結果は ORDER BY で「件数の多い順」に並べられる
*/
