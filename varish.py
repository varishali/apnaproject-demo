votes = {
    "Ali": 0,
    "Ram": 0,
    "Shyam": 0
}

voted_users = []

while True:

    print("\n1. Vote")
    print("2. Result")
    print("3. Exit")

    choice = input("Enter Choice : ")

    if choice == "1":

        user = input("Enter Your Name : ")

        if user in voted_users:
            print("You Already Voted")

        else:

            print("\nCandidates")
            print("Ali")
            print("Ram")
            print("Shyam")

            candidate = input("Vote For : ")

            if candidate in votes:

                votes[candidate] += 1

                voted_users.append(user)

                print("Vote Added")

            else:
                print("Invalid Candidate")

    elif choice == "2":

        print("\nVoting Result")

        for candidate, total_votes in votes.items():
            print(candidate, ":", total_votes)

    elif choice == "3":
        print("Voting Closed")
        break

    else:
        print("Invalid Choice")
