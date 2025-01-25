import abc
import json
import csv
from typing import Any


class AbstractFile(abc.ABC):
    """
    Абстрактный класс для работы с файлами.
    """
    
    @abc.abstractmethod
    def read(self) -> Any:
        """
        Чтение данных из файла.
        """
        pass
    
    @abc.abstractmethod
    def write(self, data: Any) -> None:
        """
        Запись данных в файл.
        """
        pass
    
    @abc.abstractmethod
    def append(self, data: Any) -> None:
        """
        Добавление данных в файл.
        """
        pass


class JsonFile(AbstractFile):
    """
    Класс для работы с JSON-файлами.
    """
    
    def __init__(self, file_path: str):
        self.file_path = file_path
    
    def read(self) -> dict:
        """Чтение данных из JSON-файла."""
        with open(self.file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    
    def write(self, data: dict) -> None:
        """Запись данных в JSON-файл."""
        with open(self.file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
    
    def append(self, data: dict) -> None:
        """Добавление данных в JSON-файл."""
        existing_data = self.read()
        existing_data.update(data)
        self.write(existing_data)


class TxtFile(AbstractFile):
    """
    Класс для работы с текстовыми файлами.
    """
    
    def __init__(self, file_path: str):
        self.file_path = file_path
    
    def read(self) -> str:
        """Чтение данных из текстового файла."""
        with open(self.file_path, 'r', encoding='utf-8') as file:
            return file.read()
    
    def write(self, data: str) -> None:
        """Запись данных в текстовый файл."""
        with open(self.file_path, 'w', encoding='utf-8') as file:
            file.write(data)
    
    def append(self, data: str) -> None:
        """Добавление данных в текстовый файл."""
        with open(self.file_path, 'a', encoding='utf-8') as file:
            file.write(data)


class CsvFile(AbstractFile):
    """
    Класс для работы с CSV-файлами.
    """
    
    def __init__(self, file_path: str):
        self.file_path = file_path
    
    def read(self) -> list:
        """Чтение данных из CSV-файла."""
        with open(self.file_path, 'r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            return list(reader)
    
    def write(self, data: list) -> None:
        """Запись данных в CSV-файл."""
        with open(self.file_path, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerows(data)
    
    def append(self, data: list) -> None:
        """Добавление данных в CSV-файл."""
        with open(self.file_path, 'a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerows(data)


