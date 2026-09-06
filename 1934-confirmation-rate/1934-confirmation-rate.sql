# Write your MySQL query statement below
select s.user_id,COALESCE(round((((A.cmf)/A.total)),2),0.00) as confirmation_rate from Signups s left join



(select user_id,sum(action='confirmed') as cmf,count(*) as total  from Confirmations  group by user_id) as A

on s.user_id=A.user_id group by s.user_id