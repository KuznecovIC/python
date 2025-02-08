from typing import Literal

class Animal:
    def __init__(self, name: str) -> None:
        self.name: str = name
        print(f"Animal {self.name} created")
        

    def voice(self) -> str:
        return "Animal voice"

    def __str__(self) -> str:
        return f"Animal {self.name}"

class Dog(Animal):
    def voice(self) -> Literal['Животное издаёт звук']:
        animal_voice: Literal['Животное издаёт звук'] = super().voice()  
        animal_voice += " Гав"
        return animal_voice
    
    def __init__(self, name: str, breed: str) -> None:
        super().__init__(name)
        self.breed: str = breed
        print(f"Dog {self.name} created")

dog = Dog("Шарик", "Дворняга")
print(dog.voice())  
print(dog)  
