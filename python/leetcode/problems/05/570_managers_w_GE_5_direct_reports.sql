
select REPORT.name
from (
    select MANAGER.name, UNDERLING.managerId, count(*) as groupSize
    from Employee as UNDERLING
    inner join Employee as MANAGER on MANAGER.id = UNDERLING.managerId
    group by UNDERLING.managerID
    having groupSize >= 5
) as REPORT

-- NOTE: Runtime 356 ms Beats 41.82%
