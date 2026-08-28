# Write your MySQL query statement below
select e.name as Employee from Employee e join Employee m on e.managerid=m.Id where e.salary>m.salary;