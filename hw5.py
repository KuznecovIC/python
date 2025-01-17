import os
from typing import Literal
from PIL import Image
from pillow_heif import register_heif_opener

QUALITY: int = 50  # Можно настроить качество сжатия

class ImageCompressor:
    def __init__(self, quality: int) -> None:
        self.quality: int = quality
        self.__supported_formats: tuple[Literal['jpg', 'jpeg', 'png']] = ('jpg', 'jpeg', 'png')

    def compress_image(self, input_path: str, output_path: str) -> None:
        """
        Сжимает изображение и сохраняет его в формате HEIF.

        Args:
            input_path (str): Путь к исходному изображению.
            output_path (str): Путь для сохранения сжатого изображения.

        Returns:
            None
        """
        with Image.open(input_path) as img:
            img.save(output_path, "HEIF", quality=self.quality)
        print(f"Сжато: {input_path} -> {output_path}")

def compress_image(input_path: str, output_path: str) -> None:
    """
    Сжимает изображение и сохраняет его в формате HEIF.
 
    Args:
        input_path (str): Путь к исходному изображению.
        output_path (str): Путь для сохранения сжатого изображения.
 
    Returns:
        None
    """
    with Image.open(input_path) as img:
        img.save(output_path, "HEIF", quality=QUALITY)
    print(f"Сжато: {input_path} -> {output_path}")

def process_directory(directory: str, compressor: ImageCompressor) -> None:
    """
    Обрабатывает все изображения в указанной директории и её поддиректориях.

    Args:
        directory (str): Путь к директории для обработки.
        compressor (ImageCompressor): Экземпляр класса для сжатия изображений.

    Returns:
        None
    """
    for root, _, files in os.walk(directory):
        for file in files:
            # Проверяем расширение файла
            if file.lower().endswith(('.jpg', '.jpeg', '.png')):
                input_path = os.path.join(root, file)
                output_path = os.path.splitext(input_path)[0] + '.heic'
                compressor.compress_image(input_path, output_path)

def main(input_path: str, quality: int) -> None:
    """
    Основная функция программы. Обрабатывает входной путь и запускает сжатие изображений.

    Args:
        input_path (str): Путь к файлу или директории для обработки.
        quality (int): Качество сжатия изображений.

    Returns:
        None
    """
    register_heif_opener()
    input_path = input_path.strip('"')  # Удаляем кавычки, если они есть
    
    compressor = ImageCompressor(quality)
   
    if os.path.exists(input_path):
        if os.path.isfile(input_path):
            # Если указан путь к файлу, обрабатываем только этот файл
            print(f"Обрабатываем файл: {input_path}")
            output_path = os.path.splitext(input_path)[0] + '.heic'
            compressor.compress_image(input_path, output_path)
        elif os.path.isdir(input_path):
            # Если указан путь к директории, обрабатываем все файлы в ней
            print(f"Обрабатываем директорию: {input_path}")
            process_directory(input_path, compressor)
            # Функция process_directory рекурсивно обойдет все поддиректории
            # и обработает все поддерживаемые изображения
    else:
        print("Указанный путь не существует")

if __name__ == "__main__":
    user_input: str = input("Введите путь к файлу или директории: ")
    quality_input: int = int(input("Введите качество сжатия (от 0 до 100): "))
    main(user_input, quality_input)

