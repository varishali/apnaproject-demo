class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def display(self):
        print(f"Name : {self.name}")
        print(f"Phone: {self.phone}")
        print("-" * 20)


class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self):
        name = input("Enter Name: ")
        phone = input("Enter Phone: ")

        contact = Contact(name, phone)
        self.contacts.append(contact)

        print("Contact Added Successfully")

    def view_contacts(self):
        if not self.contacts:
            print("No Contacts Found")
            return

        for contact in self.contacts:
            contact.display()

    def search_contact(self):
        name = input("Search Name: ")

        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                contact.display()
                return

        print("Contact Not Found")

    def delete_contact(self):
        name = input("Enter Name to Delete: ")

        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                self.contacts.remove(contact)
                print("✅ Contact Deleted")
                return

        print("Contact Not Found")


book = ContactBook()

while True:
    print("\n===== CONTACT BOOK =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        book.add_contact()

    elif choice == "2":
        book.view_contacts()

    elif choice == "3":
        book.search_contact()

    elif choice == "4":
        book.delete_contact()

    elif choice == "5":
        print("Thank You!")
        break

    else:
        print("Invalid Choice")