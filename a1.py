def add (a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


try:
    number1 = float(input("Enter first number: "))
    number2 = float(input("Enter second number: "))  
    operation = input("Enter operation (+, -, *, /): ")
    if operation == '+':
        result = add(number1, number2)
    elif operation == '-':
        result = subtract(number1, number2)
    elif operation == '*':
        result = multiply(number1, number2)
    elif operation == '/':
        result = divide(number1, number2)
    else:
        raise ValueError("Invalid operation.")
    
    print(f"The result is: {result}")
except ValueError as e:
    print(f"Error: {e}")
