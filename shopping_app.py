print("-------------------------------------")
print("\033[1mWELCOME TO SHOPPING APP\033[0m")
print("-------------------------------------")

class Shopping:
    def __init__(self):
        self.total = 0
    def product(self):

        while True:
            print("\033[1mAbalable Product\033[0m")
            print("1. Shoes = 2000")
            print("2. Shirt = 500")
            print("3. Bag = 1000")
            print("4. Exit")

            choice = input("Enter product number : ")

            if choice == "1":
                self.total += 2000
                print("Shoes added succesfully.")

                ask = input("Do you want more shoppnig ? (yes/no) : ")
                if ask.lower() == "no":
                    print("Final bill : ",self.total)
                    print("\033[1mThanks for shopping\033[0m")
                    break

            elif choice == "2":
                self.total += 500
                print("Shirt added succesfully.")

                ask = input("Do you want more shopping ? (yes/no) : ")
                if ask.lower() == "no":
                    print("Final bill. ",self.total)
                    print("\033[1mThanks for shopping\033[0m")
                    break

            elif choice == "3":
                self.total += 1000
                print("Bag added succesfully.")

                ask = input("Do you want more shopping ? (yes/no) : ")
                if ask.lower() == "no":
                    print("Total bill. ",self.total)
                    print("\033[1mThanks for shopping\033[0m")
                    break

            elif choice == "4":
                print("Shopping closed.")
                print("Your total bill : ",self.total) 
                print("\033[1mThanks for shopping\033[0m")
                break

            else:
                print("Invalid choice.")

obj = Shopping()
obj.product()                        



