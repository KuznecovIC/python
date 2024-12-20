def say_hello(name: str, age: int) -> None:
    print(f"Привет, {name.title()}! Тебе {age} лет.")
say_hello("Алексей", 30)

message: None=say_hello("Алексей",30)
def is_adult(age:int, adult_age: int = 18) -> bool:

    return age >= adult_age

result: bool = is_adult(20)
result2: bool = is_adult(17, 16)
result3: bool = is_adult(age=20, adult_age=16)

"""
напишите функцию которая принемает строку и возвращает bool значение является ли строка палиндромом используйте аннотацуию типов и документацию для функции 
срез добавить lower()
[::-1]
"""
def is_palindrome(text: str) -> bool:
    return text == text[::-1].lower()
print(is_palindrome("шалаш"))
print(is_palindrome("шалаш1"))


