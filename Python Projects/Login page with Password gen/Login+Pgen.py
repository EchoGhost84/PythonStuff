#note this may not work and its in a test phase

import random

letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

Userlist = ["Nathan","nathan"]
adminPassword = ["ADMINPASSWORD"]
Passwordlist = ["Password1","password1"]

while():
    if input() in Userlist:
        print("User Correct")
    else:
        print("User Incorrect")

    if input() in Passwordlist:
            print("Password Correct")
    else:
            print("Password Incorrect")
    break

#adds input to the userlist and adds it to a file 
while input == adminPassword:
    print("What would you like to add to the User List?")
    Userlist.append(input)
    print("Updated List", Userlist)
    with open('PasswordsList.txt', 'a') as file:
        file.write(Userlist)
print(f": User list: {Userlist}\n")

#password gen for the login
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

# convert list to string
pwd = ''.join(password_list) + '\n'

# saves the password to a file
with open('PasswordsList.txt', 'a') as file:
        file.write(pwd)
print(f"Your random password is: {pwd}\n")

Passwordlist.append(pwd)
print("Updated List", Passwordlist)

