-- Q003: 住所が「o」から始まり「shi」で終わらない学生を抽出し、別名で表示する
-- ポイント: LIKE / NOT LIKE による肯定・否定条件、AND で条件を組み合わせる

SELECT
  last_name AS 学生名,
  address1  AS 住所1
FROM student
WHERE address1 LIKE 'o%'
  AND address1 NOT LIKE '%shi';
