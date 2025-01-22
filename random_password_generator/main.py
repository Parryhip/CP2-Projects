#Samuel Andelin, Random Password Generator

#importing random
import random

#list of all letters
letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

#function for uppercase letter amount
def length(password):
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
def uppercase(password):
    while True:
        uppers = input("How many uppercase letters do you want to have in your password?\n-->")
        try:
            test = int(uppers)
        except:
            print("Please input a number!")
            continue
        if int(uppers) > len(password):
            print("You don't have enough letters in your password to have that many uppercase letters. \nPlease change the amount of uppercase letters to be able to fit in your password.")
        else:
            break
    return int(uppers)

#function for number amount
def nums(password, uppers):
    while True:
        numbers = input("How many numbers do you want to have in your password?\n-->")
        try:
            test = int(numbers)
        except:
            print("Please input a number!")
            continue
        if int(numbers) > len(password)-uppers:
            print("You don't have enough characters left in your password to have that many numbers. \nPlease change the amount of numbers to be able to fit in your password.")
        else:
            break

#function for special character amount
def special_chars(password, uppers, numbers):
    while True:
        specials = input("How many special characters do you want to have in your password?\n-->")
        try:
            test = int(specials)
        except:
            print("Please input a number!")
            continue
        if int(specials) > len(password)-uppers-numbers:
            print("You don't have enough characters left in your password to have that many special characters. \nPlease change the amount of special characters to be able to fit in your password.")
        else:
            break

#main function/user interface
def main():
    print("Welcome to the random password generator!")
    while True:
        password = ""
        uppers = uppercase(password)
        numbers = nums(password, uppers)
        special_chars(password)
    