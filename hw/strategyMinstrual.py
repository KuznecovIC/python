MISTRAL_API_KEY = 'WPBZaq7lrqbzjOPXFL2f8BFWLprRkhAx'
from abc import ABC, abstractmethod
from typing import List, Optional, Dict
import base64
from mistralai import Mistral

class RequestStrategy(ABC):
    @abstractmethod
    def execute(self, text: str, model: str, history: Optional[List[tuple[str, dict]]] = None, image_path: Optional[str] = None) -> dict:
        pass

class TextRequestStrategy(RequestStrategy):
    def execute(self, text: str, model: str, history: Optional[List[tuple[str, dict]]] = None, image_path: Optional[str] = None) -> dict:
        # Создаем клиента Mistral
        client = Mistral(api_key="MISTRAL_API_KEY")  # Используйте действующий API-ключ
        
        # Отправляем текстовый запрос
        chat_response = client.chat.complete(
            model=model,
            messages=[{"role": "user", "content": text}]
        )
        return chat_response.choices[0].message.content

class ImageRequestStrategy(RequestStrategy):
    def execute(self, text: str, model: str, history: Optional[List[tuple[str, dict]]] = None, image_path: Optional[str] = None) -> dict:
        if image_path is None:
            raise ValueError("Image path must be provided for image request.")
        
        # Преобразуем изображение в Base64
        with open(image_path, "rb") as img_file:
            encoded_image = base64.b64encode(img_file.read()).decode("utf-8")

        # Создаем клиента Mistral
        client = Mistral(api_key="MISTRAL_API_KEY")  # Используйте действующий API-ключ
        
        # Отправляем запрос с изображением и текстом
        chat_response = client.chat.complete(
            model=model,
            messages=[
                {"role": "user", "content": text},
                {"role": "system", "content": f"image:{encoded_image}"}
            ]
        )
        return chat_response.choices[0].message.content


class ChatFacade:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.text_strategy = TextRequestStrategy()
        self.image_strategy = ImageRequestStrategy()
        self.current_strategy = self.text_strategy  # По умолчанию используем текстовую стратегию
        self.history = []

    def change_strategy(self, strategy_type: str) -> None:
        if strategy_type == "text":
            self.current_strategy = self.text_strategy
        elif strategy_type == "image":
            self.current_strategy = self.image_strategy
        else:
            raise ValueError("Invalid strategy type. Choose 'text' or 'image'.")

    def select_model(self) -> str:
        # Здесь можно добавить логику выбора модели
        return "mistral-large-latest"

    def ask_question(self, text: str, model: str, image_path: Optional[str] = None) -> dict:
        response = self.current_strategy.execute(text, model, self.history, image_path)
        self.history.append((text, response))  # Сохраняем запрос и ответ в истории
        return response

    def get_history(self) -> List[tuple[str, dict]]:
        return self.history

    def clear_history(self) -> None:
        self.history.clear()

if __name__ == "__main__":
    api_key = "your_api_key_here"  # Замените на свой API-ключ
    chat = ChatFacade(api_key)

    # Смена стратегии на текстовую
    chat.change_strategy("text")

    # Выбор модели
    model = chat.select_model()

    # Отправка текстового запроса
    text_question = "What is a menstrual cycle?"
    response = chat.ask_question(text_question, model)
    print("Ответ от API:", response)

    # Смена стратегии на мультимодальную
    chat.change_strategy("image")

    # Отправка запроса с изображением
    image_path = "path/to/image.jpg"  # Путь к изображению
    response = chat.ask_question(text_question, model, image_path)
    print("Ответ от API с изображением:", response)

    # Просмотр истории запросов
    print("История запросов:", chat.get_history())