CREATE TABLE users (
user_id INT PRIMARY KEY,
email VARCHAR(255)
);

CREATE TABLE emails (
email_id INT PRIMARY KEY,
sender VARCHAR(255),
receiver VARCHAR(255),
subject VARCHAR(255),
body TEXT,
created_at TIMESTAMP
);
