import json
import csv
import yaml
from typing import List, Dict


# Работа с JSON
def read_json(file_path: str, encoding: str = "utf-8") -> dict:
    """Читает данные из JSON-файла."""
    with open(file_path, 'r', encoding=encoding) as file:
        return json.load(file)


def write_json(data: dict, file_path: str, encoding: str = "utf-8") -> None:
    """Записывает данные в JSON-файл."""
    with open(file_path, 'w', encoding=encoding) as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


def append_json(data: List[Dict], file_path: str, encoding: str = "utf-8") -> None:
    """Добавляет данные в существующий JSON-файл."""
    try:
        with open(file_path, 'r', encoding=encoding) as file:
            existing_data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        existing_data = []

    existing_data.extend(data)

    with open(file_path, 'w', encoding=encoding) as file:
        json.dump(existing_data, file, ensure_ascii=False, indent=4)


# Работа с CSV
def read_csv(file_path: str, delimiter: str = ';', encoding: str = 'windows-1251') -> List[List[str]]:
    """Читает данные из CSV-файла."""
    with open(file_path, 'r', encoding=encoding) as file:
        reader = csv.reader(file, delimiter=delimiter)
        return list(reader)


def write_csv(data: List[List[str]], file_path: str, delimiter: str = ';', encoding: str = 'windows-1251') -> None:
    """Записывает данные в CSV-файл."""
    with open(file_path, 'w', encoding=encoding, newline='') as file:
        writer = csv.writer(file, delimiter=delimiter)
        writer.writerows(data)


def append_csv(data: List[List[str]], file_path: str, delimiter: str = ';', encoding: str = 'windows-1251') -> None:
    """Добавляет данные в существующий CSV-файл."""
    with open(file_path, 'a', encoding=encoding, newline='') as file:
        writer = csv.writer(file, delimiter=delimiter)
        writer.writerows(data)


# Работа с TXT
def read_txt(file_path: str, encoding: str = "utf-8") -> str:
    """Читает данные из текстового файла."""
    with open(file_path, 'r', encoding=encoding) as file:
        return file.read()


def write_txt(data: str, file_path: str, encoding: str = "utf-8") -> None:
    """Записывает данные в текстовый файл."""
    with open(file_path, 'w', encoding=encoding) as file:
        file.write(data)


def append_txt(data: str, file_path: str, encoding: str = "utf-8") -> None:
    """Добавляет данные в конец текстового файла."""
    with open(file_path, 'a', encoding=encoding) as file:
        file.write(data)


# Работа с YAML
def read_yaml(file_path: str) -> dict:
    """Читает данные из YAML-файла."""
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)