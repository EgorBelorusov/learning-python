# Тема "SQLite"
# SQLite — это "облегчённая" база данных, которая хранится в одном файле на диске (например, database.db),
# без необходимости устанавливать и запускать отдельный сервер базы данных

import sqlite3

from urllib3.contrib.emscripten import connection


# connection = sqlite3.connect("database.db") # если файла нет — создастся новый
# cursor = connection.cursor() # "курсор" — инструмент для выполнения запросов
#
# cursor.execute("""
#         CREATE TABLE IF NOT EXISTS books (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             title TEXT,
#             author TEXT,
#             pages INTEGER,
#             is_read INTEGER
#         )
# """)
#
# connection.commit() # сохраняет изменения на диск
#
#
# # connection — соединение с файлом базы данных (аналог with open(...), только для БД)
# # cursor — объект, через который вы выполняете SQL-запросы (cursor.execute(...))
# # CREATE TABLE IF NOT EXISTS — создаёт таблицу, только если её ещё нет (чтобы не было ошибки при повторном запуске программы)
# # INTEGER PRIMARY KEY AUTOINCREMENT — специальный столбец id, который автоматически увеличивается на 1 для каждой новой записи
# # connection.commit() — обязательный шаг после любого изменения данных (INSERT/UPDATE/DELETE) — без него изменения не сохранятся на диск, останутся только "в памяти" текущего сеанса
#
#
#
# # Выполнение запросов с параметрами
# cursor.execute("INSERT INTO books (title, author, pages, is_read) VALUES (?, ?, ?, ?)", ("Война и мир", "Толстой", 1225, 0))
# connection.commit()
#
#
# # Обратите внимание на ? вместо того, чтобы вставлять значения прямо в текст запроса через f-строку.
# # Это принципиально важно — использование ? и передача значений отдельно, вторым аргументом, защищает от
# # SQL-инъекций (атаки, когда злоумышленник вставляет вредоносный SQL-код через обычное поле ввода,
# # если бы вы наивно строили запрос через f-строку с пользовательским вводом). Это тот случай,
# # когда "удобный" способ (f-строка) — потенциально опасный, и профессионалы всегда используют параметризованные запросы через ?.
#
#
# cursor.execute("SELECT * FROM books WHERE is_read = 0")
# result = cursor.fetchall() # получить ВСЕ подходящие строки как список кортежей
# for row in result:
#     print(row) # каждая row — это кортеж, например (1, 'Война и мир', 'Толстой', 1225, 0)
#
#
#
# #fetchall() — возвращает все найденные строки сразу, как список кортежей (вспомните тему кортежей — здесь они используются именно
# # потому, что запись из базы данных логически неизменяема, это просто "снимок" данных на момент запроса).
#
# # Закрытие соединения — по аналогии с закрытием файлов
# connection.close()






# Задание
# data = sqlite3.connect("library.db")
# cursors = data.cursor()
# cursors.execute("""
#         CREATE TABLE IF NOT EXISTS books (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             title TEXT,
#             pages INTEGER,
#             author TEXT,
#             is_read INTEGER
#         )
#     """)
#
# cursors.execute("INSERT INTO books (title, pages, author, is_read) VALUES (?, ?, ?, ?)", ("Книга 1", 100, "Иванов", 0))
# cursors.execute("INSERT INTO books (title, pages, author, is_read) VALUES (?, ?, ?, ?)", ("Книга 2", 200, "Петров", 1))
# cursors.execute("INSERT INTO books (title, pages, author, is_read) VALUES (?, ?, ?, ?)", ("Книга 3", 300, "Шишкин", 0))
# data.commit()
#
# cursors.execute("SELECT * FROM books")
# final = cursors.fetchall()
# for row in final:
#     print(row)
#
# cursors.execute("UPDATE books SET is_read = 1 WHERE id = 1")
# data.commit()
# cursors.execute("SELECT * FROM books WHERE is_read = 0")
# fin = cursors.fetchall()
# for row in fin:
#     print(row)






# Практика Задание 1
# connection = sqlite3.connect("dataBase.db")
# cursor = connection.cursor()
# cursor.execute("""
#     CREATE TABLE IF NOT EXISTS students (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         name TEXT,
#         grade INTEGER
#     )
#
# """)
#
# cursor.execute("INSERT INTO students (name, grade) VALUES (?, ?)", ("Миша", 4))
# cursor.execute("INSERT INTO students (name, grade) VALUES (?, ?)", ("Саша", 5))
# cursor.execute("INSERT INTO students (name, grade) VALUES (?, ?)", ("Егор", 5))
# cursor.execute("INSERT INTO students (name, grade) VALUES (?, ?)", ("Лена", 3))
# cursor.execute("INSERT INTO students (name, grade) VALUES (?, ?)", ("Злата", 2))
# connection.commit()
#
# cursor.execute("SELECT * FROM students ORDER BY grade DESC")
# data = cursor.fetchall()
#
# for i in data:
#     print(i)





# Задание 2
# connection = sqlite3.connect("booksBase.db")
# cursor = connection.cursor()
#
# cursor.execute("""
#     CREATE TABLE IF NOT EXISTS authors (
#          id INTEGER PRIMARY KEY AUTOINCREMENT,
#          name TEXT
#     )
#
# """)
#
# cursor.execute("""
#     CREATE TABLE IF NOT EXISTS books (
#          id INTEGER PRIMARY KEY AUTOINCREMENT,
#          title TEXT,
#          author_id INTEGER,
#          FOREIGN KEY (author_id) REFERENCES author(id)
#     )
#
# """)
#
#
# cursor.execute("INSERT INTO authors (name) VALUES (?)", ("Петров",))
# cursor.execute("INSERT INTO authors (name) VALUES (?)", ("Васильков",))
# cursor.execute("INSERT INTO authors (name) VALUES (?)", ("Сидоров",))
#
# cursor.execute("INSERT INTO books (title, author_id) VALUES (?, ?)", ("Книга 1", 1))
# cursor.execute("INSERT INTO books (title, author_id) VALUES (?, ?)", ("Книга 2", 2))
# cursor.execute("INSERT INTO books (title, author_id) VALUES (?, ?)", ("Книга 3", 2))
# cursor.execute("INSERT INTO books (title, author_id) VALUES (?, ?)", ("Книга 4", 3))
#
# connection.commit()
#
# cursor.execute("SELECT books.title, authors.name FROM books JOIN authors ON authors.id = books.author_id")
# connection.commit()
#
# data = cursor.fetchall()
# for i in data:
#     print(i)





# Задание 3
class BookDatabase:
    def __init__(self):
        self.connection = sqlite3.connect("BookBase.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT,
                author TEXT,
                pages INTEGER,
                is_read INTEGER
            )
        """)
        self.connection.commit()


    def add_book(self, title: str, author: str, pages: int, is_read = 0):
        self.cursor.execute("INSERT INTO books (title, author, pages, is_read) VALUES (?, ?, ?, ?)", (title, author, pages, is_read))
        self.connection.commit()




    def get_all_books(self):
        self.cursor.execute("SELECT * FROM books")
        elements = self.cursor.fetchall()
        for i in elements:
            print(i)




    def mark_as_read(self, book_id: int):
        self.cursor.execute("UPDATE books SET is_read = 1 WHERE id = ?", (book_id,))
        self.connection.commit()

















