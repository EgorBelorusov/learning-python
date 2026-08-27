# Задание 1
# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#
#     def area(self):
#         return self.width * self.height
#
#
#
#     def perimeter(self):
#         return 2 * self.width + 2 * self.height
#
#
#
#     def __str__(self):
#         return f"Площадь прямоугольника равна {self.area()}; периметр прямоугольника равен {self.perimeter()}"
#
#
# rectangle1 = Rectangle(10, 5)
# rectangle2 = Rectangle(10, 15)
#
# print(rectangle1)
# print(rectangle2)
#
#
#
#
#
#
#
#
#
#
#
# # Задание 2
# from math import pi
#
# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
#
#
#     def area(self):
#          return pi * (self.radius ** 2)
#
#
#     def describe(self):
#         print(f"Круг радиусом {self.radius}, площадь {self.area():.1f}")
#
#
# circle1 = Circle(5)
#
# circle1.describe()







# Задание 3
# class Shape:
#     def __init__(self, base):
#         self.base = base
#
#
#     def area(self):
#         pass
#
#
#
#
# class Square(Shape):
#     def area(self):
#         return self.base * self.base
#
#
#     def __str__(self):
#         return f"Площадь квадрата равна {self.area()}"
#
#
#
#
# class Triangle(Shape):
#     def __init__(self, base, height):
#         super().__init__(base)
#         self.height = height
#
#
#     def area(self):
#         return 0.5 * self.base * self.height
#
#
#     def __str__(self):
#         return f"Площадь треугольника равна {self.area()}"
#
#
#
# square = Square(10)
# triangle = Triangle(6, 4)
#
# shape_list = [square, triangle]   # список ОБЪЕКТОВ, не строк
#
# for shape in shape_list:
#     print(shape)            # единообразный вызов, Python сам знает, какой area() вызвать





# Задание 4
# class Wallet:
#     def __init__(self):
#         self._balance = 0
#
#
#     @property
#     def balance(self):
#         return self._balance
#
#
#     def deposit(self, amount):
#         if amount < 1:
#             print("Пополнение должно быть не меньше 1")
#
#         else:
#             self._balance += amount
#             print(f"Счёт пополнен на {amount}. Ваш баланс: {self._balance}")
#
#
#
#     def withdraw(self, amount):
#         if amount > self._balance:
#             print("На счёте недостаточно средств")
#
#         elif amount < 1:
#             print("Невозможно снять меньше 1")
#
#         else:
#             self._balance -= amount
#             print(f"Снятие со счёта на сумму {amount}. Ваш баланс: {self._balance}")
#
#
#     def __str__(self):
#         return f"Ваш баланс: {self._balance}"
#
#
#
#
#
# wallet1 = Wallet()
#
# wallet1.deposit(2500)
#
# wallet1.withdraw(2400)
#
# print(wallet1)









# Задание 5 "to do list на ООП"
class Task:
    def __init__(self, text):
        self.text = text
        self.done = False


    def mark_done(self):
        self.done = True


    def __str__(self):
        if self.done:
            return f"{self.text} [x]"

        else:
            return f"{self.text} [-]"






class TaskList:
    def __init__(self, filename):
        self.filename = filename
        self.tasks = []


    def load_tasks(self):
        with open(self.filename, "r", encoding="utf-8") as file:
            lines = file.readlines()

        self.tasks = []
        for line in lines:
            clean_text = line.strip()
            task = Task(clean_text)
            self.tasks.append(task)

        return self.tasks


    def show_tasks(self):
        if self.tasks:
            for item, task in enumerate(self.tasks):
                print(f"{item + 1}. {task}")

            return "Список задач выведен"
        else:
            return "Список задач пуст"


    def add_task(self, text):
        full_text = text
        task = Task(full_text)
        self.tasks.append(task)

        with open(self.filename, "w", encoding="utf-8") as file:
            for obj in self.tasks:
                file.write(obj.text + '\n')

        return "Задача добавлена"


    def remove_task(self):
        if not self.tasks:
            return "Ошибка! Список задач пуст, удалять нечего."

        try:
            del_index = int(input("Введите номер задачи для удаления: ").strip())

            if del_index < 1 or del_index > len(self.tasks):
                return "Ошибка! Задачи с таким номером не существует."

            self.tasks.pop(del_index - 1)

            with open(self.filename, "w", encoding="utf-8") as file:
                for obj in self.tasks:
                    file.write(obj.text + "\n")

            return "Задача успешно удалена!"


        except ValueError:
            return "Ошибка! Введите корректное число (номер задачи)."






task_list = TaskList("todo.txt")

while True:

    print("\n ========== Список задач ========== \n")
    print("1 - Показать задачи")
    print("2 - Добавить задачу")
    print("3 - Удалить задачу")
    print("4 - Выйти")

    try:
        user_input = int(input("Введите номер команды: ").strip())

        if user_input == 1:
            task_list.load_tasks()
            print(task_list.show_tasks())

        elif user_input == 2:
            text_user = input("Введите задачу: ")
            print(task_list.add_task(text_user))

        elif user_input == 3:
            print(task_list.remove_task())

        else:
            break

    except ValueError:
        print("Ошибка! Введите верный номер команды")














