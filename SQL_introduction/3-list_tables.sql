-- This should listed all the tables inside specified DATABASE
SELECT table_name
FROM information_schema.tables
WHERE table_schema = 'mysql';