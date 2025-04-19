from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
from datetime import datetime
import time
import os

def clear_screen():
    """Очистка терминала"""
    os.system('cls' if os.name == 'nt' else 'clear')

def setup_driver():
    """Настройка драйвера Chrome"""
    options = Options()
    
    # Путь к Chrome (укажите свой путь, если это необходимо)
    chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe"  # Замените на свой путь, если нужно
    options.binary_location = chrome_path
    
    # Основные настройки
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
    
    # Отключаем автоматизацию
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)
    
    try:
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)
        
        # Маскируем WebDriver
        driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
            "source": """
                Object.defineProperty(navigator, 'webdriver', {
                    get: () => undefined
                })
            """
        })
        return driver
    except Exception as e:
        print(f"Ошибка при запуске Chrome: {e}")
        print("Убедитесь, что Google Chrome установлен и обновлен до последней версии")
        return None

def get_element_text(driver, selector):
    """Безопасное получение текста элемента"""
    try:
        return driver.find_element(By.CSS_SELECTOR, selector).text
    except NoSuchElementException:
        return "Не найдено"

def parse_product(url):
    """Парсинг данных товара"""
    driver = setup_driver()
    if not driver:
        return None
        
    try:
        print("\nЗагрузка страницы...")
        driver.get(url)
        
        # Ожидание и прокрутка
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "h1"))
        )
        
        print("Прокрутка страницы для загрузки данных...")
        # Прокрутка страницы
        for i in range(1, 4):
            driver.execute_script(f"window.scrollTo(0, document.body.scrollHeight/{i});")
            time.sleep(1)
        
        print("Сбор данных...")
        data = {
            'Название': get_element_text(driver, "h1.product-page__title, h1"),
            'Цена': get_element_text(driver, "div.price-block__final-price ins, div.price-block__final-price").replace('₽', '').strip(),
            'Старая цена': get_element_text(driver, "div.price-block__old-price del, div.price-block__old-price").replace('₽', '').strip() or 'Нет скидки',
            'Бренд': get_element_text(driver, "div.product-page__brand span, span.product-page__brand"),
            'Артикул': get_element_text(driver, "span.product-article__value, div.product-article span"),
            'Рейтинг': get_element_text(driver, "span.product-review__rating, div.rating span"),
            'Отзывы': get_element_text(driver, "span.product-review__count-review, div.reviews-count span"),
            'Дата': datetime.now().strftime('%Y-%m-%d %H:%M')
        }
        
        return data
        
    except Exception as e:
        print(f"Ошибка парсинга: {e}")
        driver.save_screenshot('error.png')
        return None
    finally:
        driver.quit()

def display_product_data(data):
    """Красивый вывод данных в терминал"""
    if not data:
        print("Не удалось получить данные о товаре")
        return
    
    clear_screen()
    print("╔════════════════════════════════════════════╗")
    print("║          ДАННЫЕ ТОВАРА WILDBERRIES         ║")
    print("╠════════════════════════════════════════════╣")
    print(f"║ Название: {data['Название'][:45]:<45} ║")
    print("╠════════════════════════════════════════════╣")
    print(f"║ Текущая цена: {data['Цена']:<32} ║")
    print(f"║ Старая цена: {data['Старая цена']:<33} ║")
    print("╠════════════════════════════════════════════╣")
    print(f"║ Бренд: {data['Бренд'][:45]:<45} ║")
    print(f"║ Артикул: {data['Артикул'][:42]:<42} ║")
    print("╠════════════════════════════════════════════╣")
    print(f"║ Рейтинг: {data['Рейтинг']:<40} ║")
    print(f"║ Отзывы: {data['Отзывы']:<41} ║")
    print("╠════════════════════════════════════════════╣")
    print(f"║ Дата проверки: {data['Дата']:<31} ║")
    print("╚════════════════════════════════════════════╝")

if __name__ == '__main__':
    url = 'https://www.wildberries.ru/catalog/311657941/detail.aspx'
    print("Начало парсинга Wildberries...")

    product_data = parse_product(url)
    
    if product_data:
        display_product_data(product_data)
        
        # Сохранение в Excel
        try:
            df = pd.DataFrame([product_data])
            df.to_excel('wildberries_product.xlsx', index=False, engine='openpyxl')
            print("\nДанные сохранены в файл 'wildberries_product.xlsx'")
        except Exception as e:
            print(f"\nОшибка при сохранении в Excel: {e}")
    else:
        print("\nНе удалось получить данные. Проверьте файл 'error.png' для диагностики")
