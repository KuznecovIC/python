--
-- Файл сгенерирован с помощью SQLiteStudio v3.4.16 в Вс апр 13 12:38:43 2025
--
-- Использованная кодировка текста: System
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Таблица: groups
DROP TABLE IF EXISTS groups;
CREATE TABLE IF NOT EXISTS groups (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    group_name TEXT NOT NULL UNIQUE,
    start_date TEXT DEFAULT CURRENT_TIMESTAMP,
    end_date TEXT,
    profession_id INTEGER,
    FOREIGN KEY (profession_id) REFERENCES professions(id) ON DELETE SET NULL  ON UPDATE CASCADE
);
INSERT INTO groups (id, group_name, start_date, end_date, profession_id) VALUES (1, 'python411', '2025-04-12 09:14:07', NULL, 6);
INSERT INTO groups (id, group_name, start_date, end_date, profession_id) VALUES (2, 'js412', '2025-04-12 09:14:07', NULL, 5);

-- Таблица: professions
DROP TABLE IF EXISTS professions;
CREATE TABLE IF NOT EXISTS professions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL UNIQUE,
    description TEXT
);
INSERT INTO professions (id, title, description) VALUES (3, 'Frontend-разработчик', 'Создание пользовательского интерфейса веб-приложений на JavaScript');
INSERT INTO professions (id, title, description) VALUES (4, 'Backend-разработчик', 'Разработка серверной части веб-приложений на Python');
INSERT INTO professions (id, title, description) VALUES (5, 'Frontend-разработчик_2', 'Создание пользовательского интерфейса веб-приложений на JavaScript');
INSERT INTO professions (id, title, description) VALUES (6, 'Backend-разработчик_2', 'Разработка серверной части веб-приложений на Python');

-- Таблица: student_cards
DROP TABLE IF EXISTS student_cards;
CREATE TABLE IF NOT EXISTS student_cards (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        student_id INTEGER NOT NULL UNIQUE,

        number TEXT NOT NULL UNIQUE,

        FOREIGN KEY (student_id) REFERENCES students (id) ON DELETE CASCADE ON UPDATE CASCADE

    );
INSERT INTO student_cards (id, student_id, number) VALUES (1, 1, 'PY-0001');
INSERT INTO student_cards (id, student_id, number) VALUES (2, 2, 'PY-0002');
INSERT INTO student_cards (id, student_id, number) VALUES (3, 3, 'PY-0003');
INSERT INTO student_cards (id, student_id, number) VALUES (4, 4, 'PY-0004');
INSERT INTO student_cards (id, student_id, number) VALUES (5, 5, 'PY-0005');
INSERT INTO student_cards (id, student_id, number) VALUES (6, 6, 'JS-0006');
INSERT INTO student_cards (id, student_id, number) VALUES (7, 7, 'JS-0007');
INSERT INTO student_cards (id, student_id, number) VALUES (8, 8, 'JS-0008');
INSERT INTO student_cards (id, student_id, number) VALUES (9, 9, 'JS-0009');
INSERT INTO student_cards (id, student_id, number) VALUES (10, 10, 'JS-0010');

-- Таблица: students
DROP TABLE IF EXISTS students;
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    middle_name TEXT,
    last_name TEXT NOT NULL,
    age INTEGER,
    group_id INTEGER,
    -- Указание внешнего ключа
    FOREIGN KEY (group_id) REFERENCES groups(id) ON DELETE SET NULL ON UPDATE CASCADE
);
INSERT INTO students (id, first_name, middle_name, last_name, age, group_id) VALUES (1, 'Артём', 'Питонович', 'Серпентьев', 22, 1);
INSERT INTO students (id, first_name, middle_name, last_name, age, group_id) VALUES (2, 'Ольга', 'Джанговна', 'Фласкина', 19, 1);
INSERT INTO students (id, first_name, middle_name, last_name, age, group_id) VALUES (3, 'Виктор', 'Алгоритмович', 'Рекурсивный', 24, 1);
INSERT INTO students (id, first_name, middle_name, last_name, age, group_id) VALUES (4, 'Анна', 'Датафреймовна', 'Пандасова', 21, 1);
INSERT INTO students (id, first_name, middle_name, last_name, age, group_id) VALUES (5, 'Дмитрий', 'Генадьевич', 'Индентов', 20, 1);
INSERT INTO students (id, first_name, middle_name, last_name, age, group_id) VALUES (6, 'Светлана', 'Реактовна', 'Хуковская', 23, 2);
INSERT INTO students (id, first_name, middle_name, last_name, age, group_id) VALUES (7, 'Максим', 'Промисович', 'Аякcов', 20, 2);
INSERT INTO students (id, first_name, middle_name, last_name, age, group_id) VALUES (8, 'Ксения', 'Вьюевна', 'Компонентова', 19, 2);
INSERT INTO students (id, first_name, middle_name, last_name, age, group_id) VALUES (9, 'Игорь', 'Ноудович', 'Экспрессов', 25, 2);
INSERT INTO students (id, first_name, middle_name, last_name, age, group_id) VALUES (10, 'Алина', 'Домовна', 'Вёрсточкина', 22, 2);

-- Таблица: teachers
DROP TABLE IF EXISTS teachers;
CREATE TABLE IF NOT EXISTS teachers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    middle_name TEXT,
    last_name TEXT NOT NULL,
    age INTEGER,
    phone TEXT NOT NULL,
    email TEXT
);
INSERT INTO teachers (id, first_name, middle_name, last_name, age, phone, email) VALUES (1, 'Иван', 'Компиляторович', 'Кодмастеров', 45, '+7 (900) 123-45-67', 'codmaster@teachmail.ru');
INSERT INTO teachers (id, first_name, middle_name, last_name, age, phone, email) VALUES (2, 'Елена', 'Алгоритмовна', 'Сортирова', 38, '+7 (900) 234-56-78', 'sort_queen@teachmail.ru');
INSERT INTO teachers (id, first_name, middle_name, last_name, age, phone, email) VALUES (3, 'Николай', 'Фреймворкович', 'Библиотечный', 42, '+7 (900) 345-67-89', 'framework_guru@teachmail.ru');
INSERT INTO teachers (id, first_name, middle_name, last_name, age, phone, email) VALUES (4, 'Татьяна', 'Баговна', 'Дебаггер', 36, '+7 (900) 456-78-90', 'bug_hunter@teachmail.ru');
INSERT INTO teachers (id, first_name, middle_name, last_name, age, phone, email) VALUES (5, 'Михаил', 'Гитович', 'Коммитов', 41, '+7 (900) 567-89-01', 'never_merge_to_master@teachmail.ru');

-- Таблица: teachers_groups
DROP TABLE IF EXISTS teachers_groups;
CREATE TABLE IF NOT EXISTS teachers_groups (
    teacher_id INTEGER,
    group_id INTEGER,
    date_start TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (teacher_id) REFERENCES teachers(id)  ON DELETE SET NULL ON UPDATE CASCADE,
    FOREIGN KEY (group_id) REFERENCES groups(id)  ON DELETE SET NULL ON UPDATE CASCADE,
    PRIMARY KEY (teacher_id, group_id) -- составной первичный ключ
);
INSERT INTO teachers_groups (teacher_id, group_id, date_start) VALUES (1, 1, '2025-04-12 09:14:07');
INSERT INTO teachers_groups (teacher_id, group_id, date_start) VALUES (2, 1, '2025-04-12 09:14:07');
INSERT INTO teachers_groups (teacher_id, group_id, date_start) VALUES (5, 1, '2025-04-12 09:14:07');
INSERT INTO teachers_groups (teacher_id, group_id, date_start) VALUES (3, 2, '2025-04-12 09:14:07');
INSERT INTO teachers_groups (teacher_id, group_id, date_start) VALUES (4, 2, '2025-04-12 09:14:07');
INSERT INTO teachers_groups (teacher_id, group_id, date_start) VALUES (5, 2, '2025-04-12 09:14:07');

-- Таблица: teachers_professions
DROP TABLE IF EXISTS teachers_professions;
CREATE TABLE IF NOT EXISTS teachers_professions (
    teacher_id INTEGER,
    profession_id INTEGER,
    notions TEXT,
    FOREIGN KEY (teacher_id) REFERENCES teachers(id)  ON DELETE SET NULL ON UPDATE CASCADE,
    FOREIGN KEY (profession_id) REFERENCES professions(id)  ON DELETE SET NULL ON UPDATE CASCADE,
    PRIMARY KEY (teacher_id, profession_id) -- составной первичный ключ
);
INSERT INTO teachers_professions (teacher_id, profession_id, notions) VALUES (1, 6, 'Эксперт по Python с опытом написания кода во сне');
INSERT INTO teachers_professions (teacher_id, profession_id, notions) VALUES (2, 6, 'Может объяснить рекурсию рекурсивно, а потом нерекурсивно');
INSERT INTO teachers_professions (teacher_id, profession_id, notions) VALUES (3, 5, 'JavaScript-гуру, по слухам однажды починил Internet Explorer');
INSERT INTO teachers_professions (teacher_id, profession_id, notions) VALUES (4, 5, 'CSS-волшебница, умеет центрировать div с первого раза');
INSERT INTO teachers_professions (teacher_id, profession_id, notions) VALUES (5, 4, 'Универсальный боец, может работать full-stack даже на калькуляторе');

-- Индекс: idx_groups_name
DROP INDEX IF EXISTS idx_groups_name;
CREATE INDEX IF NOT EXISTS idx_groups_name ON groups(group_name);

-- Индекс: idx_groups_profession
DROP INDEX IF EXISTS idx_groups_profession;
CREATE INDEX IF NOT EXISTS idx_groups_profession ON groups(profession_id);

-- Индекс: idx_students_fullname
DROP INDEX IF EXISTS idx_students_fullname;
CREATE INDEX IF NOT EXISTS idx_students_fullname ON students(first_name, middle_name, last_name);

-- Индекс: idx_students_group
DROP INDEX IF EXISTS idx_students_group;
CREATE INDEX IF NOT EXISTS idx_students_group ON students(group_id);

-- Индекс: idx_students_lastname
DROP INDEX IF EXISTS idx_students_lastname;
CREATE INDEX IF NOT EXISTS idx_students_lastname ON students(last_name);

-- Индекс: idx_teachers_email
DROP INDEX IF EXISTS idx_teachers_email;
CREATE INDEX IF NOT EXISTS idx_teachers_email ON teachers(email);

-- Индекс: idx_teachers_fullname
DROP INDEX IF EXISTS idx_teachers_fullname;
CREATE INDEX IF NOT EXISTS idx_teachers_fullname ON teachers(first_name, middle_name, last_name);

-- Индекс: idx_teachers_lastname
DROP INDEX IF EXISTS idx_teachers_lastname;
CREATE INDEX IF NOT EXISTS idx_teachers_lastname ON teachers(last_name);

-- Индекс: idx_teachers_phone
DROP INDEX IF EXISTS idx_teachers_phone;
CREATE INDEX IF NOT EXISTS idx_teachers_phone ON teachers(phone);

-- Представление: student_info
DROP VIEW IF EXISTS student_info;
CREATE VIEW IF NOT EXISTS student_info AS

SELECT

    s.first_name,

    s.middle_name,

    s.last_name,

    s.age,

    g.group_name,

    sc.number AS student_card_number



FROM

    students s

LEFT JOIN groups g ON s.group_id = g.id

LEFT JOIN student_cards sc ON s.id = sc.student_id;

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
