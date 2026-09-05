# Write your MySQL query statement below








(select U.name as results from Users U join
(
    select user_id,count(*) as cnt from MovieRating group by user_id
)as X
on U.user_id=X.user_id and X.cnt=
(select max(cnt) from
(select count(user_id) as cnt from MovieRating group by user_id) as Y) order by results asc limit 1)

union all
(select B.title as results from Movies B join(
    select movie_id,avg(rating) as avg from MovieRating where created_at between '2020-02-01' and '2020-02-29' group by movie_id
) as C
on B.movie_id=C.movie_id and C.avg=
(select max(rt) from(
select avg(rating) as rt from MovieRating   where created_at between '2020-02-01' and '2020-02-29' group by movie_id) as A )order by results asc  limit 1)