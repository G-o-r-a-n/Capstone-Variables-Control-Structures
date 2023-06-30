import math

# Display welcome message and calculator options.

print("Welcome to the Hyperion Finance Calculator.\n")

print("We offer the following two calculation options:\n")

print(
    "Investment - to calculate the amount of interest you'll earn on your investment.\n"
    )

print("Bond - to calculate the amount you'll have to pay on a home loan.\n")

# Ask user to choose between the 2 options within a while-loop so that an invalid
# command runs another iteration of the while-loop.

# If the user enters a valid command, the while-loop will break as part of the 
# if-statement block.
while True:
    user_choice = input("Please enter Investment or Bond to proceed: ")
    
    # Format user_choice into lowercase so whichever case the command is entered will
    # be recognised e.g. Investment, INVESTMENT, INvesTMent are all treated the same.
    user_choice = user_choice.lower()
    
    # As there are only two valid commands, we can hard code them into an if-statement.
    if user_choice in ["investment", "bond"]:
        break
    
    print("\nCommand not recognised.\n")

# Using a series of while-loops in conjunction with try-except blocks.

# By separating the prompts into their own while-loops, the program can continue to ask 
# the user to enter a valid numerical value before moving onto the next prompt. 

# An invalid input will cause the while-loop to move onto another iteration where the
# user is given another chance to input a valid command.

# Identify which calculation type the user has chosen to make.
if user_choice == "investment":
    
# Ask user for investment details.
    while True:
        try:
            # money_deposit typecast as float
            money_deposit = float(
                input("\nEnter the amount of money you are depositing: £")
                )
            # Tests for a positive numerical value.
            if money_deposit <= 0:
                print("\nPlease enter a numeric value above 0.")
                continue
        
        # ValueError wil raise exception to non-numerical values due to typecasting..
        except ValueError:
            print("\nPlease enter a valid numeric value.")
            continue
        
        break
    
    while True:
        try:
            # expected_interest typecast as float
            expected_interest = float(
                input("\nEnter the interest (%) you are expecting annually: ")
                )
            # Tests for a positive numerical value.
            if expected_interest <= 0:
                print("\nPlease enter a numeric value above 0.")
                continue
        
        # ValueError wil raise exception to non-numerical values due to typecasting.
        except ValueError:
            print("\nPlease enter a valid numeric value.")
            continue
        
        break
    
    while True:
        try:
            # investment_duration typecast as integer.
            investment_duration = int(input(
                "\nEnter the amount of years you are planning to keep this investment: "
                ))
            # Tests for a positive numerical value.
            if investment_duration <= 0:
                print("\nPlease enter a numeric value above 0.")
                continue
        
        # ValueError wil raise exception to non-numerical values due to typecasting.
        except ValueError:
            print("\nPlease enter a valid numeric value.")
            continue
        
        break
    
    while True:
        while True:
            interest_type = input("\nChoose between 'Simple' or 'Compound' interest: ")
            interest_type = interest_type.lower()
        
            if interest_type in ["simple", "compound"]:
                break
            
            print("\nCommand not recognised")
            
        # Run calculations based on user's choice of interest type.
        if interest_type == "simple":
            expected_return = (
                money_deposit 
                * (1 + expected_interest / 100 * investment_duration)
                )
            break
        
        elif interest_type == "compound":
            expected_return = (
                money_deposit 
                * math.pow((1 + expected_interest / 100), investment_duration)
                )
            break
        
    
    # f-string in conjunction with {variable:.2f} to return a value rounded to 
    # 2 decimal places.
    print(f"\nYou should expect a return of £{expected_return:.2f}")

elif user_choice == "bond":
    
    # As in the previous code block, while-loop and try-except used to ensure validity
    # of user input, running the loop until validity has been confirmed.
    
    # Ask user for bond details.
    while True:
        try:
            # house_value typecast as float.
            house_value = float(input("\nEnter the current value of the house: £"))
            # Tests for a positive numerical value.
            if house_value <= 0:
                print("\nPlease enter a numeric value above 0.")
                continue
        
        # ValueError wil raise exception to non-numerical values due to typecasting.
        except ValueError:
            print("\nPlease enter valid numeric values.")
            continue
        
        break
    
    while True:
        try:
            # interest_rate typecast as float.
            interest_rate = float(input("\nEnter the annual interest rate (%): "))
            # Tests for a positive numerical value.
            if interest_rate <= 0:
                print("\nPlease enter a numeric value above 0.")
                continue
        
        # ValueError wil raise exception to non-numerical values due to typecasting.
        except ValueError:
            print("\nPlease enter valid numeric values.")
            continue
        
        break
        
    while True:
        try:
            # bond_duration typecast as integer.
            bond_duration = int(input(
                "\nEnter the number of months you expect to take to repay the bond: "
                ))
            # Tests for a positive numerical value.
            if bond_duration <= 0:
                print("\nPlease enter a numeric value above 0.")
                continue
        
        # ValueError wil raise exception to non-numerical values due to typecasting.
        except ValueError:
            print("\nPlease enter valid numeric values.")
            continue
        
        break
    
    # Annual interest converted to monthly interest for calculation purposes
    interest_rate = (interest_rate / 100) / 12
    
    # Run bond calculation.
    repayment_amount = (
        (interest_rate * house_value) 
        / (1 - (1 + interest_rate) ** (-bond_duration))
        )

    print(f"\nYou should expect to pay back £{repayment_amount:.2f} per month.")
    
print("\nThank you for using the Hyperion Finance Calculator.")