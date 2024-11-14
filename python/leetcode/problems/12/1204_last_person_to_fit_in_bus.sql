select person_name
from (
    select person_id
        , person_name
        , weight
        , turn
        , (
            select sum(weight)
            from Queue as B
            where B.turn <= A.turn
        ) as Total_weight
    from Queue as A
    having Total_weight <= 1000
    order by A.turn DESC
) as C
LIMIT 1

-- NOTE: Accepted on first Run
-- NOTE: Accepted on first Submit
-- NOTE: Runtime 2043 ms Beats 14.31%
