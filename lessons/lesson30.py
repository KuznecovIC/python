from dataclasses import dataclass
from typing import List

@dataclass
class Pizza:
    # Доступные ингредиенты и размеры
    available_products = ['сыр', 'грибы', 'колбаса', 'оливки', 'перец', 'томаты', 'анчоусы', 'лосось']
    available_sizes = ['маленькая', 'средняя', 'большая']

    size: str
    cheese_bord: bool
    additional_ingredients: List[str]

    def __post_init__(self):
        # Проверяем, что все ингредиенты доступны
        if any(ingredient.lower() not in self.available_products for ingredient in self.additional_ingredients):
            raise ValueError('Один или несколько ингредиентов не доступны для заказа')

        # Проверяем, что размер пиццы допустим
        if self.size.lower() not in self.available_sizes:
            raise ValueError('Недопустимый размер пиццы')

    def __str__(self):
        return f'Пицца. Размер "{self.size}", сырный борт: {self.cheese_bord}, ингредиенты: {self.additional_ingredients}'

class PizzaBuilder:
    def __init__(self):
        self.pizza = Pizza(size='', cheese_bord=False, additional_ingredients=[])

    def set_size(self, size):
        self.pizza.size = size
        return self

    def set_cheese_bord(self):
        self.pizza.cheese_bord = True
        return self

    def add_ingredient(self, *ingredients):
        self.pizza.additional_ingredients.extend(ingredients)
        return self

    def build(self):
        return self.pizza

class PizzaManager:
    def __init__(self):
        self.builder = PizzaBuilder()
        self.pizza: Opttional[Pizza] = None

    def make_pizza(self, size, *ingredients):
        self.pizza = self.builder.set_size(size).add_ingredient(*ingredients).build()
        
        if cheese_bord:
            self.pizza =  self.builder.set_cheese_bord().build()
            return self.pizza

if __name__ == '__main__':
    manager = PizzaManager()
    pizza = manager.make_pizza('большая', 'колбаса', 'оливки')
    print(pizza)