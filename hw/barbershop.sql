PRAGMA foreign_keys = OFF;

BEGIN TRANSACTION;

-- Удаление всех таблиц
DROP TABLE IF EXISTS appointments_services;
DROP TABLE IF EXISTS masters_services;
DROP TABLE IF EXISTS appointments;
DROP TABLE IF EXISTS services;
DROP TABLE IF EXISTS masters;

-- Таблица мастеров
CREATE TABLE masters (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    middle_name TEXT,
    phone TEXT NOT NULL
);

-- Таблица услуг
CREATE TABLE services (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT,
    price REAL NOT NULL
);

-- Таблица записей (с явным указанием столбца comment)
CREATE TABLE appointments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    phone TEXT NOT NULL,
    date TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    master_id INTEGER NOT NULL,
    status TEXT NOT NULL,
    comment TEXT NOT NULL DEFAULT '',
    FOREIGN KEY (master_id) REFERENCES masters(id) ON DELETE CASCADE
);

-- Таблица связи мастеров и услуг
CREATE TABLE masters_services (
    master_id INTEGER NOT NULL,
    service_id INTEGER NOT NULL,
    PRIMARY KEY (master_id, service_id),
    FOREIGN KEY (master_id) REFERENCES masters(id) ON DELETE CASCADE,
    FOREIGN KEY (service_id) REFERENCES services(id) ON DELETE CASCADE
);

-- Таблица связи записей и услуг
CREATE TABLE appointments_services (
    appointment_id INTEGER NOT NULL,
    service_id INTEGER NOT NULL,
    PRIMARY KEY (appointment_id, service_id),
    FOREIGN KEY (appointment_id) REFERENCES appointments(id) ON DELETE CASCADE,
    FOREIGN KEY (service_id) REFERENCES services(id) ON DELETE CASCADE
);

-- Тестовые данные
INSERT INTO masters (first_name, last_name, middle_name, phone) VALUES 
('Иван', 'Петров', 'Александрович', '+79991112233'),
('Дмитрий', 'Смирнов', 'Владимирович', '+79998887766');

INSERT INTO services (title, description, price) VALUES 
('Мужская стрижка', 'Классическая мужская стрижка', 800.0),
('Бритьё головы', 'Горячее полотенце и бритьё опасной бритвой', 600.0);

INSERT INTO appointments (name, phone, date, master_id, status, comment) VALUES
('Алексей Иванов', '+79001234567', '2023-10-15 10:00:00', 1, 'подтверждена', 'Хочу короткую стрижку'),
('Сергей Сидоров', '+79009876543', '2023-10-15 11:30:00', 2, 'ожидает', 'Укладка для мероприятия');

INSERT INTO masters_services (master_id, service_id) VALUES 
(1, 1), (1, 2),
(2, 1), (2, 2);

INSERT INTO appointments_services (appointment_id, service_id) VALUES 
(1, 1),
(2, 2);

COMMIT;

PRAGMA foreign_keys = ON;