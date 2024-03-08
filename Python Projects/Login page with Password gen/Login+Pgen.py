import random
import os 
from pathlib import Path

global username
global password

#Define character sets for password generation
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = [')', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

Passwordlist = open("C:/Users/Natha/Downloads/PythonStuff/Python Projects/Login page with Password gen/PasswordList.txt")

# Open and read user-related files, stripping contents to remove leading/trailing spaces
with open("C:/Users/Natha/Downloads/PythonStuff/Python Projects/Login page with Password gen/UserList.txt") as user_file:
    Userlist = [username.strip() for username in user_file]

with open("C:/Users/Natha/Downloads/PythonStuff/Python Projects/Login page with Password gen/PasswordList.txt") as Password_file:
    Passwordlist = [username.strip() for username in Password_file]

with open("C:/Users/Natha/Downloads/PythonStuff/Python Projects/Login page with Password gen/AdminUser.txt") as admin_user_file:
    AdminUsername = [admin.strip() for admin in admin_user_file]

with open("C:/Users/Natha/Downloads/PythonStuff/Python Projects/Login page with Password gen/AdminPassword.txt") as admin_password_file:
    AdminPassword = [admin.strip() for admin in admin_password_file]

# Set the username and password to adminUsername or Userlist and adminPassword or Passwordlist
username = AdminUsername or Userlist
password = AdminPassword or Passwordlist

adminlogin = AdminUsername
adminpass = AdminPassword
userlogin = Userlist
userPass = Passwordlist
# Explanation of code structure and purpose:
# The code reads user-related files, such as UserList.txt and PasswordList.txt, and strips their contents to remove any leading or trailing spaces.
# It uses the admin-related files (AdminUser.txt and AdminPassword.txt) to set the admin credentials.
# The username and password are then set to either the admin credentials or the user credentials, making the code more compact.


def user():
    global username
    global password
    # Introduce a while loop to keep prompting until correct credentials are entered
    while True:
        print("Welcome to the Login Page")
        print("Please enter your username")
        username = input().strip().lower()
        
        #should check if you have the correct creds before going to the next area

        if userlogin or userPass in input():
            print("What would you like to do?")
        else:
            continue

        # Check if no username is entered and prompt the user to try again
        if username == "":
            print("No input detected. Please try again.")
            continue  # Restart the loop if no username is entered

        # Check if the entered username is correct
        if username in Userlist or username in AdminUsername:
            print("Username Correct")
            # Ask for password only if the username is correct
            password = input("Please enter your password:\n").strip()

            # Check if the entered password is correct
            if password in Passwordlist or password in AdminPassword:
                print("Password Correct")
                    #the options for the user
                if password in Passwordlist:
                    print("1. Chat file" + " " + "4. Break")
                        #asks the user what they would like to do
                    choice = input("What would you like to do?\n")
                    while True:
                        if choice == "1":
                            WhatToDo()
                        elif choice == "4":
                                break
                #Break out of the loop if both username and password are correct
                break
            else:
                print("Password Incorrect. Please try again.")
        else:
            print("Username Incorrect. Please try again.")
    
user()

def WhatToDo():
    with open("Chat.txt") as file:
            file.writable(input("What would you like to say?"))
            if input() == True:
                print("message send sucsessfully!")
                input("Would you like to send another message?")
                if input() == "yes":
                    return choice == "1"
                file.close()
                
def remove():
        global username
        global password
        
        while username and password in AdminUsername or AdminPassword:
            Passwordlist.remove(input("Enter the password you want to remove\n")) 
            print("Password(s) Removed" + "your new list is:", Passwordlist)

def find_and_read_files(directory_to_search, files_to_find):
        # Check if the user is an admin before proceeding
    if username and password in AdminUsername or AdminPassword:
        print("Finding files, please wait...")

    file_contents = {}
        
        # Walk through the specified directory and search for the specified files
    for root, dirs, files in os.walk(directory_to_search):
        for filename in files_to_find:
            if filename in files:
                file_path = os.path.join(root, filename)
                    
                    # Open and read the file
                with open(file_path, 'r') as file:
                    content = file.read()
                    file_contents[filename] = content

        # Display the contents of the found files
    for filename, content in file_contents.items():
        if content is not None:
                print(f"{filename}:\n")
        else:
            print(f"{filename} not found.")

    return file_contents

# Example call with a list of filenames
directory_to_search = "C:/Users/Natha/Downloads/PythonStuff/Python Projects/Login page with Password gen"
files_to_find = ['UserList.txt', 'PasswordList.txt', 'AdminUser.txt', 'AdminPassword.txt']
result = find_and_read_files(directory_to_search, files_to_find)

# just a password genorator that saves to a file
def gen():
    global username
    global password
    # Start a loop to generate passwords as long as the user is an admin
    while username and password in AdminUsername or AdminPassword:
        print("Welcome to the Password Generator!")

        #Asks for your name
        your_name = input("What is your name?\n")
        your_use = input("What are you going to be using this Password for?\n")

        # Prompt the user for the desired number of letters, symbols, and numbers
        nr_letters = int(input("How many letters would you like in your password?\n"))
        nr_symbols = int(input("How many symbols would you like?\n"))
        nr_numbers = int(input("How many numbers would you like?\n"))

        password_list = []

        # Generate letters for the password
        for char in range(1, nr_letters + 1):
            password_list.append(random.choice(letters))

        # Generate symbols for the password
        for char in range(1, nr_symbols + 1):
            password_list.append(random.choice(numbers))
        
        # Generate numbers for the password
        for char in range(1, nr_numbers + 1):
            password_list.append(random.choice(symbols))

        # Shuffle the password characters
        random.shuffle(password_list)

        # Create a string from the shuffled password characters
        password = ""
        for char in password_list:
            password += char

        # Print the generated password and ask for user input
        print(input("This password will now be added to the list!!!" + " " + password + "\n"))

        # Update the password list and save it to a file
        password = ''.join(password_list) + " " + "(" + your_name + ")" + " " + "(" + your_use + ")" + "\n"
        with open("C:/Users/Natha/Downloads/PythonStuff/Python Projects/Login page with Password gen/PasswordList.txt", 'a') as file:
            file.writelines(password)

            print("Your Password has been added to the list!!!")
        break

while True:
    # Display menu options to the user
    print("What would you like to do?")
    choice = input("1. Remove Password  2. Find And Read Files  3. Generate password 4. Quit\n")

    # Check user choice and perform corresponding actions
    if choice == "1":
        # If choice is 1, call the remove() function
        remove()
    elif choice == "2":
        # If choice is 2, call the find_and_read_files() function with specified arguments
        find_and_read_files(directory_to_search, files_to_find)
    elif choice == "3":
        # If choice is 3, call the gen() function
        gen()
    elif choice == "4":
        # If choice is 4, break out of the loop (quit the program)
        break
    else:
        # If an invalid choice is entered, prompt the user to enter a valid choice
        print("Invalid choice. Please enter 1, 2, 3, or 4.")