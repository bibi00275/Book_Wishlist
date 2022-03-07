import sqlite3


conn = sqlite3.connect('database.sqlite')
cur = conn.cursor()

# create users table
cur.execute('''
CREATE TABLE IF NOT EXISTS user(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT,
    last_name TEXT,
    email TEXT,
    password TEXT
);
''')

# create book table
cur.execute('''
CREATE TABLE IF NOT EXISTS book(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    author INTEGER,
    isbn TEXT
);
''')

# create wishlist table
cur.execute('''
CREATE TABLE IF NOT EXISTS wishlist(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    isbn TEXT,
    user_id INTEGER,
    date_of_publication TEXT,
    title TEXT
);
''')


cur.execute('''
    INSERT INTO WISHLIST (ISBN, USER_ID, DATE_OF_PUBLICATION, TITLE)
    VALUES ('testisbn 2', 1, '07/03/2022', 'test title 2')
''')
conn.commit()
