# NOTE: table Product is not needed by this solution
select product_id, year as first_year, quantity, price
from Sales as S
where not exists(
    select product_id
    from Sales as P
    where S.product_id = P.product_id
    and P.year < S.year
)
# NOTE: 1097 ms; Beats 70.81%
