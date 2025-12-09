
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero!"
    return a / b



def calculate():
    try:
        num1 = float(input("Enter first number: "))
        operator = input("Enter operator (+, -, *, /): ").strip()
        num2 = float(input("Enter second number: "))

        if operator == "+":
            return add(num1, num2)
        elif operator == "-":
            return subtract(num1, num2)
        elif operator == "*":
            return multiply(num1, num2)
        elif operator == "/":
            return divide(num1, num2)
        else:
            return "Invalid operator!"

    except ValueError:
        return "Invalid input! Please enter valid numbers."



def clear():
    print("\n--- Calculator cleared ---\n")


def menu():
    while True:
        print("\n===== SIMPLE CALCULATOR =====")
        print("1. Calculate")
        print("2. Clear")
        print("3. Exit")

        choice = input("Choose an option (1/2/3): ")

        if choice == "1":
            result = calculate()
            print("Result:", result)

        elif choice == "2":
            clear()

        elif choice == "3":
            print("Exiting calculator. Goodbye!")
            break

        else:
            print("Invalid choice! Try again.")


# Run the program
menu()