-- Script to create the table force_name on MySQL server
-- The script ensures the table is created only if it doesn't already exist

-- Use the database provided as an argument
USE your_database_name;

-- Check if the table force_name exists and create it if it doesn't
CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL
);
