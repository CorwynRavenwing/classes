select P.product_name, S.year, S.price
from Sales as S
left join Product as P using (product_id)

