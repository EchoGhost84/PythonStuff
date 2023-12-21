#note this may not work and its in a test phase
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
Userlist = ["Nathan","nathan"]
adminPassword = ["ADMINPASSWORD"]
Passwordlist = ["Password1","password1"]

#makes sure the username and password are correct
def user():
    print("Welcome to the Login Page")
    print(input("Please enter your username\n"))

    while input() in Userlist:
        print("User Correct")
    if input not in Userlist:
        print("User Incorrect")

    print(input("Pease enter your password\n"))
    while input() in Passwordlist:
        print("User Correct")
    if input not in Passwordlist:
        print("User Incorrect")

#removes a password from the list of passwords if needed to 
def remove():
    if input == adminPassword:
        rempass = input("Enter the password you want to remove")
        while rempass:
            print("what password would you like to remove?")
            Passwordlist.remove(input()) 
            print("Password(s) Removed" + "your new list is:", Passwordlist)

#just a password genorator that saves to a file
def gen():
    while input == adminPassword:
            print("Welcome to the PyPassword Generator!")
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

            print(input("Would you like to add this password to the list?"))
            while input in list == ["yes", "Yes", "YES"]:
                password = ''.join(password_list) + '\n'
                Passwordlist.append(password)
            print("Updated List", Passwordlist)
            with open('PasswordsList.txt', 'a') as file:
                file.write(Passwordlist)
            print(f": Updated list: {Passwordlist}\n") 
            while(): 
                input in list == ["no", "No", "NO", "nO"]
                break


user()
gen()
remove()





                            #Just incase if i need it for later i dont have to redo the code#

#add()
#adds a password to the pasword list if needed to :
# def add():
#     while input == adminPassword:
#         print("What would you like to add to the User List?")
#         Userlist.append(input)
#     print("Updated List", Userlist)
#     with open('PasswordsList.txt', 'a') as file:
#         file.write(Userlist)
#     print(f": User list: {Userlist}\n")