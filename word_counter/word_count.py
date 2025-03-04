#Samuel Andelin, Word Counter

#word counting function
def word_count(filename):
    #word count variable
    count = 0

    #variable to track if the last character was a letter
    past_char_is_letter = False

    #opens the file as the keyword file 
    with open(filename, "r") as file:
        #iterates over each line in the file
        for line in file:
            #iterates over each character in the line
            for character in line:
                #if the character is a letter
                if character.isalpha():
                    #if the past character wasn't a letter
                    if not past_char_is_letter:
                        #increase the count
                        count += 1
                    #tell the prgram that the past character was a letter
                    past_char_is_letter = True 
                #if the past character was not a letter
                else:
                    #tell the program that the past character wasn't a letter
                    past_char_is_letter = False 
                    
    #prints the word count
    print(f"The word count for your file is {count} words long.")

    #returns the word count for comparing if there needs to be a new timestamp or not
    return count
