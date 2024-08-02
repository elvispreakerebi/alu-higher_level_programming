-- Script to create the table force_name on MySQL server
-- The script ensures the table is created only if it doesn't already exist

CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL
);

-- Insert sample data
INSERT INTO force_name (id, name) VALUES (1, 'Holberton School');
INSERT INTO force_name (id, name) VALUES (1, 'Python is cool');
INSERT INTO force_name (id, name) VALUES (2, 'Holberton');
INSERT INTO force_name (id, name) VALUES (3, 'School');
INSERT INTO force_name (id, name) VALUES (4, 'C is fun');
