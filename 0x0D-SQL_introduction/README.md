0x0D. SQL - Introduction

Overview
This repository contains solutions to the project tasks for learning the basics of SQL using MySQL. The project is part of the SE Foundations curriculum and covers fundamental SQL operations, including database creation, table management, and basic queries.

Concepts
Databases
SQL and Relational Algebra
DDL (Data Definition Language)
DML (Data Manipulation Language)
MySQL functions and subqueries

Installation
To install MySQL 8.0 on Ubuntu 20.04 LTS:

sudo apt update
sudo apt install mysql-server
mysql --version
Expected output: mysql  Ver 8.0.25-0ubuntu0.20.04.1 for Linux on x86_64 ((Ubuntu))

To connect to your MySQL server:
sudo mysql

To quit MySQL monitor
quit

Tasks
0. List databases
File: 0-list_databases.sql
Description: Script to list all databases in MySQL server.

1. Create a database
File: 1-create_database_if_missing.sql
Description: Script to create the database hbtn_0c_0.

2. Delete a database
File: 2-remove_database.sql
Description: Script to delete the database hbtn_0c_0.

3. List tables
File: 3-list_tables.sql
Description: Script to list all tables in a specified database.

4. First table
File: 4-first_table.sql
Description: Script to create a table called first_table.

5. Full description
File: 5-full_table.sql
Description: Script to print the full description of first_table.

6. List all in table
File: 6-list_values.sql
Description: Script to list all rows of first_table.

7. First add
File: 7-insert_value.sql
Description: Script to insert a new row in first_table.

8. Count 89
File: 8-count_89.sql
Description: Script to display the number of records with id = 89 in first_table.

9. Full creation
File: 9-full_creation.sql
Description: Script to create a table second_table and add multiple rows.

10. List by best
File: 10-top_score.sql
Description: Script to list all records of second_table ordered by score.

11. Select the best
File: 11-best_score.sql
Description: Script to list records with score >= 10 from second_table.

12. Cheating is bad
File: 12-no_cheating.sql
Description: Script to update Bob's score to 10 in second_table.

13. Score too low
File: 13-change_class.sql
Description: Script to remove records with score <= 5 in second_table.

14. Average
File: 14-average.sql
Description: Script to compute the score average in second_table.

15. Number by score
File: 15-groups.sql
Description: Script to list the number of records with the same score in second_table.

16. Say my name
File: 16-no_link.sql
Description: Script to list all records of second_table with non-null name values.

License
This project is licensed under the terms of ALX's guidelines. All rights reserved by ALX, 2024.
