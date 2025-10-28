import random
import time
sick = random.randint(0, 4)
class pet():
    def __init__(self, name, food, water):
        self.name = name
        self.food = food
        self.water = water
    def addfood(self, food):
        self.food += food
        print(self.food)
    def addwater(self, water):
        self.water += water
        print(self.water)
    def health(self):
        if sick < 4:
            print("Healthy")
        else:
             print("Sick")

dog = pet("dog", 10, 0)


while dog.food > 0:
    time.sleep(3)
    dog.food -= 1
    print(dog.food)
    



        

