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
        area = math.pi*(self.radius^2)
        #print area
        print(f"The radius of {self.name} is approximately {round(area, 2)}.")

    #method for perimeter
    def perimeter(self):
        #calculate perimeter
        perimeter = 2*math.pi*self.radius
        #print perimeter
        print(f"The perimeter of {self.name} is approximately {round(perimeter, 2)}.")
    
    #method to print attributes about self
    def __str__(self):
        return f"Name: {self.name}\nRadius: {self.radius}"

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
        #print area
        print(f"The area of {self.name} is approximately {round(area, 2)}.")

    #method for perimeter
    def perimeter(self):
        #calculate perimeter
        perimeter = (2 * self.length) + (2*self.height)
        #print perimeter
        print(f"The perimeter of {self.name} is approximately {round(perimeter, 2)}.")

#subclass for square
class square(rectangle):
    #initializing self attributes
    def __init__(self, name, length):
        #inherits name and length from rectangle
        super().__init__(name, length)
    
    #method for area
    def area(self):
        #calculate area
        area = self.length^2
        #print area
        print(f"The area of {self.name} is approximately {round(area, 2)}.")
    
    #method for perimeter
    def perimeter(self):
        #calculate perimeter
        perimeter = 4 * self.length
        #print perimeter
        print(f"The perimeter of {self.name} is approximately {round(perimeter, 2)}.")

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
        #print area
        print(f"The area of {self.name} is approximately {round(area, 2)}.")

    #method for perimeter
    def perimeter(self):
        #calculate perimeter
        perimeter = self.base + self.side2 + self.side3
        #print perimeter
        print(f"The perimeter of {self.name} is approximately {round(perimeter, 2)}.")


    


