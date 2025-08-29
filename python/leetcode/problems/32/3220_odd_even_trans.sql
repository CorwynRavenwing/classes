select transaction_date
, SUM(odd_amount) as odd_sum
, SUM(even_amount) as even_sum
from (
    select transaction_date
    , IF(even_odd = 1, amount, 0) as odd_amount
    , IF(even_odd = 0, amount, 0) as even_amount
    from (
        select amount MOD 2 as even_odd
        , amount
        , transaction_date
        from transactions as A
    ) as B
) as C
GROUP BY transaction_date
ORDER BY transaction_date ASC

-- NOTE: Acceptance Rate 68.5% (medium)

-- NOTE: Accepted on first Run
-- NOTE: Accepted on second Submit (I wrote even/odd transaction ID; they wanted even/odd transaction amount instead)
-- NOTE: Runtime 300 ms Beats 35.69%
