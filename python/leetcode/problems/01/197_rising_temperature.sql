# Write your MySQL query statement below
select A.id
from Weather as A
, Weather as B
where B.recordDate = DATE_SUB(A.recordDate, INTERVAL 1 DAY)
and A.temperature > B.temperature

