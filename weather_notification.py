import requests
from plyer import notification

CYTY = "Волжский"
KEY = "23496c2a58b99648af590ee8a29c5348"
UNITS = "metric"
LANG = "ru"
url = f'https://api.openweathermap.org/data/2.5/weather?q={CYTY}&appid={KEY}&units={UNITS}&lang={LANG}'

response = requests.get(url)  # Сделали запрос и получили объект ответа

if response.status_code == 200:  # Проверка успешности запроса
    print(response.status_code)  # Получили статус ответа
    weather_dict = response.json()

    # Получаем данные о погоде
    temp = weather_dict['main']['temp']
    feels_like = weather_dict['main']['feels_like']
    description = weather_dict['weather'][0]['description']

    print(f'Температура: {temp}°C\nОщущается как: {feels_like}°C\nОписание: {description}')

    # Отправка уведомления
    notification.notify(
        title=f"Погода в {CYTY}",
        message=f'Температура: {temp}°C\nОщущается как: {feels_like}°C\nОписание: {description}',
        app_name='Погода',
        app_icon=None,
        timeout=10,
        toast=True,
    )
else:
    print(f"Ошибка запроса: {response.status_code}")