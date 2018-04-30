One to One
SELECT * FROM customers 
JOIN addresses ON addresses.id = customers.address_id;

One to Many
SELECT * FROM orders 
JOIN customers ON customers.id = orders.customer_id;

Many to Many
SELECT * FROM orders 
JOIN items_orders ON orders.id = items_orders.order_id 
JOIN items ON items.id = items_orders.item_id;
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

-- joining tables
-- JOIN
-- find all the clients (first and last name_) billing amounts and charged date
SELECT clients.first_name, clients.last_name, billing.amount, billing.charged_datetime
FROM clients
JOIN billing ON clients.id = billing.clients_id;
-- list all the domain names and leads (first and last name) for each site
SELECT sites.domain_name, leads.first_name, leads.last_name
FROM sites
JOIN leads ON sites.id = leads.sites_id;
-- JOIN ON MULTIPLE TABLES
-- get the names of the clients, their domain names and the first names of all the leads generated from those sites
SELECT clients.first_name AS client_first, clients.last_name, sites.domain_name, leads.first_name
FROM clients
JOIN sites ON clients.id = sites.clients_id
JOIN leads ON sites.id = leads.sites_id;
-- left & right join
-- list all the clients and the sites each client has, even if the client hasn't landed a site yet
SELECT clients.first_name, clients.last_name, sites.domain_name
FROM clients
LEFT JOIN sites ON clients.id = sites.clients_id;
-- grouping rows
-- group by
-- sum, min, max, avg
-- find all the clients (first and last name) and their total billing amounts
SELECT clients.first_name, clients.last_name, SUM(billing.amount)
FROM clients
JOIN billing ON clients.id = billing.clients_id
GROUP BY clients.id;
-- group concat
-- list all the domain names associated with each client
SELECT GROUP_CONCAT(" ", sites.domain_name) AS domains, clients.first_name, clients.last_name
FROM clients
JOIN sites ON clients.id = sites.clients_id
GROUP BY clients.id;
-- count
-- find the total number of leads for each site
SELECT COUNT( leads.id), sites.domain_name
FROM sites
JOIN leads ON sites.id = leads.sites_id
GROUP BY sites.id;
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
1. What query would you run to get all tweets from the user id of 1?
SELECT *
FROM users
LEFT JOIN tweets
ON users.id = tweets.user_id
WHERE users.id = 1;
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
You can just grab the tweets by:

SELECT tweets.tweet
FROM users
LEFT JOIN tweets
ON users.id = tweets.user_id
WHERE users.id = 1;
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Or rename the output column that you want as kobe_tweets by modifying the statement to look like the following:

SELECT tweets.tweet as kobe_tweets
FROM users
LEFT JOIN tweets
ON users.id = tweets.user_id
WHERE users.id = 1;
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
2. What query would return all the tweets that the user with id 2 has tagged as favorites?
SELECT first_name, tweet
FROM users
LEFT JOIN faves
ON users.id = faves.user_id
LEFT JOIN tweets
ON faves.tweet_id = tweets.id
WHERE users.id = 2;
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
What query would you run to get all the tweets that user with id 2, or user with id 1, has tagged as favorites?
SELECT first_name, tweet
FROM users
LEFT JOIN faves
ON users.id = faves.user_id
LEFT JOIN tweets
ON faves.tweet_id = tweets.id
WHERE users.id = 1 OR users.id = 2;
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
What query would you run to get all the users that are following the user with id 1?
SELECT users.first_name as followed, users2.first_name as follower
FROM users
LEFT JOIN follows
ON users.id = follows.followed_id
LEFT JOIN users as users2
ON users2.id = follows.follower_id
WHERE users.id = 1;
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
What query would you run to get all users that are not following the user with id of 2?
This requires nested queries, which you can learn about at http://sqlzoo.net/wiki/SELECT_within_SELECT_Tutorial.

SELECT *
FROM users
WHERE users.id NOT IN (
SELECT follower_id
FROM follows
WHERE followed_id = 2
) AND users.id != 2;
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
We can run functions on specific columns and often times it is paired up with the GROUP BY statement. We will have plenty of practice with functions in the next tab. 

SELECT users.first_name as user, COUNT(users2.first_name) as follower_count
FROM users
LEFT JOIN follows
ON users.id = follows.followed_id
LEFT JOIN users as users2
ON users2.id = follows.follower_id
WHERE users.id = 1
GROUP BY users.id
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
LEFT JOIN vs JOIN
For example, running the following SQL command in our twitter database will result in the following:

SELECT first_name, tweet
FROM users
LEFT JOIN tweets
ON users.id = tweets.user_id

Notice that this result includes a final row containing Rajon with no associated tweet. 
Now if we change the LEFT JOIN command to the JOIN command, the output will be as follows:

SELECT first_name, tweet
FROM users
JOIN tweets
ON users.id = tweets.user_id
