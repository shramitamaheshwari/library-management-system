import sqlite3
from werkzeug.security import generate_password_hash

DATABASE = "library.db"


def init_db():
    conn = sqlite3.connect(DATABASE)

    with open("schema.sql") as f:
        conn.executescript(f.read())

    admin_password = generate_password_hash("admin123")
    conn.execute(
        "INSERT INTO users (name, email, password, role, approved) VALUES (?, ?, ?, ?, ?)",
        ("Admin", "admin@npcil.co.in", admin_password, "admin", 1)
    )

    conn.commit()
    conn.close()
    print("Database created: library.db")
    print("Seed admin login -> email: admin@library.com | password: admin123")


if __name__ == "__main__":
    init_db()
