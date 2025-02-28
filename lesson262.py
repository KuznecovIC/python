from typing import Callable

shop_list = ["Айфон", "Айпад", "Айфончик"]

def cach_sorter(data: list[str]) -> Callable[[], list[str]]:
    cach = []
    def sorter():
        if not cach and cach is not data:
            print('Делаем сортировку')
            return sorted(data)
        print(['Кеш!'])
        return cach
    
    return sorter

sort_result = cach_sorter(shop_list)

print(sort_result())

def decorator_1(func: Callable):
    def wrapper():
        print("Декоратор 1")
        fucn()
        print("Декоратор 2")
    return wrapper

def print_hello():
    print("Hello")

def print_goodbye():
    print("Goodbye")

print_hello_decarated = decorator_1(print_hello)

print_goodbye_decarated = decorator_1(print_goodbye)

def decorator_2(func: Callable[[str], str]) -> Callable[[str], str]:
    def wrapper(s: str) -> str:
        print("Декоратор 2")
        result = func(s)
        print("Декоратор 2")
        return result
    
    return wrapper

def print_hello2(s: str) -> str:
    return f"Hello  2 {s}"


print_hello2_decarated = decorator_2(print_hello2)

print(print_hello2_decarated("World"))

def decoration_3(func: Callable) -> Callable:
    def wrapper(*args, **kwargs):
        print("Декоратор 3")
        result = func(*args, **kwargs)
        print("Декоратор 3")
        return result
    return wrapper