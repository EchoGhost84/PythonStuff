name = input("What is your name?\n")
Age = input("How old are you?\n")

while not Age.isnumeric():
    print("Age must be a number")
    Age = input()
    
if int(Age) <= 17:
    print("You cant be on the list\n") 
elif int(Age) >= 17:
    write = name + "," + " " + Age + "\n"
    with open('ListOfNames.txt', 'a') as file:
       file.write(write)
       print("Welcome to the list")

       