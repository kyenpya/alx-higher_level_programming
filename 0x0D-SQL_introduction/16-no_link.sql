-- lists all records of the table
-- second_table where name is not empty

SELECT score, name FROM second_table WHERE name IS NOT NULL
ORDER BY score DESC;
