# Write your MySQL query statement below

select D.name as 'Department'
, E.name as 'Employee'
, E.salary as Salary
from Department as D
inner join Employee as E ON(E.departmentID = D.id)
where NOT EXISTS (
    select O.salary
    from Employee as O
    where O.departmentID = E.departmentID
    and O.salary > E.salary
)

-- NOTE: Runtime 572 ms Beats 79.16%
