-- This script creates a table called first_table in the current database.
-- The table contains two columns: id (INT) and name (VARCHAR(256)).
-- If the table already exists, the script will not fail.

-- Create the first_table if it does not already exist
CREATE TABLE IF NOT EXISTS first_table (
    id INT,
    name VARCHAR(256)
);
