#Samuel Andelin, Random Password Generator

#importing random
import random

#list of all letters
letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

#list of all special characters
specialcharacters = ["~","`","!","@","#","$","%","^","&","*","(",")","_","-","+","=","{","}","[","]","|","\\",";",":","'",'"',"<",">",",",".","?","/"]

#function for uppercase letter amount
def length():
    while True:
        length_of_password = input("What length do you want your password?\n-->")
        try:
            test = int(length_of_password)
        except:
            print("Please input a number!")
            continue
        break
    return int(length_of_password)

#function for uppercase letter amount
def uppercase(password_length):
    while True:
        uppers = input("How many uppercase letters do you want to have in your password?\n-->")
        try:
            test = int(uppers)
        except:
            print("Please input a number!")
            continue
        if int(uppers) > password_length:
            print("You don't have enough letters in your password to have that many uppercase letters. \nPlease change the amount of uppercase letters to be able to fit in your password.")
        else:
            break
    return int(uppers)

#function for number amount
def nums(password_length, uppers):
    while True:
        numbers = input("How many numbers do you want to have in your password?\n-->")
        try:
            test = int(numbers)
        except:
            print("Please input a number!")
            continue
        if int(numbers) > password_length-uppers:
            print("You don't have enough characters left in your password to have that many numbers. \nPlease change the amount of numbers to be able to fit in your password.")
        else:
            break
    return int(numbers)
#function for special character amount
def special_chars(password_length, uppers, numbers):
    while True:
        specials = input("How many special characters do you want to have in your password?\n-->")
        try:
            test = int(specials)
        except:
            print("Please input a number!")
            continue
        if int(specials) > password_length-uppers-numbers:
            print("You don't have enough characters left in your password to have that many special characters. \nPlease change the amount of special characters to be able to fit in your password.")
        else:
            break
    return int(specials)

#main function/user interface
def main():
    print("Welcome to the random password generator!")
    while True:
        password_length = length()
        password = []
        passwords = []
        uppers = uppercase(password_length)
        uppersnum = uppers
        numbers = nums(password_length, uppers)
        numbersnum = numbers
        specials = special_chars(password_length, uppers, numbers)
        specialsnum = specials
        for i in range(4):
            for i in range(password_length):
                if uppersnum != 0:
                    password.append(random.choice(letters).upper())
                    uppersnum -= 1
                elif numbersnum != 0:
                    password.append(str(random.randint(0,9)))
                    numbersnum -= 1
                elif specialsnum != 0:
                    password.append(random.choice(specialcharacters))
                    specialsnum -= 1
                else:
                    password.append(random.choice(letters))
            random.shuffle(password)
            passwords.append("".join(password))
            password = []
            uppersnum = uppers
            numbersnum = numbers
            specialsnum = specials


        print("Here are your passwords!: ")
        num = 1
        for item in passwords:
            print(f"{num}. {item}")
            num += 1
        print("\n")
        while True:
            do_it_again = input("Do you want to continue generating passwords?(y/n)\n-->")
            if do_it_again.lower() == "y":
                break
            elif do_it_again.lower() == "n":
                return
            else:
                print("Not a valid input!")
main()
    