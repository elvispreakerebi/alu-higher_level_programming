-- This script lists all records of the table 'second_table' from the database passed as an argument.
-- The results display both the score and the name (in this order).
-- Records are ordered by score in descending order (top first).

-- Query to select score and name from second_table and order by score
SELECT score, name
FROM second_table
ORDER BY score DESC;
