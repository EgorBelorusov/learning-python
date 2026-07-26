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
def is_even(numbers):
    return numbers % 2 == 0


print(is_even(2))


# Задание 2
def calculate_average(numbers):
    result = 0
    for num in numbers:
        result += num

    total = result / len(numbers)
    return total


print(calculate_average([1, 2, 3, 4, 5]))



# Задание 3
def greet_user(name, time_of_day="добрый день"):
    print(f"{name}, {time_of_day}")

greet_user("Егор", "доброе утро")