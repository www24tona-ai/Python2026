import random

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.skills = 1
        self.money = 400

    def info(self):
        print(f"Hi my name is {self.name} and I am {self.age} years old.")
        print(f"Skills: {self.skills}")
        print(f"Money: {self.money}")

    def study(self):
        self.skills += 1
        print("time to stydy")

    def chill(self):
        self.money -= random.randint(20, 100)
        print("time to chill")

    def work(self):
        self.money += 100 + random.randint(0 ,  100)
        print("hard working")


vasya = Person("Vasya", 15)
ivan = Person("Ivan", 16)

vasya.info()
ivan.info()

for day in range(366):
    vasya_choice = random.randint(1, 3)

    if vasya_choice == 1:
        vasya.study()
    if vasya_choice == 2:
        vasya.chill()
    if vasya_choice == 3:
        vasya.work()

vasya.age += 1
vasya.info()

for day in range(366):
    ivan_choice = random.randint(1, 3)

    if ivan_choice == 1:
        ivan.study()
    if ivan_choice == 2:
        ivan.chill()
    if ivan_choice == 3:
        ivan.work()

ivan.age += 1
ivan.info()
