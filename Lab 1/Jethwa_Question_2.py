#Prem Atul Jethwa
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 11 15:59:35 2022
@author: premj

Question_2
Write a program that asks the user to enter a person's age. 
The program should display a message indicating whether the person is 
an infant, child, teenager, or adult. Here are the following guidelines:
If the person is 1 year old or less, he or she is an infant.
If the person is older than 1 year, but younger than 13 years, he or she is a child.
If the person is at least 13 years old, but less than 20 years old, he or she is a teenager.
If the person is at least 20 years old, he or she is an adult.
"""

# ask user to input age
age = int(input("Please enter a person's age : " ))

# if a person is 1 or younger
if age <= 1:
    print ('The person is an infant.')
# if a person is older than 1 but younger than 13
elif age > 1 and age < 13:
    print ('The person is a child.')
# if a person is at least 13, but less than 20
elif age >= 13 and age < 20:
    print ('The person is a teenager.')
elif age >= 20:
    print ('The person is an adult.')
