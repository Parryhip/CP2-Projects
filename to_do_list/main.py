#Samuel Andelin, To Do List

#list holding all items to do
items_to_do =  []

#reading the txt file function
def read():
    #reads txt file and pushes it into a list
    with open("to_do_list\\list.txt","r") as file:
        for line in file:
            line_to_push = line.split(":")
            items_to_do.append([line_to_push[0], line_to_push[1]])

#call the read function every time the program starts
read()

#add item function
def add():
    while True:
        #asks what the name of the item the user wants to add to the to do list
        item_to_add = input("What is the name of the item that you want to add to the to do list?\n-->")
        
        #if the user wants to name their item "exit"
        if item_to_add.lower() == "exit":
            #tell them they can't because I use that keyword to let the user exit
            print("Please don't use that name O-O.")
            continue

        #if the name is not "exit", add the item as incomplete
        items_to_do.append([item_to_add, "Incomplete"])

        #clear the txt file
        with open("to_do_list\\list.txt", "w") as file:
            file.write("")
        #rewrite new contents
        with open("to_do_list\\list.txt", "a+") as file:
            for item in items_to_do:
                try:
                    file.write(f"{item[0]}:{item[1]}")
                    file.write("\n")
                except:
                    file.write(f"{item[0]}:{"Incomplete"}")
                    file.write("\n")
        print("Successfully added!")
        break

#remove item function
def remove():
    while True:
        #number to see if there is an item that is the user inputs input
        num = 0

        #prints to do list
        print("This is your to do list:")
        for item in items_to_do:
            print(f"{item[0]}: {item[1]}")

        #asks which item to remove
        item_to_remove = input("What is the name of the item that you want to remove?(or type exit to exit)\n-->")
        
        #if they want to exit
        if item_to_remove == "exit":
            break

        #else, check if the item is in the to do list
        for item in items_to_do:
            #if the item is in the to do list:
            if item_to_remove.lower() == item[0].lower(): 
                #remove item
                items_to_do.remove(item)
                num += 1
                break

        #if the item is in the to do list:
        if num != 0:
            #clear the txt file
            with open("to_do_list\\list.txt", "w") as file:
                file.write("")

            #rewrite the txt file with the new contents
            with open("to_do_list\\list.txt", "a+") as file:
                for item in items_to_do:
                    try:
                        file.write(f"{item[0]}:{item[1]}")
                        file.write("\n")
                    except:
                        file.write(f"{item[0]}:{"Incomplete"}")
                        file.write("\n")
            print("Item successfully deleted!")
            break

        #if the item is not in the text file, loop to the start
        else:
            print("Item not found!")
            continue

#update item function
def update():
    while True:
        #number to see if there is an item that is the user inputs input
        num = 0

        #print to do list
        print("This is your to do list:")
        for item in items_to_do:
            print(f"{item[0]}: {item[1]}")

        #ask if the user wants to mark the file as complete or incomplete
        type_of_update = input("Type 1 to change an item to complete, type 2 to change an item to incomplete, and type 3 to exit.\n-->")
        
        #if the user wants to mark an item complete
        if type_of_update == "1":
            update_to = "Complete"
        #if the user wants to mark an item incomplete
        elif type_of_update == "2":
            update_to = "Incomplete"
        #if the user wants to exit
        elif type_of_update == "3":
            break
        else:
            print("Invalid input!")
            continue

        #ask which item to update
        item_to_update = input("What is the name of the item that you want to update?(or type exit to exit)\n-->")
        
        #if the user wants to exit
        if item_to_update == "exit":
            break

        #check if the user input is in the txt file
        for item in items_to_do:
            #if it is, rewrite the item as complete or incomplete
            if item_to_update.lower() == item[0].lower():
                items_to_do.append([item[0], update_to])
                items_to_do.remove(item)
                num += 1
                break

        #if the user input is in the txt file
        if num != 0:
            #clear the txt file
            with open("to_do_list\\list.txt", "w") as file:
                file.write("")
            #rewrite all contents of the txt file
            with open("to_do_list\\list.txt", "a+") as file:
                for item in items_to_do:
                    try:
                        file.write(f"{item[0]}:{item[1]}")
                        file.write("\n")
                    except:
                        file.write(f"{item[0]}:{"Incomplete"}")
                        file.write("\n")
            print("Item successfully updated!")
            break
        #if the item isn't in the txt file
        else:
            print("Item not found!")
            continue

#view function
def view():
    #prints to do list
    print("This is your to do list:")
    for item in items_to_do:
        print(f"{item[0]}: {item[1]}")


#main/UI function
def main():
    print("Welcome to the to do list!")
    while True:
        #user is asked where they want to go
        choice = input("Type 1 to add an item, type 2 to remove an item, type 3 to update an item, type 4 to view the whole list, and type 5 to exit.\n-->")
        
        #go to add item function
        if choice == "1":
            add()
        #go to remove item function
        elif choice == "2":
            remove()
        #go to update item function
        elif choice == "3":
            update()
        #go to view items function
        elif choice == "4":
            view()
        #exit whole system
        elif choice == "5":
            print("Bye!")
            break
        #else, print invalid input
        else:
            print("Invalid input.")
            continue
        
#calling of the main function
main()
