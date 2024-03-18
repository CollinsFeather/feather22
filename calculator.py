def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def calculator():
    num1 = float(input("Please enter the first number:\n"))
    num2 = float(input("Please enter the second number:\n"))
    operation = input("Please enter the function (+-*/):\n")
    
    result = 0
    if operation == '+':
        result = add(num1, num2)
    elif operation == '-':
        result = subtract(num1, num2)
    elif operation == '*':
        result = multiply(num1, num2)
    elif operation == '/':
        result = divide(num1, num2)
    else:
        print("Invalid operation entered!")
        return
    
    print(f"\n>>Your result is {result}")

# Call the calculator function to start the program
calculator()
