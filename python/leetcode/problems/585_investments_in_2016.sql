# Write your MySQL query statement below
select round(sum(A.tiv_2016), 2) as tiv_2016
from Insurance as A
where exists (
    select B.pid
    from Insurance as B
    where A.pid != B.pid
    and A.tiv_2015 = B.tiv_2015
)
and NOT exists (
    select C.pid
    from Insurance as C
    where A.pid != C.pid
    and A.lat = C.lat
    and A.lon = C.lon
)
# NOTE: 449 ms; Beats 96.94% of users with MySQL
