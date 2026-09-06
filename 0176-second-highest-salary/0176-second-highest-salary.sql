# Write your MySQL query statement below

select max(Salary) as SecondHighestSalary from employee where Salary <
(select max(salary) as highest from Employee) 