# ==========================
# Contact Book Management
# ==========================

class Contact:

    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def show(self):
        print(f"Name : {self.name}")
        print(f"Phone : {self.phone}")
        print("-" * 25)


class ContactBook:

    def __init__(self):
        self.contacts = []

    # Add Contact
    def add_contact(self):

        name = input("Enter Name : ")
        phone = input("Enter Phone Number : ")

        contact = Contact(name, phone)

        self.contacts.append(contact)

        print("Contact Added Successfully")

    # View Contacts
    def view_contacts(self):

        if len(self.contacts) == 0:
            print("No Contacts Found")
            return

        print("\n===== CONTACT LIST =====")

        for contact in self.contacts:
            contact.show()

    # Search Contact
    def search_contact(self):

        name = input("Enter Name : ")

        for contact in self.contacts:

            if contact.name.lower() == name.lower():

                print("\nContact Found")
                contact.show()
                return

        print("Contact Not Found")

    # Delete Contact
    def delete_contact(self):

        name = input("Enter Name : ")

        for contact in self.contacts:

            if contact.name.lower() == name.lower():

                self.contacts.remove(contact)

                print("Contact Deleted")

                return

        print("Contact Not Found")


# ==========================
# Main Program
# ==========================

book = ContactBook()

while True:

    print("\n===== CONTACT BOOK =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice = input("Enter Choice : ")

    if choice == "1":
        book.add_contact()

    elif choice == "2":
        book.view_contacts()

    elif choice == "3":
        book.search_contact()

    elif choice == "4":
        book.delete_contact()

    elif choice == "5":
        print("Program Closed")
        break

    else:
        print("Invalid Choice")