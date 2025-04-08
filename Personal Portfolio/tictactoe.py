#Samuel Andelin, Tic Tac Toe
import random
row1 = ["", "", ""]
row2 = ["", "", ""]
row3 = ["", "", ""]
play_again = "y"
def spottaken(row, column):
    if row == 1:
        if column == 1:
            if row1[0] == "X":
                return True
            elif row1[0] == "O":
                return True
        if column == 2:
            if row1[1] == "X":
                return True
            elif row1[1] == "O":
                return True
        if column == 3:
            if row1[2] == "X":
                return True
            elif row1[2] == "O":
                return True
    elif row == 2:
        if column == 1:
            if row2[0] == "X":
                return True
            elif row2[0] == "O":
                return True
        if column == 2:
            if row2[1] == "X":
                return True
            elif row2[1] == "O":
                return True
        if column == 3:
            if row2[2] == "X":
                return True
            elif row2[2] == "O":
                return True
    elif row == 3:
        if column == 1:
            if row3[0] == "X":
                return True
            elif row3[0] == "O":
                return True
        if column == 2:
            if row3[1] == "X":
                return True
            elif row3[1] == "O":
                return True
        if column == 3:
            if row3[2] == "X":
                return True
            elif row3[2] == "O":
                return True
    else:
        return False
def display():
    print("The board now looks like this: ")
    lists = [row1, row2, row3]
    for list in lists:
        for i in range(len(list)):
            print(list[i], end="")
            print(" | ", end="")
            if i == 2 or i == 5:
                print("\n")
def plyrturn():
    while True:
        userrow = int(input("Which row do you want to play in(1/2/3)?: "))
        usercolumn = int(input("Which column do you want to play in?(1/2/3): "))
        if spottaken(int(userrow), int(usercolumn)) != True:
            if userrow == 1:
                if usercolumn == 1:
                    print("Ok!")
                    row1.pop(0)
                    row1.insert(0, "X")
                    display()

                    break
                elif usercolumn == 2:
                    print("Ok!")
                    row1.pop(1)
                    row1.insert(1, "X")
                    display()
                    break
                elif usercolumn == 3:
                    print("Ok!")
                    row1.pop(2)
                    row1.insert(2, "X")
                    display()
                    break
            elif userrow == 2:
                if usercolumn == 1:
                    print("Ok!")
                    row2.pop(0)
                    row2.insert(0, "X")
                    display()
                    break
                elif usercolumn == 2:
                    print("Ok!")
                    row2.pop(1)
                    row2.insert(1, "X")
                    display()
                    break
                elif usercolumn == 3:
                    print("Ok!")
                    row2.pop(2)
                    row2.insert(2, "X")
                    display()
                    break
            elif userrow == 3:
                if usercolumn == 1:
                    print("Ok!")
                    row3.pop(0)
                    row3.insert(0, "X")
                    display()
                    break
                elif usercolumn == 2:
                    print("Ok!")
                    row3.pop(1)
                    row3.insert(1, "X")
                    display()
                    break
                elif usercolumn == 3:
                    print("Ok!")
                    row3.pop(2)
                    row3.insert(2, "X")
                    display()
                    break
        else:
            print("Spot is taken. Please try again.")
def compturn():
    comprow = random.randint(1,3)
    compcolumn = random.randint(1,3)
    if spottaken(int(comprow), int(compcolumn)) != True:
        if comprow == 1:
            if compcolumn == 1:
                row1.pop(0)
                row1.insert(0, "O")
                display()
            if compcolumn == 2:
                row1.pop(1)
                row1.insert(1, "O")
                display()
            if compcolumn == 3:
                row1.pop(2)
                row1.insert(2, "O")
                display()
        if comprow == 2:
            if compcolumn == 1:
                row2.pop(0)
                row2.insert(0, "O")
                display()
            if compcolumn == 2:
                row2.pop(1)
                row2.insert(1, "O")
                display()
            if compcolumn == 3:
                row2.pop(2)
                row2.insert(2, "O")
                display()
        if comprow == 3:
            if compcolumn == 1:
                row3.pop(0)
                row3.insert(0, "O")
                display()
            if compcolumn == 2:
                row3.pop(1)
                row3.insert(1, "O")
                display()
            if compcolumn == 3:
                row3.pop(2)
                row3.insert(2, "O")
                display()
def game():
    while True:
        plyrturn()
        if row1[0] == "X" and row1[1] == "X" and row1[2] == "X":
            print("You won!")
            break
        elif row2[0] == "X" and row2[1] == "X" and row2[2] == "X":
            print("You won!")
            break
        elif row3[0] == "X" and row3[1] == "X" and row3[2] == "X":
            print("You won!")
            break
        elif row1[0] == "X" and row2[1] == "X" and row3[2] == "X":
            print("You won!")
            break
        elif row3[0] == "X" and row2[1] == "X" and row1[2] == "X":
            print("You won!")
            break
        elif row1[0] == "X" and row2[0] == "X" and row3[0] == "X":
            print("You won!")
            break
        elif row1[1] == "X" and row2[1] == "X" and row3[1] == "X":
            print("You won!")
            break
        elif row1[2] == "X" and row2[2] == "X" and row3[2] == "X":
            print("You won!")
            break
        compturn()
        if row1[0] == "O" and row1[1] == "O" and row1[2] == "O":
            print("You lost!")
            break
        elif row2[0] == "O" and row2[1] == "O" and row2[2] == "O":
            print("You lost!")
            break
        elif row3[0] == "O" and row3[1] == "O" and row3[2] == "O":
            print("You lost!")
            break
        elif row1[0] == "O" and row2[1] == "O" and row3[2] == "O":
            print("You lost!")
            break
        elif row3[0] == "O" and row2[1] == "O" and row1[2] == "O":
            print("You lost!")
            break
        elif row1[0] == "O" and row2[0] == "O" and row3[0] == "O":
            print("You lost!")
            break
        elif row1[1] == "O" and row2[1] == "O" and row3[1] == "O":
            print("You lost!")
            break
        elif row1[2] == "O" and row2[2] == "O" and row3[2] == "O":
            print("You lost!")
            break
while play_again == "y" or play_again == "Y":
    play_again = input("Do you want to play tic tac toe?(y/n): ")
    if play_again == "y":
        row1 = ["", "", ""]
        row2 = ["", "", ""]
        row3 = ["", "", ""]
        game()
    elif play_again == "n":
        print("Ok bye!")
    else:
        print("Not a valid input.")
        play_again = input("Do you want to play tic tac toe?(y/n): ")