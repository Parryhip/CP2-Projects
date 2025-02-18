#Samuel Andelin, Write To Notes

import csv

#How do you find a file in a folder? 
'''
Use its relative path by right clicking on it
'''

#In a python project how do you open a file?
with open('Notes\\things.txt', "w+") as file:
    file.write("This is now on my file")
    print(file.read())

with open('Notes\\things.txt', "a") as file:
    print(file.write('\n I just made another line on my file!'))

with open('Notes\\things.txt', "r") as file:
    print(file.read())

with open('Notes\\things.txt', "r") as file:
    print(file.read())

#What is the difference between writing, appending, and creation modes?
'''
r = read
w = write (overwrites whatever is already there)
w+ = read and write
a = add to what is already there
a+ + add to what is already there and read
x = new file

'''





#------------------CSV FILES---------------------------

with open('Notes\sample.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["new_user","black"])

with open("Notes\sample.csv", "r") as file:
    csv_reader = csv.reader(file)
    next(csv_reader)
    for row in csv_reader:
        print(f'username {row[0]}, favorite color {row[1]}')