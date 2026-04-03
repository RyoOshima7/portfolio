/*
Q023: 日付関数（月抽出）
- 誕生日が1月の学生を表示する
- MONTH(birthday) を使って、日付から月だけを取り出して判定する
- 表示列は id, last_name, first_name, birthday
- birthday の昇順、同日なら id 昇順で並べる
*/

SELECT
  id,
  last_name,
  first_name,
  birthday
FROM student
WHERE MONTH(birthday) = 1
ORDER BY birthday ASC, id;

/*
Learnings:
- MONTH(birthday) を使うと、DATE型の値から「月」だけを取り出して条件に使える
- WHERE MONTH(birthday) = 1 とすると、1月生まれの学生だけを抽出できる
- ORDER BY birthday ASC, id とすると、誕生日が早い順に見やすく並べられる
*/
