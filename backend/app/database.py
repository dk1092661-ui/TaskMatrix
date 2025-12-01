import sqlite3

conn = sqlite3.connect("users.db", check_same_thread=False)
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT UNIQUE,
    password TEXT
)
""")
conn.commit()


def create_user(email, password):
    cur.execute("INSERT INTO users (email, password) VALUES (?, ?)", (email, password))
    conn.commit()


def validate_user(email, password):
    cur.execute("SELECT * FROM users WHERE email=? AND password=?", (email, password))
    return cur.fetchone() is not None


def user_exists(email):
    cur.execute("SELECT * FROM users WHERE email=?", (email,))
    return cur.fetchone() is not None
