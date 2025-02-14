import re
import csv
from typing import Callable


# Декоратор для проверки пароля
def password_validator(length: int = 8, uppercase: int = 1, lowercase: int = 1, special_chars: int = 1):
    def decorator(func: Callable):
        def wrapper(username: str, password: str):
            # Проверки для пароля
            if len(password) < length:
                raise ValueError(f"Пароль должен быть не менее {length} символов.")
            if len(re.findall(r"[A-Z]", password)) < uppercase:
                raise ValueError(f"Пароль должен содержать хотя бы {uppercase} заглавную букву.")
            if len(re.findall(r"[a-z]", password)) < lowercase:
                raise ValueError(f"Пароль должен содержать хотя бы {lowercase} строчную букву.")
            if len(re.findall(r"[!@#$%^&*(),.?\":{}|<>]", password)) < special_chars:
                raise ValueError(f"Пароль должен содержать хотя бы {special_chars} специальный символ.")
            return func(username, password)
        return wrapper
    return decorator


# Декоратор для проверки имени пользователя
def username_validator(func: Callable):
    def wrapper(username: str, password: str):
        # Проверка на пробелы в имени пользователя
        if " " in username:
            raise ValueError("Имя пользователя не должно содержать пробелы.")
        return func(username, password)
    return wrapper


# Функция для регистрации пользователя
@password_validator(length=10, uppercase=2, lowercase=2, special_chars=2)
@username_validator
def register_user(username: str, password: str) -> None:
    """Функция для регистрации нового пользователя и записи данных в CSV файл."""
    with open('users.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([username, password])
    print("Пользователь зарегистрирован.")


# Запрос данных у пользователя
username_input = input("Введите имя пользователя: ")
password_input = input("Введите пароль: ")

# Тестирование
try:
    register_user(username_input, password_input)
    print("Регистрация прошла успешно!")
except ValueError as e:
    print(f"Ошибка: {e}")