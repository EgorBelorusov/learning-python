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


print(0.1 + 0.2)


# Задание 2 "операции"
# print(f"Меня зовут {name}. Мне {age} лет. Мой рост {height} см.")

print(10 + 5)
print(10 - 5)
print(10 * 5)
print(10 / 5)
print(10 // 5)
print(10 % 5)
print(10 ** 5)
print(10 % 3)
print(10 % 1)

print("ad" * 3)


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
for i in range(1, 21):
    if i % 2 == 0:
        print(i)

# 1 вариант решения
number = ""
while number != 0:
    number = int(input("Введите число: "))
    if number == 0:
        break
    else:
        print(number)

# 2 вариант решения
while True:
    number = int(input("Введите число: "))
    if number == 0:
        break
    else:
        print(number)