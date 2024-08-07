-- Write a script that uses the hbtn_0d_tvshows database to list all genres of the show Dexter.
-- Each record should display: tv_genres.name
-- Results must be sorted in ascending order by the genre name

SELECT tv_shows.title
FROM tv_genres
JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
JOIN tv_shows ON tv_shows.id = tv_show_genres.show_id
WHERE tv_genres.name = "Comedy"
ORDER BY tv_shows.title;
