# kon banega crorepati 2026b

print("===welcome to kon banega crorepati 2026===")

money = 0

#question 1
print("Q1. What is tha capital od India?")
print("a. Mumbai")
print("b. dehli")
print("c. Kolkata")
print("d. Chennai")

answer1 = input("Enter your answer:")

if answer1 == "b":
    print("cprrect answer")
    money += 1000
    print("you have won :",money)

    #question 2
    print("Next Question for -- 5000 --")
    print("Q2. what is the national animals of India ?")
    print("a. Tiger")
    print("b. Lion")
    print("c. Elephant")
    print("d. Bear")

    answer2 = input("Enter your answer:")

    if answer2 == "a":
        print("correct answer")
        money += 5000
        print("you have won :",money)
    

        #question 3
        print("Next question for -- 10000 --")
        print("Q3. what is the national bords of India ?")
        print("a. peacock")
        print("b. piegon")
        print("c. crow")
        print("d. duck")

        answer3 = input("Enter your answer:")
        if answer3 =="a":
            print("correct answer")
            money += 10000
            print("you have won :",money)

        else:
            print("wrong answer!")
            print("game over!")  
            print("money won :",money)  
    
    else:
        print("wrong answer!")
        print("game over !") 
        print("money won :",money)
else:
    print("wrong answer!")
    print("game over !")
    print("money won :",money)















