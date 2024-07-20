-- List all privileges of the MySQL users user_0d_1 and user_0d_2 on localhost

-- Check for user_0d_1 and show their privileges
SELECT CONCAT('Grants for user_0d_1@localhost') AS user_privilege;
SHOW GRANTS FOR 'user_0d_1'@'localhost';

-- Check for user_0d_2 and show their privileges
SELECT CONCAT('Grants for user_0d_2@localhost') AS user_privilege;
SHOW GRANTS FOR 'user_0d_2'@'localhost';
