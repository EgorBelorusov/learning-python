# Тема 8 "Обработка исключений"
# Базовый синтаксис
# try:
#     result = 10 / 0
# except ZeroDivisionError:
#     print("Деление на 0 невозможно")
#
#
#
#
#
# # Несколько видов ошибок
# try:
#     number = int(input("Введите число: "))
#     result = 10 / number
#
# except ValueError:
#     print("Вы ввелим не число")
#
# except ZeroDivisionError:
#     print("На 0 делить невозможно")
#
#
#
#
#
# # else и finally
# try:
#     number = int(input("Введите число: "))
# except ValueError:
#     print("Это не число")
# else:
#     print(f"Отлично, вы ввели {number}")  # выполнится, только если ошибки НЕ было
# finally:
#     print("Попытка ввода завершена")  # выполнится ВСЕГДА, была ошибка или нет
#
#
#
#
#
# # Цикл, который переспрашивает ввод, пока не получит корректные данные
# while True:
#     try:
#         age = int(input("Введите возраст: "))
#         break
#     except ValueError:
#         print("Нужно ввести число, попробуйте снова")







# ======================================================================
# Задание 1
# try:
#     num_one = int(input("Введите первое число: "))
#     num_two = int(input("Введите второе число: "))
#
#     result = num_one / num_two
#
#     print(result)
#
# except ZeroDivisionError:
#     print("На 0 делить невозможно!")
#
# except ValueError:
#     print("Введите число!")

# ======================================================================




# ======================================================================
# Задание 2
# def divide(a, b):
#     try:
#         return a / b
#
#     except ZeroDivisionError:
#         return "Деление на 0 невозможно!"
#
#
# print(divide(10, 0))
# print(divide(10, 5))

# ======================================================================




# ======================================================================
# Задание 3
# while True:
#     try:
#         number = int(input("Введите число: "))
#         break
#
#     except ValueError:
#         print("Нужно вести число!")


# ======================================================================





# ======================================================================
# Усложненное задание 1 "Обработка нескольких ошибок в словаре"
users = {"Egor": 25, "Anna": 30, "Mark": 17}

def get_user_status(users, name):
    try:
        if users[name] >= 18:
            return f"Пользователь {name} совершеннолетний - ему {users[name]} лет(года)"

        else:
            return f"Пользователь {name} несовершеннолетний - ему {users[name]} лет(года)"

    except KeyError:
        return "Пользователь не найден"

print(get_user_status(users, "Egor"))
print(get_user_status(users, "Mark"))
print(get_user_status(users, "ght"))
# ======================================================================





# ======================================================================
# Усложненное задание 2 "Безопасное чтение файла"
def read_file_safe(filename):
    try:
        with open(filename, "r") as file:
            return file.read()

    except FileNotFoundError:
        return "Файл не найден"

print(read_file_safe("notes.txt"))
print(read_file_safe("note.txt"))
# ======================================================================





# ======================================================================
# Усложненное задание 3 "Комбинация вложенных проверок"
numbers = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def safe_divide_list(numbers, divisor):
    numbers_list = []

    try:
        for num in numbers:
            result = num / divisor
            numbers_list.append(result)

        return numbers_list

    except ZeroDivisionError:
        print("На 0 делить невозможно")
        return numbers_list


print(safe_divide_list(numbers, 2))
print(safe_divide_list(numbers, 0))
# ======================================================================





# ======================================================================
# Усложненное задание 4 "Собственное заключение"
class InvalidAgeError(Exception):
    pass

def check_age(age):
    if age < 0 or age > 150:
        raise InvalidAgeError("Возраст меньше 0 или больше 150")

    else:
        return age



try:
    print(check_age(-10))
except InvalidAgeError as e:
    print(f"Ошибка: {e}")



try:
    print(check_age(1))
except InvalidAgeError as e:
    print(f"Ошибка: {e}")
# ======================================================================








