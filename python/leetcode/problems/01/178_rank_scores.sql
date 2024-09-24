select C.score, scoreRank as 'rank'
    from Scores as C
    left join (
        select B.score, ROW_NUMBER() OVER(order by score DESC) as scoreRank
        from (
            select DISTINCT A.score
            from Scores as A
            order by A.score DESC
        ) as B
    ) as D
    using(score)
    order by C.score DESC

-- NOTE: Accepted on first Submit
-- NOTE: First submit gave "beats 75%" speed; re-ran and got this value
-- NOTE: Runtime 311 ms Beats 46.20%
