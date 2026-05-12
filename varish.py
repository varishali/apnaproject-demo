# Password protected calculator
print("============================================")
print("Welcome to the password protected Calculator")
print("============================================")

password = "varish"
phone_num = "1234567890"

password = input("Enter The Password : ")



if password == "varish":
    print("==================")
    print("Correct Password !")
    print("==================")

    print("Welcome To The Calculator")

    a = int(input("Enter The First Number : "))
    b = int(input("Enter The Second Number : "))

    op = input("Enter The Operator (+,-,*,/) : ")

    if op == "+":
        print("The Addition Is : ",a+b)
    elif op == "-":
        print("The Subtraction Is : ",a-b)
    elif op == "*":
        print("The Multiplication Is : ",a*b)
    elif op == "/":
        print("The Division Is : ",a/b)
    else:
        print("Invalid Operator!")
        print("try again!")


elif password != "varish":
    print("================")
    print("Wrong Password !")
    print("================")

    phone_num = input("Enter Phone Number To Enter Calculator :")

    if phone_num == "1234567890":
        print("Welcome to the calculator")
        


        a = int(input("Enter The First Number : "))
        b = int(input("Enter The Second Number : "))

        op = input("Enter The Operator (+,-,*,/) : ")

        if op == "+":
            print("The Addition Is : ",a+b)
        elif op == "-":
            print("The Subtraction Is : ",a-b)
        elif op == "*":
            print("The Multiplication Is : ",a*b)
        elif op == "/":
            print("The Division Is : ",a/b)
        else:
            print("Invalid Operator!")
            print("try again!")

    else:
        print("Invalid Phone Number !") 
        print("You Are Not Allowed To Enter The Calculator !")
        print("Try Again !") 
           
else:
    print("Invalid Phone Number !")
   




      
    




   

        
