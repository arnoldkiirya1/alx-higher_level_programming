-- Results are grouped by genre ID and sorted in descending order by the rating sum.
SELECT tv_genres.name, SUM(tv_show_ratings.rating) AS rating_sum
FROM tv_genres
LEFT JOIN tv_show_ratings ON tv_genres.id = tv_show_ratings.genre_id
GROUP BY tv_genres.id, tv_genres.name
ORDER BY rating_sum DESC;
