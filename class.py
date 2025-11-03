
import random
import time
import threading
import keyboard
sick = 0
foodsupply = 0
death = 0
class pet():
    def __init__(self, name, food, water, happiness, hp):
        self.name = name
        self.food = food
        self.water = water
        self.happiness = happiness
        self.hp = hp
    def addwater(self, water):
        self.water += water
        print(self.water)
    def health(self):
        if sick < 4:
            print("Healthy")
        else:
             print("Sick")

print("Welcome to this very cool pet game! Your goal is to make sure your pet survives as long as they can. They start with 10 food and 20 water. To view their stats, press q. To feed them food, press z. To give water, press x. Keep your pet happy by playing with it. Press p to play with it or l to take it for a walk. Keep in mind that your pet may get sick from time to time. First name your pet to begin! ")
Name = input("Name your pet  ")
pet = pet(Name, 15, 20, 100, 100)




def loop_hunger():
    while pet.hp > 0:
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
        if pet.food > 30:
            print(f"{pet.name} died by diabetes. Game Over!")
            death = 1
    

def loop_thirst():
    while pet.hp > 0:
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
        if pet.water > 30:
            print(f"{pet.name} was too hydrated. Game Over!")
            death = 1

def loop_health():
    while pet.hp > 0:
        time.sleep(3)
        sick = random.randint(1, 6)
        d = random.randint(1, 20)
        if sick == 4:
            print(f"{pet.name} got sick. -{d} hp")
            pet.hp -= d
            sick = 0
            
def loop_hpcheck():
    while pet.hp > 0:
        if pet.hp < 1:
            print("Your pet died!!!")
            death = 1

def loop_mood():
    while pet.hp > 0:
        time.sleep(2)
        pet.happiness -= 1
        if pet.happiness == 30:
            print(f"{pet.name} is bored")
        elif pet.happiness == 10:
            print(f"{pet.name} is @#!@$&*")
        elif pet.happiness == 50:
            print(f"{pet.name} is neutral")
        elif pet.happiness == 0:
            print(f"{pet.name} fell from a high place. Game Over!")
            pet.hp = 0
def loop_event():
    while pet.hp > 0:
        time.sleep(15)
        r = random.randint(1, 8)
        if r == 1:
            print(f"{pet.name} accidentally ate a piece of chcolate. Chocolate is like poison to dogs. -20 hp but +3 food")
            pet.food += 3
            pet.hp -= 20
        elif r == 2:
            print(f"{pet.name} found a mysterious mushroom. He ate it and gained 50 hp.")
            pet.hp += 50
        elif r == 3:
            print(f"{pet.name} got into a fight with a dog. -10 hp")
            pet.hp -= 10
        elif r == 4:
            print(f"{pet.name} got hit by a recless driver. -40 hp")
            pet.hp -= 80
        elif r == 5:
            print(f"You won the lottery. You buy {pet.name} food. Max food + Max Water")
            pet.food = 25
            pet.water = 25
        elif r == 6:
            print(f"{pet.name} got hit by a meteor. -50 hp")
            pet.hp -= 50
        elif r == 7:
            print(f"{pet.name} got struck by lightning. -10 hp but +20 happiness")
            pet.happiness += 20
            pet.hp -= 10
        elif r == 8:
            print(f"{pet.name} found a potion of instant health. +90 hp")
            pet.hp -= 90

def my_function():
    pet.food += 1
    print(f"You fed {pet.name} 1 food. Food: {pet.food}")
    pet.hp += 4
    time.sleep(2)

def my_function2():
    pet.water += 1
    print(f"You gave {pet.name} 1 water. Water: {pet.water}")
    pet.hp += 4
    time.sleep(0.5)

def my_function3():
    print(f"Food: {pet.food}, Water: {pet.water}, Happiness: {pet.happiness}, Hp: {pet.hp}")

def my_function4():
    pet.happiness += 10
    pet.food -= 3
    pet.water -= 5
    pet.hp += 5

def my_function5():
    pet.happiness += 20
    pet.food -= 5
    pet.water -= 8
    pet.hp += 5

keyboard.add_hotkey('z', my_function)
keyboard.add_hotkey('x', my_function2)
keyboard.add_hotkey('q', my_function3)
keyboard.add_hotkey('p', my_function4)
keyboard.add_hotkey('l', my_function5)

thread_hunger = threading.Thread(target=loop_hunger)
thread_thirst = threading.Thread(target=loop_thirst)
thread_health = threading.Thread(target=loop_health)
thread_hpcheck = threading.Thread(target=loop_hpcheck)
thread_mood = threading.Thread(target=loop_mood)
thread_hunger.start()
thread_thirst.start()
thread_health.start()
thread_hpcheck.start()
thread_mood.start()






