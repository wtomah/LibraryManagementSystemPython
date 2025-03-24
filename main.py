#Planned Features
# User Acces to Check Out Books and Return Them
# Admin Access to Add Books to Database and Check Who Has Checked Out a Book

import pandas
from datetime import datetime

library = {
    'books':["Harry Potter", "Dr Seuss", "48 Laws of Power"],
    'quantity' : [21, 2, 11]
}

display = pandas.DataFrame(library)

def backToMainMenu():
    back = input("Would You Like to Return To Main Menu?")
    if(back == "yes"):
        userMenu()
    elif(back == "no"):
        exit()

def mainMenu():
    print("Welcome to The Library")
    
    username = input("Enter username: ")

    if(username == 'user'):
        userMenu()

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
        exit()



mainMenu()
