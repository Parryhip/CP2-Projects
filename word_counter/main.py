#Samuel Andelin, Word Counter

#importing functions from other files
from file_reading import file_read as view_file
from time_stamp import time_stamp as time
from word_count import *

#getting the timestamp
a=time()
print(a)
#main function
def main():
    print("Welcome to the word counter!")
    while True:
        choice = input("Type 1 to view current document, type 2 to view the word count, and type 3 to exit.\n-->")
        if choice == "1":
            view_file()
        elif choice == "2":
            pass
        elif choice == "3":
            break
        else:
            print("Invalid input!")



#calling of the main function
main()