# Define math functions as a class
class MathOperations:
    @staticmethod
    def addition(x, y):
        return x + y

    @staticmethod
    def subtraction(x, y):
        return x - y

    @staticmethod
    def multiplication(x, y):
        return x * y

    @staticmethod
    def division(x, y):
        return x / y

# Create an instance of the MathOperations class
math_operations = MathOperations()

# Main loop for user interaction
while True:
    choice = input("1. Addition  2. Multiplication  3. Subtraction  4. Division\n")
    
    # Check if the user's choice is valid
    if choice in ("1", "2", "3", "4"):
        try:
            number1 = float(input("Enter the first number: \n"))
            number2 = float(input("Enter the second number: \n"))
        except ValueError:
            print("Please enter valid numbers.")
            continue

        # Perform the chosen math operation and print the result
        if choice == "1":
            print(number1, "+", number2, "=", math_operations.addition(number1, number2))
        elif choice == "2":
            print(number1, "x", number2, "=", math_operations.multiplication(number1, number2))
        elif choice == "3":
            print(number1, "-", number2, "=", math_operations.subtraction(number1, number2))
        elif choice == "4":
            print(number1, "/", number2, "=", math_operations.division(number1, number2))

        # Open 'Math.txt' file and append the result
        with open('Math.txt', 'a') as file:
            file.write(f"{number1} {choice} {number2} = {math_operations.__getattribute__('addition' if choice == '1' else 'multiplication' if choice == '2' else 'subtraction' if choice == '3' else 'division')(number1, number2)}\n")

        # Ask if the user wants to perform another calculation
        calculation = input("Do another calculation? (yes/no): \n")
        if calculation.lower() == "no":
            break
    else:
        print("Invalid choice. Please enter 1, 2, 3, or 4.")
