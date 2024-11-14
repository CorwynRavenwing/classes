
select B.product_id, B.new_price as price
from Products as B
where B.change_date = (
    select MAX(change_date)
    from Products as A
    where change_date <= '2019-08-16'
    and A.product_id = B.product_id
    group by product_id
)
UNION
select C.product_id, 10 as price
from Products as C
where not exists (
    select D.new_price
    from Products as D
    where change_date <= '2019-08-16'
    and D.product_id = C.product_id
)
order by product_id

-- NOTE: Runtime 1582 ms Beats 6.91%
