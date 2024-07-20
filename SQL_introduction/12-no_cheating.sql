-- Update the score of Bob to 10 in the table second_table
-- This script updates the score for the user named 'Bob' in the table 'second_table' within the specified database.

-- Update Bob's score to 10
UPDATE second_table
SET score = 10
WHERE name = 'Bob';
