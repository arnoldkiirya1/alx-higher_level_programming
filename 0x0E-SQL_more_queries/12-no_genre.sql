-- This script lists all shows without a genre linked in the hbtn_0d_tvshows database.

-- Select the required columns from the tv_shows and tv_show_genres tables.
-- Use LEFT JOIN to include all shows, and WHERE condition to filter out shows with genre_id as NULL.
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
WHERE tv_show_genres.genre_id IS NULL
ORDER BY tv_shows.title, tv_show_genres.genre_id;
