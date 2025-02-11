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

def main():
    print("Welcome to the movie recommender!")
    while True:
        choice = input("Type 1 to search, Type 2 to get a recommendation, Type 3 to view the whole list, and type 4 to exit.\n-->")
        if choice == "1":
            while True:
                criteria_num = input("How many criteria do you want to search by? (Out of title, director, genre, rating, length, and notable actors) (or type exit to exit)\n-->")
                try:
                    test = int(criteria_num)
                except:
                    print("Not a number! Please type between 1-6.")
                    continue
                if int(criteria_num) > 6 or int(criteria_num) < 1:
                    print("Invalid number of criteria. Please type between 1-6.")
                    continue
                for i in range(int(criteria_num)):
                    criteria = input()

#calling of the main/user interface function
main()