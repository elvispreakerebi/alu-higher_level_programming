-- Task: List all genres and the number of shows linked to each genre
-- The result should display: <TV Show genre> - <Number of shows linked to this genre>
-- The first column must be called genre
-- The second column must be called number_of_shows
-- Only genres with linked shows should be displayed
-- Results must be sorted in descending order by the number of shows linked
-- Only one SELECT statement should be used

SELECT tv_genres.name AS genre, COUNT(tv_show_genres.show_id) AS number_of_shows
FROM tv_genres
JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
GROUP BY tv_genres.name
HAVING number_of_shows > 0
ORDER BY number_of_shows DESC;
