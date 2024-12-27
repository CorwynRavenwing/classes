
select category
    , sum(count) as accounts_count
from (
    select CASE
            WHEN income < 20000 THEN "Low Salary"
            WHEN income > 50000 THEN "High Salary"
            ELSE "Average Salary"
        END as category
        , 1 as count
    from Accounts
    UNION ALL
    select "Low Salary" as category, 0 as count
    UNION ALL
    select "High Salary" as category, 0 as count
    UNION ALL
    select "Average Salary" as category, 0 as count
) as A
group by category

-- NOTE: Accepted on first Run
-- NOTE: Accepted on first Submit
-- NOTE: Runtime 2904 ms Beats 11.35%
