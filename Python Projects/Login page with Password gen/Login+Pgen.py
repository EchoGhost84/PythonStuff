#note this may not work and its in a test phase
import random
import os 
from pathlib import Path

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

with open("C:/Users/Natha/Downloads/PythonStuff/Python Projects/Login page with Password gen/UserList.txt") as user_file:
    Userlist = [username.strip() for username in user_file]

with open("C:/Users/Natha/Downloads/PythonStuff/Python Projects/Login page with Password gen/PasswordList.txt") as password_file:
    Passwordlist = [password.strip() for password in password_file]

with open("C:/Users/Natha/Downloads/PythonStuff/Python Projects/Login page with Password gen/AdminUser.txt") as admin_user_file:
    adminUsername = [admin.strip() for admin in admin_user_file]

with open("C:/Users/Natha/Downloads/PythonStuff/Python Projects/Login page with Password gen/AdminPassword.txt") as admin_password_file:
    adminPassword = [admin.strip() for admin in admin_password_file]

username = adminUsername or Userlist
password = adminPassword or Passwordlist

# uls = UserList, pwl = PasswordList, adu = AdminUser, and adp = AdminPassword

def user():
    print("Welcome to the Login Page")
    print("Please enter your username")
    global username

    username = input().strip().lower()

    if username == "":
        print("No input detected. Please try again.")
        return

    if username in Userlist or username in adminUsername:
        print("Username Correct")
        # Ask for password only if the username is correct
        password = input("Please enter your password: ").strip()
        if password in Passwordlist or password in adminPassword:
            print("Password Correct")
        else:
            print("Password Incorrect")
    else:
        print("Username Incorrect")

#removes a password from the list of passwords if needed to 
def remove():
        while username and password in adminUsername or adminPassword:
            input("Enter the password you want to remove\n")
            Passwordlist.remove(input()) 
            print("Password(s) Removed" + "your new list is:", Passwordlist)

def find_and_read_files(directory_to_search, files_to_find):
    if username and password in adminUsername or adminPassword:
        print("finding files and their contents please wait...")
    file_contents = {}
    for root, dirs, files in os.walk(directory_to_search):
        for filename in files_to_find:
            if filename in files:
                file_path = os.path.join(root, filename)
                # Open and read the file
                with open(file_path, 'r') as file:
                    content = file.read()
                    file_contents[filename] = content

    for filename, content in file_contents.items():
        if content is not None:
            print(f"Content of {filename}:\n{content}")
        else:
            print(f"{filename} not found.")

    return file_contents

# Example call with a list of filenames
directory_to_search = "C:/"  # Replace with the desired directory
files_to_find = ['UserList.txt', 'PasswordList.txt', 'AdminUser.txt', 'AdminPassword.txt']
result = find_and_read_files(directory_to_search, files_to_find)

#just a password genorator that saves to a file
def gen():
            while username and password in adminUsername or adminPassword:
                print("Welcome to the Password Generator!")
                nr_letters = int(input("How many letters would you like in your password?\n"))
                nr_symbols = int(input("How many symbols would you like?\n"))
                nr_numbers = int(input("How many numbers would you like?\n"))

                password_list = []

                for char in range(1, nr_letters + 1):
                    password_list.append(random.choice(letters))

                for char in range(1, nr_symbols + 1):
                    password_list.append(random.choice(numbers))

                for char in range(1, nr_numbers + 1):
                    password_list.append(random.choice(symbols))

                random.shuffle(password_list)

                password = ""
                for char in password_list:
                    password += char
                    
                print(input("This password will now be added to the list!!!" + " " + password + "\n"))
                password = ''.join(password_list) + '\n'
                Passwordlist.append(password)
                with open("C:/Users/Natha/Desktop/PythonStuff/Python Projects/Login page with Password gen/PasswordList.txt", "w") as file:
                    file.write("\n".join(Passwordlist))
                print(f": Updated list: {Passwordlist}\n") 
                break

user()
while True:
    print("What would you like to do?")
    choice = input("1. Remove Password  2. Find And Read Files  3. Generate password 4. quit\n")

    if choice == "1":
        remove()
    elif choice == "2":
        find_and_read_files()
    elif choice == "3":
        gen()
    elif choice == "4":
        break
    else:
        print("Invalid choice. Please enter 1, 2, 3, or 4.")