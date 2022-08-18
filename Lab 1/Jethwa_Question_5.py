#Prem Atul Jethwa
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 16 20:30:08 2022
@author: premj

Question_5
In mathematics, the notation n! represents the factorial of the nonnegative
integer n. The factorial of n is the product of all the nonnegative integers 
from 1 up through n.
Write a program that asks the user to enter an integer. Then display the 
factorial, along with the formula to calculate it in ascending order. For example, if the user enters 7, your program should display:
   7! = 1 x 2 x 3 x 4 x 5 x 6 x 7 = 5040
and
   4! = 1 x 2 x 3 x 4 = 24
Write a program that lets the user enter a nonnegative integer and then uses
a loop to calculate the factorial of that number. Display the factorial.
"""

# prompt for a non negative integer
n = int(input("Enter a nonnegative integer:"))
# validate the input
while n<0:
     # re prompt for the nonnegative integer
     n = int(input("Enter a nonnegative integer:"))
print("{}! = ".format(n), end='')
fact = 1
# multiply integer 1 to n using a for loop
for i in range(1,n+1):
     fact = fact * i
     print(i, end='')
     if i != n:
         print(" x ", end='')
print(" =", fact)           # print the factorial standard output


