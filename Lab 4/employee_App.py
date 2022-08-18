# -*- coding: utf-8 -*-
"""
Created on Sat Jul 16 00:10:00 2022

@author: premjethwa
Name : Prem Atul Jethwa
UTA ID : 1001861810
"""

import employee
import pickle

#Global constants for menu choices
LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5

#Global constant for the filename
FILENAME = 'employee.dat'

#main function
def main():
    #Load the existing employee dictionary and assign it to myrecord.
    myrecord = load_employee()
    #Initialize a variable for the user's choice.
    choice = 0
    #Process menu selections until the user wants to quit the program.
    while choice != QUIT:
        #Get the user's menu choice.
        choice = get_menu_choice()
        #Process the choice.
        if choice == LOOK_UP:
            look_up(myrecord)
        elif choice == ADD:
            add(myrecord)
        elif choice == CHANGE:
            change(myrecord)
        elif choice == DELETE:
            delete(myrecord)
    #Save the myrecord dictionary to a file.
    save_employee(myrecord)

def load_employee():
    try:   
        input_file = open(FILENAME, 'rb')
        #Unpickle the dictionary.
        record_dct = pickle.load(input_file)
        input_file.close()
    except IOError:
        #Could not open the file, so create an empty dictionary.
        record_dct = {}
    #Return the dictionary.
    return record_dct

#The get_menu_choice function displays the menu and gets a validated choice from the user.
def get_menu_choice():
    print()
    print('Menu')
    print('-------------------------------------------------------------------------------')
    print('1. Look up an employee in the dictionary')
    print('2. Add a new employee to the dictionary')
    print("3. Change an existing employee’s name, depart, and job title in the dictionary")
    print('4. Delete an employee from the dictionary')
    print('5. Quit the program')
    print()
    #Get the user's choice.
    choice = int(input('Enter your choice: '))
    #Validate the choice.
    while choice < LOOK_UP or choice > QUIT:
        choice = int(input('Enter a valid choice: '))
    #return the user's choice.
    return choice

#The look_up function looks up an item in the specified dictionary.
def look_up(myrecord):
    #Get a ID_number to look up.
    ID_number = input('Enter a ID_number: ')
    #Look it up in the dictionary.
    print(myrecord.get(ID_number, 'That ID_number is not found.'))

#The add function adds a new entry into the specified dictionary.
def add(myrecord):
    #Get the record info.
    name = input('Name: ')
    ID_number = input('ID_number: ')
    department = input('Department: ')
    job_title = input('Job_title: ')
    #Create a Employee object named entry.
    entry = employee.Employee(name,ID_number,department,job_title)
    #If the ID does not exist in the dictionar, add it as a key with the entry object as the associated value.
    if ID_number not in myrecord:
        myrecord[ID_number] = entry
        print('The entry has been added.')
    else:
        print('That ID_number already exists.')

#The change function changes an existing entry in the specified dictionary.
def change(myrecord):
    #Get a ID_number to look up.
    ID_number = input('Enter a ID_number: ')
    if ID_number in myrecord:    
        #Get a new name.
        name = input('Enter the new name: ')
        #Get a new department.
        department = input('Enter the new Department: ')
        #Get a new job_title address.
        job_title = input('Enter the new Job_title: ')
        #Create a contact object named entry.
        entry = employee.Employee(name,ID_number,department,job_title)
        #Update the entry.
        myrecord[ID_number] = entry
        print('Information updated.')
    else:
        print('That ID_number is not found.')

#The delete function deletes an entry from the specified dictionary.
def delete(myrecord):
    #Get a ID_number to look up.
    ID_number = input('Enter a ID_number: ')
    #If the ID_number is found, delete the entry.
    if ID_number in myrecord:
        del myrecord[ID_number]
        print('Entry deleted.')
    else:
        print('That ID_number is not found.')

#The save_employee funtion pickles the specified object 
def save_employee(myrecord):
    #Open the file for writing.
    output_file = open(FILENAME, 'wb')
    #Pickle the dictionary and save it.
    pickle.dump(myrecord, output_file)
    #Close the file.
    output_file.close()

#Call the main function.
main()

    

