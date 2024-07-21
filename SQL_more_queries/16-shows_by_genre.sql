-- Task: List all shows and their genres from the hbtn_0d_tvshows database
-- If a show doesn’t have a genre, display NULL in the genre column
-- Each record should display: tv_shows.title - tv_genres.name
-- Results must be sorted in ascending order by the show title and genre name
-- Use only one SELECT statement

SELECT 
    tv_shows.title,
    tv_genres.name AS genre
FROM 
    tv_shows
LEFT JOIN 
    tv_genres
ON 
    tv_shows.id = tv_genres.show_id
ORDER BY 
    tv_shows.title ASC, 
    tv_genres.name ASC;
