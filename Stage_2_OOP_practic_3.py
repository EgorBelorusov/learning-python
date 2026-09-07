# Задача 1 — Класс с боевой механикой
from os import name

from requests.packages import target


# class Character:
#     def __init__(self, name: str, attack_power: int):
#         self.name = name
#         self.hp = 100
#         self.attack_power = attack_power
#
#
#     def attack(self, target):
#         target.hp -= self.attack_power
#         return f"Нанесено {self.attack_power} ед. урона '{target.name}'. Осталось {target.hp} здоровья"
#
#
#
#     def is_alive(self):
#         return self.hp > 0
#
#
#
#
# warrior = Character(name="Воин", attack_power=20)
# monster = Character(name="Монстр", attack_power=30)
#
# while warrior.is_alive() and monster.is_alive():
#     print(warrior.attack(monster))
#     if monster.is_alive():
#         print(monster.attack(warrior))
#
# winner = warrior.name if warrior.is_alive() else monster.name
# print(f"Победитель: {winner}")









# Задача 2 — Полиморфизм в бою
from random import randint

class Character:
    def __init__(self, name: str, attack_power: int):
        self.name = name
        self.hp = 100
        self.attack_power = attack_power
        self.inventory = Inventory()


    def attack(self, target):
        target.hp -= self.attack_power
        return f"{self.name} нанес {self.attack_power} ед. урона '{target.name}'. Осталось {target.hp} здоровья"



    def is_alive(self):
        return self.hp > 0


    def use_item(self, item_name: str):
        for item in self.inventory.items:
            if item.name == item_name:
                self.attack_power += item.attack_bonus  # Исправлено: attack_bonus вместо bonus
                self.inventory.remove_item(item_name)
                print(f"{self.name} использовал {item_name}. Сила атаки увеличена на {item.attack_bonus}!")
                return
        print(f"Предмет {item_name} не найден в инвентаре")


class Warrior(Character):
    pass




class Mage(Character):
    def attack(self, target):
        damage = randint(0, self.attack_power)
        target.hp -= damage
        return f"{self.name} нанес {damage} ед. урона '{target.name}'. Осталось {target.hp} здоровья"









# Задача 3 Инвентарь
class Item:
    def __init__(self, name: str, value: int, attack_bonus: int):
        self.name = name
        self.value = value
        self.attack_bonus = attack_bonus


    def __str__(self):
        return f"''{self.name}'', цена: {self.value}, бонусный урон: {self.attack_bonus}"





class Inventory:
    def __init__(self):
        self.items = []


    def add_item(self, name: str, value: int, bonus: int):
        item_inventory = Item(name, value, bonus)
        self.items.append(item_inventory)

        return f"Предмет {item_inventory.name} добавлен в инвентарь"


    def remove_item(self, name):
        for item in self.items:
            if item.name == name:
                self.items.remove(item)
                return f"Предмет '{item.name}' был удалён из инвентаря"

        return f"Предмет не найден"



    def total_value(self):
        total = 0
        for item in self.items:
            total += item.value

        return f"Общая сумма всех предметов: {total}"


    def show_items(self):
        for num, item in enumerate(self.items):
            print(f"{num + 1}. {item}")

        return "Список выведен"









warrior = Warrior(name="Воин", attack_power=40)
mage = Mage(name="Маг", attack_power=60)
monster = Character(name="Монстр", attack_power=30)
monster.hp = 300
attackers = [warrior, mage]
print(warrior.inventory.show_items())
warrior.inventory.add_item("Меч", 50, 15)
warrior.use_item("Меч")
print(warrior.inventory.show_items())

while monster.is_alive() and any(a.is_alive() for a in attackers):

    for attacker in attackers:
        if attacker.is_alive() and monster.is_alive():
            print(attacker.attack(monster))

    if monster.is_alive():
        for attacker in attackers:
            if attacker.is_alive():
                print(monster.attack(attacker))
                break

winner = f"{monster.name} победил" if any(not a.is_alive() for a in attackers) else f"{warrior.name} и {mage.name} победили"
print(f"Победитель: {winner}")














warrior = Warrior(name="Воин", attack_power=40)

print(warrior.inventory.total_value())
print(warrior.inventory.show_items())
















