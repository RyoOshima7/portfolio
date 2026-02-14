SELECT
  last_name AS 学生名,
  address1  AS 住所1
FROM student
WHERE address1 LIKE 'o%'
  AND address1 NOT LIKE '%shi';
