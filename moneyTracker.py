# Name: Shanaya John
# Student Number: 501108746
# Date: 2021-10-19
"""
Description: This program is designed to help the user to save money to attain a certain goal. The program starts by
asking the user to enter a goal (ex. "trip to London") and the amount needed to save to attain the goal. After, the user
then is asked if they want to add money, withdraw money or check their balance from this savings account. If they wish
to add money, they are prompted to enter an amount and that amount will add to the account. If they wish to withdraw
money, they are prompted to enter an amount and only if the account balance is sufficient, will the program allow the
user to withdraw. Lastly, if the user wishes to check their balance, then the program will display the total amount
present in account and tell the user whether they have reached the desired amount.
"""
# Initializing Variables
money = 0
goal_stop = True
program = True
goal = ""
goal_amount = 0
count = 0


# function asks the user to input a desired amount they want to add to account balance and returns that amount.
def add():
    user_add = float(input("Add money : "))
    return user_add


# function asks the user to input the amount they wish to withdraw and
# checks if the withdrawal amount is insufficient to current account balance.
def withdraw():
    num = float(input("withdraw amount: "))  # Asks the user to input the amount they want to withdraw
    if num <= money:
        return num  # return the inputted amount if the account balance is sufficient
    else:
        print(f"Insufficient balance, current balance is {money}")
        return 0  # returns zero when inputted balance is greater than account balance (account balance insufficient).


while program:
    while goal_stop:
        # Asks the user for a goal and the related amount once,
        # while the program is run unless the user input is invalid.
        goal_stop = False
        goal = input("Enter your saving goal\n")

        # if the user didn't enter a float type, it catches the error
        try:
            goal_amount = float(input("Enter the amount:\t"))
        except ValueError:
            goal_amount = 0

        # if the user didn't enter a value for the goal or the goal amount then the program will ask again
        if goal == "" or goal_amount == 0:
            print("invalid input")
            count += 1
            goal_stop = True
            # If user enter 3 consistent null values for goal_amount and goal then the program exits
            if count == 3:
                exit()
    user = input("Do you want to continue the program? \n").lower()
    # lower help the program understand the user input, if they are any capital letters present.

    if user.strip() == "yes":  # strip remove the spaces to help the program understand user input.
        user_option = input("Would you like to add, withdraw or check:\n").lower()
        if user_option.strip() == "add":
            money += add()  # adds the return value from add function

        elif user_option.strip() == "withdraw":
            money -= withdraw()  # subtracts the withdraw amount from the total account balance

        elif user_option == "check":
            print(f"Your current balance is {money}.")
            # Tells the user they have reached their goal
            if money >= goal_amount:
                print(f"Congratulation! You have reached your goal: {goal}")
                program = False  # End the program after the goal is reached.
            else:
                # tells the user how much they still need to save to reach their desired goal.
                print(f"You need {goal_amount - money} to reach your goal amount {goal_amount}")
        # Notifies the user that value entered is invalid
        else:
            print("invalid input. Please enter 'withdraw', 'add' or 'check'.")

    # allows user to exit the program
    elif user.strip() == "no":
        print("Goodbye")
        program = False
    # Notifies the user that value entered is invalid
    else:
        print("Invalid input. Enter 'yes' or 'no'. ")

exit()  # End the program
