candidates = {
    "Ali": 0,
    "Varish": 0,
    "Aman": 0
}

while True:

    print("\n===== Voting System =====")

    print("1. Vote")
    print("2. Result")
    print("3. Exit")

    choice = input("Enter Choice : ")

    if choice == "1":

        print("\nCandidates")

        for name in candidates:
            print(name)

        vote = input("Vote For : ")

        if vote in candidates:
            candidates[vote] += 1
            print("Vote Recorded")
        else:
            print("Invalid Candidate")

    elif choice == "2":

        print("\n===== Result =====")

        winner = ""
        max_vote = -1

        for name, vote in candidates.items():

            print(name, ":", vote)

            if vote > max_vote:
                max_vote = vote
                winner = name

        print("\nWinner :", winner)

    elif choice == "3":
        print("Voting Closed")
        break

    else:
        print("Invalid Choice")