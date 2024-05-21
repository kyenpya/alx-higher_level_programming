-- lists all records with score >= 10
-- displays in a certain order

SELECT score, name FROM second_table
WHERE score >= 10
ORDER BY score DESC;
