#Planned Features
# User Acces to Check Out Books and Return Them
# Admin Access to Add Books to Database and Check Who Has Checked Out a Book

def mainMenu():
    print("Welcome to The Library")
    
    username = input("Enter username: ")

    if(username == 'user'):
        userMenu()

def userMenu():
    print("Welcome to Library App")
    print("1. Library")
    print("2. Account Status")
    print("3. Check Out Books")
    print("4. Log Out")

    choice = int(input("Select: "))

    if (choice == 4):
        print("Goodbye!")
        exit()



mainMenu()