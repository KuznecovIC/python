import os
print(os.getcwd())  
class TxtFileHandler:
    """
    Класс для работы с текстовыми файлами.
    Предоставляет методы для чтения, записи и добавления данных в TXT файлы.
    """
    
    def read_file(self, filepath: str) -> str:
        """
        Читает содержимое файла и возвращает его в виде строки.
        Если файл не найден, возвращает пустую строку.
        
        :param filepath: Путь к файлу
        :return: Содержимое файла как строка
        """
        try:
            with open(filepath, 'r') as file:
                return file.read()
        except FileNotFoundError:
            return ""  # Возвращаем пустую строку, если файл не существует
        except PermissionError:
            print(f"Ошибка: Нет прав на чтение файла {filepath}.")
            return ""
        except Exception as e:
            print(f"Ошибка при чтении файла {filepath}: {e}")
            return ""
    
    def write_file(self, filepath: str, *data: str) -> None:
        """
        Записывает переданную строку в файл. Если файл существует, он перезаписывается.
        
        :param filepath: Путь к файлу
        :param data: Данные для записи
        """
        try:
            with open(filepath, 'w') as file:
                file.write("".join(data))  # Объединяем все строки в одну
            print(f"Данные успешно записаны в файл {filepath}.")
        except PermissionError:
            print(f"Ошибка: Нет прав на запись в файл {filepath}.")
        except Exception as e:
            print(f"Ошибка при записи в файл {filepath}: {e}")
    
    def append_file(self, filepath: str, *data: str) -> None:
        """
        Добавляет переданную строку в конец файла. Если файл не существует, он будет создан.
        
        :param filepath: Путь к файлу
        :param data: Данные для добавления
        """
        try:
            with open(filepath, 'a') as file:
                file.write("".join(data))  # Объединяем все строки в одну
            print(f"Данные успешно добавлены в файл {filepath}.")
        except PermissionError:
            print(f"Ошибка: Нет прав на добавление в файл {filepath}.")
        except Exception as e:
            print(f"Ошибка при добавлении в файл {filepath}: {e}")

# Пример использования
handler = TxtFileHandler()

# Запись в файл
handler.write_file("my_file.txt", "This is a test string.\n")

# Добавление в файл
handler.append_file("my_file.txt", "This is another string.\n")

# Чтение из файла
content = handler.read_file("my_file.txt")
print(content)
# Вывод:

class TxtFileHandler():
    """
    Класс для работы с текстовыми файлами.
    Может читать, писать и добавлять даннные в TXT файлы.
    """
    @staticmethod
    def read_file(filepath: str, encoding: str = "utf-8") -> str:
        with open(filepath, 'r') as file:
            data: str = file.read()

        return data
    @staticmethod
    def write_file(filepath: str, *data: str, encoding: str = "utf-8") -> None:
        with open(filepath, 'w') as file:
            for line in data:
                file.write(line + "\n")
        return data
    @staticmethod
    def append_file(filepath: str, *data: str, encoding: str = "utf-8") -> None:
        with open(filepath, 'a') as file:
            for line in data:
                file.write(line + "\n")
        return data
file_path = "lessom_16.txt"
txt_handler = TxtFileHandler()

txt_handler.write_file(file_path, "Привет", "Мир")



