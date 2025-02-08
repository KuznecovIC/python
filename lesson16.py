class User:
    pass

user = User()
print(user)
print(type(user))
user = User()
print(user)
print(type(user))

string_1 = str("строка")
print(type(string_1))


class Car:
    def __init__(self, model:str, color:str, year:int) -> None:
        self.color: str = color
        self.year: int = year
        self.model: str = model
car_1 = Car("BMW", "black", 2020)
car_2  = Car("Audi", "white", 2021)
print(car_1.color)
print(car_2.color)
print(car_1)
print(car_2)
    