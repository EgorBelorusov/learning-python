# Задача 1 — Класс с боевой механикой
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


    def attack(self, target):
        target.hp -= self.attack_power
        return f"{self.name} нанес {self.attack_power} ед. урона '{target.name}'. Осталось {target.hp} здоровья"



    def is_alive(self):
        return self.hp > 0




class Warrior(Character):
    pass




class Mage(Character):
    def attack(self, target):
        damage = randint(0, self.attack_power)
        target.hp -= damage
        return f"{self.name} нанес {damage} ед. урона '{target.name}'. Осталось {target.hp} здоровья"






warrior = Warrior(name="Воин", attack_power=40)
mage = Mage(name="Маг", attack_power=60)
monster = Character(name="Монстр", attack_power=30)
monster.hp = 300
attackers = [warrior, mage]


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















