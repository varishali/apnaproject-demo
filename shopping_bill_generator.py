import pandas as pd
data = {
    "Product" : ["Shoes","Shirt","Watch","Bag","T-Shirt"],
    "Price" : [700,400,250,500,350]
}

df = pd.DataFrame(data)

discount_list = []
final_price = []

for price in df["Price"]:
    if price >= 600:
        discount = price * 0.20

    else:
        discount = price * 0.10

    total = price - discount
    discount_list.append(discount)
    final_price.append(total)
df["Discount"] = discount_list
df["Final_Price"] = final_price 

print("=" *40)
print("          Online Shopping Bill")
print("=" *40)

print("\nProduct Data :\n")
print(df)