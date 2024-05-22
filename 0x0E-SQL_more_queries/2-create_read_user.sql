-- creates the database hbtn_0d_2

CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- creates the user
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- grant privileges
GRANT SELECT ON `hbtn_0d_2`.* TO USER 'user_0d_2'@'localhost';

FLUSH PRIVILEGES;
