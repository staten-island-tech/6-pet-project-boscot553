
import random
import time
import threading
import keyboard
sick = 0
foodsupply = 0
death = 0
class pet():
    def __init__(self, name, food, water):
        self.name = name
        self.food = food
        self.water = water
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

def loop_health():
    while death != 1:
        time.sleep(7)
        sick = random.randint(0, 4)
        if sick == 4:
            inx = input(f"{pet.name} is sick. Type pneumonoultramicroscopicsilicovolcanoconiosis to cure him")
            


thread_hunger = threading.Thread(target=loop_hunger)
thread_thirst = threading.Thread(target=loop_thirst)


thread_hunger.start()
thread_thirst.start()

def my_function():
    pet.food += 1
    print(f"You fed {pet.name} 1 food")
    time.sleep(3)

def my_function2():
    pet.water += 1
    print(f"You gave {pet.name} 1 water")
    time.sleep(3)

keyboard.add_hotkey('z', my_function)


keyboard.add_hotkey('x', my_function2)
keyboard.wait('esc')

if death == 1:
    pet.water = 0
    pet.food = 0




