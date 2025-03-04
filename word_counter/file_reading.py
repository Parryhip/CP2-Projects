#Samuel Andelin, Word counter

#file reading function
def file_read(filename):
    #opens the file in read mode
    with open(filename, "r") as file:
        #iterates over all of the lines in the file
        for line in file.readlines():
            #prints the line
            print(line)