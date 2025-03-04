#Samuel Andelin, Word Counter

def word_count(filename):
    count = 0
    past_char_is_letter = False 
    with open(filename, "r") as file:
        for line in file:
            for character in line:
                if character.isalpha():
                    if not past_char_is_letter:
                        count += 1
                    past_char_is_letter = True 
                else:
                    past_char_is_letter = False 
    print(f"The word count for your file is {count} words long.")
