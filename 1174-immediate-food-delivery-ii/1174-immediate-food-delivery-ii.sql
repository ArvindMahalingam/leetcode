# Write your MySQL query statement below
select round(
    sum(
        case when first_orders.order_date=D.customer_pref_delivery_date then 1 else 0
        end
    )*100/count(*)
,2) as immediate_percentage
 from delivery D join 
(select customer_id,min(order_date) as order_date from delivery group by customer_id) as first_orders
on D.customer_id=first_orders.customer_id and D.order_date=first_orders.order_date;