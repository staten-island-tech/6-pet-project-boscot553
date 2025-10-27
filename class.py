import random
sick = random.randint(0, 1)
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
        if sick < 1:
            print("Healthy")
        else:
             print("Sick")



        

dog = pet("dog", 10, 0)
dog.health()





        

