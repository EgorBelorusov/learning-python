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
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages


    def describe(self):
        print(f"Книга автора {self.author} под названием '{self.title}', размером {self.pages} листов")




book1 = Book("Что-то там", "Иванова И. И.", 150)
book2 = Book("Война и мир", "Толстой", 1225)

book1.describe()
book2.describe()




