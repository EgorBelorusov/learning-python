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
# try:
#     response = requests.get("https://jsonplaceholder.typicode.com/users/1",  timeout=5)
#     print(response.status_code)
#     data = response.json()
#     print(data["email"])
#     print(data["name"])
# except requests.exceptions.RequestException as e:
#     print(f"Ошибка запроса: {e}")
#
#
# try:
#     response = requests.get("https://jsonplaceholder.typicode.com/posts", timeout=5)
#     print(response.status_code)
#     data = response.json()
#     print(len(data))
# except requests.exceptions.RequestException as e:
#     print(f"Ошибка запроса: {e}")


# .json() — это метод объекта response, который автоматически берёт текст ответа и парсит его как JSON,
# возвращая уже готовый dict/list — экономит шаг по сравнению с ручным json.loads(response.text).



# Задание 2
# response = requests.get("https://api.open-meteo.com/v1/forecast", params={
#     "latitude": 52.52,
#     "longitude": 13.41,
#     "current": "temperature_2m",
#
# }, timeout=5)
# print(response.status_code)
# data = response.json()
# print(data["current"]["temperature_2m"])



import requests



def get_weather(name_city: str):

    try:
        geo_response = requests.get(
            "https://geocoding-api.open-meteo.com/v1/search",
            params={"name": name_city, "count": 1},
            timeout=5
        )

        geo_data = geo_response.json()

        if not geo_data.get("results"):
            return "Город не найден"

        latitude = geo_data["results"][0]["latitude"]
        longitude = geo_data["results"][0]["longitude"]


        # Шаг 2: получить погоду по этим координатам
        weather_response = requests.get(
            "https://api.open-meteo.com/v1/forecast",
            params={"latitude": latitude, "longitude": longitude, "current": ["temperature_2m", "wind_speed_10m"]},
            timeout=5
        )
        weather_data = weather_response.json()

        temp = weather_data["current"]["temperature_2m"]
        wind = weather_data["current"]["wind_speed_10m"]
        return f"В городе {name_city}: температура {temp} градусов, ветер {wind} м/сек"

    except requests.exceptions.RequestException as e:
        return f"Ошибка запроса: {e}"

print(get_weather("Riga"))










