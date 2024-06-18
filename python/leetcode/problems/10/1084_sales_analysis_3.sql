# Write your MySQL query statement below
select DISTINCT P.product_id, P.product_name
from Product as P
    LEFT JOIN Sales as S1
        on P.product_id = S1.product_id
        and S1.sale_date BETWEEN '2019-01-01' and '2019-04-01'
    LEFT JOIN Sales as S2
        on P.product_id = S2.product_id
        and S2.sale_date NOT BETWEEN '2019-01-01' and '2019-04-01'
WHERE S1.product_id IS NOT NULL
    AND S2.product_id IS NULL
ORDER BY P.product_id

