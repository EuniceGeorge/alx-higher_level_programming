-- Find the state id for California
SELECT id FROM states WHERE name = 'California';

-- List all the cities of California using the state id
SELECT * FROM cities WHERE state_id = (SELECT id FROM states WHERE name = 'California') ORDER BY id ASC;
