people = []

n = int(input("How Many People: "))

for i in range(n):

    name = input("Enter Name: ")
    people.append(name)

bill = float(input("Enter Total Bill: "))

share = bill / n

print("\n===== Split Result =====")

for person in people:
    print(f"{person} Pays ₹{share:.2f}")