#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 21:06:05 2023

@author: georgemariolis
"""


WorkIncome = 0
Others=0
#Adding the Standard Work Income
try:
    Invoice = float(input("Please add how much money have you got paid by invoice: "))
    WorkIncome += Invoice
except ValueError:
    print("Please add a numerical value")
    
# Adding Other Incomes 
while True:
    OtherIncome = input("Please add the ammount of other income Press exit if you finish: ")
    if OtherIncome.lower() == 'exit':
        break
    
    try:
        Others += float(OtherIncome)
    except ValueError:
        print("Please add a numerical value")
        
        
# Calculate VAT and Work NET 

# Calculate the VAT You need it to try it except ValueError
AfterInterest=0

VATexist = input("do you have a VAT? Please press 'Yes' or 'No: ")
if VATexist.lower() == "yes":
    VAT= float(input("Please add the number of your Vat-Rate: "))
    VAT = VAT/100
elif VATexist.lower() == "no":
    VAT = 1
    AfterInterest = WorkIncome
if VAT < 1:
    AfterInterest = WorkIncome - (WorkIncome * VAT)

#Calculate other income tax and Profit
OtherRate = float(input("Please add if there is a Tax-Rate in other income: "))
OtherRate = OtherRate/100
OtherAfterInterest = Others - (Others * OtherRate)
PBT = OtherAfterInterest + AfterInterest


# Calculate Withholding Tax
WithholdingTax = float(input("Please add the rate of your withholding Tax: "))
WithholdingTax = WithholdingTax/100
Withholding = AfterInterest * WithholdingTax
#AfterWithholding = AfterInterest - Withholding


#Calculate the income TAX & Define the NET
IncomeTax = 0
if PBT >= 0 and PBT <10001:
    IncomeTax = PBT * 0.09
elif PBT >= 10001 and PBT < 20001:
    IncomeTax = 900 + ((PBT-10000)*0.22)
elif PBT >=20001:
    IncomeTax = 2100 + ((PBT - 20000)* 0.30)

NET = PBT - IncomeTax - Withholding #Calculate the NET

print("Your work's Profit Before Taxes(PBT) is:",AfterInterest)
print("Your other's Profit Before Taxes(PBT) is:", OtherAfterInterest)
print("Your PBT is:",PBT)
print("Your Withholdind is:",Withholding)
print("Your Income Tax is:", IncomeTax)
print("Your Net Profit is:", NET)

#Calculate the Payment or Return
if IncomeTax > Withholding:
    result = IncomeTax - Withholding
    print("You will need to pay: ", result,"for the tax balance")
elif IncomeTax < Withholding:
    result = Withholding - IncomeTax
    print("You will have a return of:", result)
    

'''
If you have no VAT the last print is 0. 
If VAT = 1 the last print (AfterInterest) should be not 0. 
Other Income tax is 9% is coming after the VAT and is on the others and work
together.

Withholding tax is input some are 20 some 15 etc

Net income is afterVat and aftertax and withholding. BUT withholding - aftertax
is the tax return.

#Taxes = float(input("Please add your tax rate"))'''
