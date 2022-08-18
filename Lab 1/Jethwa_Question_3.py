#Prem Atul Jethwa
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 11 16:14:17 2022 
@author: premj

Question_3
A software company sells a package that retails for $99. Quantity discounts
are given according to the following table:
Quantity	Discount
10 – 19	      10%
20 – 49	      20%
50 – 99	      30%
100 or more	  40%
Write a program that asks the user to enter the number of packages 
purchased. The program should then display the amount of the discount 
(if any) and the total amount of the purchase after the discount.
"""

Retail_Price = 99.00
number_of_packages = float(input('\nEnter number of packages purchased : '))
#display_message = ""
if number_of_packages < 0:
    display_message = "Error: Number of packages must be greater than 0.\nRe-run program and try again."
else:
    #discount_percentage = 0
    if number_of_packages < 10:
        discount_percentage = 0
    elif number_of_packages >= 10 and number_of_packages <= 19:
        discount_percentage = .10 # 10%
    elif number_of_packages >= 20 and number_of_packages <= 49:
        discount_percentage = .20 # 20%
    elif number_of_packages >= 50 and number_of_packages <= 99:
        discount_percentage = .30 # 30%
    elif number_of_packages >= 100:
        discount_percentage = .40 # 40%
    
    package_total = number_of_packages * Retail_Price
    discount_amount = (package_total) * discount_percentage
    grand_total = package_total - discount_amount
    display_message = "Package total = $" + format(package_total, ',.2f') + \
                      "\nDiscount Percentage = " + format(discount_percentage, '.0%') + \
                      "\nDiscount amount = $" + format(discount_amount, ',.2f') + \
                      "\nGrand total  = $" + format(grand_total, ',.2f')
print("\n" + display_message + "\n")
