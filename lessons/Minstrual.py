import requests
import base64
import os

class TextRequest:
    def __init__(self, api_key: str) -> None:
        self.api_key = api_key
        self.url = "https://api.mistral.ai/v1/chat/completions"  

    def send(self, text: str, model: str) -> dict:
        """Отправка текстового запроса к API."""
        headers = {"Authorization": f"Bearer {self.api_key}", "Content-Type": "application/json"}
        payload = {"text": text, "model": model}
        try:
            response = requests.post(self.url, json=payload, headers=headers)
            response.raise_for_status()  # Возбудит исключение при ошибке
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
            return {}

class ImageRequest:
    def __init__(self, api_key: str) -> None:
        self.api_key = api_key
        self.url = "https://api.mistral.ai/v1/chat/completions"  

    def send(self, text: str, image_path: str, model: str) -> dict:
        """Отправка мультимодального запроса с изображением и текстом."""
        headers = {"Authorization": f"Bearer {self.api_key}", "Content-Type": "application/json"}

        # Проверка существования файла
        if not os.path.exists(image_path):
            print(f"Error: File {image_path} not found.")
            return {}

        try:
            with open(image_path, "rb") as image_file:
                image_base64 = base64.b64encode(image_file.read()).decode('utf-8')

            payload = {"text": text, "image": image_base64, "model": model}
            response = requests.post(self.url, json=payload, headers=headers)
            response.raise_for_status()
            return response.json()

        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
            return {}

class ChatFacade:
    def __init__(self, api_key: str) -> None:
        self.api_key = api_key
        self.text_request = TextRequest(api_key)
        self.image_request = ImageRequest(api_key)
        self.history = []

    def select_mode(self) -> int:
        """Выбор режима (текстовый или с изображением)."""
        print("Select request mode:")
        print("1 - Text")
        print("2 - Image")
        return int(input("Enter 1 or 2: "))

    def select_model(self, mode: int) -> str:
        """Выбор модели для запроса."""
        models = {
            1: ["text_model_1", "text_model_2"],
            2: ["image_model_1", "image_model_2"]
        }
        print(f"Available models: {models[mode]}")
        model = input("Select model: ")
        return model

    def load_image(self, image_path: str) -> str:
        """Загрузка изображения и преобразование в Base64."""
        return image_path

    def ask_question(self, text: str, model: str, image_path: str = None) -> dict:
        """Отправка запроса в зависимости от режима."""
        if image_path:
            return self.image_request.send(text, image_path, model)
        return self.text_request.send(text, model)

    def get_history(self) -> list:
        """Возвращает историю запросов."""
        return self.history

    def clear_history(self) -> None:
        """Очистка истории."""
        self.history = []

if __name__ == "__main__":
    api_key = "Q1tUE4sUd0t6lRceKdq7afvQr07GMdP5" 
    chat = ChatFacade(api_key)

    # Выбор режима
    mode = chat.select_mode()

    # Выбор модели
    model = chat.select_model(mode)

    # Если выбран режим с изображением, необходимо загрузить изображение
    image_path = None
    if mode == 2:
        image_path = chat.load_image("path/to/image.jpg")  

    # Отправка запроса
    text_question = "Расскажите о последних новостях в IT."
    response = chat.ask_question(text_question, model, image_path)

    print("Ответ от API:", response)

    # Просмотр истории запросов
    print("История запросов:", chat.get_history())