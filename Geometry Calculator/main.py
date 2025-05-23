#Samuel Andelin, Classes Project: Geometry Calculator

#importing neccesary functions
from shape_creation import create_square
from shape_creation import create_rectangle
from shape_creation import create_triangle
from shape_creation import create_circle
from sorting import sort

#importing all classes
from classes import square
from classes import rectangle
from classes import triangle
from classes import circle

#lists of all shapes
squares = []
rectangles = []
triangles = []
circles = []


#main function
def main():
    #greeting
    print("Welcome to the geometry calculator!")

    #main while loop
    while True:
        #main choice
        choice = input("Type 1 to make a new shape, \ntype 2 to view formulas for a shape, \ntype 3 to sort shapes by an attribute, \ntype 4 to print attributes for a shape, \ntype 5 to view all shape names, \ntype 6 to compare two shapes, \nand type 7 to exit.\n-->")
        
        #if the user wants to make a shape
        if choice == "1":
            while True:
                #user chooses what shape to make
                shape_choice = input("Type 1 to make a square, type 2 to make a rectangle, type 3 to make a triangle, type 4 to make a circle, and type 5 to go back.\n-->")
                
                #if the user wants to make a square
                if shape_choice == "1":
                    #call the create square function
                    new_square = create_square()

                    #if the user wants to exit, do so
                    if new_square == "exit":
                        break
                        
                    #add the new square to the list of all squares
                    squares.append(new_square)

                #if the user wants to make a rectangle
                elif shape_choice == "2":
                    #call the create rectangle function
                    new_rectangle = create_rectangle()

                    #if the user wants to exit, do so
                    if new_rectangle == "exit":
                        break
                        
                    #add the new rectangle to the list of all rectangles
                    rectangles.append(new_rectangle)

                #if the user wants to make a triangle
                elif shape_choice == "3":
                    #call the create triangle function
                    new_triangle = create_triangle()

                    #if the user wants to exit, do so
                    if new_triangle == "exit":
                        break
                        
                    #add the new triangle to the list of all triangles
                    triangles.append(new_triangle)

                #if the user wants to make a circle
                elif shape_choice == "4":
                    #call the create circle function
                    new_circle = create_circle()

                    #if the user wants to exit, do so
                    if new_circle == "exit":
                        break
                        
                    #add the new circle to the list of all circles
                    circles.append(new_circle)
                
                #if the user wants to exit, do so
                elif shape_choice == "5":
                    break

                #if the user's input is invalid, tell them
                else:
                    print("Not a valid input!")

        #if user wants to print out formulas
        elif choice == "2":
            while True:
                try:
                    #choice to view different formulas
                    formula_choice = input("Type 1 to view formulas for square, \ntype 2 to view formulas for rectangle, \ntype 3 to view formulas for triangle, \ntype 4 to view formulas for circle, \nand type 5 to exit.\n-->")
                    test = int(formula_choice)

                #if the user doesn't type a number
                except:
                    print("Invalid input!")
                    continue

                #if user wants to print formulas for square
                if formula_choice == "1":
                    square.formulas()

                #if user wants to print formulas for rectangle
                elif formula_choice == "2":
                    rectangle.formulas()
                    
                #if user wants to print formulas for triangle
                elif formula_choice == "3":
                    triangle.formulas()
                    
                #if user wants to print formulas for circle
                elif formula_choice == "4":
                    circle.formulas()
                    
                #if the user wants to exit
                elif formula_choice == "5":
                    break

                #if the user input is invalid, print that
                else:
                    print("Invalid input.")

        #if the user wants to sort by attributes
        elif choice == "3":
            while True:
                #choice to sort a specfic shape
                sort_choice = input("Type 1 to sort squares, type 2 to sort rectangles, type 3 to sort triangles, type 4 to sort circles, ande type 5 to exit.\n-->")

                #if the user wants to sort squares
                if sort_choice == "1":
                    sort(squares)
                
                #if the user wants to sort rectangles
                elif sort_choice == "2":
                    sort(rectangles)

                #if the user wants to sort triangles
                elif sort_choice == "3":
                    sort(triangles)

                #if the user wants to sort circles
                elif sort_choice == "4":
                    sort(circles)

                #if the user wants to exit
                elif sort_choice == "5":
                    break

                #if the user's input is invalid
                else:
                    print("Invalid input!")

        #if the user wants to see attributes for a shape
        elif choice == "4":
            while True:
                #input for the name of the shape the user wants to view attributes for
                shape_name = input("What is the name of the shape you want to see attributes for?(Or type exit to exit)\n-->")
                
                #if the user wants to exit
                if shape_name == "exit":
                    break

                #variable to hold the target shape
                targetitem = None

                #checking if the name of the shape is in the squares list
                for sq in squares:
                    if shape_name.strip() == sq.name.strip():
                        targetitem = sq
                        break
                
                #checking if the name of the shape is in the rectangles list
                for rect in rectangles:
                    if shape_name.strip() == rect.name.strip():
                        targetitem = rect
                        break

                #checking if the name of the shape is in the triangles list
                for tri in triangles:
                    if shape_name.strip() == tri.name.strip():
                        targetitem = tri
                        break

                #checking if the name of the shape is in the circles list
                for circ in circles:
                    if shape_name.strip() == circ.name.strip():
                        targetitem = circ
                        break

                #if the target item is still None, say that there is no shape with that name
                if targetitem == None:
                    print("No shape with that name!")
                    continue

                #print the attributes for the item via the __str__ method
                print(targetitem)

                #exit
                break

        #if the user wants to see the names of all of their shapes
        elif choice == "5":
            #prints all of the shapes' name
            print("----------ALL SHAPE NAMES----------")
            print("\n")
            print("\n")
            print("----------Squares----------")
            print("\n")
            for sq in squares:
                print(sq.name)
            print("\n")
            print("----------Rectangles----------")
            print("\n")
            for rect in rectangles:
                print(rect.name)
            print("\n")
            print("----------Triangles----------")
            print("\n")
            for tri in triangles:
                print(tri.name)
            print("\n")
            print("----------Circles----------")
            print("\n")
            for circ in circles:
                print(circ.name)
            print("\n")

        #if the user wants to compare two shapes
        elif choice == "6":
            while True:
                #input for the name of the first shape the user wants to compare
                shape_name = input("What is the name of the first shape you want to compare?(Or type exit to exit)\n-->")
                
                #if the user wants to exit
                if shape_name == "exit":
                    break

                #variable to hold the target shape
                targetitem1 = None

                #checking if the name of the shape is in the squares list
                for sq in squares:
                    if shape_name.strip() == sq.name.strip():
                        targetitem1 = sq
                        break
                
                #checking if the name of the shape is in the rectangles list
                for rect in rectangles:
                    if shape_name.strip() == rect.name.strip():
                        targetitem1 = rect
                        break

                #checking if the name of the shape is in the triangles list
                for tri in triangles:
                    if shape_name.strip() == tri.name.strip():
                        targetitem1 = tri
                        break

                #checking if the name of the shape is in the circles list
                for circ in circles:
                    if shape_name.strip() == circ.name.strip():
                        targetitem1 = circ
                        break

                #if the target item is still None, say that there is no shape with that name
                if targetitem1 == None:
                    print("No shape with that name!")
                    continue

                #input for the name of the second shape the user wants to compare
                shape_name2 = input("What is the name of the second shape you want to compare?(Or type exit to exit)\n-->")
                
                #if the user wants to exit
                if shape_name2 == "exit":
                    break

                #variable to hold the target shape
                targetitem2 = None

                #checking if the name of the shape is in the squares list
                for sq in squares:
                    if shape_name2.strip() == sq.name.strip():
                        targetitem2 = sq
                        break
                
                #checking if the name of the shape is in the rectangles list
                for rect in rectangles:
                    if shape_name2.strip() == rect.name.strip():
                        targetitem2 = rect
                        break

                #checking if the name of the shape is in the triangles list
                for tri in triangles:
                    if shape_name2.strip() == tri.name.strip():
                        targetitem2 = tri
                        break

                #checking if the name of the shape is in the circles list
                for circ in circles:
                    if shape_name2.strip() == circ.name.strip():
                        targetitem2 = circ
                        break

                #if the target item is still None, say that there is no shape with that name
                if targetitem2 == None:
                    print("No shape with that name!")
                    continue

                #compares area and perimeter
                targetitem1.compare_area(targetitem2)
                targetitem1.compare_perimeter(targetitem2)
                
                #exit
                break

        #if the user wants to exit
        elif choice == "7":
            print("Ok, bye!")
            return
        
        #if the user's input is invalid
        else:
            print("Invalid input!")

#calling of the main function
main()
