
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

while input == adminPassword:
        print("What would you like to add to the UserList?")
        Userlist.append(input)
        print("Updated List", Userlist)
        continue
else:
    while input == adminPassword:
        print("What would you like to add to the Passwordlist?")
        Passwordlist.append(input)
        print("Updated List", Passwordlist)
        continue
