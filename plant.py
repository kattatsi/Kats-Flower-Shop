import random

class Plant:
    n=["tulip", "rose", "levander", "jasmine", "lily", "sunflower", "violet", "iris"]
    name = random.choice(n)  #ramdom plant name 
    stage = 1
    hungry = False 
    thirsty = False
    sick = False 
    lives = 3