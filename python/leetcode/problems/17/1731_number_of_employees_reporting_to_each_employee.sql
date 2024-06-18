select M.employee_id
, M.name
, count(*) as reports_count
, round(sum(E.age) / count(*), 0) as average_age
from Employees as M
left join Employees as E ON (M.employee_id = E.reports_to)
where E.employee_id is not null
group by M.employee_id
order by M.employee_id

