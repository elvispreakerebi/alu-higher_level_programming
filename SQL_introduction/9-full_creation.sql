-- This script creates a table named second_table in the database hbtn_0c_0
-- and inserts multiple rows into it. The script will not fail if the table
-- already exists.

-- Creating the table second_table if it doesn't exist
CREATE TABLE IF NOT EXISTS second_table (
    id INT,
    name VARCHAR(256),
    score INT
);

-- Inserting multiple rows into second_table
INSERT INTO second_table (id, name, score) VALUES (1, 'John', 10);
INSERT INTO second_table (id, name, score) VALUES (2, 'Alex', 3);
INSERT INTO second_table (id, name, score) VALUES (3, 'Bob', 14);
INSERT INTO second_table (id, name, score) VALUES (4, 'George', 8);
