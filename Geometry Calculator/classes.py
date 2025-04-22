#Samuel Andelin, Classes Project: Geometry Calculator

#importing math
import math

#class for circle
class circle:
    #initializing self attributes
    def __init__(self, name, radius):
        self.radius = radius
        self.name = name

    #method for area
    def area(self):
        #calculate area
        area = math.pi*(self.radius**2)
        #return area
        return area

    #method for perimeter
    def perimeter(self):
        #calculate perimeter
        perimeter = 2*math.pi*self.radius
        #return perimeter
        return perimeter
    
    #method to print attributes about self
    def __str__(self):
        return f"Name: {self.name}\nRadius: {self.radius}\nArea: {round(self.area(), 2)}\nPerimeter: {round(self.perimeter(), 2)}"

    #static method to print the formulas used
    def formulas():
        print("Area: pi * radius^2")
        print("Perimeter: 2*pi*radius")

    #method to compare areas of circles
    def compare_area(self, circle2):
        if self.area() > circle2.area():
            print(f"{self.name} has the greater area!")
        elif circle2.area() > self.area():
            print(f"{circle2.name} has the greater area!")
        else:
            print(f"{self.name} and {circle2.name} have the same area!")

    #method to compare perimeters of circles
    def compare_perimeter(self, circle2):
        if self.perimeter() > circle2.perimeter():
            print(f"{self.name} has the greater perimeter!")
        elif circle2.perimeter() > self.perimeter():
            print(f"{circle2.name} has the greater perimeter!")
        else:
            print(f"{self.name} and {circle2.name} have the same size of perimeter!")

#class for rectangle
class rectangle:
    #initializing self attributes
    def __init__(self, name, length, height):
        self.length = length
        self.height = height
        self.name = name

    #method for area
    def area(self):
        #calculate area
        area = self.length*self.height
        #return area
        return area

    #method for perimeter
    def perimeter(self):
        #calculate perimeter
        perimeter = (2 * self.length) + (2*self.height)
        #return perimeter
        return perimeter
    
    #method to print attributes about self
    def __str__(self):
        return f"Name: {self.name}\nLength: {self.length}\nHeight: {self.height}\nArea: {round(self.area(), 2)}\nPerimeter: {round(self.perimeter(), 2)}"

    #static method to print the formulas used
    def formulas():
        print("Area: length*height")
        print("Perimeter: 2*length + 2*height")

    #method to compare areas of rectangles
    def compare_area(self, rect2):
        if self.area() > rect2.area():
            print(f"{self.name} has the greater area!")
        elif rect2.area() > self.area():
            print(f"{rect2.name} has the greater area!")
        else:
            print(f"{self.name} and {rect2.name} have the same size of area!")

    #method to compare perimeters of rectangles
    def compare_perimeter(self, rectangle2):
        if self.perimeter() > rectangle2.perimeter():
            print(f"{self.name} has the greater perimeter!")
        elif rectangle2.perimeter() > self.perimeter():
            print(f"{rectangle2.name} has the greater perimeter!")
        else:
            print(f"{self.name} and {rectangle2.name} have the same size of perimeter!")


#subclass for square
class square(rectangle):
    #initializing self attributes
    def __init__(self, name, length, height):
        #inherits name and length from rectangle
        super().__init__(name, length, height)
    
    #method for area
    def area(self):
        #calculate area
        area = self.length**2
        #return area
        return area
    
    #method for perimeter
    def perimeter(self):
        #calculate perimeter
        perimeter = 4 * self.length
        #return perimeter
        return perimeter

    #method to print attributes about self
    def __str__(self):
        return f"Name: {self.name}\nEvery Side length: {self.length}\nArea: {round(self.area(), 2)}\nPerimeter: {round(self.perimeter(), 2)}"
    
    #static method to print the formulas used
    def formulas():
        print("Area: length^2")
        print("Perimeter: length*4")

    #method to compare areas of squares
    def compare_area(self, square2):
        if self.area() > square2.area():
            print(f"{self.name} has the greater area!")
        elif square2.area() > self.area():
            print(f"{square2.name} has the greater area!")
        else:
            print(f"{self.name} and {square2.name} have the same size of area!")

    #method to compare perimeters of squares
    def compare_perimeter(self, square2):
        if self.perimeter() > square2.perimeter():
            print(f"{self.name} has the greater perimeter!")
        elif square2.perimeter() > self.perimeter():
            print(f"{square2.name} has the greater perimeter!")
        else:
            print(f"{self.name} and {square2.name} have the same size of perimeter!")

#class for triangle
class triangle:
    #initializing self attributes
    def __init__(self, name, base, side2, side3, height):
        self.name = name
        self.base = base
        self.height = height
        self.side2 = side2
        self.side3 = side3
    
    #method for area
    def area(self):
        #calculate area
        area = (self.height * self.base)/2
        #return area
        return area

    #method for perimeter
    def perimeter(self):
        #calculate perimeter
        perimeter = self.base + self.side2 + self.side3
        #return perimeter
        return perimeter
    
    #method to print attributes about self
    def __str__(self):
        return f"Name: {self.name}\nBase/Side 1 Length: {self.base}\nHeight: {self.height}\nSide 2 Length: {self.side2}\nSide 3 Length: {self.side3}\nArea: {round(self.area(), 2)}\nPerimeter: {round(self.perimeter(), 2)}"

    #static method to print the formulas used
    def formulas():
        print("Area: 0.5*base*height")
        print("Perimeter: base+side2+side3")
    
    #method to compare areas of triangles
    def compare_area(self, triangle2):
        if self.area() > triangle2.area():
            print(f"{self.name} has the greater area!")
        elif triangle2.area() > self.area():
            print(f"{triangle2.name} has the greater area!")
        else:
            print(f"{self.name} and {triangle2.name} have the same size of area!")

    #method to compare perimeters of triangles
    def compare_perimeter(self, triangle2):
        if self.perimeter() > triangle2.perimeter():
            print(f"{self.name} has the greater perimeter!")
        elif triangle2.perimeter() > self.perimeter():
            print(f"{triangle2.name} has the greater perimeter!")
        else:
            print(f"{self.name} and {triangle2.name} have the same size of perimeter!")
