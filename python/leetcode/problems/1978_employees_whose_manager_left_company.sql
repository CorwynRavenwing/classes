select E.employee_id
from Employees E
left join Employees M on (E.manager_id = M.employee_id)
where M.employee_id is null
and E.manager_id is not null
and E.salary < 30000
order by E.employee_id

