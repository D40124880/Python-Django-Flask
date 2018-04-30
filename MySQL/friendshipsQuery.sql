SELECT * FROM users
LEFT JOIN friendships ON users.id = friendships.user_id
LEFT JOIN users AS user2 ON friendships.id = users.id;

UPDATE users
SET first_name = "Jessica", last_name = "Davidson", created_at = now(), updated_at = now()
WHERE id = 4;

INSERT INTO friendships (user_id, friend_id, created_at, updated_at)
VALUES (1, 4, now(), now()), (1, 3, now(), now()), (1, 2, now(), now()), (1, 4, now(), now()), (2, 1, now(), now()), (3, 1, now(), now()), (4, 1, now(), now());

SELECT users.first_name, users.last_name, user2.first_name as friend_first_name, user2.last_name as friend_last_name
FROM users
LEFT JOIN friendships ON users.id = friendships.user_id
LEFT JOIN users AS user2 ON friendships.id = users.id;


SELECT users.first_name, users.last_name, user2.first_name as friend_first_name, user2.last_name as friend_last_name
FROM users
LEFT JOIN friendships ON friendships.friend_id = users.id
LEFT JOIN users AS user2 ON user2.id = friendships.user_id
ORDER BY user2.last_name desc;

DELETE FROM friendships
WHERE id = 1;

SELECT users.first_name, users.last_name, user2.first_name as friend_first_name, user2.last_name as friend_last_name
FROM users
LEFT JOIN friendships ON friendships.friend_id = users.id
LEFT JOIN users AS user2 ON user2.id = friendships.user_id
ORDER BY user2.last_name desc;