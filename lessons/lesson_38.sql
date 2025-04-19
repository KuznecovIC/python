-- Профессии
CREATE TABLE IF NOT EXISTS professions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL UNIQUE,
    description TEXT
);

-- Группы
CREATE TABLE IF NOT EXISTS groups (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    group_name TEXT NOT NULL UNIQUE,
    start_date TEXT DEFAULT CURRENT_TIMESTAMP,
    end_date TEXT,
    profession_id INTEGER,
    FOREIGN KEY (profession_id) REFERENCES professions(id) ON DELETE SET NULL  ON UPDATE CASCADE
);

-- Cтуденты
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


-- Таблица преподавателей
CREATE TABLE IF NOT EXISTS teachers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    middle_name TEXT,
    last_name TEXT NOT NULL,
    age INTEGER,
    phone TEXT NOT NULL,
    email TEXT
)

-- Таблица ПреподавателиГруппы - для связи Многие-ко-многим
CREATE TABLE IF NOT EXISTS teachers_groups (
    teacher_id INTEGER,
    group_id INTEGER,
    date_start TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (teacher_id) REFERENCES teachers(id)  ON DELETE SET NULL ON UPDATE CASCADE,
    FOREIGN KEY (group_id) REFERENCES groups(id)  ON DELETE SET NULL ON UPDATE CASCADE,
    PRIMARY KEY (teacher_id, group_id) -- составной первичный ключ
);

-- Таблица ПреподавателиПрофессии
CREATE TABLE IF NOT EXISTS teachers_professions (
    teacher_id INTEGER,
    profession_id INTEGER,
    notions TEXT,
    FOREIGN KEY (teacher_id) REFERENCES teachers(id)  ON DELETE SET NULL ON UPDATE CASCADE,
    FOREIGN KEY (profession_id) REFERENCES professions(id)  ON DELETE SET NULL ON UPDATE CASCADE,
    PRIMARY KEY (teacher_id, profession_id) -- составной первичный ключ
);


-- Один-к-одному
-- Транзацкии
-- Индексы
-- Триггеры
-- Вью - представления
-- Оконные функции ????

BEGIN TRANSACTION;

INSERT INTO
     professions (title, description)
VALUES
    (
        'Fronted-developer',
        'Создание пользаввательского интерфейса'
    ),
    (
        'Backend-developer',
        'Разработка серверной части веб-приложений на python'
    );

COMMIT TRANSACTION;
ROLLBACK;