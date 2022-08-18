#Prem Atul Jethwa
# -*- coding: utf-8 -*-
'''
Created on Sat Jun 11 14:40:16 2022
@author: premj

Question_1
Write a program that asks the user for a number in the range of 1 through 7. 
The program should display the corresponding day of the week, where 1 = Monday,
2 = Tuesday, 3 = Wednesday, 4 = Thursday, 5 = Friday, 6 = Saturday, and 
7 = Sunday. The program should display an error message if the user enters 
a number that is outside the range of 1 through 7.
'''

user_input = int(input('Enter a number in range of 1 through 7 : '))
if user_input == 1:
    print(user_input, '= Monday')
elif user_input == 2:
    print(user_input, '= Tuesday')
elif user_input == 3:
    print(user_input, '= Wednesday')
elif user_input == 4:
    print(user_input, '= Thursday')
elif user_input == 5:
    print(user_input, '= Friday')
elif user_input == 6:
    print(user_input, '= Saturday')
elif user_input == 7:
    print(user_input, '= Sunday')
else:
    print('Error : The given number doesnot correspond to a day of the week')