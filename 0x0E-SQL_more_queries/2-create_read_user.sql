-- creates the hbtn_0d_2 database

CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- creates user_0d_2
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- grant select privilege to user
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
