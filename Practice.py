# Мини-проект "Угадай число"
from random import randint

number_randint = randint(1, 100)
try_flag = 0
print("Загадал число от 1 до 100. Попробуй отгадать!")

while True:
    try_flag += 1
    try:
        user_input = int(input("Угадайте число: "))

        if user_input in range(1, 101):

            if user_input == number_randint:
                print("Поздравляю, Вы угадали число!")
                print(f"Количество попыток: {try_flag}")
                break

            elif user_input > number_randint:
                print("Меньше")


            else:
                print("Больше")

        else:
            print("Вы ввели число за пределами диапазона от 1 до 100. Попробуйте снова.")

    except ValueError:
        print("Ошибка! Необходимо ввести число!")







































