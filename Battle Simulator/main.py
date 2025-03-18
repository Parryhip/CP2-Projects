#samuel andelin, battle simulator

#importing time for dramatic effects, random for the randomly generated rooms and dice rolls, and csv for file handling
import time
import random
import csv

#importing neccessary functions
from combat import combat
from combat import compcombat
from sign_in import sign_in

#lists/dictionaries for player and enemy stats, and room memory
enemylist = []
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

#setting that the user is not signed in
signedin = False

#restart function
def restart(signedin):
    if signedin:
        pass
    else:
        plyr = sign_in()
        signedin = True    
    #setting up stats
    while True:
        difficulty = input("What difficulty do you want the fights to be? (easy, medium, hard)").lower()
        if difficulty == "easy":
            print("Ok! You decide to play on easy mode, where you only encounter goblins and orcs.")
            time.sleep(3)
            enemylist.append("goblin")
            enemylist.append("orc")
            return plyr, signedin
        elif difficulty == "medium":
            print("Ok! You decide to play on medium mode, where you only encounter skeletons, orcs, goblins, and werewolves.")
            time.sleep(3)
            enemylist.append("goblin")
            enemylist.append("orc")
            enemylist.append("werewolf")
            enemylist.append("skeleton")
            return plyr, signedin
        elif difficulty == "hard":
            print("Ok! You decide to play on hard mode, where it makes there be super difficult monsters.")
            time.sleep(3)
            enemylist.append("goblin")
            enemylist.append("orc")
            enemylist.append("werewolf")
            enemylist.append("dark wizard")
            enemylist.append("gelatinous cube")
            return plyr, signedin
        else:
            print("Not valid difficulty.")
            continue
        



#main function
def main(signedin):
    plyr, signedin = restart(signedin)
    current_enemy = random.choice(enemylist)
    #changing the random string to a literal
    if current_enemy == "goblin":
        enemy = goblin
    elif current_enemy == "orc":
        enemy = orc
    elif current_enemy == "werewolf":
        enemy = werewolf
    elif current_enemy == "skeleton":
        enemy = skeleton
    elif current_enemy == "gelatinous cube":
        enemy = gelatinous_cube
    elif current_enemy == "dark wizard":
        enemy = dark_wizard
    def keep_going():
        while True:
            #asking the user if they want to keep playing 
            play_again = input("Do you want to keep fighting? (y/n) ").lower()
            #if they do, the game continues
            if play_again == "y":
                return True
            elif play_again == "n":
                return False
            else:
                print("Invalid input!")

    #main while loop
    while True:
        if keep_going():
            pass
        else:
            print("Ok, bye!")
            return
        print("The current enemy is a",current_enemy+".")
        choice = input("What do you want to do? (1 to enter combat, 2 to view stats, 3 to exit) ")
        if choice == "1":
            print("You enter combat!")
            while True:
                done = combat(enemy,plyr)
                if done == "done":
                    current_enemy = random.choice(enemylist)
                    #changing the random string to a literal dictionary
                    if current_enemy == "goblin":
                        print("You earned 10 xp from killing that goblin!")
                        enemy = goblin
                    elif current_enemy == "orc":
                        print("You earned 25 xp from killing that orc!")
                        enemy = orc
                    elif current_enemy == "werewolf":
                        print("You earned 50 xp from killing that werewolf!")
                        enemy = werewolf
                    elif current_enemy == "skeleton":
                        print("You earned 50 xp from killing that skeleton!")
                        enemy = skeleton
                    elif current_enemy == "gelatinous cube":
                        print("You earned 75 xp from killing that gelatinous cube!")
                        enemy = gelatinous_cube
                    elif current_enemy == "dark wizard":
                        print("You earned 100 xp from killing that dark wizard!")
                        enemy = dark_wizard
                    print("The new monster that is arriving is a",current_enemy)
                    break
                elif done == "winner!":
                    print("Good job!")
                    return "gamedone"
                else:
                    


                    

                    #calling of the computer combat function
                    ogenemyhp = enemy["hp"]
                    resultofcombat = compcombat(enemy, plyr)
                    if resultofcombat == "wump_wump":
                        print("You died!")
                        time.sleep(1)
                        print("This means that you lose all of your xp, but don't worry, your character is still saved.")
                        with open("Battle Simulator/characters.csv", "r") as file:
                            csv_reader = csv.reader(file)
                            rows = list(csv_reader)

                        for row in rows:
                            if row[0] == plyr["username"]:
                                row[6] = "0"

                        with open("Battle Simulator/characters.csv", "w", newline="") as file:
                            csv_writer = csv.writer(file)
                            csv_writer.writerows(rows)

                        signedin = False
                        restart(signedin)
                        break
                    if resultofcombat == "done":
                        enemy["hp"] = ogenemyhp
                        break
                    elif resultofcombat == "win!!!":
                        return "gamedone"
                    else:
                        plyr["hp"] = resultofcombat

                        with open("Battle Simulator/characters.csv", "r") as file:
                            csv_reader = csv.reader(file)
                            rows = list(csv_reader)

                        for row in rows:
                            if row[0] == plyr["username"]:
                                row[2] = str(plyr["hp"])

                        with open("Battle Simulator/characters.csv", "w", newline="") as file:
                            csv_writer = csv.writer(file)
                            csv_writer.writerows(rows)
        elif choice == "2":
            if 0 <= plyr["xp"] and plyr["xp"] < 50:
                level = 1
            elif 50 <= plyr["xp"] and plyr["xp"] < 150:
                level = 2
            elif 150 <= plyr["xp"] and plyr["xp"] < 300:
                level = 3
            elif 300 <= plyr["xp"] and plyr["xp"] < 500:
                level = 4
            elif 500 <= plyr["xp"] and plyr["xp"] < 750:
                level = 5
            else:
                level = 6
            print("Here are your stats:")
            print(f"Attack: {plyr["attack"]}")
            print(f"Armor: {plyr["armor"]}")
            print(f"Dexterity: {plyr["dexterity"]}")
            print(f"Hp: {plyr["hp"]}")
            print(f"Level: {level}")


#calling of the main function
main(signedin)
