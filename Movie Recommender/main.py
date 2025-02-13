#Samuel Andelin, Movie Recommender

#import csv reading 
import csv

#dictionary containing all information
movies = {}

#function to push all of the movies into a readable dictionary
def read():
    with open("Movie Recommender\Movies list.csv", "r") as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        for row in csv_reader:
            dictionary_to_push = {row[0]:{  
                                "Director" : row[1],
                                "Genre" : row[2],
                                "Rating" : row[3],
                                "Length" : row[4],
                                "Notable Actors" : row[5:]
                                }}
            movies.update(dictionary_to_push)

#calling the reading function
read()

#add filter function
def add_filter():
    which_filter = input("Type 1 to add the title filter, \ntype 2 to add the director filter, \ntype 3 to add the genre filter, \ntype 4 to add the rating filter, \ntype 5 to add to the length filter, \ntype 6 to add the notable actors filter, \nand type 7 to exit.")



#search function
def search():
    choice = input("Type 1 to add a filter, type 2 to remove a filter, type 3 to view the movies with the filters, and type 4 to exit.\n-->")
    if choice == "1":
        add_filter()

#view function
def view():
    print("Here are all of your movies:")
    num = 0
    for movie in movies:
        print(f"{movie}: ")
        for key, value in movies.items():
            print(key)
            for item in list(key.items()):
                print(item)
        num += 1

#main function
def main():
    print("Welcome to the movie recommender!")
    while True:
        choice = input("Type 1 to search, Type 2 to view the whole list, and type 3 to exit.\n-->")
        if choice == "1":
            search()
        elif choice == "2":
            view()
        elif choice == "3":
            break

#calling of the main/user interface function
main()