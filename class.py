
import random
import time
import threading
import keyboard
sick = 0
foodsupply = 0
death = 0
class pet():
    def __init__(self, name, food, water, hp):
        self.name = name
        self.food = food
        self.water = water
        self.hp = hp
    def addwater(self, water):
        self.water += water
        print(self.water)
    def health(self):
        if sick < 4:
            print("Healthy")
        else:
             print("Sick")

print("Welcome to this very cool pet game! Your goal is to make sure your pet survives as long as they can. They start with 10 food and 20 water. To view their stats, press q. To feed them food, press z. To give water, press x. If he gets sick, follow the doctors instructions to cure him. First name your pet to begin! ")
Name = input("Name your pet  ")
pet = pet(Name, 10, 20, 100)




def loop_hunger():
    while pet.food > 0:
        time.sleep(10)
        pet.food -= 1
        pet.hp -= 5
        print(f"Food: {pet.food}")
        if pet.food == 5:
            print(f"{pet.name} is hungry")
        elif pet.food == 2:
            print(f"{pet.name} is starving!!!")
        if pet.food == 0:
            print(f"{pet.name} starved to death. Game Over!")
            death = 1
        if pet.food == 25:
            print(f"{pet.name} died by diabetes. Game Over!")
            death = 1
    

def loop_thirst():
    while pet.water > 0:
        time.sleep(7)
        pet.water -= 1
        pet.hp -= 3
        print(f"Water: {pet.water}")
        if pet.water == 5:
            print(f"{pet.name} is thirsty")
        elif pet.water == 2:
            print(f"{pet.name} is very thirsty!!!")
        if pet.water == 0:
            print(f"{pet.name} was dehydrated. Game Over!")
            death = 1
        if pet.water == 25:
            print(f"{pet.name} was too hydrated. Game Over!")
            death = 1

def loop_health():
    while pet.hp > 0:
        time.sleep(7)
        sick = random.randint(3, 4)
        if sick == 4:
            inx = input(f"An Unknown Virus had entered {pet.name} body. Type pneumonoultramicroscopicsilicovolcanoconiosis to cure him                                          ")
            if "pneumonoultramicroscopicsilicovolcanoconiosis" in inx:
                sick = 0
                pet.hp += 10
            elif inx != "pneumonoultramicroscopicsilicovolcanoconiosis":
                print("Please type pneumonoultramicroscopicsilicovolcanoconiosis to cure your pet!!!")
       

def loop_sick():
    while pet.hp > 0:
        while sick == 4:
            pet.hp -= 5
            time.sleep(3)
            
def loop_hpcheck():
    while pet.hp > 0:
        if pet.hp < 1:
            print("Your pet died!!!")
            death = 1

def my_function():
    pet.food += 1
    print(f"You fed {pet.name} 1 food. Food: {pet.food}")
    pet.hp += 4
    time.sleep(3)

def my_function2():
    pet.water += 1
    print(f"You gave {pet.name} 1 water. Water: {pet.water}")
    pet.hp += 4
    time.sleep(3)

def my_function3():
    print(f"Food: {pet.food}, Water: {pet.water}, Hp: {pet.hp}")

keyboard.add_hotkey('z', my_function)
keyboard.add_hotkey('x', my_function2)
keyboard.add_hotkey('q', my_function3)

thread_hunger = threading.Thread(target=loop_hunger)
thread_thirst = threading.Thread(target=loop_thirst)
thread_health = threading.Thread(target=loop_health)
thread_hpcheck = threading.Thread(target=loop_hpcheck)
thread_sick = threading.Thread(target=loop_sick)
thread_hunger.start()
thread_thirst.start()
thread_health.start()
thread_hpcheck.start()
thread_sick.start()






