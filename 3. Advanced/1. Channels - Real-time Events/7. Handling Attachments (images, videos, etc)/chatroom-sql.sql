
CREATE TABLE IF NOT EXISTS users(
	id SERIAL PRIMARY KEY,
	username VARCHAR(30) NOT NULL UNIQUE,
	email VARCHAR(30) NOT NULL UNIQUE
)

INSERT INTO users(username, email) VALUES
('nik', 'nik@gmail.com'),
('bun', 'bun@yahoo.com'),
('joe', 'joe@gmail.com'),
('keza', 'keza@gmail.com');

CREATE TABLE IF NOT EXISTS chatroom(
	id SERIAL PRIMARY KEY,
	room_name VARCHAR(100) NOT NULL UNIQUE
);

INSERT INTO chatroom(room_name) VALUES ('roomx'), ('roomy'), ('roomz'), ('rooma'), ('roomb');
	
CREATE TABLE IF NOT EXISTS chatroom_users(
	user_id INT REFERENCES users(id) ON DELETE CASCADE,
	room_id INT REFERENCES chatroom(id) ON DELETE CASCADE,
	PRIMARY KEY(user_id, room_id)
);

INSERT INTO chatroom_users VALUES (1, 2), (2, 4), (1, 3), (4, 1);
INSERT INTO chatroom_users VALUES (2, 2), (3, 4), (4, 3), (3, 1);


SELECT *
FROM users;

SELECT *
FROM chatroom;

SELECT *
FROM chatroom_users;

SELECT *
FROM chatroom cr
INNER JOIN chatroom_users cru ON cru.room_id = cr.id
WHERE cru.user_id = 1;

SELECT cr.*, us.*
FROM chatroom cr
INNER JOIN chatroom_users cru ON cr.id = cru.room_id
INNER JOIN users us ON us.id = cru.user_id
WHERE cr.id IN (
	SELECT cr.id
	FROM chatroom cr
	INNER JOIN chatroom_users cru ON cru.room_id = cr.id
	WHERE cru.user_id = 1
) AND us.id != 1;


SELECT cr.*, us.*
FROM chatroom cr
INNER JOIN chatroom_users cru1 
    ON cr.id = cru1.room_id
INNER JOIN chatroom_users cru2 
    ON cr.id = cru2.room_id
INNER JOIN users us 
    ON us.id = cru2.user_id
WHERE cru1.user_id = 1
AND us.id != 1;


SELECT cr.*,
(
    SELECT u.username
    FROM auth_user u
    JOIN chatroom_users cru
      ON u.id = cru.user_id
    WHERE cru.chatroom_id = cr.id
    AND u.id != %(user_id)s
    LIMIT 1
) AS receiver
FROM chatroom cr
JOIN chatroom_users cru_main
  ON cr.id = cru_main.chatroom_id
WHERE cru_main.user_id = %(user_id)s;
