select I.employee_id
from (
    select employee_id from Employees
    UNION
    select employee_id from Salaries
) as I
LEFT JOIN Salaries as S USING(employee_id)
LEFT JOIN Employees as E USING(employee_id)
WHERE (
    salary is null
    or name is null
)
ORDER BY employee_id

