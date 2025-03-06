#Samuel Andelin, Battle Simulator

#importing time
import time
import random
import csv

#sign in function
def sign_in():
    while True:
        #user input to sign in, sign up, be anonymous, or exit
        choice = input("Type 1 to sign in, type 2 to sign up, type 3 to be anonymous, and type 4 to exit.\n-->")
        
        #if the user wants to sign in 
        if choice == "1":
            while True:
                #variable whether to exit or not
                go_to_first_choice = False

                #username login loop
                while True:
                    #variable whether to loop back or not
                    loopback = True

                    #user input for username
                    username = input("What is your username?(or type exit to exit)\n-->").strip()
                    
                    #if user wants to exit
                    if username.lower() == "exit":
                        go_to_first_choice = True
                        break

                    #reads all usernames and compares them to user input
                    with open("Battle Simulator\characters.csv", "r") as file:
                        for line in file:
                            items = line.split(":")
                            if username == items[0]:
                                loopback = False
                                break

                    #if the username isn't found        
                    if loopback:
                        print("Username not found!!!")
                        continue
                    else:
                        break
                if go_to_first_choice:
                    break

                #loop for password checking
                while True:
                    #variable to loopback or not
                    loopback = True

                    #user input for password
                    password = input("What is your password?(or type exit to exit)\n-->").strip()

                    #if the user wants to exit
                    if password.lower() == "exit":
                        go_to_first_choice = True
                        break

                    #reads all passwords and compares them
                    with open("Battle Simulator\characters.csv", "r") as file:
                        for line in file:
                            items = line.split(":")
                            if username == items[0]:
                                #if user input matches
                                if password == items[1]:
                                    print("Signed in successfully!")
                                    return username
                                #if user input doesn't match
                                else:
                                    print("Invalid password!")
                                    break
                    
                    if loopback:
                        continue
                if go_to_first_choice:
                    break
                
        #if the user wants to make an account        
        elif choice == "2":
            while True:
                #variable for looping back or not
                loopback = False

                #user input to create a new account username
                username = input("What is the username that you want to create?\n-->").strip()

                #if the user wants to make their username "exit" tell them no
                if username.lower() == "exit":
                    print("Don't use that username please.")
                    continue

                #checks if the username is already taken
                with open("Battle Simulator\characters.csv", "r") as file:
                    for line in file:
                        items = line.split(":")
                        if username == items[0]:
                            print("Username is already taken!")
                            loopback = True

                #if the prgram needs to loop back, do so
                if loopback:
                    continue

                #if not, exit the create username section
                else:
                    break
            while True:
                #user input to create a new account password
                password = input("What is the password that you want to create?\n-->").strip()

                #if the user wants to make their username "exit" tell them no
                if password.lower() == "exit":
                    print("Don't use that password please.")
                    continue

                #verification of password
                confirm_password = input("Please type your password again to confirm.\n-->")

                #if passwords match, input all info
                if password == confirm_password:
                    print("Username of",username,"and password of",password,"has been inputted successfully!")
                    with open("Battle Simulator\characters.csv", "a") as file:
                        file.write("\n")
                        file.write(username+":"+password)
                    def load_plyr():
                        with open("Battle Simulator\characters.csv", "r") as file:
                            csv_reader = csv.reader(file)
                            for line in csv_reader:
                                if line[0] == username:
                                    loaded_plyr = {}
                                    loaded_plyr["username"] = line[0]
                                    loaded_plyr["hp"] = line[1]
                                    loaded_plyr["items"] = line[2]
                                    loaded_plyr["equippeditems"] = line[3]
                                    loaded_plyr["attack"] = line[4]
                                    loaded_plyr["armor"] = line[5]
                                    loaded_plyr["dexterity"] = line[6]
                                    loaded_plyr["monsters_killed"] = line[7]
                                else:
                                    continue

                        return loaded_plyr
                    plyr = load_plyr()
                    print("Now lets roll some D20s for your hp!")
                    time.sleep(1)
                    print("You got ")
                    for i in range(0, 6):
                        roll = random.randint(1, 20)
                        plyr["hp"] = plyr["hp"] + roll
                        print(roll)
                        time.sleep(0.5)
                    print("Your hp is " + str(plyr["hp"]))
                    time.sleep(1)
                    print("Now let's roll some six sided dice for your attack!")
                    time.sleep(1)
                    print("You got ")
                    for i in range(0, 6):
                        roll = random.randint(1, 6)
                        plyr["attack"] = plyr["attack"] + roll
                        print(roll)
                        time.sleep(0.5)
                    print("Your attack is " + str(plyr["attack"]))
                    time.sleep(1)
                    print("Now let's roll some six sided dice for your dexterity!")
                    time.sleep(1)
                    print("You got ")
                    for i in range(0, 6):
                        roll = random.randint(1, 6)
                        plyr["dexterity"] = plyr["dexterity"] + roll
                        print(roll)
                        time.sleep(0.5)
                    print("Your dexterity is " + str(plyr["dexterity"]))
                    return plyr
                #if passwords don't match, loop back
                else:
                    print("Passwords do not match!!!")
                    continue
        
        #if the user wants to be anonymous
        elif choice == "3":
            return "anonymous"
        
        #if the user wants to exit
        elif choice == "4":
            return "exit"
        
        #if the user is stupid and can't figure out how to type a good input
        else:
            print("Not a valid option!")