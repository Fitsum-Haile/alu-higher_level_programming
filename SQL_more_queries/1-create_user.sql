-- Create user_0d_1 with all privileges on the MySQL server

-- Check if the user already exists
SET @user_exists := (SELECT COUNT(*) FROM mysql.user WHERE user = 'user_0d_1' AND host = 'localhost');

-- If the user does not exist, create it and grant all privileges
IF @user_exists = 0 THEN
    CREATE USER 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
    GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;
    FLUSH PRIVILEGES;
END IF;
