-- This script lists all shows with their respective genre_id in the hbtn_0d_tvshows database.

-- Select the required columns from the tv_shows and tv_show_genres tables and join them using the show_id column.
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title, tv_show_genres.genre_id;
