select query_name
, round(sum(quality_ratio) / count(quality_ratio), 2) as quality
, round(100 * sum(is_poor) / count(is_poor), 2) as poor_query_percentage
from (
    select Q.query_name
    , (rating / position) as quality_ratio
    , (rating < 3) as is_poor
    from Queries as Q
    where Q.query_name is not null
) as D
group by query_name

