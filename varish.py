bookmarks = {}

while True:

    print("\n===== Bookmark Manager =====")
    print("1. Add Bookmark")
    print("2. View Bookmarks")
    print("3. Search Bookmark")
    print("4. Delete Bookmark")
    print("5. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":

        name = input("Website Name: ")
        url = input("Website URL: ")

        bookmarks[name] = url

        print("Bookmark Added!")

    elif choice == "2":

        if len(bookmarks) == 0:
            print("No Bookmarks Found!")

        else:

            for name, url in bookmarks.items():
                print(f"{name} -> {url}")

    elif choice == "3":

        name = input("Search Website: ")

        if name in bookmarks:
            print(bookmarks[name])
        else:
            print("Bookmark Not Found!")

    elif choice == "4":

        name = input("Delete Website: ")

        if name in bookmarks:
            del bookmarks[name]
            print("Deleted Successfully!")
        else:
            print("Bookmark Not Found!")

    elif choice == "5":
        break

    else:
        print("Invalid Choice!")