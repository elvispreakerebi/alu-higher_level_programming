-- Task: List all genres and the number of shows linked to each genre
-- The result should display: <TV Show genre> - <Number of shows linked to this genre>
-- The first column must be called genre
-- The second column must be called number_of_shows
-- Only genres with linked shows should be displayed
-- Results must be sorted in descending order by the number of shows linked
-- Only one SELECT statement should be used

SELECT
    g.name AS genre,
    COUNT(tg.tv_show_id) AS number_of_shows
FROM
    genres g
JOIN
    tv_show_genres tg ON g.id = tg.genre_id
GROUP BY
    g.name
HAVING
    COUNT(tg.tv_show_id) > 0
ORDER BY
    number_of_shows DESC;
