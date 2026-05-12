print("================")
print("   CALCULATOR   ")
print("================")

a = int(input("enter first number : "))
b = int(input("enter second number : "))

print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = input("enter your choice : ")

if choice == "1":
    print("Result : ",a+b)

elif choice == "2":
    print("Result : ",a-b)

elif choice == "3":
    print("Result : ",a*b)

elif choice == "4":
    #if b != 0 :
    print("Result : ",a/b)
    #else:
       # print("Error : Division by zero is not allowed.")               




   

        
