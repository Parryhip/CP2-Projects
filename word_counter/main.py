#Samuel Andelin, Word Counter

#importing functions from other files
from file_reading import file_read as view_file
from time_stamp import time_stamp as time
from word_count import word_count as words

#getting the timestamp
time_stamp = time()

#main function
def main():
    print("Welcome to the word counter!")
    print(f"File last updated at {time_stamp}.")
    while True:
        filename = input("To start, give the relative path of the file that you want to work with.(Or type exit to exit)\n-->")
        if filename == "exit":
            return
        try:
            with open(filename, "r"):
                pass
            break
        except:
            print("Invalid relative path!")
    while True:
        choice = input("Type 1 to view current document, type 2 to view the word count, and type 3 to exit.\n-->")
        if choice == "1":
            view_file(filename)
        elif choice == "2":
            words(filename)
        elif choice == "3":
            break
        else:
            print("Invalid input!")



#calling of the main function
main()