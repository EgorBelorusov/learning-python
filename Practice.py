# Мини-проект "Угадай число"
from random import randint
from unittest import result


# def guess_number_game():
#     number_randint = randint(1, 100)
#     attempts_count = 0
#     print("Загадал число от 1 до 100. Попробуй отгадать!")
#
#     while True:
#         attempts_count += 1
#         try:
#             user_input = int(input("Угадайте число: "))
#
#             if user_input in range(1, 101):
#
#                 if user_input == number_randint:
#                     print("Поздравляю, Вы угадали число!")
#                     print(f"Количество попыток: {attempts_count}")
#                     return attempts_count
#
#                 elif user_input > number_randint:
#                     print("Меньше")
#
#
#                 else:
#                     print("Больше")
#
#             else:
#                 print("Вы ввели число за пределами диапазона от 1 до 100. Попробуйте снова.")
#
#         except ValueError:
#             print("Ошибка! Необходимо ввести число!")
#
#
#
#
#
# print(guess_number_game())




# ================================================================
# Мини-проект "Генератор пароля"
# import string
# from random import choice
#
# def generate_password(length):
#     set_chars = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
#     password_storage = ""
#
#     for i in range(length):
#         char = choice(set_chars)
#         password_storage += char
#
#     return password_storage
#
#
#
# try:
#     user_input = int(input("Введите длину пароля: "))
#     print(generate_password(user_input))
#
# except ValueError:
#     print("Ошибка! Введите число.")





# ================================================================
# Мини-проект "Калькулятор"
def calculator(number_one, sign, number_two):

    try:
        if sign in ["+", "-", "*", "/"]:

            if sign == "+":
                result = number_one + number_two
                return result

            elif sign == "-":
                result = number_one - number_two
                return result

            elif sign == "*":
                result = number_one * number_two
                return result

            else:
                result = number_one / number_two
                return result

        else:
            return "Неверная операция!"

    except ZeroDivisionError:
        return "Делить на 0 невозможно."








while True:

        try:
            number_first = int(input("Введите первое число: "))
            operation = input("Введите знак: ")
            number_second = int(input("Введите второе число: "))

            print(calculator(number_first, operation, number_second))


            users_input = input("Хотите продолжить? Введите 'q' для выхода или любую клавишу для продолжения: ")

            if users_input.lower() == 'q':
                break


        except ValueError:
            print("Ошибка! Введите число.")











