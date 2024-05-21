-- lists all records with the same score
-- in the second_table

SELECT score, COUNT('score')AS NUMBER
FROM second_table
GROUP BY score
ORDER BY score DESC;
