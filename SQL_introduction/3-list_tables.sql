-- This listed all the TABLES
SELECT table_name
FROM information_schema.tables
WHERE table_schema =  @@database_name;