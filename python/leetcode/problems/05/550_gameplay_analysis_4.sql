# Write your MySQL query statement below

select (
    round( SUM(D.second_day_logon) / count(*), 2)
) as fraction
FROM (
    select C.player_id,
        (
            SELECT COUNT(*)
            FROM Activity as B
            WHERE C.player_id = B.player_id
            AND DATE_ADD(first_date, INTERVAL 1 DAY) = B.event_date
        ) as second_day_logon
    from (
        select A.player_id, min(A.event_date) as first_date
        from Activity as A
        group by A.player_id
    ) AS C
) as D

