# Write your MySQL query statement below
delete from Person C
where C.id in (
    select * from (
        select B.id from Person B
        INNER JOIN Person A
            ON A.email = B.email
            and A.id < B.id
    ) as D
)
