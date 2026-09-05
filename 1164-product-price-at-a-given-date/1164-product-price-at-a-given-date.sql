select distinct D.product_id,COALESCE(J.price,10) as price from  Products D left join
(select P.product_id,P.new_price as price from Products P join
(select product_id,max(change_date) as dd from Products where change_date<='2019-08-16' group by product_id)
as date_match
on P.product_id=date_match.product_id and P.change_date=date_match.dd) as J
on J.product_id=D.product_id;