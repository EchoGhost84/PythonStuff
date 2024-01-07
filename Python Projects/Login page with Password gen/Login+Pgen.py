# note this may not work and its in a test phase
import random
import os 
from pathlib import Path
global username
global password
# Define character sets for password generation
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# Open and read user-related files, stripping contents to remove leading/trailing spaces
with open("C:/Users/Natha/Downloads/PythonStuff/Python Projects/Login page with Password gen/UserList.txt") as user_file:
    Userlist = [username.strip() for username in user_file]

with open("C:/Users/Natha/Downloads/PythonStuff/Python Projects/Login page with Password gen/PasswordList.txt") as password_file:
    Passwordlist = [password.strip() for password in password_file]

with open("C:/Users/Natha/Downloads/PythonStuff/Python Projects/Login page with Password gen/AdminUser.txt") as admin_user_file:
    AdminUsername = [admin.strip() for admin in admin_user_file]

with open("C:/Users/Natha/Downloads/PythonStuff/Python Projects/Login page with Password gen/AdminPassword.txt") as admin_password_file:
    AdminPassword = [admin.strip() for admin in admin_password_file]

# Set the username and password to adminUsername or Userlist and adminPassword or Passwordlist
username = AdminUsername or Userlist
password = AdminPassword or Passwordlist

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

        # Check if no username is entered and prompt the user to try again
        if username == "":
            print("No input detected. Please try again.")
            continue  # Restart the loop if no username is entered

        # Check if the entered username is correct
        if username in Userlist or username in AdminUsername:
            print("Username Correct")
            # Ask for password only if the username is correct
            password = input("Please enter your password: ").strip()

            # Check if the entered password is correct
            if password in Passwordlist or password in AdminPassword:
                print("Password Correct")
                break  # Break out of the loop if both username and password are correct
            else:
                print("Password Incorrect. Please try again.")
        else:
            print("Username Incorrect. Please try again.")
user()

# removes a password from the list of passwords if needed to 
def remove():
        global username
        global password
        
        while username and password in AdminUsername or AdminPassword:
            input("Enter the password you want to remove\n")
            Passwordlist.remove(input()) 
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
directory_to_search = "C:/"  # Replace with the desired directory
files_to_find = ['UserList.txt', 'PasswordList.txt', 'AdminUser.txt', 'AdminPassword.txt']
result = find_and_read_files(directory_to_search, files_to_find)

# just a password genorator that saves to a file
def gen():
    global username
    global password
    # Start a loop to generate passwords as long as the user is an admin
    while username and password in AdminUsername or AdminPassword:
        print("Welcome to the Password Generator!")

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
        password = ''.join(password_list) + '\n'
        Passwordlist.append(password)
        with open("C:/Users/Natha/Desktop/PythonStuff/Python Projects/Login page with Password gen/PasswordList.txt", "w") as file:
            file.write("\n".join(Passwordlist))
        
        # Print the updated list and break out of the loop
        print(f": Updated list: {Passwordlist}\n")
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
