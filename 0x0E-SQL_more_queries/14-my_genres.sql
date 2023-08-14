-- This script lists all genres of the show "Dexter" from the hbtn_0d_tvshows database.

-- Select the genre name from the tv_genres table for the specific show "Dexter."
-- Use JOIN to link tv_shows and tv_show_genres tables based on show_id and genre_id.
-- Use WHERE clause to filter shows with title "Dexter."
-- Results are sorted in ascending order by the genre name.
SELECT tv_genres.name
FROM tv_genres
JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
JOIN tv_shows ON tv_shows.id = tv_show_genres.show_id
WHERE tv_shows.title = 'Dexter'
ORDER BY tv_genres.name ASC;
