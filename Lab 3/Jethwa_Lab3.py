# -*- coding: utf-8 -*-
"""
Name : Prem Atul Jethwa
UTA ID : 1001861810
"""

import sqlite3

#Define the method view_detail() to view a record to the table.
def view_detail(conn):
    cur = conn.execute('SELECT Name, Wins, Losses, Ties FROM Player ORDER by Wins desc')
    print("{0:16}{1:10}{2:10}{3:10}{4:10}".format("Name", "Wins", "Losses", "Ties", "Games"))
    print("-" * 60)
    for r in cur:
        print("{0:10}{1:10}{2:12}{3:8}{4:11}".format(r[0].capitalize(), r[1], r[2], r[3], r[1] + r[2] + r[3]))
    print()

#Define the method add_detail() to add a record to the table.
def add_detail(conn):
    c = conn.cursor()
    playerName = input("Name: ")
    c.execute("select name from Player where name = ?",(playerName,))
    data = c.fetchall()
    if len(data) == 0:
        numWins = int(input("Wins: "))
        numLosses = int(input("Losses: "))
        numTies = int(input("Ties: "))
        data = (playerName, numWins, numLosses, numTies)
        insertQuery = 'insert into Player values (?,?,?,?)'
        conn.execute(insertQuery, data)
        print(playerName.capitalize(), " was added to " + "database.\n")
    else:
        print("This name is already present in the " + "database.")

#Define the method deleteRecord() to delete a record.
def delete_detail(conn):
    playerName = input("Name: ")
    conn.execute("delete from Player where name =?",(playerName,))
    print(playerName.capitalize(), "was deleted from " + "database.\n")

#Define the method updateRecord() to update a record in the table.
def update_detail(conn):
    c = conn.cursor()
    playerName = input("Enter a name of player whose " + "details you want to update: ")
    c.execute("select name from Player where name = ?", (playerName,))
    data = c.fetchall()
    if len(data) != 0:
        numWins = int(input("Enter new number of " + "wins: "))
        numLosses = int(input("Enter new number of " + "losses: "))
        numTies = int(input("Enter new number of " + "ties: "))
        data = (numWins, numLosses, numTies, playerName)
        updateQuery = '''update Player set wins = ?, losses = ?, ties = ? WHERE name = ?'''
        c.execute(updateQuery, data)
        print("The record with the name ", playerName.capitalize(), " is updated.\n")
    else:
        print("This name is not present in the " + "database.")

#Define the method displayMenu() to show the menu of choices.
def disp_menu():
    print("\nCOMMAND MENU")
    print("view   - View Player")
    print("add    - Add a Player")
    print("del    - Delete a Player")
    print("update - Update a Player")
    print("exit   - Exit Program\n")

#Define the main() function.
if __name__ == '__main__':
    print("Player Manager")
    conn = sqlite3.connect('players_Data.db')
    conn.execute('''CREATE TABLE IF NOT EXISTS Player
        (
        name TEXT NOT NULL,
        wins INT NOT NULL,
        losses INT NOT NULL,
        ties INT NOT NULL
        );''')

#Call the function disp_menu() to show the command menu.
    disp_menu()
    while True:
        inputCommand = input("Command: ")
        if inputCommand.lower() == "view": view_detail(conn)
        elif inputCommand.lower() == "add": add_detail(conn)
        elif inputCommand.lower() == "del": delete_detail(conn)
        elif inputCommand.lower() == "update": update_detail(conn)
        elif inputCommand.lower() == "exit": print("Bye!")

conn.commit()
conn.close()