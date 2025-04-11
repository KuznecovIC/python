-- Шаг 1: Включение поддержки внешних ключей
PRAGMA foreign_keys = ON;

-- Шаг 2: Удаление таблиц в правильном порядке
DROP TABLE IF EXISTS appointments_services;
DROP TABLE IF EXISTS masters_services;
DROP TABLE IF EXISTS appointments;
DROP TABLE IF EXISTS services;
DROP TABLE IF EXISTS masters;

-- Шаг 3: Создание таблицы masters
CREATE TABLE masters (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    middle_name TEXT,
    phone TEXT NOT NULL
);

-- Шаг 4: Создание таблицы services
CREATE TABLE services (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT,
    price REAL NOT NULL
);

-- Шаг 5: Создание таблицы appointments
CREATE TABLE appointments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    phone TEXT NOT NULL,
    date TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    master_id INTEGER NOT NULL,
    status TEXT NOT NULL,
    FOREIGN KEY (master_id) REFERENCES masters(id) ON DELETE CASCADE
);

-- Шаг 6: Создание таблицы masters_services
CREATE TABLE masters_services (
    master_id INTEGER NOT NULL,
    service_id INTEGER NOT NULL,
    PRIMARY KEY (master_id, service_id),
    FOREIGN KEY (master_id) REFERENCES masters(id) ON DELETE CASCADE,
    FOREIGN KEY (service_id) REFERENCES services(id) ON DELETE CASCADE
);

-- Шаг 7: Создание таблицы appointments_services
CREATE TABLE appointments_services (
    appointment_id INTEGER NOT NULL,
    service_id INTEGER NOT NULL,
    PRIMARY KEY (appointment_id, service_id),
    FOREIGN KEY (appointment_id) REFERENCES appointments(id) ON DELETE CASCADE,
    FOREIGN KEY (service_id) REFERENCES services(id) ON DELETE CASCADE
);

-- Шаг 8: Вставка данных в masters
INSERT INTO masters (first_name, last_name, middle_name, phone) VALUES 
('Иван', 'Петров', 'Александрович', '+79991112233');
INSERT INTO masters (first_name, last_name, middle_name, phone) VALUES 
('Дмитрий', 'Смирнов', 'Владимирович', '+79998887766');

-- Шаг 9: Вставка данных в services
INSERT INTO services (title, description, price) VALUES 
('Мужская стрижка', 'Классическая мужская стрижка', 800.0);
INSERT INTO services (title, description, price) VALUES 
('Бритьё головы', 'Горячее полотенце и бритьё опасной бритвой', 600.0);
INSERT INTO services (title, description, price) VALUES 
('Оформление бороды', 'Моделирование и оформление бороды', 500.0);
INSERT INTO services (title, description, price) VALUES 
('Окрашивание волос', 'Окрашивание волос или бороды', 1200.0);
INSERT INTO services (title, description, price) VALUES 
('Укладка волос', 'Стильная укладка с использованием профессиональной косметики', 400.0);

-- Шаг 10: Вставка данных в masters_services
INSERT INTO masters_services (master_id, service_id) VALUES (1, 1);
INSERT INTO masters_services (master_id, service_id) VALUES (1, 2);
INSERT INTO masters_services (master_id, service_id) VALUES (1, 3);
INSERT INTO masters_services (master_id, service_id) VALUES (2, 1);
INSERT INTO masters_services (master_id, service_id) VALUES (2, 4);
INSERT INTO masters_services (master_id, service_id) VALUES (2, 5);

-- Шаг 11: Вставка данных в appointments
INSERT INTO appointments (name, phone, date, master_id, status) VALUES
('Алексей Иванов', '+79001234567', '2023-10-15 10:00:00', 1, 'подтверждена');
INSERT INTO appointments (name, phone, date, master_id, status) VALUES
('Сергей Сидоров', '+79009876543', '2023-10-15 11:30:00', 2, 'ожидает');
INSERT INTO appointments (name, phone, date, master_id, status) VALUES
('Михаил Орлов', '+79007654321', '2023-10-16 09:00:00', 1, 'отменена');
INSERT INTO appointments (name, phone, date, master_id, status) VALUES
('Антон Егоров', '+79005432109', '2023-10-16 14:00:00', 2, 'подтверждена');

-- Шаг 12: Вставка данных в appointments_services
INSERT INTO appointments_services (appointment_id, service_id) VALUES (1, 1);
INSERT INTO appointments_services (appointment_id, service_id) VALUES (1, 3);
INSERT INTO appointments_services (appointment_id, service_id) VALUES (2, 5);
INSERT INTO appointments_services (appointment_id, service_id) VALUES (3, 2);
INSERT INTO appointments_services (appointment_id, service_id) VALUES (4, 1);
INSERT INTO appointments_services (appointment_id, service_id) VALUES (4, 4);
-- Вывод всех мастеров
SELECT * FROM masters;

-- Вывод всех услуг
SELECT * FROM services;

-- Вывод всех записей
SELECT a.id, a.name, a.phone, a.date, 
       m.first_name || ' ' || m.last_name as master_name,
       a.status
FROM appointments a
JOIN masters m ON a.master_id = m.id;

-- Вывод связей мастеров и услуг
SELECT m.first_name || ' ' || m.last_name as master_name,
       s.title as service_name
FROM masters_services ms
JOIN masters m ON ms.master_id = m.id
JOIN services s ON ms.service_id = s.id;

-- Вывод записей с услугами
SELECT a.name as client_name,
       GROUP_CONCAT(s.title, ', ') as services,
       a.date,
       m.first_name || ' ' || m.last_name as master_name,
       a.status
FROM appointments a
JOIN masters m ON a.master_id = m.id
JOIN appointments_services aps ON a.id = aps.appointment_id
JOIN services s ON aps.service_id = s.id
GROUP BY a.id;