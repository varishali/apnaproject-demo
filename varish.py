cart = []

total = 0

while True:

    print("\n1. Add Item")
    print("2. View Cart")
    print("3. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":

        item = input("Enter Item Name: ")

        price = int(input("Enter Price: "))

        cart.append((item, price))

        total += price

        print("Item Added!")

    elif choice == "2":

        print("\n===== CART =====")

        for item, price in cart:

            print(item, "-", price)

        print("Total Bill:", total)

    elif choice == "3":

        print("Thank You!")

        break

    else:

        print("Invalid Choice!")
