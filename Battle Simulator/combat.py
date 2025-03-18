#Samuel Andelin, Battle Simulator

#importing time and random
import time
import random

#importing other needed functions
from win_checking import monsterloser
from win_checking import loser

#combat function
def combat(current_enemy, plyr):
    plcehldr = current_enemy["hp"]
    print("Your attack is",str(plyr["attack"]),"which means that your roll will have a modifier of +",str(plyr["attack"] // 3))
    time.sleep(0.5)
    #player attacks
    print("Rolling die for damage... ")
    time.sleep(2)
    plyrdamage = random.randint(1, 20)
    print("You got a " + str(plyrdamage))
    time.sleep(0.5)
    print("You hit the monster for " +str(plyrdamage + plyr["attack"] // 3) + " damage!")
    plcehldr -= plyrdamage + plyr["attack"] // 3
    time.sleep(0.5)
    print("The monster has " + str(plcehldr) + " hp left.")
    #checking enemy stats
    monsterded = monsterloser(plcehldr)
    if monsterded:
        return "done"
    else:
        return plcehldr


#computer attacking function
def compcombat(enemy, plyr):
    plcehldr = plyr["hp"]
    while True:
        #enemy attacks
        if enemy['hp'] <= 0:
            print("The enemy is dead")
            break
        else:
            print("The monster attacks!")
            time.sleep(0.5)
            print("The enemy's strength is " + str(enemy["attack"]) +" which means that his roll will have a modifier of + " +str(enemy["attack"] // 3))
            time.sleep(0.5)
            print("Rolling die...")
            enemyattack = random.randint(1, 20)
            time.sleep(2)
            print("The enemy attacks you for " +str(enemyattack + enemy["attack"] // 3))
            time.sleep(0.5)
            plcehldr -= (enemyattack + (enemy["attack"] // 3))
            print("You have " + str(plcehldr) + " hp left.")
            time.sleep(0.5)
        
        #checking player stats
        combatplyrlose = loser(plcehldr)
        if combatplyrlose:
            return "wump_wump"
        else:
            return plcehldr