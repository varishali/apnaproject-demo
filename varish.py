# Candidates
votes = {

    "Ali": 0,

    "Varish": 0,

    "Aman": 0
}


# Voted users
voted_users = []


while True:


    print("\n===== ONLINE VOTING SYSTEM =====")


    # User ID
    user = input("Enter User ID : ")


    # Already voted
    if user in voted_users:


        print("You Already Voted ")


    else:


        print("\nCandidates :")


        for candidate in votes:

            print(candidate)


        # Vote input
        vote = input("Enter Candidate Name : ")


        # Candidate exists
        if vote in votes:


            votes[vote] += 1


            voted_users.append(user)


            print("Vote Submitted ")


        else:


            print("Invalid Candidate")


    # Exit
    stop = input("\nStop Voting ? (yes/no) : ")


    if stop == "yes":

        break

print("\n===== FINAL RESULT =====")


for candidate, total in votes.items():

    print(candidate, ":", total)