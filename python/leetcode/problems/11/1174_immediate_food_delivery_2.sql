select (
    round(
        100 * SUM(D.is_immediate) / count(D.customer_id),
        2
    )
) as immediate_percentage
from (
    select B.customer_id
    , B.order_date
    , B.customer_pref_delivery_date
    , CASE
            WHEN B.order_date = B.customer_pref_delivery_date THEN 1
            ELSE 0
        END as is_immediate

    from Delivery as B
    inner join (
        select A.customer_id
        , min(A.order_date) as first_order
        from Delivery as A
        group by A.customer_id
    ) as C
    on B.customer_id = C.customer_id and B.order_date = C.first_order
) as D

-- NOTE: prior version is subscription-only
-- NOTE: Accepted on second Submit (too many precision digits)
-- NOTE: Runtime 575 ms Beats 96.27%
