"""
This program calculates the simple/compound interest on an investment or repayment cost
on a bond, depending on the values inputted by the user.
"""

import math

print("investment - To calculate the amount of interest you'll earn on your investment")
print("bond - To calculate the amount you'll have to pay on a home loan")
option = input("Enter either 'investment' or 'bond' from the menu above to proceed: ")

if option.lower() == "investment":
    deposit = float(input("Please enter the amount of money you are depositing: "))
    interest_rate = float(input("Please enter the interest rate percentage: "))
    years = int(input("Enter the number of years to invest for: "))
    interest = input("Select 'simple' or 'compound' interest: ")
    if interest == "simple":
        total = deposit * (1 + (interest_rate / 100) * years)
    else:
        total = deposit * math.pow((1 + (interest_rate / 100)), years)
    print(f"Total = {total}")

elif option.lower() == "bond":
    house_value = float(input("Please enter the current value of the house: "))
    interest_rate = float(input("Please enter the interest rate percentage: "))
    months = int(input("Please enter the number of months planned to repay the bond: "))
    repayment = (((interest_rate / 100) / 12) * house_value) / (
        1 - (1 + ((interest_rate / 100) / 12)) ** (-months)
    )
    print(f"Repayment per month = {repayment}")

else:
    print(f"{option} is not a valid selection.")
