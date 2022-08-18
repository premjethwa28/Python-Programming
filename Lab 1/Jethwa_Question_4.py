#Prem Atul Jethwa
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 16 20:17:58 2022
@author: premj

Question_4
Write a program that displays a table of the Celsius temperature 0 through 20 
and their Fahrenheit equivalents. The formula for converting a temperature 
from Celsius to Fahrenheit is
F = ((C*9/5)+32)
Where F is the Fahrenheit temperature and C is the Celsius temperature. 
Your program must use a loop to display the table.
"""

print('Celsius to Fahrenheit Conversion Table')  #Display the statement
print('Celsius      Fahrenheit')       #Display the column of the temperatures
print("-----------------------")

#Begin the for loop to display the value of Celsius to Fahrenheit
for C in range(0,21):
    F=(9/5)*C+32        #Compute the Fahrenheit
    print(C,"            {0:.2f}".format(F)) #Display the Celsius along with its Fahrenheit.
