-- Q002: クラブ名に「o」または「u」を含むレコードを抽出し、別名で表示する
-- ポイント: LIKE による部分一致検索、OR 条件は括弧でまとめる

SELECT
  id   AS クラブID,
  name AS クラブ名
FROM club
WHERE name LIKE '%o%'
   OR name LIKE '%u%';
