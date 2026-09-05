
select person_name from
(select turn,person_name,sum(weight) over (order by turn) as totalweight from Queue) as BUS
where BUS.totalweight<=1000 order by turn desc limit 1;