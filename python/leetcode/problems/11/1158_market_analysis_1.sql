
select user_id as buyer_id
    , join_date
    , count(O.order_id) as orders_in_2019
from Users as U
left join orders as O
    ON (
        O.buyer_id = U.user_id
        and O.order_date like '2019-%'
    )
group by U.user_id

-- NOTE: Runtime 1231 ms Beats 84.63%
