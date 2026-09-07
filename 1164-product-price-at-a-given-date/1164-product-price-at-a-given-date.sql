select distinct X.product_id,COALESCE(J.PRICE,10) as price from Products X  left join
(select P.product_id,P.new_price as price from Products P join
(select product_id,max(change_date) as fd from Products where change_date<='2019-08-16' group by product_id) as ff
on P.product_id=ff.product_id and ff.fd=P.change_date) as J

on J.product_id=X.product_id




