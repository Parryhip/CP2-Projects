#Samuel Andelin, Battle Simulator

#importing time and random
import time
import random

#importing other needed functions
from win_checking import monsterloser
from win_checking import loser

#combat function
def combat(current_enemy, plyr, lootlist):   
    while True:
        combataction = input("Type 1 to attack normally, type 2 to use a potion, type 3 to cast spell, and type 4 to use ability.\n-->")
        if combataction == "1":
            print("Your attack is",str(plyr["attack"]),"which means that your roll will have a modifier of +",str(plyr["attack"] // 3))
            time.sleep(0.5)
            #player attacks
            print("Rolling die for damage... ")
            time.sleep(2)
            plyrdamage = random.randint(1, 20)
            print("You got a " + str(plyrdamage))
            time.sleep(0.5)
            print("You hit the monster for " +str(plyrdamage + plyr["attack"] // 3) + " damage!")
            placeholderforenemyhp -= plyrdamage + plyr["attack"] // 3
            time.sleep(0.5)
            print("The monster has " + str(placeholderforenemyhp) + " hp left.")
            #checking enemy stats
            monsterded = monsterloser(current_enemy, placeholderforenemyhp)
            if monsterded:
                plyr["monsters_killed"] += 1
                lootchance = random.randint(1, 2)
                actualloot = random.choice(lootlist)
                if lootchance == 1:
                    print("You got a " + actualloot + "!")
                    plyr["items"].append(actualloot)
                    enemy = ""
                    return "done"
                else:
                    print("You got no loot from the monster.")
                    enemy = ""
                    return "done"
            else:
                break
        elif combataction == "potion":
            print("What potion do you want to drink?: ")
            print(plyr["items"])
            equipp = input(": ")
            if equipp == "potion of health" and "potion of health" in plyr[
                "items"] and "potion of health" in plyr["items"]:
                plyr["items"].remove("potion of health")
                print("You drink the potion of strength.")
                print("This gives your health a boost of + 50")
                plyr["hp"] = plyr["hp"] + 50
                print("Your hp is now " + str(plyr["hp"]))
            elif equipp == "potion of strength" and "potion of strength" in plyr[
                "items"] and "potion of strength" in plyr["items"]:
                print("You drink the potion of strength.")
                print("This gives your attack a modifier of + 2")
                plyr["items"].remove("potion of strength")
                plyr["attack"] = plyr["attack"] + 2
                print("Your attack is now " + str(plyr["attack"]))
            elif equipp == "potion of speed" and "potion of speed" in plyr[
                "items"] and "potion of speed" in plyr["items"]:
                print("You drink the potion of speed.")
                print("This gives your dexterity a modifier of + 2")
                plyr["items"].remove("potion of speed")
                plyr["dexterity"] = plyr["dexterity"] + 2
                print("Your dexterity is now " + str(plyr["dexterity"]))
            else:
                print("You do not have that potion.")


#computer attacking function
def compcombat(enemy, plyr):
    while True:
        #enemy attacks
        monsteractionchance = random.randint(1, 2)
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
            plyr["hp"] = plyr["hp"] - (enemyattack + (enemy["attack"] // 3))
            print("You have " + str(plyr["hp"]) + " hp left.")
            time.sleep(0.5)
        #randomly generated attacks
        
        #checking player stats
        combatplyrlose = loser()
        if combatplyrlose:
            return "wump_wump"
        else:
            break