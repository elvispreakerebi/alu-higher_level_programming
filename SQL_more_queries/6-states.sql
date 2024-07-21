-- Task: Create the database hbtn_0d_usa and the table states
-- Description: 
-- - The database hbtn_0d_usa should be created if it doesn't exist
-- - The table states should be created in the database hbtn_0d_usa
-- - The table states should have columns:
--     - id: INT, unique, auto generated, not null, primary key
--     - name: VARCHAR(256), not null
-- - The script should not fail if the database or table already exists

-- Create the database hbtn_0d_usa if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Use the database hbtn_0d_usa
USE hbtn_0d_usa;

-- Create the table states if it doesn't exist
CREATE TABLE IF NOT EXISTS states (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);
