select A.month
    , A.country
    , count(A.id) as trans_count
    , sum(A.approved) as approved_count
    , sum(A.amount) as trans_total_amount
    , sum(A.approved_amount) as approved_total_amount
from (
    select id
        , LEFT(trans_date,7) as month
        , country
        , CASE
            WHEN state = "approved" THEN 1
            ELSE 0
        END as approved
        , amount
        , CASE
            WHEN state = "approved" then amount
            ELSE 0
        END as approved_amount
    from Transactions
) as A
group by A.month, A.country

-- NOTE: Accepted on first Submit
-- NOTE: Runtime 780 ms Beats 24.10%
