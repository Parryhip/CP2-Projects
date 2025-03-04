#Samuel Andelin, Word counter

#file reading function
def file_read(filename):
    with open(filename, "r") as file:
        for line in file.readlines():
            print(line)