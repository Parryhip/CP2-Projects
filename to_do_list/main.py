#Samuel Andelin, To Do List

#list holding all items to do
items_to_do =  []

#reading the txt file function
def read():
    with open("to_do_list\list.txt","r") as file:
        for line in file:
            items_to_do.append([line[0], line[1]])

#call the read function every time the program starts
read()

#add item function
def add():
    item_to_add = input("What is the name of the item that you want to add to the to do list?\n-->")
    items_to_do.append("\n")
    items_to_do.append([item_to_add, "Incomplete"])
    with open("to_do_list\list.txt", "w") as file:
        file.write("")
    with open("to_do_list\list.txt", "a"):
        for item in items_to_do:
            file.append(item)
            file.append("\n")
    print("Successfully added!")

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
        item_to_remove = input("What is the name of the item that you want to update?(or type exit to exit)\n-->")
        if item_to_remove == "exit":
            break
        for item in items_to_do:
            if item_to_remove.lower() == item[0].lower():
                items_to_do.remove(item)
                num += 1
                break
        if num != 0:
            print("Item successfully deleted!")
            break
        else:
            print("Item not found!")
            continue



        
