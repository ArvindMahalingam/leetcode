# Write your MySQL query statement below
select S.product_id,S.year AS first_year ,S.quantity,S.price from Sales S join

(select product_id,min(year) as first_year from Sales group by product_id) as FIRSTYEAR
on S.product_id=FIRSTYEAR.product_id and S.year=FIRSTYEAR.first_year ;