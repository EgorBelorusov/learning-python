# Тема "HTTP-запросы через requests"
# Базовый GET-запрос — получение данных с сервера
import requests

# response = requests.get("https://api.github.com")
# print(response.status_code)
# print(response.text)
#
#
#
#
#
# response = requests.get("https://api.github.com")
# data = response.json()
# print(data["current_user_url"])
#
#
#
#
# # Передача параметров в запрос
# params = {"q": "python", "sort": "stars"}
# response = requests.get("https://api.github.com/search/repositories", params = params)
#
#
#
#
# # Обработка ошибок при запросах — важная практика
# try:
#     response = requests.get("https://api.example.com/data", timeout=5)
#     response.raise_for_status()   # вызовет исключение, если код ответа НЕ 200-299
#     data = response.json()
# except requests.exceptions.RequestException as e:
#     print(f"Ошибка запроса: {e}")






# Задание — поработаем с бесплатным публичным API, не требующим регистрации/ключа
try:
    response = requests.get("https://jsonplaceholder.typicode.com/users/1",  timeout=5)
    print(response.status_code)
    data = response.json()
    print(data["email"])
    print(data["name"])
except requests.exceptions.RequestException as e:
    print(f"Ошибка запроса: {e}")


try:
    response = requests.get("https://jsonplaceholder.typicode.com/posts", timeout=5)
    print(response.status_code)
    data = response.json()
    print(len(data))
except requests.exceptions.RequestException as e:
    print(f"Ошибка запроса: {e}")





