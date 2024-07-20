-- Task: List all records from the table 'second_table' of the database 'hbtn_0c_0'
-- Display only rows with a non-null 'name' value
-- Results should show 'score' and 'name', ordered by descending 'score'

USE hbtn_0c_0;

SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
