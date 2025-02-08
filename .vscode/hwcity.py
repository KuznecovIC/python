from typing import List, Optional
from PIL import Image
import os
import json
from dataclasses import dataclass
from typing import Dict


# Модели и логика игры с городами
@dataclass
class City:
    name: str
    population: int
    subject: str
    district: str
    latitude: float
    longitude: float
    is_used: bool = False


# Функция для загрузки данных из JSON файла
def load_cities_from_file(filename: str) -> List[Dict]:
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)


class CitiesSerializer:
    def __init__(self, city_data: List[Dict]):
        self.cities = [City(
            name=city["name"],
            population=city["population"],
            subject=city["subject"],
            district=city["district"],
            latitude=float(city["coords"]["lat"]),
            longitude=float(city["coords"]["lon"])
        ) for city in city_data]

    def get_all_cities(self) -> List[City]:
        return self.cities

    def find_city_by_letter(self, letter: str) -> Optional[City]:
        # Ищем город, который начинается с указанной буквы
        for city in self.cities:
            if not city.is_used and self.normalize_letter(city.name[0]) == letter.lower():
                city.is_used = True
                return city
        return None

    def normalize_letter(self, letter: str) -> str:
        # Нормализуем буквы для проверки на мягкий и твердый знак
        soft_hard_letters = {'ь', 'ъ', 'ы'}
        if letter.lower() in soft_hard_letters:
            return letter.lower()
        return letter.lower()


class CityGame:
    def __init__(self, cities_serializer: CitiesSerializer):
        self.cities_serializer = cities_serializer  # Сохраняем ссылку на сериализатор городов
        self.cities = cities_serializer.get_all_cities()
        self.used_cities = []
        self.last_letter = None

    def start_game(self) -> None:
        print("Игра начинается!")
        
        # ПК выбирает первый город
        first_city = self.get_random_city()
        if first_city:
            print(f"Джарвис выбирает город: {first_city.name}")
            self.last_letter = self.normalize_last_letter(first_city.name[-1])
            first_city.is_used = True
        else:
            print("Города для игры не найдены.")
            return

        # Игра продолжается, пока есть доступные города
        while True:
            print(f"Последняя буква: {self.last_letter.upper()}")
            # Игрок вводит город
            player_city_name = input(f"Введите город, начинающийся на букву {self.last_letter.upper()}: ").strip()
            
            # Проверка на существование города
            player_city = self.get_city_by_name(player_city_name)
            if player_city:
                player_city.is_used = True
                self.last_letter = self.normalize_last_letter(player_city.name[-1])  # Новая буква для следующего города
            else:
                print("Город не найден или уже использован. Попробуйте снова.")
                continue

            # ПК находит город на последнюю букву
            pc_city = self.get_pc_city()
            if pc_city:
                print(f"Джарвис выбирает город: {pc_city.name}")
                self.last_letter = self.normalize_last_letter(pc_city.name[-1])
            else:
                print("Джарвис не может найти город. Игра завершена.")
                break

    def normalize_last_letter(self, letter: str) -> str:
        # Если последняя буква это мягкий знак, твердый знак или "ы", берем букву перед ней
        soft_hard_letters = {'ь', 'ъ', 'ы'}
        if letter.lower() in soft_hard_letters:
            return self.get_previous_letter(letter)
        return letter.lower()

    def get_previous_letter(self, letter: str) -> str:
        # Возвращаем предыдущую букву для мягкого знака, твердого знака или "ы"
        letter_mapping = {
            'ь': 'ь',
            'ъ': 'ъ',
            'ы': 'и'  # Например, если буква "ы", берем "и"
        }
        return letter_mapping.get(letter.lower(), letter.lower())

    def get_random_city(self) -> Optional[City]:
        # Получаем случайный город, который ещё не был использован
        for city in self.cities:
            if not city.is_used:
                city.is_used = True
                return city
        return None

    def get_city_by_name(self, name: str) -> Optional[City]:
        # Ищем город по имени
        for city in self.cities:
            if city.name.lower() == name.lower() and not city.is_used:
                return city
        return None

    def get_pc_city(self) -> Optional[City]:
        # ПК находит город, начинающийся на последнюю букву
        pc_city = self.cities_serializer.find_city_by_letter(self.last_letter)
        return pc_city


# Класс для сжатия изображений

class ImageCompressor:
    supported_formats = ['.jpeg', '.jpg', '.png']  # Атрибут класса

    def __init__(self, quality: int):
        self.__quality = quality  # Приватный атрибут

    @property
    def quality(self) -> int:
        return self.__quality

    @quality.setter
    def quality(self, value: int) -> None:
        if 0 <= value <= 100:
            self.__quality = value
        else:
            raise ValueError("Quality must be between 0 and 100")

    def compress_image(self, input_path: str, output_path: str) -> None:
        """
        Сжимает изображение, используя указанный путь и качество.
        """
        with Image.open(input_path) as img:
            img.save(output_path, quality=self.quality)

    @classmethod
    def process_directory(cls, directory: str, quality: int) -> None:
        """
        Обрабатывает все изображения в указанной директории.
        """
        if not os.path.isdir(directory):
            print(f"Ошибка: Директория {directory} не найдена.")
            return

        compressor = cls(quality)
        for filename in os.listdir(directory):
            if any(filename.lower().endswith(ext) for ext in cls.supported_formats):
                input_path = os.path.join(directory, filename)
                output_path = os.path.join(directory, f"compressed_{filename}")
                compressor.compress_image(input_path, output_path)
                print(f"Изображение {filename} сжато и сохранено как {output_path}")


# Пример использования

# Загрузка данных для игры
city_data = load_cities_from_file("cities.json")

# Создаем сериализатор городов
cities_serializer = CitiesSerializer(city_data)

# Создаем игру
game = CityGame(cities_serializer)

# Начинаем игру
game.start_game()

