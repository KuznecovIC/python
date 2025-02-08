from marvel import simple_set, small_dict, full_dict




def foo_0(x):
    return x + 10

foo = lambda x: x + 10

print(foo(10))
print(foo_0(10))

simple_list = list(simple_set)

new_simple_list: list[any] = []

for film in simple_list:
    new_simple_list.append(film)


new_simple_list: list[str] = [film for film in simple_list]


result_list_3: list[str] = [film for film in simple_list if 'чел' in film.lower()]

def search_string(string, key) -> bool:
    return key.lower() in string.lower()

result_list_3 = filter(lambda string: search_string(string, 'чел'), simple_list)
print(list(result_list_3))

result_list_4 = []

for film in simple_list:
    result_list_4.append(film.replace(' ', '_').lower())

result = [film.replace(' ', '_').lower() for film in simple_list]
result_list_4 = list(map(lambda film: film.replace(' ', '_').lower(), simple_list))

print(result_list_4)

result_film_5 = []

for film in simple_list:
    if ' ' in film:
        result_film_5.append(film.replace(' ', '_').lower())
    else:
        result_film_5.append(film)

result_film_5 =  [film.replace(' ', '_').lower() if ' ' in film else film for film in simple_list]

result_film_5 = list(map(lambda film: film.replace(' ', '_').lower() if ' ' in film else film, simple_list))

print(result_film_5) 

result_list_6 = []

for film in simple_list:
    if len(film) > 15:
        if ' ' in film:
            result_list_6.append(film.replace(' ', '_').lower())
        else:
            result_list_6.append(film)

result_list_6 = [film.replace(' ', '_').lower() if ' ' in film else film for film in simple_list if len(film) > 15]

result_list_6 = list(map(lambda film: film.replace(' ', '_').lower() if ' ' in film else film, filter(lambda film: len(film) > 15, simple_list)))

print(result_list_6)