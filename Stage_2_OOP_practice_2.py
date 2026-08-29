# Задание практики № 2 "Программа учета/создания книг и фильмов"
class Media:
    def __init__(self, title):
        self.title = title
        self.is_finished = False


    def make_finished(self):
        self.is_finished = True





class Book(Media):
    def __init__(self, title, author, pages):
        super().__init__(title)
        self.author = author
        self.pages = pages


    def __str__(self):
        if self.is_finished:
            return f"Книга '{self.title}', написанная {self.author}, имеет {self.pages} страниц(-ы). Статус: прочитано"

        else:
            return f"Книга '{self.title}', написанная {self.author}, имеет {self.pages} страниц(-ы). Статус: не прочитано"





class Movie(Media):
    def __init__(self, title, director, duration):
        super().__init__(title)
        self.director = director
        self.duration = duration


    def __str__(self):
        if self.is_finished:
            return f"Фильм '{self.title}', снятый {self.director}, продолжительностью {self.duration} минут. Статус: просмотрено"

        else:
            return f"Фильм '{self.title}', снятый {self.director}, продолжительностью {self.duration} минут. Статус: не просмотрено"





class MediaList:
    def __init__(self):
        self.items = []


    def add_book(self, title, author, pages):
        book = Book(title, author, pages)
        self.items.append(book)
        print("Книга добавлена")


    def add_movie(self, title, director, duration):
        movie = Movie(title, director, duration)
        self.items.append(movie)
        print("Фильм добавлен")


    def show_all(self):
        if self.items:
            for item, obj in enumerate(self.items):
                print(f"{item + 1}. {obj}")

        else:
            print("Список пуст")


    def mark_finished(self, number: int):
        if number < 1 or number > len(self.items):
            print("Такого номера нет в списке!")
        else:
            clean_number = number - 1
            item = self.items[clean_number]
            item.make_finished()





media_list = MediaList()

while True:

    print("\n ========== Список задач ========== \n")
    print("1 - Показать всё")
    print("2 - Добавить книгу")
    print("3 - Добавить фильм")
    print("4 - Отметить как просмотрено/прочитано")
    print("5 - Выйти")

    try:
        user_input = int(input("Введите номер команды: ").strip())

        if user_input == 1:
            media_list.show_all()

        elif user_input == 2:
            title_book = input("Введите название книги: ").strip()
            author = input("Введите автора: ").strip()
            pages = int(input("Количество страниц: ").strip())

            media_list.add_book(title_book, author, pages)


        elif user_input == 3:
            title_movie = input("Введите название фильма: ").strip()
            director = input("Введите режиссера: ").strip()
            duration = int(input("Введите длительность: ").strip())

            media_list.add_movie(title_movie, director, duration)



        elif user_input == 4:
            num_user = int(input("Введите номер книги/фильма: "))
            media_list.mark_finished(num_user)





        else:
            break

    except ValueError:
        print("Ошибка! Введите верный номер команды")






















