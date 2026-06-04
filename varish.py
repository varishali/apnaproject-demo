votes = {
    "Aman": 0,
    "Rahul": 0,
    "Sahil": 0
}

while True:

    print("\n===== Voting System =====")
    print("1. Cast Vote")
    print("2. View Results")
    print("3. Declare Winner")
    print("4. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":

        print("\nCandidates:")
        for candidate in votes:
            print(candidate)

        candidate = input("\nEnter Candidate Name: ")

        if candidate in votes:
            votes[candidate] += 1
            print("Vote Cast Successfully!")
        else:
            print("Invalid Candidate!")

    elif choice == "2":

        print("\n===== Results =====")

        for candidate, vote_count in votes.items():
            print(f"{candidate} : {vote_count} Votes")

    elif choice == "3":

        winner = max(votes, key=votes.get)

        print("\n===== Winner =====")
        print(f"{winner} won with {votes[winner]} votes!")

    elif choice == "4":

        print("Thanks For Using Voting System!")
        break

    else:
        print("Invalid Choice!")