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


# Задание 2
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


# Задание 3
# name = input("Введите имя: ")
# age = int(input("Введите возраст: "))
# height = float(input("Введите рост (см): "))
#
# print(f"Привет, меня зовут {name}. Мне {age} лет. Рост {height} см. Через 10 лет мне будет {age + 10}")

# Задание 4
user_age = int(input("Введите ваш возраст: "))

if user_age > 0 and user_age < 150:

    print("Возраcт введен корректно")

    if user_age < 18:
        print("Ты несовершеннолетний")
    elif 18 <= user_age <= 65:
        print("Ты взрослый")
    else:
        print("Ты пенсионер")

else:
    print("Проверьте введенные данные")

