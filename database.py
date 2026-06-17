import sqlite3

DATABASE = "library.db"


def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row  # access columns by name, e.g. row["title"]
    conn.execute("PRAGMA foreign_keys = ON")  # SQLite has this off by default
    return conn
