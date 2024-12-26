#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 23:02:18 2023

@author: georgemariolis
"""

'''When you brake after the think you want to happen 
    Python is going out of the loop, so the variable stays alive''';
    
    
profit = 0

while True:   
        income = input('Add the amount of the money you earn: ')
        if income.lower() == 'exit':
            print(income)
            break # Exit the loop when 'Exit' is entered 
        if not income.isdigit():
            print("please add a numerical value for money") # Display this for non-numeric inputs
            continue # Continue the loop without adding the non-numeric input
        profit = profit + float(income)
        print(profit)

while True:
    try:
       sail = float(input('How many months did you sail: '))
       break # If conversion to float is successful, exit the loop
    except ValueError:
       print('Please add a valid numerical value for months')
       
while True:
    try:
        home = float(input('How many months will you stay asshore: '))
        break # If conversion to float is successful, exit the loop
    except ValueError:
        print("please add a valid value for months")



#  Make Variables which are going to be calculated later
months = sail + home
Taxes = profit * 0.3
AfterTaxes = profit - Taxes
Savings = AfterTaxes * 0.05

# print the results you take by calculating data
print("Your taxes are",Taxes)
print("Your savings are", Savings)



fixedExpenses = 0
while True: # Make a loop to add fixed expenses
        fixedInput = input("Please add your fixed expenses amount, if you finished press Exit: ")
        if fixedInput.lower() == "exit":
            break # exit the loop when the user enters exit
        if not fixedInput.isdigit():
            print("Please add a numerical value for expenses")
            continue
        fixedExpenses = fixedExpenses + float(fixedInput)
        print("Yours fixed expenses amount is:",fixedExpenses)
    
    
    
# Make variables and define 
NET = AfterTaxes - Savings - fixedExpenses
PeriodNET = NET/months
UpcomingNET = NET/home

print('Your Net Profit is: ',NET)
print("Your Monthly Fixed Expences are: ",fixedExpenses)
print("Your monthly Net Profit is: ",PeriodNET)
print("Your Upcoming Monthly Net Profit is:",UpcomingNET)




Utilities = 0
while True:   # loop to add utilities expenses 
    UtiInp = input("Please Add Your Utilities Expenses: ")
    if UtiInp == 'exit':
        break
    if not UtiInp.isdigit():
        print("Please add a numerical value for tilities expenses")
        continue
    Utilities = Utilities + float(UtiInp)


RemainAmount = UpcomingNET - Utilities
print("You have ",RemainAmount," left for your month")


