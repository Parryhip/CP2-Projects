#Samuel Andelin, Word counter

#file reading function
def file_read():
    with open("word_counter\\writing.txt", "r") as file:
        for line in file.readlines():
            print(line)