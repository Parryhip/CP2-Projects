#Samuel Andelin, Advanced function notes

# 1. What is a helper function?
    #a function called inside another function to help with a specific task 

def check_input(user_txt):
    return not any(char.isdigit() for char in user_txt)


def hello(name):
    check_input(name)
    if check_input(name):
        print(f"hello {name}!")
    else:
        print("Please only input letters!")
        user = input("What is your name?\n-->").strip().capitalize()
        # 8. What is recursion?
            #when you call a function inside itself
        hello(user)
        # 9. How does recursion work?
            #You call the function again from inside itself


user = input("What is your name?\n-->").strip().capitalize()

hello(user)


# 2. What is the purpose of a helper function?
    #to make your function SIMPLER

# 3. What is an inner function?
    #a function defined inside another function

def fun1():#wrapper function ---- mostly exists to keep the inner function safe
    msg = "This is the outer function"
    def fun2():
        print(msg)
    fun2()
fun1()

# 4. What is the scope of a variable in a function WITH an inner function?
    #Local INCLUDING the inner function

# 5. Why do we use inner functions?
    #access to local variables and organize sections of your function

# 6. What is a closure function?
    #a function to return using different values in the same outer function call

def fun(a):
    #outer function remembers the value of a

    def adder(b): #closure function
        return a+b
    return adder #returns the closure

val = fun(10)

print(val(5))

# 7. Why do we write closure functions?
    #to keep things safe, decrease number of parameters
def end(income):

    def calc(cost, type):
        percent = (cost/income) * 100
        print(f"Your {type} is ${cost:.2f} and that is {percent:.0f}%")
    return calc

def user_input(type):
    return int(input(f"What is your monthly {type}: \n-->$"))

income = user_input("Income")
rent = user_input("Rent")
utilities = user_input("Utilities")
transportation = user_input("Transportation")

ready = end(income)

ready(rent, "Rent")
ready(utilities, "Utilities")
ready(transportation, "Transportation")