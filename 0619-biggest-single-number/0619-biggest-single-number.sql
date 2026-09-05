# Write your MySQL query statement below
select Max(numero) as num from
(select num as numero,count(num) as C from MyNumbers group by num) as COUNTNUMBER
where C=1;