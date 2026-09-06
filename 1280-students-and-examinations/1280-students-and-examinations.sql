# Write your MySQL query statement below
select S.student_id,S.student_name,K.subject_name,count(e.subject_name) as attended_exams
from Students S cross join Subjects K left join examinations e on S.student_id=E.student_id and K.subject_name=E.subject_name group by
S.student_id,S.student_name,k.subject_name order by Student_id,subject_name asc;