def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

print("Select an operation please:")
print("1) Add")
print("2) Subtract")
print("3) Multiply")
print("4) Divide")

while True:
    try:
        cNumber = int(input("Enter your cNumber (1/2/3/4): "))
        if cNumber in [1, 2, 3, 4]:
            number1 = float(input("Please enter the first number: "))
            number2 = float(input("Please enter the second number: "))

            if cNumber == 1:
                print(number1, "+", number2, "=", addition(number1, number2))
            elif cNumber == 2:
                print(number1, "-", number2, "=", subtraction(number1, number2))
            elif cNumber == 3:
                print(number1, "*", number2, "=", multiplication(number1, number2))
            elif cNumber == 4:
                print(number1, "/", number2, "=", division(number1, number2))
            break
        else:
            print("Invalid input. Please enter a number between 1 and 4.")
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 4.")