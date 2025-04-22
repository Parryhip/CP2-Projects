#Samuel Andelin, Classes Project: Geometry Calculator

#function for sorting shapes
def sort(list):
    while True:
        #asks user what attribute they want to sort by
        sortby = input("Type 1 to sort by area, type 2 to sort by perimeter, and type 3 to exit.\n-->")
        
        #if the user wants to sort by area
        if sortby == "1":
            #sorts the list of shapes
            areasorted = sorted(list, key=lambda item: item.perimeter())

            #print the title
            print("-----------Sorted by Area (least to greatest)-----------")
            print("\n")

            #Iterate through every item in the sorted list
            for item in areasorted:
                #print the square
                print(item.name)

            #white space
            print("\n")

        #if the user wants to sort by perimeter
        elif sortby == "2":
            #sorts the list of shapes
            perimetersorted = sorted(list, key=lambda item: item.perimeter())

            #print the title
            print("-----------Sorted by Perimeter (least to greatest)-----------")
            print("\n")

            #Iterate through every item in the sorted list
            for item in perimetersorted:
                #print the item
                print(item.name)

            #white space
            print("\n")
        
        #if the user wants to exit
        elif sortby == "3":
            break

        #if the user's input is invalid
        else:
            print("Invalid input!")