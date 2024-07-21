-- This SQL script lists all the cities of California from the database hbtn_0d_usa.
-- The states table contains only one record where name = 'California'.
-- Results are sorted in ascending order by cities.id.
-- The script does not use the JOIN keyword.
-- The database name will be passed as an argument of the mysql command.

-- Select the state id of California from the states table
SELECT @california_state_id := id
FROM states
WHERE name = 'California';

-- Select all the cities of California sorted by cities.id in ascending order
SELECT id, name
FROM cities
WHERE state_id = @california_state_id
ORDER BY id ASC;
