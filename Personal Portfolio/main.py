#Samuel Andelin, Personal Portfolio

def main():
    #greeting
    print("Welcome to my personal portfolio!")

    #inner function for holding the descriptions
    def descriptions():
        while True:
            #number to display the projects
            num = 1

            #all o fthe projects
            projects = ["1st Semester Final", "Piglatin Converter", "Tic Tac Toe", "Movie Recommender", "Password Generator", "Financial Calculator"]
            
            #prints all of the projects with a number by them
            for project in projects:
                print(f"{num}. {project}")
                num += 1

            try:
                #user choice to pick which project to view descriptions about
                choice = int(input("Type the number by the project that you want to view the description for(or type exit to exit).\n-->"))
                
                #if user wants to view description about the 1st project
                if choice == "1":
                    print("This project was my first semester final project, where I made a game where you fight monsters from room to room. To complete it, you have to defeat the final boss. You can get loot from monsters, which helps you defeat harder ones, such as the final boss. The process of coding this project was very stressful and rushed because I was studying for every final that week. From this project I learned better how to use dictionaries for information about specific places (rooms in this case) and how to hold attributes for those places. Overall, I am glad at how this project turned out and I am proud of the way I was able to implement so many cool features.")
                #if user wants to view description about the 2nd project
                elif choice == "2":
                    print("This project was made in my first semester class. In this project you type in a message and it converts it to piglatin, or vice versa. I really liked this project because it was a good and easy way to learn how to split and concatenate strings. It really helped me learn about string manipulation. The programming process on this one was pretty easy, there wasn't any stress, so I think that I was able to code in peace of mind.")
                #if user wants to view description about the 3rd project
                elif choice == "3":
                    print("This project was made in my first semester class and it is simply the classic tic tac toe game. You enter where you want to go as x and it plays the game against the computer. If you get three in a row, you win. If the computer gets three in a row, they win. I really liked coding this project because it helped me learn about lists and how to break up a project into simpler tasks, such as board viewing, player turn, computer turn, win checking, and the main function to run the game. The programming process on this project was generally pretty relaxed, but it was also a pretty big project, so it was very tedious.")
                #if user wants to view description about the 4th project
                elif choice == "4":
                    print("This project was made in my second semester class. It is a movie recommender where you can input filters and it will print out movies that meet those required filters. This project helped me to learn how to read from csvs and be able to filter data in a good fashion, such as iterating over movies in specific categories until they met all requirements. The programming process on this was frustrating because I had a lot of errors in my csv file reading. In the end though, I was able to work those out and get it working.")
                #if user wants to view description about the 5th project
                elif choice == "5":
                    print("This project was made in my second semester class. It generates passwords for specfic reuired amounts of special characters, numbers, and uppercase letters. I leanred more about conditionals paired with string reading because I had to check that the created passwords contained the required characters. The programming process on this project was very relazed and fun. i was able to have a lot of fun with this project in being able to customize the types of passwords it printed out.")
                #if user wants to view description about the 6th project
                elif choice == "6":
                    print("This project was made in my second semester class. It is a calculator that generates amounts of money for specific budgets, expenses, interest, loans, and more. I leanred more about functional decompostion in this project because I used a lot of seperate files for different things the user wanted to do. The programming process on this project was confusing because i didn't fully understand the project description at first and didn't really know very well how to fulfill the requirements.")
                #if the user doesn't input a valid number
                else:
                    print("Not a valid project number!")
            
            #if the user doesn't type a number (integer)
            except:
                #if the user is trying to exit, do so
                if choice == "exit":
                    return
                #else, tell them their input is invalid
                else:
                    print("Not a number!")
    def programs():
        while True:
            #number to display the projects
            num = 1

            #all of the projects
            projects = ["1st Semester Final", "Piglatin Converter", "Tic Tac Toe", "Movie Recommender", "Password Generator", "Financial Calculator"]
            
            #prints all of the projects with a number by them
            for project in projects:
                print(f"{num}. {project}")
                num += 1

            try:
                #user choice to pick which project to run
                choice = int(input("Type the number by the project that you want to run(or type exit to exit).\n-->"))
                
                #if user wants to run the 1st project
                if choice == "1":
                    pass
                #if user wants to run the 2nd project
                elif choice == "2":
                    pass
                #if user wants to run the 3rd project
                elif choice == "3":
                    pass
                #if user wants to run the 4th project
                elif choice == "4":
                    pass
                #if user wants to run the 5th project
                elif choice == "5":
                    pass
                #if user wants to run the 6th project
                elif choice == "6":
                    pass
                #if the user doesn't input a valid number
                else:
                    print("Not a valid project number!")
            
            #if the user doesn't type a number (integer)
            except:
                #if the user is trying to exit, do so
                if choice == "exit":
                    return
                #else, tell them their input is invalid
                else:
                    print("Not a number!")
    while True:
        choice = input("Type 1 to view and run the programs, type 2 to view the descriptions, and type 3 to exit.\n-->")
        if choice == "1":
            programs()
        elif choice == "2":
            descriptions()
        else:
            print("Ok, bye!")