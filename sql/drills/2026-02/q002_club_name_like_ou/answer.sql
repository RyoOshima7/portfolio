SELECT
  id   AS クラブID,
  name AS クラブ名
FROM club
WHERE name LIKE '%o%'
   OR name LIKE '%u%';
