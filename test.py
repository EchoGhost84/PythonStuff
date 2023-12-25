import os

txt = 'Passwordlist.txt'
print(os.path.abspath(txt))

# i have this here incase the other way doesnt work and i can just copy and paste it if needed
uls = 'UserList.txt'
print("Found the .txt file Here:" + os.path.abspath(uls))
pwl = 'Passwordlist.txt'
print("Found the .txt file Here:" + os.path.abspath(pwl))
adu = 'AdminPassword.txt'
print("Found the txt file Here:" + os.path.abspath(adu))
adp = 'AdminUser.txt'
print("Found the txt file Here:" + os.path.abspath(adp))
if FileNotFoundError() or FileExistsError():
    print("check if the file exists or where the file is")
else: 
     print("we found the files")

# i have this here incase the other way doesnt work and i can just copy and paste it if needed
Userlist = open(r"C:/Users/Natha/OneDrive/Desktop/PythonStuff/Python Projects/Login page with Password gen/UserList.txt",'r').readlines()
Userlist = [username.strip() for username in Userlist]
Passwordlist = open(r"C:/Users/Natha/OneDrive/Desktop/PythonStuff/Python Projects/Login page with Password gen/PasswordList.txt",'r+').readlines()
Passwordlist = [username.strip() for username in Passwordlist]
adminUsername =  open(r"C:/Users/Natha/OneDrive/Desktop/PythonStuff/Python Projects/Login page with Password gen/AdminUser.txt",'r').readlines()
adminUsername = [username.strip() for username in adminUsername]
adminPassword =  open(r"C:/Users/Natha/OneDrive/Desktop/PythonStuff/Python Projects/Login page with Password gen/AdminPassword.txt",'r').readlines()
adminPassword = [username.strip() for username in adminPassword]
