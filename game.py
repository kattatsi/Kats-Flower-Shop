import random
from plant import Plant 
class game:
    gold = 5
    food = 5
    meds = 3
    seeds = 3
    action = 4
    round = 1
    run = True

    garden = []
    for i in range(0, 10):
        garden.append(0)
    
    #plant new flower in position num
    def plant(self, num):
        if self.seeds == 0:
            print("No more seeds")
        elif 0 <= num <=10:
            self.garden[num-1] = Plant()
            self.seeds -= 1
        elif num > 10:
            print("The garden has only 10 spots, bitch!")

    #sell plant in position num
    def sell(self, num):
        if (self.garden[num-1]==0):
            print ("You dont have a plant in this spot to sell locoooo")
        elif (self.garden[num-1].hungry==False and self.garden[num-1].thirsty==False and self.garden[num-1].sick==False and self.garden[num - 1].stage == 5):
            self.gold = self.gold + 5
            self.garden[num - 1] = 0
            print("Sold plant ", num)
            print ("You have ", gold, "gold.")
        else:
            print ("You can't do that you duffus!")
    
    #feed plant in position num
    def feed(self, num):
        if self.food==0:
            print("You don't have food. Please buy more:'(")
            return
        self.food-=1
        self.garden[num-1].hungry = False

    #water plant in position num
    def water(self, num):
        self.garden[num-1].thirsty = False
     
    def med(self, num):
        if self.meds==0:
            print ("You don't have meds. Please buy more:'(")
        self.meds-=1
        self.garden[num-1].sick = False
    
    #buy supplies
    def buy(self, type, quantity):
        if self.gold==0:  
            print("You don't have money meow")
            return
        if quantity<0:
            print ("Give a number >0 dum dum")
            return
        if (type=="food"):
            if self.gold-quantity<0:
                print("You don't have enough money for all this")
                return
            self.food+=quantity
            self.gold-=quantity
        if (type=="meds"):
            if self.gold-2*quantity<0:
                print ("You don't have enough money for all this")
                return
            self.meds+=quantity
            self.gold-=quantity*2
        if (type=="seeds"):
            if self.gold-quantity<0:
                print("You don't have enough money for all this")
                return
            self.seeds+=quantity
            self.gold-=quantity
    
    #next move update 
    def next(self):
        self.action=4
        self.rounds()
        for i in range(0, 10):
            if (self.garden[i] != 0):
                ph = random.randint(1, 100)
                pt = random.randint(1, 100)
                ps = random.randint(1, 100)
            if (ph < 21):
                self.garden[i].hungry = True
            if (pt < 31):
                self.garden[i].thirsty = True
            if (ps < 16):
                self.garden[i].sick = True
        
        print("You are on round  ", self.round)
        print ("You have 4 actions. Use them wisely!")
        print ("You have ", self.gold, " gold.")
        print ("Stages: ", end=" ")
        for i in range (0,10):
            if self.garden[i]!=0:
                print (self.garden[i].stage, end=" ")
            else:
                print ("0", end=" ")
        print()
        print ("Hungry: ", end=" ")
        for i in range(0,10):
            if ((self.garden[i]!=0) and (self.garden[i].hungry == True)):
                print (i+1, end=" ")
        print ()
        print ("Thirsty: ", end=" ")
        for i in range(0,10):
            if ((self.garden[i]!=0) and (self.garden[i].thirsty == True)):
                print (i+1, end=" ")
        print ()
        print ("Sick: ", end=" ")
        for i in range(0,10):
            if ((self.garden[i]!=0) and (self.garden[i].sick == True)):
                print (i+1, end=" ")
        print ()
        print ("Lives: ", end=" ")
        for i in range(0,10):
            if (self.garden[i]!=0):
                print (self.garden[i].lives, end=" ")
            else:
                print ("0", end=" ")
        print()
        print ("You have left  ",self.seeds," seeds, ",self.food," food, ",self.meds," meds.")
    

    def rounds(self):
        self.round= self.round + 1
        for i in range(0, 10):
            if ((self.garden[i]!=0) and (self.garden[i].stage<5)):
                self.garden[i].stage+=1
            if ((self.garden[i]!=0) and (self.garden[i].lives==0)):
                print ("You are uselesss!! The plant in pot ", i+1, "died. ")
                self.garden[i]=0
            if ((self.garden[i]!=0) and (self.garden[i].hungry==True or self.garden[i].sick==True or self.garden[i].thirsty==True)):
                self.garden[i].lives-=1

    def actions(self, charge):
        if (self.action-charge)==0:
            self.action=0
            print("No more actions dum dum. You go to the next round. ")
            return True
        elif (self.action-charge)<0:
            print ("You cant do that dum dum. You dont have enough actions. Choose something else")
            print ("You still have ", self.action, " actions. ")
            return False
        else:
            self.action-=charge
            print ("You still have left ", self.action, " actions. ")
            return True
        
    def no_plants(self):
        empty=True
        for i in range(0,10):
            if self.garden[i]!=0:
                empty=False
        return empty
    

    def go(self, input):
        if self.action == 0:
            self.next()
        if self.gold>=100:
            print ("You winn!! You did it! You reached 100 gold.")
            self.run = False
            return 
        if(self.gold==0 and self.no_plants()==True):
            print ("You don't have neither gold nor plants. You are a loser. Adios!")
            self.run = False
            return
        
        #to input[0] exei thn entolh pou mas endiaferei gia thn kinhsh pou thelei na kanei

        if len(input)==0:
            return 

        if (input[0]=="next"):
            self.next()
            return
        if (input[0]=="plant"):
            if self.actions(1):
                self.plant(int(input[1]))
            return
        if (input[0]=="sell"):
            if self.actions(1):
                self.sell(int(input[1]))
            return
        if (input[0]=="feed"):
            if self.actions(0.25):
                self.feed(int(input[1]))
            return
        if (input[0]=="water"):
            if self.actions(0.25):
                self.water(int(input[1]))
            return
        if (input[0]=="med"):
            if self.actions(0.25):
                self.med(int(input[1]))
            return
        if (input[0]=="buy"):
            if self.actions(0.5):
                self.buy(input[1], int(input[2]))
            return
