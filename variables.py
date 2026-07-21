# Задание 1
# Переменные каждого типа
# name = "Mark"
# age = 30
# height = 180.4
# is_alive = True

# Вывод на экран
# print(name)
# print(age)
# print(height)
# print(is_alive)
#
# # Вывод типа переменной
# print(type(name))
# print(type(age))
# print(type(height))
# print(type(is_alive))


# print(0.1 + 0.2)


# Задание 2 "операции"
# print(f"Меня зовут {name}. Мне {age} лет. Мой рост {height} см.")

# print(10 + 5)
# print(10 - 5)
# print(10 * 5)
# print(10 / 5)
# print(10 // 5)
# print(10 % 5)
# print(10 ** 5)
# print(10 % 3)
# print(10 % 1)
#
# print("ad" * 3)


# Задание 3 "f-строки, input"
# name = input("Введите имя: ")
# age = int(input("Введите возраст: "))
# height = float(input("Введите рост (см): "))
#
# print(f"Привет, меня зовут {name}. Мне {age} лет. Рост {height} см. Через 10 лет мне будет {age + 10}")

# Задание 4 "if, elif, else"
# user_age = int(input("Введите ваш возраст: "))
#
# if user_age > 0 and user_age < 150:
#
#     print("Возраcт введен корректно")
#
#     if user_age < 18:
#         print("Ты несовершеннолетний")
#     elif 18 <= user_age <= 65:
#         print("Ты взрослый")
#     else:
#         print("Ты пенсионер")
#
# else:
#     print("Проверьте введенные данные")


# Задание 5 "for, while"
# for i in range(1, 21):
#     if i % 2 == 0:
#         print(i)
#
# # 1 вариант решения
# number = ""
# while number != 0:
#     number = int(input("Введите число: "))
#     if number == 0:
#         break
#     else:
#         print(number)
#
# # 2 вариант решения
# while True:
#     number = int(input("Введите число: "))
#     if number == 0:
#         break
#     else:
#         print(number)


# Задания посложнее № 1 "Стороны треугольника"

# side_one = float(input("Введите длинну первой стороны треугольника: ")) # 5
# side_two = float(input("Введите длинну второй стороны треугольника: ")) # 5
# side_three = float(input("Введите длинну третьей стороны треугольника: ")) # 7
#
# if side_two + side_three > side_one and side_one + side_three > side_two and side_one + side_two > side_three:
#
#     if side_three == side_two == side_one:
#         print("Треугольник равносторонний")
#
#     elif side_one == side_two or side_three == side_one or side_three == side_two:
#         print("Треугольник равнобедренный")
#
#     else:
#         print("Треугольник разносторонний")
#
# else:
#     print("Треугольника не существует")


# Задания посложнее № 2 "Калькулятор с проверкой"

# number_one = float(input("Введите первое число: "))
# number_two = float(input("Введите второе число: "))
# sign = input("Введите знак операции: ")
#
# if sign in ["+", "-", "*", "/"]:
#
#         if sign == "+":
#             print(number_one + number_two)
#
#         elif sign == "-":
#             print(number_one - number_two)
#
#         elif sign == "*":
#             print(number_one * number_two)
#
#         else:
#             if number_two == 0:
#                 print("На ноль делить нельзя")
#
#             else:
#                 print(number_one / number_two)
#
# else:
#     print("Неизвестная операция")


# Задания посложнее № 3 "Таблица умножения"
# for i in range(1,6):
#     row = ""
#     for j in range(1,6):
#         row = row + str(i * j) + " "
#     print(row)


# Задания посложнее № 4 "Поиск простого числа"
# Вариант решения № 1
# number = int(input("Введите число: "))
# is_prime = True
#
# if number > 1:
#
#     for i in range(2, number):
#
#         if number % i == 0:
#             is_prime = False
#             break
#
#     if is_prime:
#         print("Число простое.")
#     else:
#         print("Число не простое.")
#
# else:
#     print("Числа 0, 1 и отрицательные не являются простыми.")


# Вариант решения № 2
# number = int(input("Введите число: "))
# list = []
#
# if 0 < number > 1:
#
#     for i in range(2, number):
#
#         if number % i == 0:
#             list.append(i)
#             break
#
#
#     if list:
#         print("Число простое.")
#     else:
#         print("Число не простое.")
#
# else:
#     print("Числа 0, 1 и отрицательные не являются простыми.")




# # Усложненные задачи № 5 "FizzBuzz"
# for i in range(1, 31):
#     if i % 3 == 0 and i % 5 == 0:
#         print(f"{i} - FizzBuzz")
#
#     elif i % 3 == 0:
#         print(f"{i} - Fizz")
#
#     elif i % 5 == 0:
#         print(f"{i} - Buzz")
#
#     else:
#         print(i)


