import random
#tyxaio onoma gia fyto
f=["tulip", "rose", "levander", "jasmine", "lily", "sunflower", "violet", "iris"]
gold=5
round=1
food=5
meds=3
seeds=3
action=4
#fyto class
class Plant(object):
    name = random.choice(f)
    stage = 1
    hungry = False
    thirsty = False
    sick = False
    lives = 3
#lista me 10 fyta sthn seira
garden = []
for i in range(0, 10):
    garden.append(0)
def plant(num):
    global seeds
    global action
    if seeds==0:
        print ("Δεν έχεις άλλους σπόρους :(")
        return
    if 0 <= num <= 10:
        garden[num-1]=Plant()
        seeds -= 1
    else:
        print("I don't know how to write greek on mac!!!")
#poulaei thn glastra kai thn diagrafei apo ton khpo alliws eisai mpoufos
def sell(num):
    if (garden[num-1]==0):
        print ("Δεν έχεις φυτό εκεί για να πουλήσεις λοκοοοο")
        return
    if (garden[num-1].hungry==False and garden[num-1].thirsty==False and garden[num-1].sick==False and garden[num - 1].stage == 5):
         global gold
         gold = gold + 5
         garden[num - 1] = 0
         print("sold plant ", num)
         print ("Έχεις ", gold, "gold. ")
    else:
        print ("Άκυρη εντολη! Είσαι μπουφος!;)")
#tsaizei to sygkekrimeno fyto
def feed(num):
    global food
    if food==0:
        print("Δεν έχεις αλλο φαγητό. Αγόρασε τιποτα.")
        return
    food-=1
    garden[num-1].hungry = False
#potizei to sygkekrimeno fyto
def water(num):
    garden[num-1].thirsty = False
#lismataki gia sygkekrimeno fyto
def med(num):
    global meds
    if meds==0:
        print ("Δεν έχεις άλλα φάρμακα. Αγόρασε τίποτα.")
    meds-=1
    garden[num-1].sick = False

def buy(type, quantity):
    global gold
    global food
    global meds
    global seeds
    if gold==0:
        print("Δεν έχεις λεφτά βλάχα")
        return
    if quantity<0:
        print ("Δώσε κανονικό νούμερο να τελειώνουμε...")
        return
    if (type=="food"):
        if gold-quantity<0:
            print("Δεν σου φτάνουν τα λεφτααα...")
            return
        food+=quantity
        gold-=quantity
    if (type=="meds"):
        if gold-2*quantity<0:
            print ("Δεν σου φτάνουν τα λεφτααα...")
            return
        meds+=quantity
        gold-=quantity*2
    if (type=="seeds"):
        if gold-quantity<0:
            print("Δεν σου φτάνουν τα λεφτααα...")
            return
        seeds+=quantity
        gold-=quantity
def next():
    global round
    global action
    action=4
    rounds()
    for i in range(0, 10):
        if (garden[i] != 0):
            ph = random.randint(1, 100)
            pt = random.randint(1, 100)
            ps = random.randint(1, 100)
            if (ph < 21):
                garden[i].hungry = True
            if (pt < 31):
                garden[i].thirsty = True
            if (ps < 16):
                garden[i].sick = True
        else:
            continue
    print("Είσαι στον γύρο ", round)
    print ("Έχεις πάλι 4 ενέργειες. Use them wisely!")
    print ("Έχεις ", gold, " gold")
    print ("Stages: ", end=" ")
    for i in range (0,10):
        if garden[i]!=0:
            print (garden[i].stage, end=" ")
        else:
            print ("0", end=" ")
    print()
    print ("Hungry: ", end=" ")
    for i in range(0,10):
        if ((garden[i]!=0) and (garden[i].hungry == True)):
            print (i+1, end=" ")
    print ()
    print ("Thirsty: ", end=" ")
    for i in range(0,10):
        if ((garden[i]!=0) and (garden[i].thirsty == True)):
            print (i+1, end=" ")
    print ()
    print ("Sick: ", end=" ")
    for i in range(0,10):
        if ((garden[i]!=0) and (garden[i].sick == True)):
            print (i+1, end=" ")
    print ()
    print ("Lives: ", end=" ")
    for i in range(0,10):
        if (garden[i]!=0):
            print (garden[i].lives, end=" ")
        else:
            print ("0", end=" ")
    print()
    print ("Σου απομένουν ",seeds," σπόροι, ",food," τρόφιμα, ",meds," φάρμακα.")
def rounds():
    global round
    round= round + 1
    for i in range(0, 10):
        if ((garden[i]!=0) and (garden[i].stage<5)):
            garden[i].stage+=1
        if ((garden[i]!=0) and (garden[i].lives==0)):
            print ("Έισαι άχρηστος!! Το φυτό στη γλάστρα ", i+1, "πέθανε.")
            garden[i]=0
        if ((garden[i]!=0) and (garden[i].hungry==True or garden[i].sick==True or garden[i].thirsty==True)):
            garden[i].lives-=1
def actions(charge):
    global action
    if (action-charge)==0:
        action=0
        print("Τελείωσαν οι ενέργειες σου μπουφο. Πας στον επομενο γύρο. ")
        return True
    elif (action-charge)<0:
        print ("Δεν μπορείς να το κάνεις αυτό σαίνι. Δεν έχεις αρκετές ενέργειες. Διάλεξε κάτι άλλο...")
        print ("Έχεις ακόμα ", action, " ενέργεις. ")
        return False
    else:
        action-=charge
        print ("Σου μένουν ακόμα ", action, " ενέργειες. ")
        return True
def no_plants():
    empty=True
    for i in range(0,10):
        if garden[i]!=0:
            empty=False
    return empty
def main():
    global action
    global gold
    game=True
    while (game):
        if(action==0):
            next()
            continue
        if gold>100:
            print ("Νίκησες!! We did it. Ναι τα καταφέραμε. We did it! Έφτασες τα 100 gold.")
            break
        if(gold==0 and no_plants()==True):
            print ("Δεν έχεις κανένα φυτό ούτε λεφτά. Άρα είσαι loser. Adios!")
            break
        cmd = input("input: ").split()

        if len(cmd)==0:
            continue

        if (cmd[0]=="next"):
            next()
            continue
        if (cmd[0]=="plant"):
            if actions(1):
                plant(int(cmd[1]))
                continue
            else:
                continue
        if (cmd[0]=="sell"):
            if actions(1):
                sell(int(cmd[1]))
                continue
            else:
                continue
        if (cmd[0]=="feed"):
            if actions(0.25):
                feed(int(cmd[1]))
                continue
            else:
                continue
        if (cmd[0]=="water"):
            if actions(0.25):
                water(int(cmd[1]))
                continue
            else:
                continue
        if (cmd[0]=="med"):
            if actions(0.25):
                med(int(cmd[1]))
                continue
            else:
                continue
        if (cmd[0]=="buy"):
            if actions(0.5):
                buy(cmd[1], int(cmd[2]))
                continue
            else:
                continue
main()
