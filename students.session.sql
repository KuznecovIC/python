CREATE TABLE IF NOT EXISTS students (
     id INTEGER PRIMARY KEY AUTOINCREMENT,
     first_name TEXT NOT NULL,
     middle_name TEXT DEFAULT 'Без отчества',
     last_name TEXT NOT NULL,
     age INTEGER,
     group_name TEXT NOT NULL
);