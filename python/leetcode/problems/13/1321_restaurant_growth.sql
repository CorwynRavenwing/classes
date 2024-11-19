
select visited_on
    , amount
    , round(average_amount, 2) as average_amount
from (
    select visited_on
        , sum(amount) over (
            order by visited_on
            range interval 6 day preceding
        ) as amount
        , avg(amount) over (
            order by visited_on
            range interval 6 day preceding
        ) as average_amount
    from (
        select visited_on
            , sum(amount) as amount
        from Customer
        group by visited_on
    ) as A
) as B
where B.visited_on >= (
    select date_add(min(visited_on), interval 6 day)
    from Customer
)

-- NOTE: Accepted on first Submit
-- NOTE: Runtime 395 ms Beats 55.22%
