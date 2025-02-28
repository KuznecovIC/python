from typing import List, Tuple, Optional, Dict, Union, Any, Callable, Iterable, Generator, Set

list_num = [1, 2, 3, 4, 5]

def func(num:List[int]) -> None:
    print(list_num)

func(list_num)

class Myclass:
    pass

cl: Myclass = Myclass()


def fucn8(a):
    # a - хранится тут
    def inner8():
        # a - используется тут
        print(a)
    return inner8
 
banan = print
banan("Привет!")
 
# Вызов функции 8
foo = fucn8("пирожок")
foo()

def counter(start_value: int) -> Callable[[], int]:
    def inner():
        nonlocal start_value
        start_value += 1
        return start_value
    return inner

counter1 = counter(10)

counter2 = counter(20)

print(counter1())
print(counter2())
print(counter1())
print(counter2())

