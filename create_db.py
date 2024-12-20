DB_USER = "postgres"
PASSWORD = "coderslab"
HOST = "127.0.0.1"

CREATE_DB = "CREATE DATABASE workshop;"
CREATE_USER = """CREATE TABLE users (
                        id SERIAL PRIMARY KEY,
                        username VARCHAR(255) UNIQUE,
                        hashed_password VARCHAR(80) NOT NULL
                        );"""
CREATE_MESSAGES_TABLE = """CREATE TABLE messages (
                        id SERIAL PRIMARY KEY,
                        from_id INT REFERENCES users(id) ON DELETE CASCADE,
                        to_id INT REFERENCES users(id) ON DELETE CASCADE,
                        creation_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
                        text VARCHAR(255) NOT NULL
                        );"""