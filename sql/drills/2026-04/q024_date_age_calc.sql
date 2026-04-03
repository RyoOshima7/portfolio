/*
Q024: 日付関数（年齢計算）
- 学生の年齢（満年齢）を計算して表示する
- TIMESTAMPDIFF(YEAR, birthday, CURDATE()) を使って年齢を求める
- 表示列は id, last_name, first_name, birthday, age
- age の降順、同年齢なら id 昇順で並べる
*/

SELECT
  id,
  last_name,
  first_name,
  birthday,
  TIMESTAMPDIFF(YEAR, birthday, CURDATE()) AS age
FROM student
ORDER BY age DESC, id;

/*
Learnings:
- CURDATE() は今日の日付を返し、TIMESTAMPDIFF(YEAR, birthday, CURDATE()) で満年齢を計算できる
- AS age と別名を付けると、計算結果を分かりやすい列名で表示できる
- 計算した age を ORDER BY に使うと、年齢順の一覧を簡潔に作れる
*/
