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
        self.garden[num-1] = Plant()
        self.seeds -= 1

    #sell plant in position num
    def sell(self, num):
        if (self.garden[num-1]==0):
            print ("You dont have a plant in this spot to sell locoooo")
        elif (self.garden[num-1].hungry==False and self.garden[num-1].thirsty==False and self.garden[num-1].sick==False):
            self.gold = self.gold + 5
            self.garden[num - 1] = 0
            print("Sold plant ", num)
            print ("You have ", self.gold, "gold.")
        else:
            print("Meow")
    
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
        if not self.enough(type, quantity):
            return
        if (type=="food"):
            self.food+=quantity
            self.gold-=quantity
            return 
        if (type=="meds"):
            self.meds+=quantity
            self.gold-=quantity*2
            return 
        if (type=="seeds"):
            self.seeds+=quantity
            self.gold-=quantity
            return 
    
    #next move update 
    def next(self):
        self.action=4
        self.rounds()
        for i in range(0, 10):
            if (self.garden[i] != 0):
                ph = random.randint(1, 100)
                pt = random.randint(1, 100)
                ps = random.randint(1, 100)
                if (ph < 21 and self.garden[i]!=0):
                    self.garden[i].hungry = True
                if (pt < 31 and self.garden[i]!=0):
                    self.garden[i].thirsty = True
                if (ps < 16 and self.garden[i]!=0):
                    self.garden[i].sick = True
        
        print("You are on round ", self.round)
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
            print("You finished your actions pooks. You go to the next round. ")
            return 0
        elif (self.action-charge)<0:
            print ("You cant do that dum dum. You dont have enough actions. Choose something else")
            print ("You still have ", self.action, " actions. ")
            return -1
        else:
            self.action-=charge
            print ("You still have left ", self.action, " actions. ")
            return 1
        
    def no_plants(self):
        empty=True
        for i in range(0,10):
            if self.garden[i]!=0:
                empty=False
        return empty
    
    def enough(self, type, quantity):
        if self.gold==0:  
            print("You don't have money meow")
            return False
        if quantity<0:
            print ("Give a number >0 dum dum")
            return False
        if (type=="food"):
            if self.gold-quantity<0:
                print("You don't have enough money for all this. Buy less maybe...")
                return False 
            return True
        if (type=="meds"):
            if self.gold-2*quantity<0:
                print ("You don't have enough money for all this. Buy less maybe..")
                return False 
            return True
        if (type=="seeds"):
            if self.gold-quantity<0:
                print("You don't have enough money for all this. Buy less maybe..")
                return False
            return True


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
            n = int(input[1])
            if self.seeds == 0:
                print("No more seeds")
                return
            elif (n > 10 or n < 1):
                print("The garden has only 10 spots (1-10), bitch!")
                return 
            elif self.garden[n-1]!=0:
                print("You have a flower there!")
                return 
            else:
                act = self.actions(1)
                if act == 0:
                    self.plant(n)
                    self.next()
                elif act == 1:
                    self.plant(n)
            return
        if (input[0]=="sell"):
            num = int(input[1])
            if (self.garden[num-1]==0):
                print ("You dont have a plant in this spot to sell locoooo")
                return
            elif (self.garden[num-1].hungry==False and self.garden[num-1].thirsty==False and self.garden[num-1].sick==False and self.garden[num - 1].stage == 5):
                act = self.actions(1)
                if act == 0:
                    self.sell(num)
                    self.next()
                elif act == 1:
                    self.sell(num)
            elif (self.garden[num - 1].stage!= 5):
                print("You can't sell this plant. Its not ready yet!")
            elif (self.garden[num-1].hungry==True or self.garden[num-1].thirsty==True or self.garden[num-1].sick==True):
                print("Nobody wantes to buy this. Its not looking good bruhhhh...")
            return
        if (input[0]=="feed"):
            act = self.actions(0.25)
            if act == 0:
                self.feed(int(input[1]))
                self.next()
            elif act == 1:
                self.feed(int(input[1]))
            return
        if (input[0]=="water"):
            act = self.actions(0.25)
            if act == 0:
                self.water(int(input[1]))
                self.next()
            elif act == 1:
                self.water(int(input[1]))
            return
        if (input[0]=="med"):
            act = self.actions(0.25)
            if act == 0:
                self.med(int(input[1]))
                self.next()
            elif act == 1:
                self.med(int(input[1]))
            return
        if (input[0]=="buy"):
            money = self.enough(input[1], int(input[2]))
            if money:
                act = self.actions(0.5)
                if act == 0:
                    self.buy(input[1], int(input[2]))
                    self.next()
                elif act == 1:
                    self.buy(input[1], int(input[2]))
            return 
