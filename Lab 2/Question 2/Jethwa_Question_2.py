# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 23:56:21 2022

@author: premj
"""

#defining an empty dictionary to store contacts

contact=dict()

#method to add a contact

def add():
    #getting inputs
    print('Enter the following contact info:')
    name=input('Name: ')
    email=input('Email: ')
    phone=input('Phone: ')
    #adding contact to dictionary
    contact[name]=[email,phone]
    #updating the contacts.txt file
    save_to_file()
    print('Do you want to add another record?')
    choice=input('Y = yes, anything else = no: ')
    if choice=='Y' or choice=='y':
        #adding one more contact
        add()

#method to show list of contacts
def show():
    print('List of contact(s):')
    index=1
    #looping through contacts dict and displaying each contact
    for i in contact:
        print('Contact #',index)
        print('\tName: ',i)
        print('\tEmail: ',contact[i][0])
        print('\tPhone: ', contact[i][1])
        print('-----------------------------')

#method to search for a contact
def search():
    #getting name
    name = input('Enter a name to search for: ')
    #checking if the name exists
    if name in contact:
        #found
        print('Name: ', name)
        print('Email: ', contact[name][0])
        print('Phone: ', contact[name][1])
    else:
        #not found
        print('Not found!')

#method to modify a contact
def modify():
    #getting name and checking if name exists
    name = input('Enter a name to search for update: ')
    if name in contact:
        email = input('Enter the new email for update: ')
        phone = input('Enter the new phone for update: ')
        #updating the details
        contact[name]=[email,phone]
        #updating the contacts file
        save_to_file()
        print('The file has been updated')
    else:
        print('Not found!')

#method to delete a contact
def delete():
    name = input('Which name do you want to delete: ')
    #removing the contact if exists
    if name in contact:
        contact.pop(name)
        save_to_file()
        print('The file has been updated')
    else:
        print('Not found!')

#method to save contacts into contacts.txt file whenever a contact is
#added or updated or deleted
def save_to_file():
    filename='contact.txt'
    #opening contact.txt file for writing
    file=open(filename,'w+')
    #saving each contact as semi colon separated values in each line
    for i in contact:
        file.write(i+';''\n'+contact[i][0]+';''\n'+contact[i][1]+'\n')
    #closing file
    file.close()

#method to load contacts from contact.txt file whenever program is run
def open_file():
    filename='contact.txt'
    #resetting contacts dict
    contact.clear()
    try:
        #opening file
        file=open(filename)
        #looping through file
        for line in file:
            #removing newline character from line
            line=line.strip()
            #splitting line by semi colon to create a list
            fields=line.split(';')
            #adding contact to the dictionary
            if len(fields)==3:
                #here 0th field is name, 1st is email and 2nd is phone
                contact[fields[0]]=[fields[1],fields[2]]
        file.close() #closing file
    except:
        #exception occurred, resetting the contacts
        contact.clear()

#main method
def main():
    #loading current contacts from contact.txt file
    open_file()
    #looping until user wishes to quit
    choice=0
    while choice!=6:
        #displaying menu
        print('\n   CHOICE MENU')
        print('1) Add a contact')
        print('2) Show the list of contacts')
        print('3) Search for a name in list')
        print('4) Modify a contact')
        print('5) Delete a contact from the list')
        print('6) Quit')
        #getting choice
        choice=int(input('Enter your choice: '))
        #handling choice
        if choice==1:
            add()
        elif choice==2:
            show()
        elif choice==3:
            search()
        elif choice==4:
            modify()
        elif choice==5:
            delete()
        elif choice==6:
            print('Exiting the program...')
        elif choice!=6:
            print('Invalid choice!')
#invoking main method
main()
