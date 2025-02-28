from dataclasses import dataclass
from typing import List, Dict


@dataclass
class City:
    name: str  # Название города
    lat: float  # Широта
    lon: float  # Долгота
    district: str  # Федеральный округ
    population: int  # Население
    subject: str  # Субъект РФ


class CitiesIterator:
    def __init__(self, cities_data: List[Dict]):
        self.cities_data = cities_data
        self.population_filter = None
        self.sorted = False

    def set_population_filter(self, min_population: int):
        """Устанавливает минимальный порог населения для фильтрации."""
        self.population_filter = min_population

    def sort_by(self, parameter: str, reverse: bool = False):
        """Сортирует города по указанному параметру."""
        if parameter not in ['name', 'lat', 'lon', 'district', 'population', 'subject']:
            raise ValueError(f"Неверный параметр для сортировки: {parameter}")
        self.cities_data.sort(key=lambda city: city[parameter], reverse=reverse)
        self.sorted = True

    def validate_city(self, city_data: Dict):
        """Проверка наличия всех обязательных полей в словаре города."""
        required_keys = ['name', 'district', 'population', 'subject', 'coords']
        for key in required_keys:
            if key not in city_data:
                raise ValueError(f"Отсутствует обязательное поле: {key}")

        # Проверка наличия координат
        coords = city_data['coords']
        if 'lat' not in coords or 'lon' not in coords:
            raise ValueError("Отсутствуют координаты 'lat' или 'lon' в поле 'coords'")

    def __iter__(self):
        """Реализация метода итерации."""
        for city_data in self.cities_data:
            self.validate_city(city_data)

            # Преобразуем данные города в объект City
            coords = city_data['coords']
            city = City(
                name=city_data['name'],
                lat=float(coords['lat']),
                lon=float(coords['lon']),
                district=city_data['district'],
                population=city_data['population'],
                subject=city_data['subject']
            )

            # Фильтрация по населению
            if self.population_filter and city.population < self.population_filter:
                continue

            yield city


# Пример данных о городах
cities_list = [
    {
        "coords": {"lat": "52.65", "lon": "90.08333"},
        "district": "Сибирский",
        "name": "Абаза",
        "population": 14816,
        "subject": "Хакасия"
    },
    {
        "coords": {"lat": "55.7558", "lon": "37.6176"},
        "district": "Центральный",
        "name": "Москва",
        "population": 12506468,
        "subject": "Москва"
    },
    {
        "coords": {"lat": "59.9343", "lon": "30.3351"},
        "district": "Северо-Западный",
        "name": "Санкт-Петербург",
        "population": 5351935,
        "subject": "Санкт-Петербург"
    }
]

# Создание итератора и установка фильтрации и сортировки
cities_iterator = CitiesIterator(cities_list)
cities_iterator.set_population_filter(5000000)  # Фильтрация по минимальному населению
cities_iterator.sort_by("name")  # Сортировка по названию

# Итерация и вывод данных о городах
for city in cities_iterator:
    print(city)