# Write your MySQL query statement below
select  distinct firstrow.num as ConsecutiveNums from Logs firstrow join Logs secondrow on firstrow.id+1=secondrow.id join Logs thirdrow on secondrow.id+1=thirdrow.id where firstrow.num=secondrow.num
and secondrow.num=thirdrow.num