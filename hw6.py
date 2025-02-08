"""
19.01.2025
Тема: ООП Ч5. Наследование. Множественное. Иерархическое. MRO. Урок: 20
"""
 
from abc import ABC, abstractmethod
 
 
class AbstractDocument(ABC):
    def __init__(self, file_path: str) -> None:
        self.file_path = file_path
        self.file: None = self.open()
   
    @abstractmethod
    def open(self):
        pass
 
    @abstractmethod
    def read(self):
        pass
 
    @abstractmethod
    def append(self):
        pass
   
    @abstractmethod
    def write(self):
        pass
 
    def __str__(self) -> str:
        return f"{self.__class__.__name__} - {self.file_path}"
 
 
class TxtDocument(AbstractDocument):
    def __init__(self, file_path: str) -> None:
        super().__init__(file_path)
 
    def open(self) -> str:
        with open(self.file_path, "r", encoding="utf-8") as file:
            return file.read()
    def read(self):
        pass
    def append(self):
        pass
    def write(self):
        pass
 
 
class PdfDocument(AbstractDocument):
    def __init__(self, file_path: str) -> None:
        super().__init__(file_path)
 
    def open(self):
        pass
    def read(self):
        pass
    def append(self):
        pass
    def write(self):
        pass
 
 
# abstract = AbstractDocument() # Это не работает. Мы не можем создать экземпляр абстрактного класса
#md_file = MarkdownDocument("file.md")
pdf_file = PdfDocument("file.pdf")
 
#print(md_file)
print(pdf_file)

file = "my_file.txt"
print(file)
txt_file = TxtDocument(file)
print(txt_file.file)


class A:
    def __init__(self) -> None:
        print("Инициализация класса A")

    def method_a(self):
        print("Метод класса A")

class B:
    def __init__(self) -> None:
        print("Инициализация класса B")
    
    def method_b(self):
        print("Метод класса B")

class C(A, B):
    def __init__(self) -> None:
        super().__init__()
        print("Инициализация класса C")


    def method_c(self):
        print("Метод класса C")

# Создаем экземпляр класса C
c = C()
c.method_a()  # метод класса A

# Создаём миксины для различных способностей животных
class SwimMixin:
    def swim(self):
        return f"{self.__class__.__name__} плавает в воде"
 
class FlyMixin:
    def fly(self):
        return f"{self.__class__.__name__} летит по небу"
 
class RunMixin:
    def run(self):
        return f"{self.__class__.__name__} бежит по земле"
 
# Базовый класс животного
class Animal:
    def __init__(self, name):
        self.name = name
 
    def eat(self):
        return f"{self.name} кушает"
 
# Теперь создаём конкретных животных с нужными способностями
class Duck(Animal, SwimMixin, FlyMixin):
    def make_sound(self):
        return "Кря-кря!"
 
class Cat(Animal, RunMixin):
    def make_sound(self):
        return "Мяу!"
 
class Penguin(Animal, SwimMixin, RunMixin):
    def make_sound(self):
        return "Ква-ква!"