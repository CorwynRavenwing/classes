# Write your MySQL query statement below
select C.name as Customers
from Customers as C
left join Orders O on O.customerId = C.id
where O.id is null
