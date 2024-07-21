-- Script to create the database hbtn_0d_usa and the table cities
-- The cities table will have columns: id, state_id, and name
-- The id is a unique, auto-generated, non-null primary key
-- The state_id is a non-null foreign key referencing the states table
-- The name is a non-null VARCHAR(256)

-- Create the database if it does not already exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Use the database
USE hbtn_0d_usa;

-- Create the table cities if it does not already exist
CREATE TABLE IF NOT EXISTS cities (
    -- id column: unique, auto-generated, non-null primary key
    id INT AUTO_INCREMENT PRIMARY KEY,
    -- state_id column: non-null foreign key referencing states table
    state_id INT NOT NULL,
    -- name column: non-null VARCHAR(256)
    name VARCHAR(256) NOT NULL,
    -- Constraint to ensure state_id references id in states table
    FOREIGN KEY (state_id) REFERENCES states(id)
);
