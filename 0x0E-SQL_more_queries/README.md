0x0E. SQL - More Queries

Description
This project is part of the ALX SE program and focuses on advanced SQL queries. You'll learn how to create users, manage permissions, and use advanced SQL features such as joins, subqueries, and constraints.

Learning Objectives
By the end of this project, you should be able to explain the following concepts without using Google:

How to create a new MySQL user
How to manage privileges for a user to a database or table
What's a PRIMARY KEY
What's a FOREIGN KEY
How to use NOT NULL and UNIQUE constraints
How to retrieve data from multiple tables in one request
What are subqueries
What are JOIN and UNION

Requirements
Allowed editors: vi, vim, emacs
All your files will be executed on Ubuntu 20.04 LTS using MySQL 8.0 (version 8.0.25)
All your files should end with a new line
All your SQL queries should have a comment just before (i.e. syntax above)
All your files should start by a comment describing the task
All SQL keywords should be in uppercase (SELECT, WHERE, etc.)
A README.md file, at the root of the folder of the project, is mandatory
The length of your files will be tested using wc

Tasks
0. My privileges!
Write a script that lists all privileges of the MySQL users user_0d_1 and user_0d_2 on your server (in localhost).

File: 0-privileges.sql

1. Root user
Write a script that creates the MySQL server user user_0d_1.

File: 1-create_user.sql

2. Read user
Write a script that creates the database hbtn_0d_2 and the user user_0d_2.

File: 2-create_read_user.sql

3. Always a name
Write a script that creates the table force_name on your MySQL server.

File: 3-force_name.sql

4. ID can't be null
Write a script that creates the table id_not_null on your MySQL server.

File: 4-never_empty.sql

5. Unique ID
Write a script that creates the table unique_id on your MySQL server.

File: 5-unique_id.sql

6. States table
Write a script that creates the database hbtn_0d_usa and the table states (in the database hbtn_0d_usa) on your MySQL server.

File: 6-states.sql

7. Cities table
Write a script that creates the database hbtn_0d_usa and the table cities (in the database hbtn_0d_usa) on your MySQL server.

File: 7-cities.sql

8. Cities of California
Write a script that lists all the cities of California that can be found in the database hbtn_0d_usa.

File: 8-cities_of_california_subquery.sql

9. Cities by States
Write a script that lists all cities contained in the database hbtn_0d_usa.

File: 9-cities_by_state_join.sql

10. Genre ID by show
Write a script that lists all shows contained in hbtn_0d_tvshows that have at least one genre linked.

File: 10-genre_id_by_show.sql

11. Genre ID for all shows
Write a script that lists all shows contained in the database hbtn_0d_tvshows.

File: 11-genre_id_all_shows.sql

12. No genre
Write a script that lists all shows contained in hbtn_0d_tvshows without a genre linked.

File: 12-no_genre.sql

13. Number of shows by genre
Write a script that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.

File: 13-count_shows_by_genre.sql

How to Use

Install MySQL 8.0 on Ubuntu 20.04 LTS:
sudo apt update
sudo apt install mysql-server

Connect to your MySQL server:
sudo mysql

Run the SQL scripts provided in the repository. Each script can be executed using the following command:
cat <script_file.sql> | mysql -uroot -p
