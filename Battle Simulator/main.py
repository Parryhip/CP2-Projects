#samuel andelin, battle simulator

#importing time for dramatic effects, random for the randomly generated rooms and dice rolls
import time
import random

#importing neccessary functions
from combat import combat
from combat import compcombat
from sign_in import sign_in

#lists/dictionaries for player and enemy stats, and room memory
placeholderforenemyhp = 0
enemylist = []
lootlist = [
    "potion of strength", "potion of health", "potion of speed",
    "potion of strength", "potion of health", "potion of speed",
    "potion of strength", "potion of health", "potion of speed",
    "potion of strength", "potion of health", "potion of speed",
    "potion of strength", "potion of health", "potion of speed",
    "potion of strength", "potion of health", "potion of speed", "longsword",
    "longsword", "longsword", "greatsword", "greatsword",
    "sword of the ancient ones", "breastplate", "breastplate", "breastplate", "breastplate", 
    "helmet", "helmet", "helmet", "helmet", "helmet", "helmet", "leggings", "leggings", "leggings",
    "leggings", "leggings", "boots", "boots", "boots", "boots", "boots", "boots", "boots", "boots"
]

plyr = {
    "hp": 0,
    "items": [],
    "equippeditems": [],
    "attack": 0,
    "armor": 0,
    "dexterity": 0,
    "monsters_killed": 0,
    "goal": 0,
}
goblin = {
    "hp": 20,
    "attack": 5,
    "dexterity": 30,
}
werewolf = {
    "hp": 60,
    "attack": 14,
    "dexterity": 10,
}
orc = {
    "hp": 30,
    "attack": 10,
    "dexterity": 4,
}
skeleton = {
    "hp": 60,
    "attack": 7,
    "dexterity": 12,
}
gelatinous_cube = {
    "hp": 100,
    "attack": 16,
    "dexterity": 1,
}
dark_wizard = {
    "hp": 200,
    "attack": 20,
    "dexterity": 20,
}


#restart function
def restart():
    plyr = sign_in()
    while True:
        #asking the user if they want to keep playing 
        play_again = input("Do you want to keep fighting? (y/n) ").lower()
        #if they do, the game continues
        if play_again == "y":
            #setting up stats
            while True:
                difficulty = input("What difficulty do you want the fights to be? (easy, medium, hard)").lower()
                if difficulty == "easy":
                    print("Ok! You decide to play on easy mode, where you start with a greatsword(modifies strength by + 4), , a potion of speed(modifies dexterity by + 2), a potion of health(increases health by 50), and a potion of strength(modifies strength by + 2). You also only encounter goblins and orcs.")
                    time.sleep(3)
                    enemylist.append("goblin")
                    enemylist.append("orc")
                    plyr["items"].append("greatsword")
                    plyr["items"].append("potion of health")
                    plyr["items"].append("potion of strength")
                    break
                elif difficulty == "medium":
                    print("Ok! You decide to play on medium mode, where you start with a longsword(modifies strength by + 2), a potion of speed(modifies dexterity by + 2) and a potion of strength(modifies strength by + 2). You encounter skeletons and orcs, goblins and werewolves.")
                    time.sleep(3)
                    enemylist.append("goblin")
                    enemylist.append("orc")
                    enemylist.append("werewolf")
                    enemylist.append("skeleton")
                    plyr["items"].append("longsword")
                    plyr["items"].append("potion of strength")
                    break
                elif difficulty == "hard":
                    print(
                        "Ok! You decide to play on hard mode, where you start with a normal sword(modifies strength by + 0) and makes there be super difficult monsters."
                    )
                    time.sleep(3)
                    enemylist.append("goblin")
                    enemylist.append("orc")
                    enemylist.append("werewolf")
                    enemylist.append("gelatinous cube")
                    enemylist.append("dark_wizard")
                    enemylist.append("gelatinous_cube")
                    break
                else:
                    print("Not valid difficulty.")



#main function
def main():
    #main while loop
    while True:
        choice = input("What do you want to do? (1 to attack, 2 to look at inventory, 3 to equip swords, 4 to drink potions) ")
        if choice == "1":
            #checking certain assets of the rooms in case to call the combat function
            print("You attack the enemy!")
            global placeholderforenemyhp
            #changing the random string to a literal
            if current_enemy == "goblin":
                enemy = goblin
            elif current_enemy == "orc":
                enemy = orc
            elif current_enemy == "werewolf":
                enemy = werewolf
            elif current_enemy == "skeleton":
                enemy = skeleton
            elif current_enemy == "gelatinous_cube":
                enemy = gelatinous_cube
            elif current_enemy == "dark_wizard":
                enemy = dark_wizard
            placeholderforenemyhp = enemy["hp"]
            while True:
                done = combat(enemy,plyr,lootlist)
                if done == "done":
                    print("Well done!")
                    break
                elif done == "winner!":
                    print("Good job!")
                    return "gamedone"
                else:
                    #calling of the computer combat function
                    resultofcombat = compcombat()
                    if resultofcombat == "wump_wump":
                        print("You died!")
                        restart()
                        break
                    if resultofcombat == "done":
                        break
                    elif resultofcombat == "win!!!":
                        return "gamedone"

        elif choice == "2":
            print("You look at your inventory!")
            print("These are the items in your inventory: ")
            print(plyr["items"])
            time.sleep(0.5)
        elif choice == "3":
            print("What do you want to equip?: ")
            print(plyr["items"])
            equip = input(": ")
            if equip == "longsword" and "longsword" in plyr["items"] and "longsword" not in plyr["equippeditems"]:
                print("You equip your longsword.")
                print("Now you have a modifier of + 2 attack")
                plyr["equippeditems"].append("longsword")
                plyr["attack"] = plyr["attack"] + 2
            elif equip == "greatsword" and "greatsword" in plyr["items"] and "greatsword" not in plyr["equippeditems"]:
                print("You equip your greatsword.")
                print("Now you have a modifier of + 4 attack")
                plyr["equippeditems"].append("greatsword")
                plyr["attack"] = plyr["attack"] + 4
            elif equip == "sword of the ancient ones" and "sword of the ancient ones" in plyr["items"] and "sword of the ancient ones" not in plyr["equippeditems"]:
                print("You equip the sword of the ancient ones.")
                print("Light falls upon you as you wield this sword.")
                print("Nothing can stand in your way as this sword gives you an attack modifier of + 10")
                plyr["equippeditems"].append("sword of the ancient ones")
                plyr["attack"] = plyr["attack"] + 10
            else:
                print("You do not have that sword or you have it equipped already.")
        elif choice == "4":
            print("What potion do you want to drink?: ")
            print(plyr["items"])
            equipp = input(": ")
            if equipp == "potion of health" and "potion of health" in plyr["items"] and "potion of health" in plyr["items"]:
                plyr["items"].remove("potion of health")
                print("You drink the potion of strength.")
                print("This gives your health a boost of + 50")
                plyr["hp"] = plyr["hp"] + 50
                print("Your hp is now " + str(plyr["hp"]))
            elif equipp == "potion of strength" and "potion of strength" in plyr["items"] and "potion of strength" in plyr["items"]:
                print("You drink the potion of strength.")
                print("This gives your attack a modifier of + 2")
                plyr["items"].remove("potion of strength")
                plyr["attack"] = plyr["attack"] + 2
                print("Your attack is now " + str(plyr["attack"]))
            elif equipp == "potion of speed" and "potion of speed" in plyr["items"] and "potion of speed" in plyr["items"]:
                print("You drink the potion of speed.")
                print("This gives your dexterity a modifier of + 2")
                plyr["items"].remove("potion of speed")
                plyr["dexterity"] = plyr["dexterity"] + 2
                print("Your dexterity is now " + str(plyr["dexterity"]))
            else:
                print("You do not have that potion.")


restart()
