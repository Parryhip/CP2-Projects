#samuel andelin, battle simulator

#importing time for pauses, random for the dice rolls, and csv for file handling
import time
import random
import csv

#importing neccessary functions
from combat import combat
from combat import compcombat
from sign_in import sign_in

#lists/dictionaries for enemy stats
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
    #if the user is already signed in
    if signedin:
        pass

    #if the user hasn't signed in yet
    else:
        #calls sign in function
        plyr = sign_in()

        #if the player wants to exit from the sign in function
        if plyr == "exit":
            #tell that to the main function that is calling restart
            return "exit", "exit"
        
        #set that the user is signed in
        signedin = True    

    #finds out which mode the user wants to play in
    while True:
        #asks which difficulty the user wants to play in
        difficulty = input("What difficulty do you want the fights to be? (easy, medium, hard)").lower()
        
        #adds monsters to the possible monsters list based on difficulty
        if difficulty == "easy":
            #easy mode only has goblin and orcs
            print("Ok! You decide to play on easy mode, where you only encounter goblins and orcs.")
            time.sleep(3)
            #adds the enemies to the list
            enemylist.append("goblin")
            enemylist.append("orc")
            return plyr, signedin
        elif difficulty == "medium":
            #medium mode has goblin, orcs, werewolves, and skeletons
            print("Ok! You decide to play on medium mode, where you only encounter skeletons, orcs, goblins, and werewolves.")
            time.sleep(3)
            #adds the enemies to the list
            enemylist.append("goblin")
            enemylist.append("orc")
            enemylist.append("werewolf")
            enemylist.append("skeleton")
            return plyr, signedin
        elif difficulty == "hard":
            #hard mode has goblin, orcs, werewolves, skeletons, gelatinous cubes, and dark wizards
            print("Ok! You decide to play on hard mode, where it makes there be super difficult monsters.")
            time.sleep(3)
            #adds the enemies to the list
            enemylist.append("goblin")
            enemylist.append("orc")
            enemylist.append("werewolf")
            enemylist.append("dark wizard")
            enemylist.append("gelatinous cube")
            return plyr, signedin
        #if the user finds it too hard to input a 4-6 letter word
        else:
            #tell them to try again
            print("Not valid difficulty.")
            continue
        



#main function
def main(signedin):
    #function for updating csv file
    def update_player_stat(plyr, stat, value):
        #opens csv file, reads it, and puts it into a list of rows to be used later
        with open("Battle Simulator/characters.csv", "r") as file:
            csv_reader = csv.reader(file)
            rows = list(csv_reader)

        #iterates over the rows and changes the stat
        for row in rows:
            if row[0] == plyr["username"]:
                row[stat] = str(value)

        #opens csv file and rewrites all of the contents with the updated ones
        with open("Battle Simulator/characters.csv", "w", newline="") as file:
            csv_writer = csv.writer(file)
            csv_writer.writerows(rows)


    #calls the function to restart
    plyr, signedin = restart(signedin)

    #if user wanted to exit in the sign in function
    if plyr == "exit":
        print("Ok, bye!")
        #exit
        return
    
    #chooses a random enemy to fight
    current_enemy = random.choice(enemylist)


    #changing the random string to a literal dictionary
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


    
    #main while loop
    while True:
        #prints what the current enemy is
        print("The current enemy is a",current_enemy+".")

        #asks user what they want to do
        choice = input("What do you want to do? (1 to enter combat, 2 to view stats, 3 to exit) ")

        #if the user wants to enter combat
        if choice == "1":
            print("You enter combat!")

            #main combat loop
            while True:
                #calls the player combat function
                done = combat(enemy,plyr)

                #if the player kills the monster, give them xp
                if done == "done":
                    #gives xp to the player based on what monster it is
                    if current_enemy == "goblin":
                        print("You earned 10 xp from killing that goblin!")
                        plyr["xp"] += 10
                    elif current_enemy == "orc":
                        print("You earned 25 xp from killing that orc!")
                        plyr["xp"] += 25
                    elif current_enemy == "werewolf":
                        print("You earned 50 xp from killing that werewolf!")
                        plyr["xp"] += 50
                    elif current_enemy == "skeleton":
                        print("You earned 50 xp from killing that skeleton!")
                        plyr["xp"] += 50
                    elif current_enemy == "gelatinous cube":
                        print("You earned 75 xp from killing that gelatinous cube!")
                        plyr["xp"] += 75
                    elif current_enemy == "dark wizard":
                        print("You earned 100 xp from killing that dark wizard!")
                        plyr["xp"] += 100

                    #update the xp
                    update_player_stat(plyr, 4, plyr["xp"])

                    #gets a new enemy
                    current_enemy = random.choice(enemylist)

                    #changing the random string to a literal dictionary copy (to change it more freely)
                    if current_enemy == "goblin":
                        enemy = goblin.copy()
                    elif current_enemy == "orc":
                        enemy = orc.copy()
                    elif current_enemy == "werewolf":
                        enemy = werewolf.copy()
                    elif current_enemy == "skeleton":
                        enemy = skeleton.copy()
                    elif current_enemy == "gelatinous cube":
                        enemy = gelatinous_cube.copy()
                    elif current_enemy == "dark wizard":
                        enemy = dark_wizard.copy()
                    #displays the new monster that is arriving
                    print("The new monster that is arriving is a",current_enemy)
                    break
                else:
                    #updates the enemy hp
                    enemy["hp"] = done

                    #calling of the computer combat function
                    resultofcombat = compcombat(enemy, plyr)

                    #if the player died during combat, reset xp and give them 50 hp
                    if resultofcombat == "wump_wump":
                        print("You died!")
                        time.sleep(1)
                        print("This means that you lose all of your xp, but don't worry, your character is still saved and revives with a base 50 hp.")
                        
                        #resetting stats
                        plyr["xp"] = 0
                        plyr["hp"] = 50
                        update_player_stat(plyr, 2, plyr["hp"])
                        update_player_stat(plyr, 4, plyr["xp"])

                        #have the player sign in again
                        signedin = False
                        if restart(signedin) == "exit":
                            return
                        break

                    #if the monster dies, exit combat loop
                    if resultofcombat == "done":
                        break

                    #if the fight is still going
                    else:
                        #updates the player hp
                        plyr["hp"] = resultofcombat
                        update_player_stat(plyr, 2, plyr["hp"])

        #if the user wants to view their stats
        elif choice == "2":
            #if statements find out which level the user is
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

            #prints stats
            print("Here are your stats:")
            print(f"Attack: {plyr["attack"]}")
            print(f"Hp: {plyr["hp"]}")
            print(f"Xp: {plyr["xp"]}")
            print(f"Level: {level}")
        
        #if the user wants to exit
        elif choice == "3":
            print("Ok, bye!")
            #exit
            return

#calling of the main function
main(signedin)
