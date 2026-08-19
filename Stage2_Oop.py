# Этап 2. ООП, классы, объекты, атрибуты, методы
from symtable import Class

# class Dog: # объявление класса
#     def __init__(self, name, age):  # конструктор
#         self.name = name  # создаёт атрибут
#         self.age = age  # создаёт атрибут
#
#     def bark(self):
#         print(f"{self.name} говорит: Гав!")
#
#
#
# dog1 = Dog("Рекс", 3)
#
# dog1.bark()
# print(dog1.name)




# =======================================================
# Задание 1
# class Book:
#     def __init__(self, title, author, pages):
#         self.title = title
#         self.author = author
#         self.pages = pages
#
#
#     def describe(self):
#         print(f"Книга автора {self.author} под названием '{self.title}', размером {self.pages} листов")
#
#
#
#
# book1 = Book("Что-то там", "Иванова И. И.", 150)
# book2 = Book("Война и мир", "Толстой", 1225)
#
# book1.describe()
# book2.describe()





# ==========================================================================================================================================
# ==========================================================================================================================================
# Атрибуты объекта vs атрибуты класса
# ==========================================================================================================================================
# ==========================================================================================================================================






# Атрибуты класса (class attributes) — значение, которое общее для всех объектов этого класса
# class Book:
#     library_name = "Городская библиотека"  # атрибут класса — общий для всех книг
#
#     def __init__(self, title, author, pages):
#         self.title = title      # атрибут объекта — свой у каждой книги
#         self.author = author
#         self.pages = pages





# Методы, изменяющие состояние объекта
# class Book:
#     def __init__(self, title, author, pages):
#         self.title = title
#         self.author = author
#         self.pages = pages
#         self.current_page = 0        # новый атрибут — сколько страниц уже прочитано
#
#     def read(self, pages_read):
#         self.current_page += pages_read
#         print(f"Прочитано {self.current_page} из {self.pages} страниц")
#
#
#
#
#
# book1 = Book("Книга1", "Толстой", 100)
#
# book1.read(1)
# book1.read(5)
# book1.read(70)




# Магический метод __str__ — как объект выглядит при печати
# class Book:
#     def __init__(self, title, author, pages):
#         self.title = title
#         self.author = author
#         self.pages = pages
#
#     def __str__(self): # метод красиво выводит объект
#         return f"«{self.title}» — {self.author}, {self.pages} стр."
#
#
#
# book3 = Book("Книга1", "Толстой", 100)
# print(book3)






# Задание 1
# class Book:
#     library_name = "Школьная библиотека"
#
#     def __init__(self, title, author, pages):
#         self.title = title
#         self.author = author
#         self.pages = pages
#         self.current_page = 0
#
#     def read(self, page_read):
#         self.current_page += page_read
#         print(f"Прочитано {self.current_page} из {self.pages}")
#
#     def __str__(self):
#         return f"Книга автора {self.author} под названием '{self.title}', размером {self.pages} листов"
#
#
#
#
# book1 = Book("Что-то там", "Иванова И. И.", 150)
# book2 = Book("Война и мир", "Толстой", 1225)
#
# book2.read(30)
# book2.read(10)
#
# print(book2)





# ==========================================================================================================================================
# ==========================================================================================================================================
# Наследование — переиспользование и расширение классов
# ==========================================================================================================================================
# ==========================================================================================================================================






# class Animal:
#     def __init__(self, name):
#         self.name = name
#
#     def make_sound(self):
#         print(f"{self.name} издаёт какой-то звук")
#
#
#
# class Dog(Animal): # Dog (дочерний класс) наследует Animal (Animal родительский класс)
#     def __init__(self, name, breed):
#         super().__init__(name) # вызываем __init__ родителя, чтобы не дублировать self.name = name
#         self.breed = breed
#
#
#     def make_sound(self): # переопределение метода - замена родительского метода на метод дочернего класса
#         print(f"{self.name} говорит: Гав!")
#
#
#
# class Cat(Animal):
#     def make_sound(self):
#         print(f"{self.name} говорит: Мяу!")
#
#
#
# dog = Dog("Норик", "дворняга")
# cat = Cat("Барсик")
#
# dog.make_sound()
# cat.make_sound()




# Задание 1
# class Vehicle:
#     def __init__(self, brand):
#         self.brand = brand
#         self.speed = 0
#
#
#     def accelerate(self, increment):
#         self.speed += increment
#         print(f"Текущая скорость {self.brand} {self.speed} км/ч")
#
#
#
#
#
# class Car(Vehicle):
#     def __init__(self, brand, fuel_type):
#         super().__init__(brand)
#         self.fuel_type = fuel_type
#
#
#     def accelerate(self, increment):
#         super().accelerate(increment)
#         print(f"Двигатель в обзоре!")
#
#
#
#
#
# class Bicycle(Vehicle):
#     pass
#
#
#
#
# vehicle = Vehicle("Нисан")
# car = Car("Toyota", "Дизель")
# bicycle = Bicycle("Велик")
#
#
# vehicle.accelerate(20)
# vehicle.accelerate(20)
#
# car.accelerate(120)
# car.accelerate(30)
#
# bicycle.accelerate(15)
# bicycle.accelerate(15)





# ==========================================================================================================================================
# ==========================================================================================================================================
# Инкапсуляция — сокрытие внутренних деталей объекта
# ==========================================================================================================================================
# ==========================================================================================================================================





# class Book:
#     library_name = "Школьная библиотека"
#
#     def __init__(self, title, author, pages):
#         self.title = title
#         self.author = author
#         self.pages = pages
#         self.current_page = 0
#
#
#
#     @property # геттер, читает значения
#     def pages(self):
#         return self._pages
#
#     @pages.setter # сеттер. изменяет значение с проверкой
#     def pages(self, value):
#         if value <= 0:
#             print("Количество страниц не может быть меньше 1")
#         else:
#             self._pages = value
#
#     def read(self, page_read):
#         self.current_page += page_read
#         print(f"Прочитано {self.current_page} из {self.pages}")
#
#     def __str__(self):
#         return f"Книга автора {self.author} под названием '{self.title}', размером {self.pages} листов"
#
#
#
#
#
#
# book1 = Book("Что-то там", "Иванова И. И.", 150)
# book2 = Book("Война и мир", "Толстой", 1225)
#
# book1.pages = 0
#
# print(book1.pages)
#
# book2.read(30)
# book2.read(10)
#
# print(book2)





# ==========================================================================================================================================
# ==========================================================================================================================================
# datetime— работа с датами и временем
# ==========================================================================================================================================
# ==========================================================================================================================================




# получение текущей даты
from datetime import datetime, timedelta
#
#
# now = datetime.now()
# print(now)
# print(now.year)    # 2026
# print(now.month)   # 8
# print(now.day)     # 18
# print(now.hour)    # 14
# print(now.minute)  # 32
#
#
# # создание даты вручную
# birthday = datetime(2002, 12, 12)
#
#
# # форматирование даты в красивую форму
# print(now.strftime("%d.%m.%Y"))       # "18.08.2026"
# print(now.strftime("%H:%M"))           # "14:32"
# print(now.strftime("%d %B %Y, %A"))   # "18 August 2026, Tuesday"
#
#
# #
# today = datetime.now()
# deadline = datetime(2026,12, 31)
#
# diff = deadline - today
# print(diff.days)
#
# tomorrow = today + timedelta(days=1)  # прибавить 1 день
# next_week = today + timedelta(weeks=1)
#
#
#
#
# # Регулярные выражения (regex)
import  re
from unittest import result

#
# text = "мой номер: 58679376"
# result = re.search(r"\d+", text)
#
# if result:
#     print(result.group())
#
#
#
# # re.findall()— найти совпадение ВСЕ, причем не только первое
# text = "Телефоны: 89261234567 и 89007654321"
# numbers = re.findall(r"\d+", text)
# print(numbers)  # ['89261234567', '89007654321']
#
#
# # re.match()для простой валидации
# email = "test@example.com"
# if re.match(r"^\w+@\w+\.\w+$", email):
#     print("Похоже на email")




# Задание 1
time_now = datetime.now()

print(time_now)
print(time_now.strftime("%d.%m.%Y.%H:%M"))


# Задание 2
today = datetime.now()
new_year = datetime(today.year, 12, 31)

difference = new_year - today

print(difference.days)



# Задание 3
text = "Мне 25 лет, у меня 3 кота и 100 рублей"

result = re.findall(r"\d+", text)

print(result)


# Задание 4
email = "user@mail.com"

if re.match(r"^\w+@\w+\.\w+$", email):
    print("Похоже на email")





