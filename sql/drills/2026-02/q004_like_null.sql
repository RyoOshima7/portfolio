/*
Q004: LIKEとNULL判定
- club の name が 'c' で始まる部活を表示
- affiliation で position が NULL のレコードだけを表示
- ※ 2本のSQLでOK
*/

-- 1) club.name が 'c' で始まる
SELECT
  id,
  name,
  group_name
FROM club
WHERE name LIKE 'c%';

-- 2) position が NULL の所属レコード
SELECT
  student_id,
  club_id,
  position
FROM affiliation
WHERE position IS NULL;

/*
Learnings:
- LIKE は部分一致検索に使う（% は「任意の0文字以上」）：'c%' は「cで始まる」
- NULL は「値がない/不明」なので、= では比較できない → IS NULL / IS NOT NULL を使う
*/
