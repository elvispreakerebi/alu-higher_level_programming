-- This script lists all the tables of a database in your MySQL server
-- The database name will be passed as an argument of the mysql command
-- If the database hbtn_0c_0 doesn’t exist, the script should not fail
-- SQL keywords are in uppercase

-- Use the provided database
USE mysql;

-- Ensure the script does not fail if the database does not exist
-- The following statement will only create the procedure if the database exists
DELIMITER //

CREATE PROCEDURE list_tables (IN db_name VARCHAR(255))
BEGIN
  DECLARE CONTINUE HANDLER FOR SQLEXCEPTION BEGIN END;
  SET @stmt = CONCAT('SELECT table_name FROM information_schema.tables WHERE table_schema = "', db_name, '"');
  PREPARE stmt FROM @stmt;
  EXECUTE stmt;
  DEALLOCATE PREPARE stmt;
END //

DELIMITER ;

-- Call the procedure to list tables from the specified database
CALL list_tables('hbtn_0c_0');

-- Drop the procedure after use to clean up
DROP PROCEDURE IF EXISTS list_tables;
