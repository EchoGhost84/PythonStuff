#note this may not work and its in a test phase
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
Userlist = open(r"C:\Users\Natha\OneDrive\Desktop\PythonStuff\Python Projects\Login page with Password gen\UserList.txt",'r').readlines()
Passwordlist = open(r"C:\Users\Natha\OneDrive\Desktop\PythonStuff\Python Projects\Login page with Password gen\PasswordList.txt",'r').readlines()
adminUsername =  open(r"C:\Users\Natha\OneDrive\Desktop\PythonStuff\Python Projects\Login page with Password gen\AdminUser.txt",'r').readlines()
adminPassword =  open(r"C:\Users\Natha\OneDrive\Desktop\PythonStuff\Python Projects\Login page with Password gen\AdminPassword.txt",'r').readlines()
#makes sure the username and password are correct
def user():
    print("Welcome to the Login Page")
    print("Please enter your username")

    username = input().strip().lower()
    if username in Userlist or adminUsername:
        print("User Correct")
    else:
        print("User Incorrect")

    print("Pease enter your password")
    password =input().strip()
    if password in Passwordlist or adminPassword:
        print("Password Correct")
    else:
        print("Password Incorrect")
    
#removes a password from the list of passwords if needed to 
def remove():
        rempass = input("Enter the password you want to remove")
        while rempass:
            print("what password would you like to remove?")
            Passwordlist.remove(input()) 
            print("Password(s) Removed" + "your new list is:", Passwordlist)

#just a password genorator that saves to a file
def gen():
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

            print(input("Would you like to add this password to the list?"))
            while input == ["yes", "Yes", "YES"]:
                password = ''.join(password_list) + '\n'
                Passwordlist.append(password)
            print("Updated List", Passwordlist)
            with open('PasswordsList.txt', 'a') as file:
                file.write(Passwordlist)
            print(f": Updated list: {Passwordlist}\n") 
            while(): 
                input == ["no", "No", "NO", "nO"]
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