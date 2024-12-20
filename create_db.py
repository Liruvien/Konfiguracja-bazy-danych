from psycopg2 import connect, OperationalError
from psycopg2.errors import DuplicateDatabase, DuplicateTable

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

try:
    cnx = connect(user=DB_USER, password=DB_PASSWORD, host=DB_HOST)
    cnx.autocommit = True
    cursor = cnx.cursor()

    try:
        cursor.execute(CREATE_DB)
        print("Database created")
    except DuplicateDatabase as e:
        print("Database exists ", e)
    cnx.close()
except OperationalError as e:
    print("Connection Error: ", e)


try:
    cnx = connect(database="workshop", user=DB_USER, password=DB_PASSWORD, host=DB_HOST)
    cnx.autocommit = True
    cursor = cnx.cursor()

    try:
        cursor.execute(CREATE_USERS_TABLE)
        print("Table users created")
    except DuplicateTable as e:
        print("Table exists ", e)
    try:
        cursor.execute(CREATE_MESSAGES_TABLE)
        print("Table messages created")
    except DuplicateTable as e:
        print("Table exists ", e)
    cnx.close()
except OperationalError as e:
    print("Connection Error: ", e)