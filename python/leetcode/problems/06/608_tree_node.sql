select Data.id,
CASE
    WHEN Parent is NULL THEN "Root"
    WHEN Children = 0 THEN "Leaf"
    ELSE "Inner"
END as type
from (
    select Self.id
    , Parent.id AS Parent
    , COUNT(Child.id) as Children
    from Tree as Self
    left join Tree as Parent on Parent.id = Self.p_id
    left join Tree as Child on Self.id = Child.p_id
    group by Self.id
) as Data

-- NOTE: Runtime 488 ms Beats 33.95%
