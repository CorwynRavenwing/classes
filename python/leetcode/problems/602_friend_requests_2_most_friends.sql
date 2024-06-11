# Write your MySQL query statement below

select C.id, count(C.friend) as num from (
    select A.requester_id as id, A.accepter_id as friend
    from RequestAccepted as A
    UNION ALL
    select B.accepter_id as id, B.requester_id as friend
    from RequestAccepted as B
) as C
group by C.id
order by num desc
limit 1

# NOTE: 319 ms; Beats 94.48% of users with MySQL
