-- 코드를 입력하세요
SELECT
    CATEGORY, SUM(SALES)
FROM
    BOOK
INNER JOIN
    BOOK_SALES USING (BOOK_ID)
WHERE
    SALES_DATE LIKE '2022-01%'
GROUP BY
    CATEGORY
ORDER BY
    CATEGORY;