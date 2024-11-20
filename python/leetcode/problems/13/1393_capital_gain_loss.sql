-- SHORTCUT: since we are guaranteed that every Buy is matched to a
-- later Sell, and since we are only buying / selling a single stock
-- in each transaction, we don't actually have to care what day they
-- happened on, or how far apart; we only care about Buy vs. Sell
-- and the price on those two days

select stock_name
    , SUM(capital_change) as capital_gain_loss
from (
    select stock_name
        , CASE operation
            WHEN "Buy" THEN -price
            WHEN "Sell" THEN price
            ELSE -000
          END as capital_change
    from Stocks
    order by stock_name
) as A
group by stock_name

-- NOTE: Accepted on first Run
-- NOTE: Accepted on first Submit
-- NOTE: Runtime 4054 ms Beats 5.20%
