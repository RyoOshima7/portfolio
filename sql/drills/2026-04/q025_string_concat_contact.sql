/*
Q025: 文字列関数（連結）
- 学生の連絡先を「氏名(メール)」形式で表示する
- CONCAT を使って、姓・名・メールアドレスを1つの文字列にまとめる
- 表示列は id, contact
- id の昇順で並べる
*/

SELECT
  id,
  CONCAT(last_name, ' ', first_name, '(', mail, ')') AS contact
FROM student
ORDER BY id;

/*
Learnings:
- CONCAT() を使うと、複数の文字列や列の値を1つの文字列として連結できる
- 固定文字（半角スペースや括弧）も CONCAT の中に入れることで、見やすい表示形式を作れる
- AS contact としておくと、加工後の文字列が何を表す列か分かりやすくなる
*/
