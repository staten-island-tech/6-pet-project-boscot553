import random
import time
import threading
import keyboard
sick = 0
foodsupply = 2
useless_variable = 0
class pet():
    def __init__(self, name, food, water, happiness, sanitation, hp):
        self.name = name
        self.food = food
        self.water = water
        self.happiness = happiness
        self.sanitation = sanitation
        self.hp = hp
    def loop_hunger(self, water):
        self.water += water
        print(self.water)
    def health(self):
        if sick < 4:
            print("Healthy")
        else:
             print("Sick")
    def feed(self):
        if self.hp > 0:
            self.food += 1
            print(f"You fed {self.name} 1 food. Food: {self.food}")
            self.hp += 2
            time.sleep(foodsupply)
    def drink(self):
        if self.hp > 0:
            self.water += 1
            print(f"You gave {self.name} 1 water. Water: {self.water}")
            self.hp += 1
            time.sleep(0.5)
    def view_stats(self):
        if self.hp > 0:
            print(f"Food: {self.food}, Water: {self.water}, Happiness: {self.happiness}, Cleanness: {self.sanitation}, Hp: {self.hp}")
    def play(self):
        if self.hp > 0 and self.food > 0 and self.water > 0:
            print(f"You played with {self.name}")
            self.happiness += 10
            self.food -= 3
            self.water -= 5
            self.hp += 5
            self.sanitation -= 5
    def walk(self):
        if self.hp > 0:
            print(f"You took {self.name} for a walk")
            self.happiness += 20
            self.food -= 5
            self.water -= 8
            self.hp += 5
            self.sanitation -= 10
    def heal(self):
        if self.hp < 100:
            if self.hp > 0:
                self.hp += 20
                print("+10 hp")
                time.sleep(5)
    def Ummmm(self):
        if self.hp > 0:
            print("Why did you eat your pet?")
            self.hp = 0
    def wash(self):
        if self.sanitation < 90:
            self.sanitation += 10
            self.happiness -= 10
            print("You gave your pet a shower. +10 cleaness")
    def loop_hunger(self):
        while self.hp > 0:
            time.sleep(8)
            if self.hp > 0:
                self.food -= 1
                self.hp -= 5
                print(f"Food: {self.food}")
            if self.food == 7:
                print(f"{self.name} is hungry")
            elif self.food == 2:
                print(f"{self.name} is starving!!!")
            if self.food > 30:
                print(f"{self.name} died by diabetes. ")
                self.hp = 0
            if self.food < 1:
                self.hp = 0
    def loop_thirst(self):
        while self.hp > 0:
            time.sleep(6)
            if self.hp > 0:
                self.water -= 1
                self.hp -= 3
                print(f"Water: {self.water}")
            if self.water == 5:
                print(f"{self.name} is thirsty")
            elif self.water == 2:
                print(f"{self.name} is very thirsty!!!")
            if self.water > 30:
                print(f"{self.name} was too hydrated. ")
                self.hp = 0
            if self.water < 1:
                self.hp = 0

print("Welcome to this very cool but slightly difficult pet game! Your goal is to make sure your pet survives as long as they can. They start with 15 food and 20 water. To view their stats, press q. To feed   your pet food,   press z.To give water, press x. Keep your pet happy by playing with it. Press p to play with it or l to take it for a walk. Keep in mind that your pet may get sick from time to time. Also keeping your pet clean is essential because your pet's chances of getting sick increases drastically as his cleanness level decreases. To clean him, press c but keep in mind that your pet does not like taking baths. You may heal your pet over time by giving  your pet food, water or pressing h. Most importantly, whatever you do, do not press k. First name your pet to begin! ")
Name = input("Name your pet  ")

while useless_variable == 0:
    int = 0
    num = 0
    for char in Name:
        if Name[num].isnumeric():
            int += 1
        else:
            num += 1
    if int > 0:
        Name = input("Invalid Name. Pick a new name  ")
    else:
        break
    

pet = pet(Name, 15, 20, 100, 100, 100)

 



def loop_health():
    while pet.hp > 0:
        sickchance = 6
        if pet.sanitation < 50 and pet.sanitation > 30:
            sickchance = 4
        elif pet.sanitation <= 30:
            sickchance = 2
        time.sleep(10)
        if pet.hp > 0:
            sick = random.randint(1, sickchance)
            d = random.randint(10, 25)
            if sick == 1:
                print(f"{pet.name} got sick. -{d} hp")
                pet.hp -= d
                sick = 0
        
            
def loop_timer():
    timer = 0
    while pet.hp > 0:
        time.sleep(0.1)
        timer += 0.1
    timer = round(timer, 1)
    print(timer)

def loop_hpcheck():
    while pet.hp > 0:
        if pet.hp > 100:
            pet.hp = 100
    print("Game Over")


def loop_mood():
    while pet.hp > 0:
        if pet.hp < 1:
            break
        time.sleep(1.5)
        pet.happiness -= 1
        if pet.happiness == 30:
            print(f"{pet.name} is bored")
        elif pet.happiness == 10:
            print(f"{pet.name} is @#!@$&*")
        elif pet.happiness == 50:
            print(f"{pet.name} is neutral")
        elif pet.happiness == 0:
            print(f"{pet.name} didn't want to live anymore. Game Over!")
            pet.hp = 0

def loop_event():
    while pet.hp > 0:
        t = random.randint(10, 35)
        time.sleep(t)
        r = random.randint(1, 12)
        if pet.hp < 1:
            break
        if r == 1:
            print(f"{pet.name} accidentally ate a piece of chcolate. Chocolate is like poison to dogs. -20 hp but +3 food")
            pet.food += 3
            pet.hp -= 20
        elif r == 2:
            print(f"{pet.name} found a mysterious mushroom. He ate it and gained 30 hp.")
            pet.hp += 30
        elif r == 3:
            print(f"{pet.name} got into a fight with a dog. -10 hp")
            pet.hp -= 10
        elif r == 4:
            print(f"{pet.name} got hit by a recless driver. -40 hp")
            pet.hp -= 40
        elif r == 5:
            print(f"You won the lottery. You buy {pet.name} food. Max food + Max Water")
            pet.food = 25
            pet.water = 25
            foodsupply == 2
        elif r == 6:
            print(f"{pet.name} got hit by a meteor. -50 hp")
            pet.hp -= 50
        elif r == 7:
            print(f"{pet.name} got struck by lightning. -10 hp but +20 happiness")
            pet.happiness += 20
            pet.hp -= 10
        elif r == 8:
            print(f"{pet.name} found a potion of instant health. +40 hp")
            pet.hp += 40
        elif r == 9:
            print(f"{pet.name} found a mysterious mushroom. He ate it and got poisoned.")
            pet.hp -= 20
        elif r == 10:
            print("You forgot to buy food for your pet today. You'll have to start rationing your food.")
            foodsupply == 4
        elif r == 11:
            print(f"{pet.name} drank some poisonous water. ")
            pet.hp -= 15
            pet.water += 3
        elif r == 12:
            print(f"{pet.name} was hit by a boulder. ")
            pet.hp -= 20

def loop_clean():
    while pet.hp > 0:
        time.sleep(1)
        pet.sanitation -= 1




keyboard.add_hotkey('z', pet.feed)
keyboard.add_hotkey('x', pet.drink)
keyboard.add_hotkey('q', pet.view_stats)
keyboard.add_hotkey('p', pet.play)
keyboard.add_hotkey('l', pet.walk)
keyboard.add_hotkey('h', pet.heal)
keyboard.add_hotkey('k', pet.Ummmm)
keyboard.add_hotkey('c', pet.wash)

thread_hunger = threading.Thread(target=pet.loop_hunger)
thread_thirst = threading.Thread(target=pet.loop_thirst)
thread_health = threading.Thread(target=loop_health)
thread_hpcheck = threading.Thread(target=loop_hpcheck)
thread_mood = threading.Thread(target=loop_mood)
thread_event = threading.Thread(target=loop_event)
thread_timer = threading.Thread(target=loop_timer)
thread_clean = threading.Thread(target=loop_clean)
thread_hunger.start()
thread_thirst.start()
thread_health.start()
thread_hpcheck.start()
thread_mood.start()
thread_event.start()
thread_timer.start()
thread_clean.start()




