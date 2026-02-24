/*
Q005: DISTINCTとLIMIT
- student の pref（都道府県）を重複なしで一覧表示
- pref を昇順で並べる
- 先頭5件だけを表示
*/

SELECT DISTINCT
  pref
FROM student
ORDER BY pref ASC
LIMIT 5;

/*
Learnings:
- DISTINCT は「重複行をまとめて1行にする」
- LIMIT は「返す行数の上限」を決める（例：5件だけ）
- 先頭N件を“意味のある順番”にするために、LIMIT の前に ORDER BY を書く
*/
