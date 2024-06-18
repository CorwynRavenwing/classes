# Write your MySQL query statement below

select distinct A.num as ConsecutiveNums
from Logs A
where exists (
    select B.id
    from Logs B
    where B.id = A.id + 1
      and B.num = A.num
)
and   exists (
    select C.id
    from Logs C
    where C.id = A.id + 2
      and C.num = A.num
)

