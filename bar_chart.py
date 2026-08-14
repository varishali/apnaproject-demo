def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Divide by zero nahi ho sakta"
    return a / b

def calculator():
    print("Calculator Shuru")
    print("Operations: +, -, *, /")
    
    num1 = float(input("Pehla number: "))
    op = input("Operation choose karein (+, -, *, /): ")
    num2 = float(input("Dusra number: "))

    if op == "+":
        result = add(num1, num2)
    elif op == "-":
        result = subtract(num1, num2)
    elif op == "*":
        result = multiply(num1, num2)
    elif op == "/":
        result = divide(num1, num2)
    else:
        result = "Invalid operation!"

    print(f"Result: {result}")

calculator()