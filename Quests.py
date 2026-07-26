

# Блок 1. Строки
# Задача 1.1 — Палиндром
# words_user = input("Введите слово: ").strip().lower()
#
# if words_user[::-1] == words_user:
#     print("Слово является палиндромом")
#
# else:
#     print("Слово не является палиндромом")





# Задача 1.2 — Подсчёт слов
# words_user = input("Введите предложение:").strip().split()
# quantity = len(words_user)
# print(f"В предложении {quantity} слов(-а)")





# Задача 2.1 — Сумма и среднее
# numbers = [4, 8, 15, 16, 23, 42]
# total = 0
#
# for i in numbers:
#     total += i
#
# avg = total / len(numbers)
# print(f"Сумма равна {total}. Среднее арифметическое равно {avg}")




# Задача 2.2 — Второй по величине
# numbers = [4, 8, 15, 16, 23, 42, 2, 30, 50, 0]
# biggest_one = float('-inf')
# biggest_two = float('-inf')
#
# for num in numbers:
#     if num > biggest_one:
#         biggest_two = biggest_one
#         biggest_one = num
#
#     elif biggest_one > num > biggest_two:
#         biggest_two = num
#
#
# print(f"Первое по величине число {biggest_one}")
# print(f"Второе по величине число {biggest_two}")




# Задача 3.1 — Подсчёт частоты букв
# word_user = input("Введите слово: ").strip().lower()
# word_dict = {}
#
# for i in word_user:
#     if i in word_dict:
#         word_dict[i] += 1
#
#     else:
#         word_dict[i] = 1
#
#
# print(word_dict)




# Задача 4.1 — Общие элементы
# goods_one = ["виноград", "яблоки", "сливы", "апельсины"]
# goods_two = ["черешня", "яблоки", "персики", "апельсины"]
#
# for i in goods_one:
#     for j in goods_two:
#         if i == j:
#             print(i)















