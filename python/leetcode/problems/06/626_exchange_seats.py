
select CASE
    WHEN MOD(id,2) = 0 THEN id - 1
    WHEN id = (select max(id) from seat) THEN id
    ELSE id + 1
END as id
, student
from seat
order by id     # yes, this works,
# despite the fact that "id" is a real field
# and a *different* derived field

# NOTE: Accepted on first Submit
# NOTE: Runtime 355 ms Beats 33.14%
