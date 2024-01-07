import os
from pathlib import Path

#opens the file location for heach password or username list 
with open("C:/Users/Natha/Downloads/PythonStuff/Python Projects/Login page with Password gen/UserList.txt") as user_file:
    Userlist = [username.strip() for username in user_file]

with open("C:/Users/Natha/Downloads/PythonStuff/Python Projects/Login page with Password gen/PasswordList.txt") as password_file:
    Passwordlist = [password.strip() for password in password_file]

with open("C:/Users/Natha/Downloads/PythonStuff/Python Projects/Login page with Password gen/AdminUser.txt") as admin_user_file:
    adminUsername = [admin.strip() for admin in admin_user_file]

with open("C:/Users/Natha/Downloads/PythonStuff/Python Projects/Login page with Password gen/AdminPassword.txt") as admin_password_file:
    adminPassword = [admin.strip() for admin in admin_password_file]

#changes the var for username and password lists to one var
username = adminUsername or Userlist
password = adminPassword or Passwordlist

#finds the files on the system and prints the contents of the files 
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

