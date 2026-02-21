/*
Q001: SELECTと別名(AS)
- student から id, last_name, first_name, pref, grade を取り出す
- last_name を last、first_name を first として表示する
*/

SELECT
  id,
  last_name  AS last,
  first_name AS first,
  pref,
  grade
FROM student;

/*
Learnings:
- AS で列の表示名（別名）を付けられる
- 出力（レポート/分析結果）の可読性が上がる
*/
