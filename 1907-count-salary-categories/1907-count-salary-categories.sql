# Write your MySQL query statement below
select 'Low Salary' as Category,COUNT(CASE WHEN INCOME<20000 THEN 1  end ) as accounts_count from Accounts
union 
select 'Average Salary' as Category,Count(Case when income between 20000 and 50000 then 1 end) as accounts_count from accounts
union
select 'High Salary' as Category,count(Case when income>50000 then 1  end) as accounts_count from accounts