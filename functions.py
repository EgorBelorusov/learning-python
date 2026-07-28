# Тема 6 "Функции"
# Объявление функции
# def summa(a, b):
#     return a + b
#
# print(summa(1, 2))
#
#
#
#
# def greet(name):
#     print(f"Привет, {name}!")
#
# greet("Марк")
#
#
#
# # Значение по умолчанию  в параметре
# def greet(name, greeting="Привет"):
#     print(f"{greeting}, {name}!")
#
# greet("Марк")                    # "Привет, Марк!"
# greet("Анна", "Добрый день")     # "Добрый день, Анна!"
from unittest import result



# Область видимости
# Переменные, созданные внутри функции, существуют только внутри неё — они называются локальными
# Переменные, объявленные вне любой функции — глобальные



# Задание 1
# def is_even(numbers):
#     return numbers % 2 == 0
#
#
# print(is_even(2))
#
#
# # Задание 2
# def calculate_average(numbers):
#     result = 0
#     for num in numbers:
#         result += num
#
#     total = result / len(numbers)
#     return total
#
#
# print(calculate_average([1, 2, 3, 4, 5]))
#
#
#
# # Задание 3
# def greet_user(name, time_of_day="добрый день"):
#     print(f"{name}, {time_of_day}")
#
# greet_user("Егор", "доброе утро")





# ============================================================================
# *args **kwargs
# ============================================================================

# *args и **kwargs — функции с произвольным числом аргументов
# *args собирает любое количество позиционных аргументов в один кортеж с именем args
# (само имя args — просто соглашение, можно назвать иначе, но так принято).
# Внутри функции args ведёт себя как обычный кортеж — можно перебрать циклом, как в примере.

# def sum_all(*args):
#     total = 0
#     for num in args:
#         total += num
#     return total
#
# print(sum_all(1, 2, 3))       # 6
# print(sum_all(1, 2, 3, 4, 5)) # 15
#
#
# # Здесь kwargs внутри функции — обычный словарь {"name": "Марк", "age": 30, "city": "Москва"}.
#
# def print_info(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")
#
# print_info(name="Марк", age=30, city="Москва")






# Задание 1

def find_max(*args):
    number = float("-inf")
    for num in args:
        if num > number:
            number = num

    return number

print(find_max(1,2,3,4,5,6,7,8,9,100))



# Задание 2

def print_profile(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_profile(name="Марк", age=30, city="Москва")





# Задание 3

# count = 1
#
# def func(num):
#     count = count + num
#     return count
#
# print(func(10))




def func(count):
    return count + 1

count = 1
print(func(2))