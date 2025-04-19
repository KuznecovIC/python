import math
# квадраты мое решение

def square(x):
   return x * x

print(square(4))

# решение deepseek
def sum_of_squares(n):
    total = 0
    for i in range(1, n + 1):
        total += i ** 2
    return total

# Проверка
#print(sum_of_squares(3))  # Должно вывести 14
#print(sum_of_squares(5))  # Должно вывести 55 (1 + 4 + 9 + 16 + 25)

# Задача: Проверка на простое число

def number_del_one(x):
        if x <= 1:
            return True
        
        for i in range(2, int(math.sqrt(x)) + 1):
            if x % i == 0:
        
              return False
        return True


print(number_del_one(7)) 
        
# решение deepseek

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# Проверка
print(is_prime(7))    # True
print(is_prime(10))   # False
print(is_prime(1))    # False
print(is_prime(2))    # True

# Задача: Разворот слов в строке

def reverse_word(word):
    return word[::-1]

print(reverse_word("hello"))

# Решение deepseek
def reverse_words(sentence):
    words = sentence.split()  # Разбиваем строку на слова
    reversed_words = [word[::-1] for word in words]  # Разворачиваем каждое слово
    return ' '.join(reversed_words)  # Собираем обратно в строку

# Проверка
print(reverse_words("Hello World"))    # "olleH dlroW"
print(reverse_words("Python is fun"))  # "nohtyP si nuf"

# Задача: Шифр Цезаря

def caesar_cipher(text, shift):
    shifted_text = ""
    for char in text:
        if char.isalpha():
            ascii_offset = ord('A') if char.isupper() else ord('a')
            shifted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            shifted_text += shifted_char
        else:
            shifted_text += char
    return shifted_text

# Проверка
print(caesar_cipher("Hello, World!", 3))  # "Khoor, Zruog!"

# решение deepseek
def caesar_cipher(text, shift):
    result = []
    for char in text:
        if 'A' <= char <= 'Z':
            new_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        elif 'a' <= char <= 'z':
            new_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            new_char = char  # Не буквы оставляем как есть
        result.append(new_char)
    return ''.join(result)

# Проверка
print(caesar_cipher("ABC", 1))     # "BCD"
print(caesar_cipher("XYZ", 3))     # "ABC"
print(caesar_cipher("Hello, World!", 5))  # "Mjqqt, Btwqi!"

# Задание 1. Частотный анализ букв (лёгкое)

def count_letters(text):
    counts = {}
    for char in text:
        if char.isalpha():
            char = char.lower()
            counts[char] = counts.get(char, 0) + 1
    return counts

# Проверка
print(count_letters("Hello, World!"))

# Задание 2. Рекурсивный палиндром (среднее)

def is_palindrome(word):
    if len(word) <= 1:
        return True
    return word[0] == word[-1] and is_palindrome(word[1:-1])

print(is_palindrome("racecar"))   
print(is_palindrome("hello")) 

# Задание 3. Умножение матриц (сложное)

def matrix_multiply(a, b):
    result = [[0] * len(b[0]) for _ in range(len(a))]
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                result[i][j] += a[i][k] * b[k][j]
    return result
a = [[1, 2], [3, 4]]  
b = [[5, 6], [7, 8]]  
print(matrix_multiply(a, b))  


    