# Write your MySQL query statement below


select
    case count(distinct salary)
    when 0 then null
    when 1 then null
    else (
        select distinct salary as SecondHighestSalary
        from Employee
        order by salary DESC
        limit 1
        offset 1
    ) end as SecondHighestSalary
from Employee

# NOTE: 418 ms; Beats 88.53% of users with MySQL
