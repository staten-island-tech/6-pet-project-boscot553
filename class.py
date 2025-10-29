
import random
import time
import threading

sick = random.randint(0, 4)
foodsupply = 0
death = 0
class pet():
    def __init__(self, name, food, water):
        self.name = name
        self.food = food
        self.water = water
    def addfood(self, food):
        if foodsupply > food:
            self.food += food
            foodsupply -= food
            print(f"You fed {pet.name} {food} food")
        elif foodsupply < food:
            print("Insuffieient amount of food. Spam E to get food.")
    def addwater(self, water):
        self.water += water
        print(self.water)
    def health(self):
        if sick < 4:
            print("Healthy")
        else:
             print("Sick")

Name = input("Name your pet  ")
pet = pet(Name, 10, 20)

def loop_hunger():
    while pet.food > 0:
        time.sleep(10)
        pet.food -= 1
        print(f"Food: {pet.food}")
        if pet.food == 5:
            print(f"{pet.name} is hungry")
        elif pet.food == 2:
            print(f"{pet.name} is starving!!!")
    print(f"{pet.name} starved to death. Game Over!")


def loop_thirst():
    while pet.water > 0:
        time.sleep(7)
        pet.water -= 1
        print(f"Water: {pet.water}")
        if pet.water == 5:
            print(f"{pet.name} is thirsty")
        elif pet.water == 2:
            print(f"{pet.name} is very thirsty!!!")
    print(f"{pet.name} was dehydrated. Game Over!")




thread_hunger = threading.Thread(target=loop_hunger)
thread_thirst = threading.Thread(target=loop_thirst)


thread_hunger.start()
thread_thirst.start()
if input == 'z':
    print("z")
    




