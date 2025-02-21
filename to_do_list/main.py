#Samuel Andelin, To Do List

#list holding all items to do
items_to_do =  []

#reading the txt file function
def read():
    with open("to_do_list\\list.txt","r") as file:
        for line in file:
            line_to_push = line.split(":")
            items_to_do.append([line_to_push[0], line_to_push[1]])

#call the read function every time the program starts
read()

#add item function
def add():
    while True:
        item_to_add = input("What is the name of the item that you want to add to the to do list?\n-->")
        if item_to_add.lower() == "exit":
            print("Please don't use that name O-O.")
            continue
        items_to_do.append([item_to_add, "Incomplete"])
        with open("to_do_list\\list.txt", "w") as file:
            file.write("")
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
        num = 0
        print("This is your to do list:")
        for item in items_to_do:
            print(f"{item[0]}: {item[1]}")
        item_to_remove = input("What is the name of the item that you want to remove?(or type exit to exit)\n-->")
        if item_to_remove == "exit":
            break
        for item in items_to_do:
            if item_to_remove.lower() == item[0].lower():
                items_to_do.remove(item)
                num += 1
                break
        if num != 0:
            with open("to_do_list\\list.txt", "w") as file:
                file.write("")
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
        else:
            print("Item not found!")
            continue

#update item function
def update():
    while True:
        num = 0
        print("This is your to do list:")
        for item in items_to_do:
            print(f"{item[0]}: {item[1]}")
        type_of_update = input("Type 1 to change an item to complete, type 2 to change an item to incomplete, and type 3 to exit.\n-->")
        if type_of_update == "1":
            update_to = "Complete"
        elif type_of_update == "2":
            update_to = "Incomplete"
        elif type_of_update == "3":
            break
        else:
            print("Invalid input!")
            continue
        item_to_update = input("What is the name of the item that you want to update?(or type exit to exit)\n-->")
        if item_to_update == "exit":
            break
        for item in items_to_do:
            if item_to_update.lower() == item[0].lower():
                items_to_do.append([item[0], update_to])
                items_to_do.remove(item)
                num += 1
                break
        if num != 0:
            with open("to_do_list\\list.txt", "w") as file:
                file.write("")
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
        else:
            print("Item not found!")
            continue

#view function
def view():
    print("This is your to do list:")
    for item in items_to_do:
        print(f"{item[0]}: {item[1]}")


#main/UI function
def main():
    print("Welcome to the to do list!")
    while True:
        choice = input("Type 1 to add an item, type 2 to remove an item, type 3 to update an item, type 4 to view the whole list, and type 5 to exit.\n-->")
        if choice == "1":
            add()
        elif choice == "2":
            remove()
        elif choice == "3":
            update()
        elif choice == "4":
            view()
        elif choice == "5":
            print("Bye!")
            break
        else:
            print("Invalid input.")
            continue
        
#calling of the main function
main()
