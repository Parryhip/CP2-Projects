#Samuel Andelin, Morse code Translator

#list of all letters in order
all_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '', ' ']

#list of all morse code letters in order
all_morse_code_letters = ['.-','-...','-.-.','-..','.','..-.','--.','....','..','.---','-.-','.-..','--','-.','---','.--.','--.-','.-.','...','-','..-','...-','.--','-..-','-.--','--..', '/', ' / ']

#function to change morse code to english
def morse_to_english():
    message =  input("What is your message in morse code? (use '/' in between letters and ' ' between words)\n-->")
    message += "/"
    print("Your morse code message in English is: ")
    current_letter = []
    new_message = []
    num_count = 0
    good_to_go = False
    for i in message:
        if i == " ":
            new_message.append(all_letters[all_morse_code_letters.index("".join(current_letter))])
            current_letter = []
            new_message.append(" ")
            continue
        else:
            if i != "/":
                current_letter.append(i)
        if i != "/":
            good_to_go = False
        else:
            good_to_go = True

        for f in all_morse_code_letters:
            if f == "".join(current_letter): 
                if good_to_go:
                    new_message.append(all_letters[all_morse_code_letters.index("".join(current_letter))])
                    current_letter = []
                good_to_go = True
                
            
    print("".join(new_message))

#function to convert english into morse code
def english_to_morse():
    message = input("What is your message in English?\n-->")
    print("Your English message to morse code is: ")
    new_message = []
    for i in message:
        new_message.append(all_morse_code_letters[all_letters.index(i)])
        try:
            if message[message.index(i)+1] == " " or message[message.index(i)-1] == " ":
                continue
            else:
                new_message.append("/")
        except:
            continue
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