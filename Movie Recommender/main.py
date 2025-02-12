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

#search function
def search():
    while True:
        possible_criteria = ["title", "director", "genre", "rating", "notable actors"]
        criteria_num = input("How many criteria do you want to search by? (Out of title, director, genre, rating, length, and notable actors) (or type exit to exit)\n-->")
        try:
            test = int(criteria_num)
        except:
            print("Not a number! Please type between 1-6.")
            continue
        if int(criteria_num) > 6 or int(criteria_num) < 1:
            print("Invalid number of criteria. Please type between 1-6.")
            continue
        while True:
            for i in range(int(criteria_num)):
                criterias = []
                criteria = input("What is the name of the criteria that you want to search for? (Out of title, director, genre, rating, length, and notable actors) (or type exit to exit)\n-->")
                if criteria == "exit":
                    return
                if criteria.capitalize() in possible_criteria and criteria.capitalize() not in criterias:
                    criterias.append("criteria")
                else:
                    num += 1
                    break
            if num == 0:
                break
            else:
                print("Not a valid criteria!")
                continue
        searches = []
        for item in criterias:
            if item.capitalize == "Notable Actors":
                specific_search = input("What are the notable actors that you want to search for? (Input as a comma seperated list)\n-->")
                searches.append((item.capitalize(), specific_search.split(",")))
            else:
                specific_search = input(f"What is the {item} that you want to search for?\n-->")
                searches.append((item.capitalize(), specific_search))
        print("Here are the movies with: ")
        num2 = 0
        for item2 in searches:
            print(f"{item2[0]} of {item2[1]}")
            if "Title" in item2:
                num2 +=1
        if num2 > 0:
            valid = False
            for search in searches:
                if "Title" in search:
                    for movie in movies:
                        if search[1] in movie.keys():
                            current_movie = movie
                            valid = True
                            breakout = True
                            searches.remove(search)
                            break
                        else:
                            breakout = False
                if breakout:
                    break
            if valid:
                for search in searches:
                    for movie in movies:
                        if search[0] == "Notable Actors":
                            pass
                            if search[1] in movie[search[0]]:
                                pass

            else:
                pass
            
        else:
            pass

            


#main function
def main():
    print("Welcome to the movie recommender!")
    while True:
        choice = input("Type 1 to search, Type 2 to view the whole list, and type 3 to exit.\n-->")
        if choice == "1":
            search()

#calling of the main/user interface function
main()