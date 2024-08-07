-- Task: Print the full description of the table first_table from the database hbtn_0c_0 without using DESCRIBE or EXPLAIN statements

-- Select table information from information_schema
SELECT 
    COLUMN_NAME, 
    COLUMN_TYPE, 
    IS_NULLABLE, 
    COLUMN_KEY, 
    COLUMN_DEFAULT, 
    EXTRA
FROM 
    INFORMATION_SCHEMA.COLUMNS
WHERE 
    TABLE_SCHEMA = 'hbtn_0c_0'
    AND TABLE_NAME = 'first_table';
