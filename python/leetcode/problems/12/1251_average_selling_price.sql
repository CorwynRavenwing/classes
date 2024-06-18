select T.product_id
, IFNULL(round(sum(T.total) / sum(T.units), 2), 0) as average_price
from (
    select P.product_id, US.units, (US.units * P.price) as total
    from Prices as P
    left join UnitsSold as US USING(product_id)
    where (
        US.purchase_date BETWEEN start_date AND end_date
     or US.purchase_date is null
    )
    order by product_id
) as T
group by T.product_id

