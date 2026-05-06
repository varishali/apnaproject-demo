num1 = int(input("Enter First Number : "))
num2 = int(input("Enter Second Number : "))

print("Choose Operator : [+,-,*,/,**]")

op = input("Enter Operator : ")

if op == "+":
    print("Addition is : ",num1+num2)

elif op == "-":
    print("Subtraction : ",num1-num2)

elif op == "*":
    print("Multiplication is : ",num1*num2)

elif op == "/":
    if num2 != 0:
        print("Division is : ",num1/num2)
    else:
        print("Cannot Divide by Zero! ")


elif op == "**":
    print("Exponent is : ",num1**num2)

else:
    print("Invalid Operator!")















