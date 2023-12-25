#note this may not work and its in a test phase
import random
import os 
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# uls = UserList, pwl = PasswordList, adu = AdminUser, and adp = AdminPassword
for root, dirs, files in os.walk(r''):
    for name in files:
          if name == 'UserList.txt':
               print(os.path.abspath(os.path.join(root, name)))
for root, dirs, files in os.walk(r''):
     for name in files:
          if name == 'Passwordlist.txt':pass    
               print(os.path.abspath(os.path.join(root, name)))

for root, dirs, files in os.walk(r''):
     for name in files:
          if name == 'AdminPassword.txt':
               print(os.path.abspath(os.path.join(root, name)))

for root, dirs, files in os.walk(r''):
     for name in files:
          if name == 'AdminUser.txt':
               print(os.path.abspath(os.path.join(root, name)))
               
uls = open(r'UserList.txt').readlines()
print("Found the txt file Here:" + os.path.abspath(uls))

pwl = open(r'Passwordlist.txt').readlines()
print("Found the txt file Here:" + os.path.abspath(pwl))

adu = open(r'AdminPassword.txt').readlines()
print("Found the txt file Here:" + os.path.abspath(adu))

adp = open(r'AdminUser.txt').readlines()
print("Found the txt file Here:" + os.path.abspath(adp))

if FileNotFoundError() or FileExistsError():
    print("check if the file exists or where the file is")
else: 
     print("we found the files")

Userlist = uls
Userlist = [username.strip() for username in Userlist]
Passwordlist = pwl
Passwordlist = [username.strip() for username in Passwordlist]
adminUsername =  adu
adminUsername = [username.strip() for username in adminUsername]
adminPassword =  adp
adminPassword = [username.strip() for username in adminPassword]

username = adminUsername or Userlist
password = adminPassword or Passwordlist
#makes sure the username and password are correct

print("Welcome to the Login Page")
print("Please enter your username")
def user():
    global username
    username = input().strip().lower()
    if username in Userlist or username in adminUsername:
        print("User Correct")
    else:
        print("User Incorrect")
            
    print("Please enter your password")
    password = input().strip()
    if password in Passwordlist or password in adminPassword:
        print("Password Correct")
    else:
        print("Password Incorrect")
        
#removes a password from the list of passwords if needed to 
def remove():
        if password in Passwordlist or password in adminPassword:
            input("Enter the password you want to remove\n")
            Passwordlist.remove(input()) 
            print("Password(s) Removed" + "your new list is:", Passwordlist)

        
#just a password genorator that saves to a file
def gen():
            while username in adminUsername:
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
                with open("C:/Users/Natha/OneDrive/Desktop/PythonStuff/Python Projects/Login page with Password gen/PasswordList.txt", "w") as file:
                    file.write("\n".join(Passwordlist))
                print(f": Updated list: {Passwordlist}\n") 
                break
user()

print("what would you like to do?")
input("1" + ".gen password" + " " + "2" + ".remove password," + " " + "3" ".quit\n")
while():
    if input() == "1":
        gen()

    if input() == "2":
        remove()
        
    if input() == "3":
        break