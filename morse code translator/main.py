#Samuel Andelin, Morse code Translator

#list of all letters in order
all_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#list of all morse code letters in order
all_morse_code_letters = ['.-','-...','-.-.','-..','.','..-.','--.','....','..','.---','-.-','.-..','--','-.','---','.--.','--.-','.-.','...','-','..-','...-','.--','-..-','-.--','--..', ' / ']

def morse_to_english(message):
    print("Your morse code message in English is: ")
    new_message = []
    for i in message:
        index_thing = i.index()
        new_message.append(all_letters(index_thing).strip())
    print("".join(new_message))
