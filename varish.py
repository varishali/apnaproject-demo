# Product stock
stock = {

    "Laptop": 5,

    "Mouse": 10,

    "Keyboard": 7
}


while True:


    print("\n===== INVENTORY =====")


    # Show stock
    for item, qty in stock.items():

        print(item, ":", qty)


    # User input
    product = input("\nEnter Product Name : ")


    # Product exists
    if product in stock:


        quantity = int(input("Enter Quantity : "))


        # Stock available
        if quantity <= stock[product]:


            stock[product] -= quantity


            print("Order Successful ")


        else:


            print("Not Enough Stock ")


    else:


        print("Product Not Found")


    # Stop program
    stop = input("Exit ? (yes/no) : ")


    if stop == "yes":

        break