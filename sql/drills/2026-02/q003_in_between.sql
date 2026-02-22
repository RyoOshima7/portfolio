/*
Q003: INとBETWEEN
- student から pref が ('Oosakafu','Kyoutofu','Naraken') の学生、または grade が 1〜2 の学生を表示
- 表示列: id, last_name, first_name, pref, grade
*/

SELECT
  id,
  last_name,
  first_name,
  pref,
  grade
FROM student
WHERE pref IN ('Oosakafu','Kyoutofu','Naraken')
   OR grade BETWEEN 1 AND 2;

/*
Learnings:
- IN は「= を複数並べる」代わりに使える（候補が増えても読みやすい）
- BETWEEN は範囲指定（両端を含む）：BETWEEN 1 AND 2 は 1 と 2 も含む
- OR 条件は「どちらか満たせばOK」なので、要件を日本語で再確認してから書く
*/
