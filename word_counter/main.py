#Samuel Andelin, Word Counter

#importing functions from other files
from file_reading import file_read as view_file
from time_stamp import time_stamp as time
from word_count import word_count as words

#main function
def main():
    print("Welcome to the word counter!")
    while True:
        #asks for the user to give the file path of the file they are writing to
        filename = input("To start, give the relative path of the file that you want to work with.(Or type exit to exit)\n-->")
        
        #if the user wants to exit, do so
        if filename == "exit":
            return
        
        #checks if the filename actually exists
        try:
            with open(filename, "r"):
                pass
            break
        except:
            print("Invalid relative path!")

    #variable to run the word counter for the first time
    done = False

    #enters the main loop where user can choose to view the document, view the word count (with a timestamp if the word count has changed) or exit
    while True:
        #asks user if they want to view the file, view the word count, or exit
        choice = input("Type 1 to view current document, type 2 to view the word count, and type 3 to exit.\n-->")
        
        #if the user wants to view the file
        if choice == "1":
            #call the function to view the file
            view_file(filename)

        #if the user wants to view the word count
        elif choice == "2":
            #if it is the first time running the word count function in the code, run it and then move on
            if not done:
                #sets the previous word count to the word count currently so that the next time the function is run, it has something to compare to
                previous_word_count = words(filename)
                #tells the program that it is done running the word count function for the first time
                done = True

            #if it is not the first time running the program    
            else:
                #the new word count is set
                new_word_count = words(filename)
                #if the word count has changed
                if new_word_count != previous_word_count:
                    #getting the timestamp
                    time_stamp = time()
                    #tells the user the last time that the document's word stamp was updated
                    print(f"Word count last updated at {time_stamp}.")
                #sets the previous word count to the current to compare to next time it is run
                previous_word_count = new_word_count

        #if the user wants to exit        
        elif choice == "3":
            break

        #if the user's input is invalid
        else:
            print("Invalid input!")



#calling of the main function
main()