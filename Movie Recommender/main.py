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

#list of all filters
filters = []

#add filter function
def add_filter():
    while True:
        print("Here are all of your filters so far:")
        for filter in filters:
            print(f"{filter[0]}: {filter[1]}")
        which_filter = input("Type 1 to add the title filter, \ntype 2 to add the director filter, \ntype 3 to add the genre filter, \ntype 4 to add the rating filter, \ntype 5 to add to the length filter, \ntype 6 to add the notable actors filter, \nand type 7 to exit.")
        try:
            test = int(which_filter)
        except:
            print("Please type a number!")
            continue
        if which_filter ==  "1":
            title = input("What is the name of the title that you want to search by?\n-->")
            filters.append(("Title", title))
        elif which_filter == "2":
            director = input("What is the name of the director that you want to search for?\n-->")
            filters.append(("Director", director))
        elif which_filter == "3":
            genre = input("What is the name of the genre that you want to search for?\n-->")
            filters.append(("Genre", genre))
        elif which_filter == "4":
            while True:
                rating = input("What is the name of the rating that you want to search for?(G, PG, PG-13, R)\n-->")
                if rating.upper() != "G" and rating.upper() != "PG" and rating.upper() != "PG-13" and rating.upper() != "R":
                    print("Not a valid rating!!!")
                else:
                    filters.append(("Rating", rating))
                    break
        elif which_filter == "5":
            while True:
                length = input("What is the name of the length that you want to search for? (Automatically searches for movies 20 minutes above and below the input)\n-->")
                try:
                    test = int(length)
                except:
                    print("Not a number!!!")
                    continue
                if int(length) < 0:
                    print("No negative lengths!")
                    continue
                if int(length)-20 < 0:
                    filters.append(("Length", (0,int(length)+20)))
                    break
                else:
                    filters.append(("Length", (int(length)-20,int(length)+20)))
                    break
        elif which_filter == "6":
            while True:
                actors = input("What is the name of the notable actor that you want to search for?\n-->")
                filters.append("Notable Actor", actors)
        elif which_filter == "7":
            return

#function to remove a filter
def remove_filter():
    while True:
        print("Here are all of your filters so far:")
        for filter in filters:
            print(f"{filter[0]}: {filter[1]}")
        print("Here are all of your filters so far:")
        for filter in filters:
            print(f"{filter[0]}: {filter[1]}")
        which_filter = input("Type 1 to remove the title filter, \ntype 2 to remove the director filter, \ntype 3 to remove the genre filter, \ntype 4 to remove the rating filter, \ntype 5 to remove to the length filter, \ntype 6 to remove the notable actors filter, \nand type 7 to exit.")
        try:
            test = int(which_filter)
        except:
            print("Please type a number!")
            continue
        if which_filter ==  "1":
            num = 0
            print("Here are all of the title filters that you have:")
            for filter in filters:
                if filter[0] == "Title":
                    print(f"{num}: {filter[1]}")
                    num += 1
        elif which_filter == "2":
            num = 0
            print("Here are all of the director filters that you have:")
            for filter in filters:
                if filter[0] == "Director":
                    print(f"{num}: {filter[1]}")
                    num += 1
        elif which_filter == "3":
            num = 0
            print("Here are all of the genre filters that you have:")
            for filter in filters:
                if filter[0] == "Genre":
                    print(f"{num}: {filter[1]}")
                    num += 1
        elif which_filter == "4":
            num = 0
            print("Here are all of the rating filters that you have:")
            for filter in filters:
                if filter[0] == "Rating":
                    print(f"{num}: {filter[1]}")
                    num += 1
        elif which_filter == "5":
            num = 0
            print("Here are all of the length filters that you have:")
            for filter in filters:
                if filter[0] == "Length":
                    print(f"{num}: {filter[1]}")
                    num += 1
        elif which_filter == "6":
            num = 0
            print("Here are all of the notable actor filters that you have:")
            for filter in filters:
                if filter[0] == "Notable Actor":
                    print(f"{num}: {filter[1]}")
                    num += 1
        elif which_filter == "7":
            return

#viewing the movies with the filters function
def view_with_filters():
    pass

#search function
def search():
    while True:
        choice = input("Type 1 to add a filter, type 2 to remove a filter, type 3 to view the movies with the filters, and type 4 to exit.\n-->")
        if choice == "1":
            add_filter()
        elif choice == "2":
            remove_filter()
        elif choice == "3":
            view_with_filters()
        elif choice == "4":
            return
        else:
            print("Not a valid input!!!")

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