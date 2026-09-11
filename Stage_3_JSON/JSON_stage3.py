# Модуль json — преобразование между Python-объектами и JSON
import json
#
# data = {"name": "Егор", "age": 23}
#
# json_string = json.dumps(data) # превращает Python-объект в JSON-строку
#
# print(json_string)
#
# pythin_object = json.loads(json_string) # JSON строка → Python dict
#
# print(pythin_object["name"])
#
#
#
#
#
# # Работа с JSON-файлами напрямую
# with open("data.json", "w", encoding="utf-8") as file:
#     json.dump(data, file, ensure_ascii=False, indent=4)
#
#
# with open("data.json", "r", encoding="utf-8") as file:
#     loaded_data = json.load(file)




# Задание 1
character = {"name": "Воин", "hp": 100, "attack_power": 25}

json_str = json.dumps(character, ensure_ascii=False, indent=4) # преобразуем в json-строку
print(json_str)


with open("character.json", "w", encoding="utf-8") as file:
    json.dump(character, file, ensure_ascii=False, indent=4)


with open("character.json", "r", encoding="utf-8") as file:
    character_load = json.load(file)

print(character_load["name"])















