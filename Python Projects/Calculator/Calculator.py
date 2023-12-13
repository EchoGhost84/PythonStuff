def addition(x, y):
    return x + y

def subtraction(x, y):
    return x - y

def multiplication(x, y):
    return x * y

def division(x, y):
    return x / y

while True:
    
    choice = input("1. Addition" + ' ' + "2. Multiplication" + ' ' + "3. Subtraction" + ' '  "4. Division\n")
    if choice in ("1. Addition", "2. Multiplication", "3. Subtraction", "4. Division"):
        try:
            number1 = float(input("gimmie first number: \n"))
            number2 = float(input("gimmie second number: \n"))
        except ValueError:
            print("Please enter a number.")
            continue

        if choice == "1. Addition":
            print(number1, "+", number2, "=", addition(number1, number2))

        if choice == "2. Multiplication":
            print(number1, "x", number2, "=", multiplication(number1, number2))

        if choice == "3. Subtraction":
            print(number1, "-", number2, "=", subtraction(number1, number2))

        if choice == "4. Division": 
            print(number1, "/", number2, "=", division(number1, number2))

        calculation = input("another? (yes/no): \n")
        if calculation == "no":
                break
        else:
                print("Invalid Input\n")



