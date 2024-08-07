-- SQL script to list all cities in the database hbtn_0d_usa
-- Each record displays: cities.id - cities.name - states.name
-- Results are sorted in ascending order by cities.id
-- The database name will be passed as an argument of the mysql command

SELECT cities.id, cities.name, states.name
FROM cities
JOIN states ON cities.state_id = states.id
ORDER BY cities.id;
