#Samuel Andelin, Financial Calculator
def goal_saving(rateofinput, amountperdeposit, goal):
    if rateofinput == 1:
        print("If you were to save $"+str(amountperdeposit)+" every month, it would take you "+str(goal/amountperdeposit)+" months to reach your goal.")
    elif rateofinput == 2:
        print("If you were to save $"+str(amountperdeposit)+" every week, it would take you "+str(goal/amountperdeposit)+" weeks to reach your goal.")
def compound_interest(loan, interest, years):
    final_loan = loan
    for i in range(years):
        a = (1+interest)*final_loan
        final_loan = a
    print("With an interest rate of "+ str(interest) + ", your loan of "+str(loan)+" will grow to be a loan of "+ str(final_loan)+".")
def budget_allocator(categories, percentages, income):
    for i in categories:
        amount = float(percentages[0])*float(int(income)/100)
        print("For your category named "+i+" you should spend $"+str(amount)+" of your income")
        percentages.pop(0)
def main():
    print("Welcome to the financial calculator!")
    while True:
        print("\n")
        user_action = input("Type 1 for goal saving calculator,\n2 for compound interest calculator,\n3 for budget allocator,\n4 for sale price calculator,\nand 5 for tip calculator!")    
        if user_action == "1":
            goal = float(input("What is your goal? (Without the dollar sign) "))
            rateofinput = int(input("Type 1 if you are depositing money for the goal on a weekly basis and 2 for a monthly basis."))
            amountperdeposit = float(input("How much money are you depositing each time for the goal? (Without the dollar sign)"))
            print("\n")
            goal_saving(rateofinput, amountperdeposit, goal)
        elif user_action == "2":
            loan_amount = float(input("How much is your loan? (Without the dollar sign) "))
            interest_rate = float(input("What is the interest rate per year? (Without the percent sign) "))
            years = int(input("How many years are you having the interest grow? "))
            print("\n")
            compound_interest(loan_amount, interest_rate, years)
        elif user_action == "3":
            categories = []
            percentages = []
            category_num = input("How many categories do you want to split your income into? ")
            percent_left = 100
            for i in range(int(category_num)):
                new_category = input("What is the name of the category that you want to create?")
                while True:
                    new_category_percentage = input("What percentage of your income do you want going into this category? (Without the percent sign)(No decimals allowed!!!)")
                    if int(new_category_percentage) > 100:
                        print("Percentage is too high!")
                        continue
                    a = percent_left - float(new_category_percentage)
                    percent_left = a
                    if percent_left < 0:
                        print("You don't have enough percentage left to allocate that much!")
                    else:
                        break
                print("You have "+str(percent_left)+"% of your income left to allocate")
                categories.append(new_category)
                percentages.append(float(new_category_percentage))
            income = input("What is your income? ")
            budget_allocator(categories, percentages, income)

main()