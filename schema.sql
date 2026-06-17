DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS books;
DROP TABLE IF EXISTS borrow_records;

CREATE TABLE users (
    employee_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email endswith '@npcil.co.in',
    password TEXT NOT NULL,
    role TEXT NOT NULL DEFAULT 'user',
    approved INTEGER NOT NULL DEFAULT 0
);

CREATE TABLE books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    isbn TEXT,
    total_copies INTEGER NOT NULL DEFAULT 1,
    available_copies INTEGER NOT NULL DEFAULT 1
);

CREATE TABLE borrow_records (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    book_id INTEGER NOT NULL,
    status TEXT NOT NULL DEFAULT 'pending',
    request_date TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    decision_date TEXT,
    return_date TEXT,
    FOREIGN KEY (user_id) REFERENCES users (employee_id),
    FOREIGN KEY (book_id) REFERENCES books (id)
);
