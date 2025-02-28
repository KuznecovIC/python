string = "Банан"
my_list = ["Банан", "Апельсин", "Груша"]

MIN_VALUE = 0
MAX_VALUE = 1000000000000000000000000000000


range_nums = range(MIN_VALUE, MAX_VALUE)

#for num in range_nums:
    #print(num)

even_nums = filter(lambda x: x % 2 == 0, range_nums)

string_nums = map(lambda x: str(x) + " число", even_nums)

from typing import Generator

#def my_generator(start: int, stop: int) -> Generator[int]:
    #for i in range(start, stop):
       # yield i

#gen = my_generator(0, 2)

#print(next(gen))
#print(next(gen))
#print(next(gen))

def advanced_generator(start:int, stop: int) -> Generator[int, str, float]:
    while current < stop:
        command = yield current

        if command == 'double':
            current *= 2
        elif command == 'square':
            current **= 2
        elif command == 'cube':
            current **= 3
        else:
            current += 1
    return current

def advanced_generator_2(start: int, stop: int) -> Generator[int, str | None, float]:
    current = start
    while current < stop:
        current_value = current
        yield current_value

        command = yield current

        if command == 'double':
            current *= 2
        elif command == 'square':
            current **= 2
        elif command == 'cube':
            current **= 3
        else:
            current += 1
    return current

gen = advanced_generator_2(0, 10)

gen.send(None)
gen.send('double')
gen.send('square')
gen.send('cube')
print(gen.send(None))
for num in gen:
    print(num)

while gen:
    try:
        print(next(gen))
    except StopIteration:
        print('Конец')

from random import choice

fruit_list = ['Банан', 'Апельсин', 'Груша', 'Яблоко', 'Киви', 'Ананас']

def __init__(self, products: list[str]):
    self.products = products

def __iter__(self):
    return self

def __next__(self):
    if not self.products:
        raise StopIteration
    
    fruit = choice(self.products)

    self.products.remove(fruit)

    return fruit

coctail_gen = CoctailGenerator(fruit_list)

for fruit in coctail_gen:
    print(fruit)
        
