from dataclasses import dataclass
from typing import List, Dict, Optional, Iterator


@dataclass
class City:
    """Датакласс для представления информации о городе."""
    name: str
    lat: str
    lon: str
    district: str
    population: int
    subject: str


class CitiesIterator:
    """Итератор для обработки данных о городах России."""
    
    def __init__(self, cities: List[Dict]) -> None:
        """
        Инициализация итератора списком словарей с данными о городах.
        
        Args:
            cities: Список словарей с информацией о городах.
                    Каждый словарь должен содержать ключи: name, district, population, subject,
                    и вложенный словарь coords с ключами lat и lon.
        """
        self._cities_data = cities
        self._min_population: Optional[int] = None
        self._sort_parameter: Optional[str] = None
        self._reverse_sort: bool = False
        self._processed_cities: List[City] = []
        self._index: int = 0
        
        self._validate_data()
        self._process_cities()
    
    def _validate_data(self) -> None:
        """Проверяет наличие всех обязательных полей в каждом словаре города."""
        required_fields = {'name', 'district', 'population', 'subject', 'coords'}
        coord_fields = {'lat', 'lon'}
        
        for city_data in self._cities_data:
            missing_fields = required_fields - set(city_data.keys())
            if missing_fields:
                raise ValueError(f"Отсутствуют обязательные поля: {missing_fields}")
            
            missing_coord_fields = coord_fields - set(city_data['coords'].keys())
            if missing_coord_fields:
                raise ValueError(f"Отсутствуют обязательные поля координат: {missing_coord_fields}")
    
    def _process_cities(self) -> None:
        """Преобразует словари с данными городов в объекты City."""
        self._processed_cities = []
        for city_data in self._cities_data:
            city = City(
                name=city_data['name'],
                lat=city_data['coords']['lat'],
                lon=city_data['coords']['lon'],
                district=city_data['district'],
                population=city_data['population'],
                subject=city_data['subject']
            )
            self._processed_cities.append(city)
        
        self._apply_filters_and_sort()
    
    def _apply_filters_and_sort(self) -> None:
        """Применяет текущие настройки фильтрации и сортировки."""
        # Фильтрация по населению
        filtered_cities = (
            [city for city in self._processed_cities if city.population >= self._min_population]
            if self._min_population is not None
            else self._processed_cities.copy()
        )
        
        # Сортировка
        if self._sort_parameter:
            try:
                filtered_cities.sort(
                    key=lambda city: getattr(city, self._sort_parameter),
                    reverse=self._reverse_sort
                )
            except AttributeError:
                raise ValueError(f"Недопустимый параметр для сортировки: {self._sort_parameter}")
        
        self._filtered_sorted_cities = filtered_cities
    
    def set_population_filter(self, min_population: int) -> None:
        """
        Устанавливает минимальное значение населения для фильтрации городов.
        
        Args:
            min_population: Минимальное значение населения. Города с населением меньше этого значения будут исключены.
        """
        self._min_population = min_population
        self._apply_filters_and_sort()
    
    def sort_by(self, parameter: str, reverse: bool = False) -> None:
        """
        Сортирует города по указанному параметру.
        
        Args:
            parameter: Название атрибута City для сортировки (например, 'name', 'population').
            reverse: Если True, сортировка будет в обратном порядке.
        """
        self._sort_parameter = parameter
        self._reverse_sort = reverse
        self._apply_filters_and_sort()
    
    def __iter__(self) -> Iterator[City]:
        """Возвращает итератор для обхода городов с текущими настройками фильтрации и сортировки."""
        self._index = 0
        return self
    
    def __next__(self) -> City:
        """Возвращает следующий город в соответствии с текущими настройками фильтрации и сортировки."""
        if self._index < len(self._filtered_sorted_cities):
            city = self._filtered_sorted_cities[self._index]
            self._index += 1
            return city
        raise StopIteration


# Пример использования
if __name__ == "__main__":
    # Тестовые данные
    cities_data = [
    {
        "coords": {"lat": "52.65", "lon": "90.08333"},
        "district": "Сибирский",
        "name": "Абаза",
        "population": 14816,
        "subject": "Хакасия"
    },
    {
        "coords": {"lat": "53.71667", "lon": "91.41667"},
        "district": "Сибирский",
        "name": "Абакан",
        "population": 184769,
        "subject": "Хакасия"
    },
    {
        "coords": {"lat": "53.68333", "lon": "53.65"},
        "district": "Приволжский",
        "name": "Абдулино",
        "population": 17274,
        "subject": "Оренбургская область"
    },
    {
        "coords": {"lat": "44.86667", "lon": "38.16667"},
        "district": "Южный",
        "name": "Абинск",
        "population": 38596,
        "subject": "Краснодарский край"
    },
    {
        "coords": {"lat": "55.9", "lon": "38.05"},
        "district": "Центральный",
        "name": "Апрелевка",
        "population": 35514,
        "subject": "Московская область"
    },
    {
        "coords": {"lat": "56.26667", "lon": "90.5"},
        "district": "Сибирский",
        "name": "Ачинск",
        "population": 105259,
        "subject": "Красноярский край"
    },
    {
        "coords": {"lat": "43.35", "lon": "46.1"},
        "district": "Северо-Кавказский",
        "name": "Хасавюрт",
        "population": 155144,
        "subject": "Дагестан"
    },
    {
        "coords": {"lat": "56.85", "lon": "53.21667"},
        "district": "Приволжский",
        "name": "Ижевск",
        "population": 646277,
        "subject": "Удмуртия"
    },
    {
        "coords": {"lat": "56.31667", "lon": "44.0"},
        "district": "Приволжский",
        "name": "Нижний Новгород",
        "population": 1244254,
        "subject": "Нижегородская область"
    },
    {
        "coords": {"lat": "55.75583", "lon": "37.61778"},
        "district": "Центральный",
        "name": "Москва",
        "population": 13010112,
        "subject": "Москва"
    },
    {
        "coords": {"lat": "59.95", "lon": "30.31667"},
        "district": "Северо-Западный",
        "name": "Санкт-Петербург",
        "population": 5601911,
        "subject": "Санкт-Петербург"
    },
    {
        "coords": {"lat": "55.03333", "lon": "82.91667"},
        "district": "Сибирский",
        "name": "Новосибирск",
        "population": 1633595,
        "subject": "Новосибирская область"
    },
    {
        "coords": {"lat": "56.83333", "lon": "60.58333"},
        "district": "Уральский",
        "name": "Екатеринбург",
        "population": 1544376,
        "subject": "Свердловская область"
    },
    {
        "coords": {"lat": "55.79639", "lon": "49.10889"},
        "district": "Приволжский",
        "name": "Казань",
        "population": 1308660,
        "subject": "Татарстан"
    },
    {
        "coords": {"lat": "53.2", "lon": "50.15"},
        "district": "Приволжский",
        "name": "Самара",
        "population": 1144759,
        "subject": "Самарская область"
    },
    {
        "coords": {"lat": "47.23333", "lon": "39.71667"},
        "district": "Южный",
        "name": "Ростов-на-Дону",
        "population": 1142162,
        "subject": "Ростовская область"
    },
    {
        "coords": {"lat": "55.6", "lon": "37.61667"},
        "district": "Центральный",
        "name": "Химки",
        "population": 257128,
        "subject": "Московская область"
    },
    {
        "coords": {"lat": "54.73333", "lon": "55.96667"},
        "district": "Приволжский",
        "name": "Уфа",
        "population": 1144809,
        "subject": "Башкортостан"
    },
    {
        "coords": {"lat": "55.03333", "lon": "82.91667"},
        "district": "Сибирский",
        "name": "Бердск",
        "population": 102850,
        "subject": "Новосибирская область"
    },
    {
        "coords": {"lat": "56.1325", "lon": "47.25194"},
        "district": "Приволжский",
        "name": "Чебоксары",
        "population": 497807,
        "subject": "Чувашия"
    },
    {
        "coords": {"lat": "54.78333", "lon": "32.05"},
        "district": "Центральный",
        "name": "Смоленск",
        "population": 320170,
        "subject": "Смоленская область"
    },
    {
        "coords": {"lat": "52.71667", "lon": "41.43333"},
        "district": "Центральный",
        "name": "Мичуринск",
        "population": 90451,
        "subject": "Тамбовская область"
    },
    {
        "coords": {"lat": "52.03333", "lon": "113.5"},
        "district": "Сибирский",
        "name": "Чита",
        "population": 349983,
        "subject": "Забайкальский край"
    },
    {
        "coords": {"lat": "56.13222", "lon": "40.39889"},
        "district": "Центральный",
        "name": "Владимир",
        "population": 349951,
        "subject": "Владимирская область"
    }

    ]

    print("=== Пример использования итератора ===")
    
    # 1. Создаем итератор
    cities_iter = CitiesIterator(cities_data)
    
    # 2. Фильтруем по населению (>= 15000)
    cities_iter.set_population_filter(15000)
    
    # 3. Сортируем по названию
    cities_iter.sort_by("name")
    
    print("\nГорода с населением >= 15000, отсортированные по имени:")
    for city in cities_iter:
        print(f"{city.name} ({city.population} чел.)")
    
    # 4. Сортируем по населению (по убыванию)
    cities_iter.sort_by("population", reverse=True)
    
    print("\nТе же города, отсортированные по населению (по убыванию):")
    for city in cities_iter:
        print(f"{city.name}: {city.population} чел.")
    
    # 5. Пример без фильтрации
    print("\nВсе города без фильтрации по населению:")
    cities_iter.set_population_filter(0)  # Сбрасываем фильтр
    for city in cities_iter:
        print(f"{city.name}: {city.population} чел.")

cities_iter = CitiesIterator(cities_data)
cities_iter.set_population_filter(100000)  # Только крупные города
cities_iter.sort_by("population", reverse=True)  # Сортировка по убыванию населения

print("Крупнейшие города:")
for city in cities_iter:
    print(f"{city.name} - {city.population} чел.")