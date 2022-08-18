# -*- coding: utf-8 -*-
"""
Created on Wed Jul 20 03:08:39 2022

@author: premjethwa
Name : Prem Atul Jethwa
Student ID : 1001861810

"""

from tkinter import * #importing tkinter
from tkinter import messagebox
import math           #importing math python modules

root = Tk()
root.title("Homework 5 - Login Window")
root.geometry("400x350")  #setting window dimensions
lbl = Label(root, text="Please Login", justify='center')
lbl.pack()
label1 = Label(root, text="Username:", width=20)
label1.place(x=3, y=130)
username = StringVar()
password = StringVar()
entry1 = Entry(root, textvariable=username)
entry1.place(x=135, y=130)
label2 = Label(root, text="Password:", width=20)
label2.place(x=5, y=180)
entry2 = Entry(root, textvariable=password, show="*")
entry2.place(x=135, y=180)

def Hypotenuse():
    top = Toplevel()
    top.title("Right Triangle Calculator")
    top.geometry("400x250")   #setting window dimensions
    sideA = StringVar()
    sideB = StringVar()
    sideC = StringVar()
    
    labelA = Label(top, text='Side A:')    #creating a label and entry field for side A
    labelA.place(x=2, y=2)   
    entryA = Entry(top, textvariable=sideA, width=30)
    entryA.place(x=60, y=2)
    labelB = Label(top, text='Side B:')   #creating a label and entry field for side A
    labelB.place(x=2, y=30)
    entryB = Entry(top, textvariable=sideB, width=30)
    entryB.place(x=60, y=30)
    labelC = Label(top, text='Side C:')   #creating a label and entry field for side A
    labelC.place(x=2, y=60)
    entryC = Entry(top, textvariable=sideC, width=30)
    entryC.place(x=60, y=60)
    entryC.configure(state="disabled")
    Button(top, text="Calculate", width=7, command=lambda: Calc_Hyp(sideA.get(), sideB.get())).place(x=100, y=100)  #calling CalcAns on clicking this
    Button(top, text="Exit", width=7, command=root.destroy).place(x=170, y=100)   #exiting application on clicking this

    def Calc_Hyp(s1, s2):
        s3 = math.sqrt((int(s1) ** 2) + (int(s2) ** 2))  #calculating and inserting in C entry label
        sideC.set('{:.3f}'.format(s3))

def Open_Window(user, password):
    pass_text = open('Users.txt', 'r')
    line = pass_text.readline()
    while (line != ''):
        lin = line.strip()
        ar = lin.split("|")
        if (ar[0] == user and ar[1] == password):
            Hypotenuse()
            break
        else:
            line = pass_text.readline()
    else:
        messagebox.showwarning("Login Failed", "Try again")
        pass
    pass_text.close()

Button(root, text="Login", width=7, command=lambda: Open_Window(username.get(), password.get())).place(x=100, y=220)
Button(root, text="Exit", width=7, command=root.destroy).place(x=160, y=220)   #exiting application on clicking this

root.mainloop()         #starting the application