import sqlite3
import os
import sys
from typing import List, Tuple

DB_PATH = r"C:\Users\omegasigmakladdmen\Downloads\python\data\barbershop.db"
SQL_PATH = r"C:\Users\omegasigmakladdmen\Downloads\python\hw\barbershop.sql"

def ensure_database():
    """Гарантированно создает новую базу данных с правильной структурой"""
    # Удаляем старую базу, если существует
    max_attempts = 3
    for attempt in range(max_attempts):
        try:
            if os.path.exists(DB_PATH):
                os.remove(DB_PATH)
            break
        except PermissionError:
            if attempt == max_attempts - 1:
                print("Ошибка: Не удалось удалить старую базу данных.")
                print("Закройте все программы, которые могут использовать базу данных.")
                sys.exit(1)
            time.sleep(1)
    
    # Создаем директорию, если не существует
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    
    # Создаем новую базу и выполняем скрипт
    conn = None
    try:
        conn = sqlite3.connect(DB_PATH)
        
        # Включаем проверку внешних ключей
        conn.execute("PRAGMA foreign_keys = ON")
        
        # Читаем SQL-скрипт
        with open(SQL_PATH, 'r', encoding='utf-8') as f:
            sql_script = f.read()
        
        # Выполняем скрипт
        conn.executescript(sql_script)
        conn.commit()
        
        # Проверяем структуру таблицы
        cursor = conn.cursor()
        cursor.execute("PRAGMA table_info(appointments)")
        columns = [col[1] for col in cursor.fetchall()]
        
        if 'comment' not in columns:
            # Если столбец отсутствует, добавляем его
            try:
                cursor.execute("ALTER TABLE appointments ADD COLUMN comment TEXT DEFAULT ''")
                conn.commit()
                print("Столбец 'comment' был успешно добавлен в таблицу appointments")
            except sqlite3.OperationalError as e:
                raise ValueError(f"Не удалось добавить столбец 'comment': {e}")
        
    except Exception as e:
        if conn:
            conn.rollback()
        print(f"Ошибка инициализации базы данных: {e}")
        sys.exit(1)
    finally:
        if conn:
            conn.close()

def get_connection() -> sqlite3.Connection:
    """Возвращает соединение с базой данных"""
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON")
    return conn

def find_appointments_by_phone(phone: str) -> List[Tuple]:
    """Поиск записей по телефону"""
    conn = get_connection()
    try:
        cursor = conn.cursor()
        query = """
        SELECT 
            a.id,
            a.name,
            a.phone,
            a.date,
            m.first_name || ' ' || m.last_name,
            GROUP_CONCAT(s.title, ', '),
            a.status,
            COALESCE(a.comment, '')
        FROM appointments a
        JOIN masters m ON a.master_id = m.id
        JOIN appointments_services aps ON a.id = aps.appointment_id
        JOIN services s ON aps.service_id = s.id
        WHERE a.phone = ?
        GROUP BY a.id
        """
        cursor.execute(query, (phone,))
        return cursor.fetchall()
    finally:
        conn.close()

def main():
    try:
        print("=== Инициализация базы данных ===")
        ensure_database()
        
        print("\n=== Тестирование поиска ===")
        phone = '+79001234567'
        print(f"Поиск записей для телефона: {phone}")
        
        appointments = find_appointments_by_phone(phone)
        
        if not appointments:
            print("Записи не найдены")
        else:
            print("\nНайденные записи:")
            for app in appointments:
                print(f"""
ID: {app[0]}
Клиент: {app[1]}
Телефон: {app[2]}
Дата: {app[3]}
Мастер: {app[4]}
Услуги: {app[5]}
Статус: {app[6]}
Комментарий: {app[7]}
{'='*40}""")
                
    except Exception as e:
        print(f"\nОшибка: {e}")
    finally:
        input("\nНажмите Enter для выхода...")

if __name__ == "__main__":
    main()
    