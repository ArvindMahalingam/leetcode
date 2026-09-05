# Write your MySQL query statement below

Select cust as customer_id from
(select customer_id as cust,count(distinct(product_key)) as number from Customer group by customer_id) as ProductCount where number=(select count(*) from Product);