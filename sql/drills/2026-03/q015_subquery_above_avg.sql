/*
Q015: サブクエリ（全体平均との差）
- point テーブル全体の平均点より高い点数のレコードを表示する
- 表示列は student_id, subject_id, point
- point の高い順、同点なら student_id 昇順、subject_id 昇順で並べる
*/

SELECT
  student_id,
  subject_id,
  point
FROM point
WHERE point > (SELECT AVG(point) FROM point)
ORDER BY point DESC, student_id, subject_id;

/*
Learnings:
- (SELECT AVG(point) FROM point) は、point テーブル全体の平均点を先に求めるサブクエリ
- WHERE point > (...) と書くと、平均点より高いレコードだけに絞り込める
- ORDER BY point DESC, student_id, subject_id で、高得点順に並べつつ同点時の順番も安定させられる
*/
