# Этап 2. ООП, классы, объекты, атрибуты, методы
from symtable import Class

class Dog: # объявление класса
    def __init__(self, name, age):  # конструктор
        self.name = name  # создаёт атрибут
        self.age = age  # создаёт атрибут

    def bark(self):
        print(f"{self.name} говорит: Гав!")



dog1 = Dog("Рекс", 3)

dog1.bark()
print(dog1.name)




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





# Атрибуты объекта vs атрибуты класса
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
class Book:
    library_name = "Школьная библиотека"

    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
        self.current_page = 0

    def read(self, page_read):
        self.current_page += page_read
        print(f"Прочитано {self.current_page} из {self.pages}")

    def __str__(self):
        return f"Книга автора {self.author} под названием '{self.title}', размером {self.pages} листов"




book1 = Book("Что-то там", "Иванова И. И.", 150)
book2 = Book("Война и мир", "Толстой", 1225)

book2.read(30)
book2.read(10)

print(book2)

