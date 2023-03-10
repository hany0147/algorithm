-- 코드를 입력하세요
SELECT
    CAR_ID,
    CASE
        WHEN START_DATE <= 20221016 AND END_DATE >= 20221016 THEN '대여중'
        ELSE '대여 가능'
    END AS AVAILABILITY
    
FROM
    CAR_RENTAL_COMPANY_RENTAL_HISTORY
WHERE
    END_DATE >= 20221016
GROUP BY
    CAR_ID
ORDER BY
    CAR_ID DESC;