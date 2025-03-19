#Samuel Andelin, Battle Simulator

#importing time and random
import time
import random

#importing other needed functions
from win_checking import monsterloser
from win_checking import loser

#combat function
def combat(current_enemy, plyr):
    #uses a placeholder for the enemy hp to modify
    plcehldr = current_enemy["hp"]

    #lists info about the user's attack
    print("Your attack is",str(plyr["attack"]),"which means that your roll will have a modifier of +",str(plyr["attack"] // 3))
    time.sleep(0.5)
    
    #player attacks
    print("Rolling die for damage... ")
    time.sleep(2)
    plyrdamage = random.randint(1, 20)
    print("You got a " + str(plyrdamage))
    time.sleep(0.5)
    print("You hit the monster for " +str(plyrdamage + plyr["attack"] // 3) + " damage!")

    #math and subtracting from the enemy hp (placeholder)
    plcehldr -= plyrdamage + plyr["attack"] // 3
    time.sleep(0.5)

    #lists how much hp the enemy has left
    print("The monster has " + str(plcehldr) + " hp left.")

    #checking enemy stats
    monsterded = monsterloser(plcehldr)

    #if the monster is dead, tell that to main
    if monsterded:
        return "done"
    
    #if the monster is not dead, give main the updated enemy hp after the attack
    else:
        return plcehldr


#computer attacking function
def compcombat(enemy, plyr):
    #creates a modifiable placeholder for player hp
    plcehldr = plyr["hp"]

    #attack loop of the computer attacking
    while True:
        #If the enemy is dead, exit
        if enemy['hp'] <= 0:
            print("The enemy is dead")
            break

        #if the computer is still alive
        else:
            print("The monster attacks!")
            time.sleep(0.5)
            #info about monster attack strength
            print("The enemy's strength is " + str(enemy["attack"]) +" which means that his roll will have a modifier of + " +str(enemy["attack"] // 3))
            time.sleep(0.5)
            #random dice attack roll
            print("Rolling die...")
            enemyattack = random.randint(1, 20)
            time.sleep(2)
            print("The enemy attacks you for " +str(enemyattack + enemy["attack"] // 3))
            time.sleep(0.5)
            #updates player hp
            plcehldr -= (enemyattack + (enemy["attack"] // 3))
            print("You have " + str(plcehldr) + " hp left.")
            time.sleep(0.5)
        
        #checking player stats
        combatplyrlose = loser(plcehldr)
        #if the player died
        if combatplyrlose:
            return "wump_wump"
        #if not, give main the updated player hp
        else:
            return plcehldr