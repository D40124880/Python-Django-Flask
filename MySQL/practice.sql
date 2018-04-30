Let's see what's in the users table by running:

SELECT * 
FROM users;


faves
Let's see what's in the faves table by running:

SELECT * 
FROM faves;


follows
Let's see what's in the follows table by running:

SELECT *  
FROM follows;


tweets
Let's see what's in the tweets table by running:

SELECT *
FROM tweets;


Basics
What query would you run to get all of the users?

SELECT * 
FROM users;
What query would you run to only get the first names of all of the users?
SELECT first_name 
FROM users;
What query would you run to only get the first and last names of all of the users? 
SELECT first_name, last_name
FROM users;
SELECT w/ Conditionals
What query would you run to only get the first name of users with id of 2?

SELECT first_name
FROM users
WHERE id = 2;
What query would you run to get the last names of users with id of 2 or 3?

SELECT last_name
FROM users
WHERE id = 2 OR id = 3;
What query would you run to get all of the users with id greater than 2?
SELECT *
FROM users
WHERE id > 2;
What query would you run to get all of the users with id less than or equal to 3?
SELECT *
FROM users
WHERE id <= 3;
What query would you run to get all of the users with first names ending in "e"?
SELECT * 
FROM users
WHERE first_name LIKE "%e";
What query would you run to get all of the users with first names starting in "K"?
SELECT * 
FROM users
WHERE first_name LIKE "K%";
SELECT w/ Sorting
What query would you run to get all of the users with the youngest users at the top of the table?

SELECT *
FROM users
ORDER BY birthday DESC;
What query would you run to get all of the users with the oldest users at the top of the table?

SELECT *
FROM users
ORDER BY birthday ASC;
What query would you run to get all of the users with the first name that ends with "e" with the youngest users at the top of the table?

SELECT *
FROM users
WHERE first_name LIKE "%e"
ORDER BY birthday DESC;
What query would you run to get only the first names of all of the users in alphabetical order?

SELECT first_name
FROM users
ORDER BY first_name;


---------------------------------------------------------------------------------------------------------------------------------------------------------------------------



INSERT INTO tweets (tweet, user_id, created_at, updated_at)
VALUES	("helloooo", 1, NOW(), NOW());
INSERT INTO table_name (column_name1, column_name2) 
VALUES('column1_value', 'column2_value');



UPDATE table_name SET column_name1 = 'some_value', column_name2='another_value' WHERE condition(s)



DELETE FROM table_name WHERE condition(s)
IMPORTANT: if WHERE condition is not added to the DELETE statement, it will delete all the records on the table.
for safe use when deleting use: SET SQL_SAFE_UPDATES = 0; run it then refresh it again

SELECT CONCAT("MR.", first_name, " ", last_name) AS Together FROM users;
-- will result in "MR. Kobe Bryant

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

-- concat()
SELECT CONCAT("MR.", first_name, " ", last_name) AS Together FROM users;
-- concat _ws()
SELECT CONCAT_WS("MR.", first_name, last_name) AS Full_Name FROM users;
-- length()
SELECT CONCAT(last_name) AS last_len FROM users;
-- lower()
SELECT LOWER(first_name) AS first_lowercas FROM users;


-- date()
-- hour()
SELECT HOUR(joined_datetime) AS date_hour, joined_datetime FROM users;
-- datetime()
SELECT DAYNAME(joined_datetime) AS day_name, joined_datetime FROM users;
-- month()
SELECT MONTH(joined_datetime) AS month_number, joined_datetime FROM users;
-- now() -- gives you the current time as of now now
SELECT NOW() AS right_name;
-- date_format()
SELECT DATE_FORMAT(joined_datetime, "%W  %M %e %Y") FROM users;

