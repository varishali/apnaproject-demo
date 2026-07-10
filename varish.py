class Product:
    def __init__(self, name, price, qty):
        self.name = name
        self.price = price
        self.qty = qty

    def total(self):
        return self.price * self.qty    

    def show(self):
        print(f"{self.name} | ${self.price} * {self.qty} = ${self.total()}")


class Cart:
    def __init__(self):
        self.items = []

    # add product
    def add_product(self):

        name = input("Enter Product Name : ")
        price = int(input("Enter Product Price : "))
        qty = int(input("Enter Product Quantity : "))

        product = Product(name,price,qty)

        self.items.append(product)

        print("Product Added ..")

    # view cart
    def view_cart(self):
        if len(self.items) == 0:
            print("Cart is Empty")
            return
        print("===  CART  ===")

        bill = 0

        for item in self.items:
            item.show()
            bill += item.total()

        print("Total Bill $:",bill)

    # remove product
    def remove_product(self):
        name = input("Product Name : ")
        for item in self.items:
            if item.name.lower() == name.lower():
                self.items.remove(item)

                print("Product Removed")

                return

        print("Product Not Found")


# main program
cart = Cart()

while True:
    
    print("\n===== SHOPPING CART =====")
    print("1. Add Product")
    print("2. View Cart")
    print("3. Remove Product")
    print("4. Exit")

    choice = input("Enter Choice : ")

    if choice == "1":
        cart.add_product()

    elif choice == "2":
        cart.view_cart()

    elif choice == "3":
        cart.remove_product()

    elif choice == "4":
        print("Thank You")
        break

    else:
        print("Invalid Choice")

                     
