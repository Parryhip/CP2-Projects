#Samuel Andelin, Morse code Translator

#list of all letters in order
all_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '', ' ']

#list of all morse code letters in order
all_morse_code_letters = ['.-','-...','-.-.','-..','.','..-.','--.','....','..','.---','-.-','.-..','--','-.','---','.--.','--.-','.-.','...','-','..-','...-','.--','-..-','-.--','--..', '/', ' / ']

#function to change morse code to english
def morse_to_english():
    message =  input("What is your message in morse code? (use '/' in between letters and ' ' between words)\n-->")
    #adds a slash to the end to signify the end of the end letter
    message += "/"
    print("Your morse code message in English is: ")
    #list for the current letter to decode
    current_letter = []
    #list for the new message to pushed into
    new_message = []
    #tells the function that the morse code letter shouldn't be decoded yet
    good_to_go = False
    #iterates over each letter in the message
    for i in message:
        #if the user is adding a space between words
        if i == " ":
            #decodes and adds the current letter
            new_message.append(all_letters[all_morse_code_letters.index("".join(current_letter))])
            #sets the current letter to decode to be an empty list
            current_letter = []
            #adds a space to go between words
            new_message.append(" ")
            continue
        else:
            if i != "/":
                #adds the current part of the morse code letter to the letter to decode list
                current_letter.append(i)
        if i != "/":
            #if there is not a break between letters, tell the function to not decode the letter yet
            good_to_go = False
        else:
            #otherwise, tell the function to decode the letter
            good_to_go = True
        #iterates over every morse code letter
        for f in all_morse_code_letters:
            #checks if the current letter matches a letter in the morse code letter list
            if f == "".join(current_letter): 
                #if it is time to decode a letter
                if good_to_go:
                    #adds the decoded letter
                    new_message.append(all_letters[all_morse_code_letters.index("".join(current_letter))])
                    #sets the current letter to decode to be an empty list
                    current_letter = []                
    #prints the decoded message
    print("".join(new_message))

#function to convert english into morse code
def english_to_morse():
    message = input("What is your message in English?\n-->")
    print("Your English message to morse code is: ")
    new_message = []
    #iterates over all letters in the message
    for i in message:
        #puts a morse code letter unique to the specific letter
        new_message.append(all_morse_code_letters[all_letters.index(i)])
        #checks if there is a space or not to add a /
        try:
            if message[message.index(i)+1] == " " or message[message.index(i)-1] == " ":
                continue
            else:
                new_message.append("/")
        except:
            continue
    #prints the end result message
    print("".join(new_message))

#main function, user interface
def main():
    print("Welcome to the morse code translator!")
    while True:
        choice = input("Type 1 to translate morse code into english, type 2 to translate english into morse code, and type 3 to exit.\n-->")
        if choice == "1":
            morse_to_english()
        elif choice == "2":
            english_to_morse()
        elif choice == "3":
            break
        else:
            print("Not a valid choice!")
main()