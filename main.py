#Planned Features
# User Acces to Check Out Books and Return Them
# Admin Access to Add Books to Database and Check Who Has Checked Out a Book

import pandas
from datetime import datetime

library = {
    ('Harry Potter', 11)
}

display = pandas.DataFrame(library, columns =['Book', 'Quantity'])

def backToAdminMenu():
    back = input("Would You Like to Return To Admin Menu? ")
    if(back == "yes"):
        userMenu()
    elif(back == "no"):
        exit()

def backToMainMenu():
    back = input("Would You Like to Return To Main Menu? ")
    if(back == "yes"):
        userMenu()
    elif(back == "no"):
        exit()

def mainMenu():
    print("Welcome to The Library")
    
    username = input("Enter username: ")

    if(username == 'user'):
        userMenu()
    elif(username == 'admin'):
        adminMenu()

def userMenu():
    print("Welcome to Library App\n")
    print("1. Library\n")
    print("2. Account Status\n")
    print("3. Check Out Books\n")
    print("4. Log Out\n")

    choice = int(input("Select: "))

    if (choice == 1):
        print("Available Books")
        print(display)
        backToMainMenu()
        

    if (choice == 2):
        now = datetime.now()
        print("Time", now)
        backToMainMenu()

    if (choice == 3):
        print("Sorry. This feature is currently under construction.")
        userMenu()


    if (choice == 4):
        print("Goodbye!")
        mainMenu()

def adminMenu():
    print("Welcome Admin\n")
    print("1. Add Books\n")
    print("2. Display Books\n")
    print("3. Log Out\n")
    print("4. Exit\n")

    choice = int(input("Select: "))
    
    if(choice == 1):
        print("Sorry. This feature is currently under construction.")
        backToAdminMenu()

       
        #bookName = input("Enter book name: ")
        #bookQuantity = int(input("Enter quantity: "))
        #library.update({bookName, bookQuantity})
        #backToAdminMenu()

    if (choice == 2):
        print("Available Books")
        print(display)
        backToAdminMenu()
        
    if (choice == 3):
        print("Goodbye")
        mainMenu()

    if (choice == 4):
        exit()

mainMenu()
