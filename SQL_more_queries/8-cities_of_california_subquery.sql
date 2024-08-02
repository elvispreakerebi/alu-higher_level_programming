-- This SQL script lists all the cities of California from the database hbtn_0d_usa.
-- The states table contains only one record where name = 'California'.
-- Results are sorted in ascending order by cities.id.
-- The script does not use the JOIN keyword.
-- The database name will be passed as an argument of the mysql command.

SELECT cities.id, cities.name
FROM cities
WHERE cities.state_id = (
  SELECT states.id
  FROM states
  WHERE states.name = 'California'
)
ORDER BY cities.id ASC;
