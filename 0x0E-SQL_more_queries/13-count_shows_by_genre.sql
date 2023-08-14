-- Select the genre and count the number of shows for each genre.
-- Use LEFT JOIN to include all genres, and GROUP BY clause to group records by genre_id.
-- The COUNT function is used to count the number of shows for each genre.
SELECT tv_genres.name AS genre, COUNT(tv_show_genres.show_id) AS number_of_shows
FROM tv_genres
LEFT JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
GROUP BY tv_genres.name
HAVING COUNT(tv_show_genres.show_id) > 0
ORDER BY number_of_shows DESC;
