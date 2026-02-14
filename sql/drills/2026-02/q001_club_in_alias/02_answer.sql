-- Q001: クラブIDを条件指定し、クラブIDとクラブ名を別名で表示する
-- ポイント: AS による別名指定、同一カラムの複数条件は IN を使用

SELECT
  id   AS クラブID,
  name AS クラブ名
FROM club
WHERE id IN (2, 9, 10, 14, 18, 22, 24, 25);
