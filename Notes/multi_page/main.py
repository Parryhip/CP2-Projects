#Samuel Andelin, Using Multiple Pages Notes

#----------------------------------------------------------How do you make multiple files in python?

#just make the file by selecting "new file"

#----------------------------------------------------------How do you get a function from another file

#import the function

from calcs import mult as x

print(x(43214513461515,6000000000000000000000000))

#----------------------------------------------------------How do you get variables from another file?

#Return the values through the functions

def returning_example():
    #do stuff
    thing = 67
    return thing

#----------------------------------------------------------How do you have a function with multiple returns?

#seperate with commas

def multiple_object_returns():
    return "matthew", 36, "orange"

#----------------------------------------------------------Why would you use multiple pages for a python project? 

#to organize things better