# Write your MySQL query statement below

select A.name as results
FROM (
    select U.name, count(R.movie_id) as ratingCount
    from users as U
    left join MovieRating as R USING(user_id)
    group by U.user_id
    order by ratingCount DESC, U.name ASC
    limit 1
) as A
UNION ALL
select B.title as results
FROM (
    select M.title, sum(R.rating) / count(R.rating) as average_rating
    from Movies as M
    left join MovieRating as R USING(movie_id)
    where created_at BETWEEN '2020-02-01' and '2020-02-29'
    group by M.movie_id
    order by average_rating DESC, M.title ASC
    limit 1
) as B

-- NOTE: 957 ms; Beats 97.96%
