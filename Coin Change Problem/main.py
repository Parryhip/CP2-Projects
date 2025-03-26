#Samuel Andelin, Coin Change Problem

#importing needed functions
from countries import US
from countries import EU
from countries import JP
from countries import EN


#main function
def main():
    print("Welcome to the coin change problem! \nThis program will calculate the least number of coins to get an amount in usd, yen, euros, and pounds!")
    while True:
        country = input("What country do you want to make change in? (1 for United States, 2 for Europe, 3 for Japan, 4 for England, or type 5 to exit)")
        if country == "1":
            US()
        elif country == "2":
            EU()
        elif country == "3":
            JP()
        elif country == "4":
            EN()
        elif country == "5":
            print("Ok, bye!")
            break
        else:
            print("Invalid input!")