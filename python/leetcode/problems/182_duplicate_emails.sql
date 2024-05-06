# Write your MySQL query statement below
select DISTINCT A.email
from Person A
, Person B
where A.email = B.email
and A.id < B.id

