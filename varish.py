inventory = {}

while True:

    print("\n===== Inventory Management System =====")
    print("1. Add Product")
    print("2. View Products")
    print("3. Update Stock")
    print("4. Delete Product")
    print("5. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":

        product = input("Enter Product Name: ")
        stock = int(input("Enter Stock Quantity: "))

        inventory[product] = stock

        print("Product Added Successfully!")

    elif choice == "2":

        if len(inventory) == 0:
            print("No Products Found!")

        else:

            print("\n===== Product List =====")

            for product, stock in inventory.items():
                print(f"{product} : {stock}")

    elif choice == "3":

        product = input("Enter Product Name: ")

        if product in inventory:

            stock = int(input("Enter New Stock: "))
            inventory[product] = stock

            print("Stock Updated!")

        else:
            print("Product Not Found!")

    elif choice == "4":

        product = input("Enter Product Name: ")

        if product in inventory:

            del inventory[product]

            print("Product Deleted!")

        else:
            print("Product Not Found!")

    elif choice == "5":

        print("Thanks For Using Inventory System!")
        break

    else:

        print("Invalid Choice!")