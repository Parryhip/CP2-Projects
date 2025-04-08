#Samuel Andelin, Personal Portfolio

def main():
    print("Welcome to my personal portfolio!")
    def descriptions():
        while True:
            num = 1
            projects = ["1st Semester Final", "Piglatin Converter", "Tic Tac Toe", "Movie Recommender", "Password Generator", "Financial Calculator"]
            for project in projects:
                print(f"{num}. {project}")
                num += 1
            choice = input("Type the number by the project that you want to view the description for.\n-->")
    def programs():
        pass
    while True:
        choice = input("Type 1 to view and run the programs, type 2 to view the descriptions, and type 3 to exit.\n-->")
        if choice == "1":
            programs()
        elif choice == "2":
            descriptions()
        else:
            print("Ok, bye!")