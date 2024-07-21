-- This script creates a MySQL server user 'user_0d_1' with all privileges
-- and sets the password to 'user_0d_1_pwd'. If the user already exists, 
-- the script will not fail.

-- Create the user if it does not already exist
CREATE USER IF NOT EXISTS 'user_0d_1'@'%' IDENTIFIED BY 'user_0d_1_pwd';

-- Grant all privileges to the user
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'%';

-- Apply the changes
FLUSH PRIVILEGES;
