SELECT P.product_id,
       COALESCE(M.price, 10) AS price
FROM
(
    SELECT DISTINCT product_id
    FROM Products
) AS P
LEFT JOIN
(
    SELECT P1.product_id, P1.new_price AS price
    FROM Products P1
    JOIN
    (
        SELECT product_id, MAX(change_date) AS meow
        FROM Products
        WHERE change_date <= '2019-08-16'
        GROUP BY product_id
    ) AS M
    ON P1.product_id = M.product_id
    AND P1.change_date = M.meow
) AS M
ON P.product_id = M.product_id;