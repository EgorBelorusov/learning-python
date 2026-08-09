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
# def calculated(number_one, sign, number_two):
#
#     try:
#         if sign in ["+", "-", "*", "/"]:
#
#             if sign == "+":
#                 result = number_one + number_two
#                 return result
#
#             elif sign == "-":
#                 result = number_one - number_two
#                 return result
#
#             elif sign == "*":
#                 result = number_one * number_two
#                 return result
#
#             else:
#                 result = number_one / number_two
#                 return result
#
#         else:
#             return "Неверная операция!"
#
#     except ZeroDivisionError:
#         return "Делить на 0 невозможно."
#
#
#
#
#
#
#
# def run_calculate():
#     while True:
#
#             try:
#                 number_first = int(input("Введите первое число: ").strip())
#                 operation = input("Введите знак: ").strip()
#                 number_second = int(input("Введите второе число: ").strip())
#
#                 print(calculated(number_first, operation, number_second))
#
#
#                 users_input = input("Хотите продолжить? Введите 'q' для выхода или любую клавишу для продолжения: ")
#
#                 if users_input.lower() == 'q':
#                     break
#
#
#             except ValueError:
#                 print("Ошибка! Введите число.")
#
#
#
#
# run_calculate()





# ================================================================
# Мини-проект "To-do лист"

def load_tasks():
    with open("todo.txt", "r", encoding="utf-8") as file:

        tasks = file.readlines()

        return tasks





def show_tasks(tasks):
    print("Список задач:")
    for item, task in enumerate(tasks):

        print(f"{item + 1}. {task}")

    return "Список задач выведен!"





def add_task(tasks):
    input_task = input("Введите новую задачу: ").strip()

    tasks.append(input_task + "\n")

    with open("todo.txt", "w", encoding="utf-8") as file:

        file.writelines(tasks)

        return "Задача успешно добавлена!"





def remove_task(tasks):

    if not tasks:
        return "Ошибка! Список задач пуст, удалять нечего."

    try:
        del_index = int(input("Введите номер задачи для удаления: ").strip())

        if del_index < 1 or del_index > len(tasks):
            return "Ошибка! Задачи с таким номером не существует."

        tasks.pop(del_index - 1)

        with open("todo.txt", "w", encoding="utf-8") as file:
            file.writelines(tasks)

        return "Задача успешно удалена!"

    except ValueError:
        return "Ошибка! Введите корректное число (номер задачи)."



tasks = load_tasks()

while True:

    print("\n ========== Список задач ========== \n")
    print("1 - Показать задачи")
    print("2 - Добавить задачу")
    print("3 - Удалить задачу")
    print("4 - Выйти")

    try:
        user_input = int(input("Введите номер команды: ").strip())

        if user_input == 1:
            tasks = load_tasks()
            print(show_tasks(tasks))

        elif user_input == 2:
            print(add_task(tasks))

        elif user_input == 3:
            print(remove_task(tasks))

        else:
            break

    except ValueError:
        print("Ошибка! Введите верный номер команды")










