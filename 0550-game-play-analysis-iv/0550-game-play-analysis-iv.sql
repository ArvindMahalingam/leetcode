# Write your MySQL query statement below
select round(
    sum(
        case when DATEDIFF(A.event_date,firstday.meow)=1 then 1 else 0
        end
    )/count(distinct(A.player_id)) 
,2) as fraction from Activity A join
(select player_id,min(event_date) as meow from Activity group by player_id) as firstday
on A.player_id=firstday.player_id