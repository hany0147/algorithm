-- 코드를 입력하세요
SELECT FOOD_TYPE, REST_ID, REST_NAME, A.FAVORITES
FROM REST_INFO A
WHERE A.FAVORITES = (
    SELECT MAX(B.FAVORITES)
    FROM REST_INFO B
        INNER JOIN REST_INFO
            ON A.FOOD_TYPE = B.FOOD_TYPE)
GROUP BY FOOD_TYPE
ORDER BY FOOD_TYPE DESC;
-- 음식종류 별로 그룹을 짓는 데, 거기서 가장 많은 즐겨찾기 수를 가진 식당을 뽑아내라

# SELECT
#     FOOD_TYPE, REST_ID, REST_NAME, FAVORITES
# FROM
#     REST_INFO
# ORDER BY
#     FOOD_TYPE,
#     FAVORITES DESC