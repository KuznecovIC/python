import requests
from plyer import notification

# Константы для работы с API
CITY = "Волгоград"
API_KEY = "23496c2a58b99648af590ee8a29c5348"
UNITS = "metric"
LANGUAGE = "ru"

# Класс для работы с запросами погоды
class WeatherRequest:
    def __init__(self, api_key: str, units: str = "metric", language: str = "ru"):
        self.api_key = api_key
        self.units = units
        self.language = language
        self.__url = ""
        self.__response = {}

    def __get_request_url(self, city: str) -> None:
        self.__url = fr"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={self.api_key}&units={self.units}&lang={self.language}"

    def get_weather(self, city: str) -> None:
        self.__get_request_url(city)
        response = requests.get(self.__url)
        self.__response = response.json()

    def get_clear_weather_data(self, city: str):
        self.get_weather(city)
        result_dict = {}
        result_dict["temp"] = self.__response['main']['temp']
        result_dict["feels_like"] = self.__response['main']['feels_like']
        result_dict["description"] = self.__response['weather'][0]['description']
        return result_dict
    
    def get_weather_string(self, weather_dict: dict) -> str:
        temp = weather_dict['temp']
        feels_like = weather_dict['feels_like']
        description = weather_dict['description']
        return f'Температура: {temp}°C\nОщущается как: {feels_like}°C\nОписание: {description}'

# Класс для отправки уведомлений
class Notification:
    @staticmethod
    def send_notification(title: str, message: str, app_name: str = "Weather") -> None:
        print(f"Sending notification: {title} - {message}")  # Логируем, что уведомление отправляется
        notification.notify(
            title=title,
            message=message,
            app_name=app_name,
            app_icon=None,
            timeout=15,
            toast=False,
        )

    def __call__(self, title: str, message: str) -> None:
        self.send_notification(title, message)

# Фасадный класс, объединяющий функциональность погоды и уведомлений
class WeatherFacade:
    def __init__(self, api_key: str, units: str = "metric", language: str = "ru") -> None:
        self.weather = WeatherRequest(api_key, units, language)  # Экземпляр WeatherRequest
        self.notification = Notification()  # Экземпляр Notification

    def __call__(self, city: str) -> None:
        weather_dict = self.weather.get_clear_weather_data(city)  # Получаем данные о погоде
        title = f"Погода в {city}"  # Заголовок уведомления
        message = self.weather.get_weather_string(weather_dict)  # Строка с данными о погоде
        self.notification(title, message)  # Отправляем уведомление

# Главная программа
if __name__ == "__main__":
    weather = WeatherFacade(API_KEY)  # Создаём фасад
    input_city = input("Введите город: ")  # Запрашиваем у пользователя название города
    weather(input_city)  # Вызываем фасад с данным городом
        
        
        

