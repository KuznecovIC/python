--CREATE TABLE IF NOT EXISTS students (
--    id INTEGER PRIMARY KEY AUTOINCREMENT,
--    first_name TEXT NOT NULL,
--    middle_name TEXT DEAFULT "Без отчества",
--    last_name TEXT NOT NULL,
--    age INTEGER,
--    group_name TEXT NOT NULL
--);

--INSERT INTO students (first_name, last_name, group_name)
--VALUES ("Филлип", "Киркоров", "python411");

--SELECT * FROM students;

--UPDATE students
--SET age = 40, middle_name = "Бедросович"
--WHERE id = 1;

--SELECT * FROM students;

--INSERT INTO students (first_name, middle_name, last_name, age, group_name)
--VALUES
--("Анастасия", "Ивановна", "Ивлеева", 30, "python411"),
--("Филлип", "Бедросович", "Киркоров", 50, "python411"),
--("Владимир", "Николаевич", "Путов", 30, "python411"),
--("Григорий", "Станиславович", "Шлепс", 60, "python411");

--SELECT * FROM students;

--CREATE TABLE IF NOT EXISTS groups (
--    id INTEGER PRIMARY KEY AUTOINCREMENT,
--    group_name TEXT NOT NULL UNIQUE
--);

--CREATE TABLE IF NOT EXISTS students (
--    id INTEGER PRIMARY KEY AUTOINCREMENT,
--    first_name TEXT NOT NULL,
--    middle_name TEXT,
--    last_name TEXT NOT NULL,
--    age INTEGER,
--   group_id INTEGER,
--    FOREIGN KEY (group_id) REFERENCES groups(id)
--);

--INSERT INTO students (first_name, middle_name, last_name, age, group_name)
--VALUES
--("Анастасия", "Ивановна", "Ивлеева", 30, 1),
--("Филлип", "Бедросович", "Киркоров", 50, 1),
--("Владимир", "Николаевич", "Путов", 30, 1),
--("Григорий", "Станиславович", "Шлепс", 60, 1);

--SELECT * FROM students;

CREATE TABLE IF NOT EXISTS teachers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    middle_name TEXT DEFAULT "Без отчества",
    last_name TEXT NOT NULL,
    age INTEGER,
    phone TEXT,
    email TEXT
);


CREATE TABLE IF NOT EXISTS teachers_groups (
    teacher_id INTEGER,
    groups_id INTEGER,
    date_start TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (teacher_id) REFERENCES teachers(id),
    FOREIGN KEY (groups_id) REFERENCES groups(id)
);

INSERT INTO groups (group_name)
VALUES ("python411"), ("python412");

INSERT INTO teachers (first_name, last_name, phone, )
VALUES
("Сергей", "Бурунов", "+7(999)999-99-99"),
("Станислав", "Петров", "+7(888)888-88-88"),
("Григорий", "Безруков", "+7(777)777-77-77"),
("Тарзан", "Тарзанович", "+7(666)666-66-66");

INSERT INTO teachers_groups (teacher_id, groups_id)
VALUES
(1, 1),
(2, 1);

INSERT INTO teachers_groups (teacher_id, groups_id)
VALUES
((SELECT id FROM teachers WHERE last_name = "Петров"),
(SELECT id FROM groups WHERE group_name = "python411"));


SELECT tch.first_name, tch.last_name, g.group_name
FROM teachers_groups tg
JOIN teachers tch ON tg.teacher_id = tch.id
JOIN groups g ON tg.group_id = g.id;

SELECT tch.first_name, tch.last_name, g.group_name
FROM teachers tch
JOIN teachers_groups tg ON tch.id = tg.teacher_id
JOIN groups g ON tg.group_id = g.id;

SELECT tch.first_name, tch.last_name, g.group_name
FROM groups g 
JOIN teachers_groups tg ON g.id = tg.group_id
JOIN teachers tch ON tg.teacher_id = tch.id;