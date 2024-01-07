def remove():
    global Passwordlist

    print("Remove Password")
    password_to_remove = input("Enter the password you want to remove: ")

    if password_to_remove in Passwordlist:
        Passwordlist.remove(password_to_remove)
        with open("C:/Users/Natha/Downloads/PythonStuff/Python Projects/Login page with Password gen/PasswordList.txt", "w") as file:
            file.write("\n".join(Passwordlist))
        print(f"Password removed. Updated list: {Passwordlist}")
    else:
        print("Password not found in the list.")


