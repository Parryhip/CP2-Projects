#Samuel Andelin, Coin change problem

#United States function
def US():
    #while loop in case the user does something incorrectly
    while True:
        #try-except to handle the user inputting an invalid amount
        try:
            #asks user for the amount to convert to change
            amount = float(input("What is the amount of money in US dollars?(use decimals for cents)(will be rounded to the nearest cent)\n-->"))
        
        #if the user inputs something other than an integer or float
        except:
            print("Not a valid amount of money!")

        #if the user inputs a number less than a cent, tell them not to
        if amount < 0.01:
            print("Please input a number that is at least a cent!")
            continue

        #rounds the amount to the nearest cent
        amount = round(amount, 2)

        #opening file to use in read mode
        with open("Coin Change Problem/money.txt", "r") as file:
            #lists for holding items
            items = []
            usedcoins = []

            #iterates over every line
            for line in file:
                #splits each line and inputs the value of data and its name into the items list
                splitline = line.split(",")
                for item in splitline:
                    itemname, itemvalue = item.split("-") 
                    items.append([itemname,float(itemvalue)])
                #breaks out of loop because we just want the first line
                break

            #list to be able to modify of the coins
            possible_coins = items.copy()

            #loops until the amount left is 0
            while amount != 0 or amount < 0.01:
                #iterates over every coin
                for coin in possible_coins:
                    #if the biggest item's value is less than or equal to the user amount 
                    if possible_coins[-1][1] <= amount:
                        #subtract the coin amount from the user amount
                        amount -= float(round(possible_coins[-1][1], 2))

                        #append the coin onto the usedcoins list
                        usedcoins.append(possible_coins[-1][0])
                        print(amount)
                        amount = round(amount, 2)
                    #if the biggest coin is less than the amount left
                    else:
                        #remove it from the possible coin list
                        possible_coins.pop(-1)
                if amount < 0.01:
                    break

            #prints the change
            print("Your change is:")

            #prints the number of each coin used for change and its type
            for item in items:
                print(f"{item[0]}: {usedcoins.count(item[0])}")

            #returns to main function
            return              

        

#Europe function
def EU():
    #while loop in case the user does something incorrectly
    while True:
        #try-except to handle the user inputting an invalid amount
        try:
            #asks user for the amount to convert to change
            amount = float(input("What is the amount of money in euros?(use decimals for euro cents)(will be rounded to the nearest cent)\n-->"))
            
        #if the user inputs something other than an integer or float
        except:
            print("Not a valid amount of money!")
        
        #if the user inputs a number less than a cent, tell them not to
        if amount < 0.01:
            print("Please input a number that is at least a euro cent!")
            continue

        #rounds the amount to the nearest cent
        amount = round(amount, 2)

        #opening file to use in read mode
        with open("Coin Change Problem/money.txt", "r") as file:
            #lists for holding items
            items = []
            usedcoins = []

            #line count to track which line we are on
            line_count = 1

            #iterates over every line
            for line in file:
                #checks that the line is the second
                if line_count == 2:
                    pass
                #if the line isn't the second, add 1 to the line ocunt and continue to the next iteration
                else:
                    line_count += 1
                    continue
                #splits each line and inputs the value of data and its name into the items list
                splitline = line.split(",")
                for item in splitline:
                    itemname, itemvalue = item.split("-") 
                    items.append([itemname,float(itemvalue)])
                #breaks out of loop because we just want the second line
                break

            #list to be able to modify of the coins
            possible_coins = items.copy()
            
            #loops until the amount left is 0
            while amount != 0 or amount < 0.01:
                #iterates over every coin
                for coin in possible_coins:
                    #if the biggest item's value is less than or equal to the user amount 
                    if possible_coins[-1][1] <= amount:
                        #subtract the coin amount from the user amount
                        amount -= round(possible_coins[-1][1], 2)
                        #append the coin onto the usedcoins list
                        usedcoins.append(possible_coins[-1][0])
                        amount = round(amount, 2)
                    #if the biggest coin is less than the amount left
                    else:
                        #remove it from the possible coin list
                        possible_coins.pop(-1)
                if amount < 0.01:
                    break
            
            #prints the change
            print("Your change is:")

            #prints the number of each coin used for change and its type
            for item in items:
                print(f"{item[0]}: {usedcoins.count(item[0])}")  

            #returns to main function
            return              
    

#Japan function
def JP():
    #while loop in case the user does something incorrectly
    while True:
        #try-except to handle the user inputting an invalid amount
        try:
            #asks user for the amount to convert to change
            amount = float(input("What is the amount of money in yen?(will be rounded to the nearest yen)\n-->"))              

        #if the user inputs something other than an integer or float
        except:
            print("Not a valid amount of money!")
        
        
        #if the user inputs a number less than a cent, tell them not to
        if amount < 1:
            print("Please input a number that is at least one yen!")
            continue

        #rounds the amount to the nearest cent
        amount = round(amount, 2)

        #opening file to use in read mode
        with open("Coin Change Problem/money.txt", "r") as file:
            #lists for holding items
            items = []
            usedcoins = []

            #line count to track which line we are on
            line_count = 1

            #iterates over every line
            for line in file:
                #checks that the line is the third
                if line_count == 3:
                    pass
                #if the line isn't the third, add 1 to the line ocunt and continue to the next iteration
                else:
                    line_count += 1
                    continue
                #splits each line and inputs the value of data and its name into the items list
                splitline = line.split(",")
                for item in splitline:
                    itemname, itemvalue = item.split("-") 
                    items.append([itemname,float(itemvalue)])
                #breaks out of loop because we just want the third line
                break

            #list to be able to modify of the coins
            possible_coins = items.copy()

            #loops until the amount left is 0
            while amount != 0 or amount < 1:
                #iterates over every coin
                for coin in possible_coins:
                    #if the biggest item's value is less than or equal to the user amount 
                    if possible_coins[-1][1] <= amount:
                        #subtract the coin amount from the user amount
                        amount -= round(possible_coins[-1][1], 2)
                        #append the coin onto the usedcoins list
                        usedcoins.append(possible_coins[-1][0])
                        amount = round(amount, 2)

                    #if the biggest coin is less than the amount left
                    else:
                        #remove it from the possible coin list
                        possible_coins.pop(-1)
                if amount < 0.01:
                    break

            #prints the change
            print("Your change is:")

            #prints the number of each coin used for change and its type
            for item in items:
                print(f"{item[0]}: {usedcoins.count(item[0])}")  

            #returns to main function
            return


#British/English function
def EN():
    #while loop in case the user does something incorrectly
    while True:
        #try-except to handle the user inputting an invalid amount
        try:
            #asks user for the amount to convert to change
            amount = float(input("What is the amount of money in pounds?(use decimals for pence)(will be rounded to the nearest pence)\n-->"))              

        #if the user inputs something other than an integer or float
        except:
            print("Not a valid amount of money!")
        
        
        #if the user inputs a number less than a cent, tell them not to
        if amount < 0.01:
            print("Please input a number that is at least one pence!")
            continue

        #rounds the amount to the nearest cent
        amount = round(amount, 2)

        #opening file to use in read mode
        with open("Coin Change Problem/money.txt", "r") as file:
            #lists for holding items
            items = []
            usedcoins = []

            #line count to track which line we are on
            line_count = 1

            #iterates over every line
            for line in file:
                #checks that the line is the fourth
                if line_count == 4:
                    pass
                #if the line isn't the fourth, add 1 to the line ocunt and continue to the next iteration
                else:
                    line_count += 1
                    continue
                #splits each line and inputs the value of data and its name into the items list
                splitline = line.split(",")
                for item in splitline:
                    itemname, itemvalue = item.split("-") 
                    items.append([itemname,float(itemvalue)])
                #breaks out of loop because we just want the fourth line
                break

            #list to be able to modify of the coins
            possible_coins = items.copy()

            #loops until the amount left is 0
            while amount != 0 or amount < 0.01:
                #iterates over every coin
                for coin in possible_coins:
                    #if the biggest item's value is less than or equal to the user amount 
                    if possible_coins[-1][1] <= amount:
                        #subtract the coin amount from the user amount
                        amount -= round(possible_coins[-1][1], 2)
                        #append the coin onto the usedcoins list
                        usedcoins.append(possible_coins[-1][0])
                        amount = round(amount, 2)
                        
                    #if the biggest coin is less than the amount left
                    else:
                        #remove it from the possible coin list
                        possible_coins.pop(-1)
                if amount < 0.01:
                    break

            #prints the change
            print("Your change is:")

            #prints the number of each coin used for change and its type
            for item in items:
                print(f"{item[0]}: {usedcoins.count(item[0])}")  

            #returns to main function
            return

