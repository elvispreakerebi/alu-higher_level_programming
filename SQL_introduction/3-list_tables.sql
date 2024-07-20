-- Task: List all tables of a database in MySQL server
-- This SQL script lists all the tables in the specified database

-- Use the database specified as an argument
USE mysql;

-- Query to list all tables in the current database
SELECT 
    TABLE_NAME 
FROM 
    INFORMATION_SCHEMA.TABLES 
WHERE 
    TABLE_SCHEMA = 'mysql';
