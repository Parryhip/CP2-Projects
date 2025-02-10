#Samuel Andelin, Reading files Notes

#How do you open a file in your program?
with open('Notes/things.txt', 'r') as file:
    content = file.read()

#How do you alter text to work as data in a program?:
    # read the file
    # set the file to be a variable


# What is a CSV file?:
    # Comma seperated values 
    # A lot more usable than txt files


# How are they used in programming?
    #used to save large pieces of info in a seperate file

import csv

with open("Notes\sample.csv", "r") as file:
    csv_reader = csv.reader(file)
    next(csv_reader)
    for row in csv_reader:
        print(f'username {row[0]}, favorite color {row[1]}')

