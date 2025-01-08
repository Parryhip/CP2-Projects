#Samuel Andelin, Financial Calculator
def goal_saving(rateofinput, amountperdeposit, goal):
    if rateofinput == 1:
        print("If you were to save $"+str(amountperdeposit)+" every month, it would take you "+str(goal/amountperdeposit)+" months to reach your goal.")
    elif rateofinput == 2:
        print("If you were to save $"+str(amountperdeposit)+" every week, it would take you "+str(goal/amountperdeposit)+" weeks to reach your goal.")
def main():
    print("Welcome to the financial calculator!")
    user_action = input("Type 1 for goal saving calculator,\n2 for compound interest calculator,\n3 for budget allocator,\n4 for sale price calculator,\nand 5 for tip calculator!")    
    if user_action == "1":
        goal = int(input("What is your goal? (Without the dollar sign)"))
        rateofinput = int(input("Type 1 if you are depositing money for the goal on a weekly basis and 2 for a monthly basis."))
        amountperdeposit = int(input("How much money are you depositing each time for the goal? (Without the dollar sign)"))
        goal_saving(rateofinput, amountperdeposit, goal)
main()