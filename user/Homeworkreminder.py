"""
prog: Homeworkreminder.py
Name: Dimitrios Syrbopoulos
Date: 5/06/2018
Desc: Organises your work and reminds you
"""

#import modules
import sqlite3
import time
import datetime
from datetime import date
import sys
#instantiate variables
response = ""
item = ""
notes = ""
due = ""
reminder = ""
#set up database and connect
conn = sqlite3.connect('homeworkD.db')
c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS homework (item TEXT, due TEXT, notes TEXT, reminder TEXT)")
#gets user input and adds to database
def dynamic_data_entry():
    item = str(input ("item : "))
    due = str(input ("due : "))
    notes = str(input ("notes : "))
    reminder = str(input ("reminder (weekly? daily?: "))
    c.execute("INSERT INTO homework (item, due, notes, reminder) VALUES (?, ?, ?, ?)",(item, due, notes, reminder))
    conn.commit()
#deletes requested homework
def delete (id):
    id = input ("Which item do you want to delete?")
    sqlcommand = 'DELETE FROM homework WHERE item =?'
    c.execute(sqlcommand, (id,))
    prompt ()
#lists all the homework in the database
def printList ():
    c.execute("SELECT * FROM homework")
    print("All Homework : ")
    result = c.fetchall()
    for r in result:
        for part in r:
            print (part)
        print ("\n")
    prompt ()
#asks user for instruction
def prompt ():
    response = input ("[N] add homework [T] list homework due today or tomorrow \n[L] list all homework or [D] delete homework [Q] quit\n")
    if response == "N":
        dynamic_data_entry()
        time.sleep(1)
    elif response == "L":
        printList ()
    elif response == "T":
#get current date in dd/mm/yyyy format
        currentdate = date.today().strftime("%d/%m/%Y")
#add one day to today to get tomorrows date
        nextday = date.today() + datetime.timedelta(days=1)
        tomorrow = nextday.strftime("%d/%m/%Y")
#find todays homework due today in the data base
        c.execute("SELECT * FROM homework WHERE due = ?",(currentdate,))
        data = c.fetchall()
        for r in data:
            print ('** DUE TODAY **\n')
            for part in r:
                print (part)
#hash n is line return
            print ("\n")
#find homework due tomorrow
        c.execute("SELECT * FROM homework WHERE due = ?",(tomorrow,))
        data = c.fetchall()
        for r in data:
            print ('** DUE TOMORROW **\n')
            for part in r:
                print (part)
            print ("\n")
#launch delete function
    elif response == "D":
        delete ()
#quit and goodbye
    elif response == "Q":
        sys.exit("Goodbye, and Good Luck!")
#not using one of the leters it prints other message
    else:
        print ("Sorry, command not recognised. Try again!")
    prompt()
#main function runs function once and then launches prompt
def main():
    print('*************\nHOMEWORK REMINDER\n*************\n')
    printList()
    print ("G'day, would you like to :\n")
    prompt()
#setup python run with error and exit
if __name__=="__main__":
    try :
        main()
    except KeyboardInterrupt:
        print ('Interrupted')
#close data base on exit
    finally :
        c.close
        conn.close()






