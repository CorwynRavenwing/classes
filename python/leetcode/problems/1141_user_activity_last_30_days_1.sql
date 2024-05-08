select activity_date as day
, count(user_id) as active_users
from (
select DISTINCT activity_date, user_id
from Activity as A
where activity_date between
    DATE_SUB(DATE '2019-07-27', interval 29 day)
    and DATE_ADD(DATE '2019-07-28', interval 1 day)
order by activity_date
) as U
group by activity_date

