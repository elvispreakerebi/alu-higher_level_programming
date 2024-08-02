-- Script to create the table id_not_null on a MySQL server
-- The table will have an id column with a default value of 1 and a name column with a maximum length of 256 characters
-- If the table already exists, the script will not fail

-- Check if the table id_not_null exists, if not create it
CREATE TABLE IF NOT EXISTS unique_id (
    id INT UNIQUE DEFAULT 1,
    name VARCHAR(256)
);
