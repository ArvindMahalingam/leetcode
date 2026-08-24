# Write your MySQL query statement below
select d.name as department ,e.name as employee ,sal.max_salary as Salary from department d join employee e on d.id=e.departmentId join (
select departmentId,max(salary) as max_salary from Employee group by departmentId
) as sal on e.departmentId=sal.departmentId where e.salary=sal.max_salary;
