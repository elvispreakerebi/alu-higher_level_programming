-- Script to list all genres of the show Dexter
-- The tv_shows table contains only one record where title = Dexter (but the id can be different)
-- Each record should display: tv_genres.name
-- Results must be sorted in ascending order by the genre name
-- You can use only one SELECT statement
-- The database name will be passed as an argument of the mysql command

SELECT
    tg.name
FROM
    tv_genres tg
JOIN
    tv_show_genres tsg ON tg.id = tsg.genre_id
JOIN
    tv_shows ts ON tsg.show_id = ts.id
WHERE
    ts.title = 'Dexter'
ORDER BY
    tg.name ASC;
