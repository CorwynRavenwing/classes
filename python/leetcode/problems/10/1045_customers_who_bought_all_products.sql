select customer_id
from Customer C
group by customer_id
having
    count(
        DISTINCT product_key
    ) = (
        select count(DISTINCT product_key)
        from Product P
    )
-- NOTE: Accepted on first Submit
-- NOTE: Runtime 613 ms Beats 62.79%
