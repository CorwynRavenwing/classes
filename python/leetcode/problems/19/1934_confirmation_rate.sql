select A.user_id
, IFNULL(ROUND(AVG(B.action_value),2),0) as confirmation_rate
from Signups as A
LEFT JOIN (
    select user_id
    , CASE
        WHEN action = "timeout" THEN 0
        WHEN action = "confirmed" THEN 1
        ELSE 999
    END as action_value
    from Confirmations
) as B USING(user_id)
GROUP BY user_id

-- NOTE: Accepted on first Run
-- NOTE: Accepted on first Submit
-- NOTE: Runtime 957 ms Beats 23.54%
