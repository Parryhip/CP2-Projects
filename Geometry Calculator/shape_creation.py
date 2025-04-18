#Samuel Andelin, Classes Project: Geometry Calculator

#importing classes
from main import square
from main import rectangle
from main import triangle
from main import circle

#function to create a new square
def create_square():
    while True:
        #asks for the name of the square (or to exit)
        name = input("What is the name of your square?(or type exit to exit)\n-->")

        #if the user wants to exit, do so
        if name == "exit":
            return "exit"

        try:
            #asks the user for the length of the square
            side_length = input("What is the length/height of your square?\n-->")

            #tests if the number is below 0
            if side_length <= 0:
                raise Exception("That is not a positive number!")

            #tests if the length is an integer
            test = float(side_length)

        #if the user inputs a number below or equal to 0 or not a number at all, display that they need to change their input
        except:
            print("Please input a number above 0.")
            continue

        #print that the square was created successfully
        print("Square succesfully created!")

        #return the new square
        return square(name, side_length)
    
#function to make a new rectangle
def create_rectangle():
    while True:
        #asks for the name of the rectangle (or to exit)
        name = input("What is the name of your rectangle?(or type exit to exit)\n-->")

        #if the user wants to exit, do so
        if name == "exit":
            return "exit"

        try:
            #asks the user for the base/length of the rectangle
            base = input("What is the base/length of your rectangle?\n-->")

            #asks the user for the height of the rectangle
            height = input("What is the height of your rectangle?\n-->")

            #tests if the numbers are below 0
            if base <= 0 or height <= 0:
                raise Exception("That is not a positive number!")

            #tests if the lengths are floats/integers
            test1 = float(base)
            test2 = float(height)

        #if the user inputs a number below or equal to 0 or not a number at all, display that they need to change their input
        except:
            print("Please input a number above 0.")
            continue

        #print that the rectangle was created successfully
        print("Rectangle succesfully created!")

        #return the new rectangle
        return rectangle(name, base, height)
    
#function to create a triangle
def create_triangle():
    while True:
        #asks for the name of the triangle (or to exit)
        name = input("What is the name of your triangle?(or type exit to exit)\n-->")

        #if the user wants to exit, do so
        if name == "exit":
            return "exit"

        try:
            #asks the user for the base/side 1 of the triangle
            base = input("What is the base/side 1 length of your triangle?\n-->")

            #asks the user for the height of the triangle
            height = input("What is the height of your triangle?\n-->")

            #asks the user for the side 2 of the triangle
            side2 = input("What is the side 2 length of your triangle?\n-->")

            #asks the user for the side 3 of the triangle
            side3 = input("What is the side 3 length of your triangle?\n-->")

            #tests if the numbers are below 0
            if base <= 0 or height <= 0 or side2 <= 0 or side3 <= 0:
                raise Exception("That is not a positive number!")

            #tests if the lengths are floats/integers
            test1 = float(base)
            test2 = float(height)
            test3 = float(side2)
            test4 = float(side3)

        #if the user inputs a number below or equal to 0 or not a number at all, display that they need to change their input
        except:
            print("Please input a number above 0.")
            continue

        #print that the triangle was created successfully
        print("Triangle succesfully created!")

        #exit loop
        return triangle(name, base, side2, side3, height)
    
#function to create a new circle
def create_circle():
    while True:
        #asks for the name of the circle (or to exit)
        name = input("What is the name of your circle?(or type exit to exit)\n-->")

        #if the user wants to exit, do so
        if name == "exit":
            return "exit"

        try:
            #asks the user for the radius of the circle
            radius = input("What is the radius of your circle?\n-->")

            #tests if the numbers are below 0
            if radius <= 0:
                raise Exception("That is not a positive number!")

            #tests if the lengths are floats/integers
            test1 = float(radius)

        #if the user inputs a number below or equal to 0 or not a number at all, display that they need to change their input
        except:
            print("Please input a number above 0.")
            continue

        #print that the circle was created successfully
        print("Circle succesfully created!")

        #return new circle
        return circle(name, radius)