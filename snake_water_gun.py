import random

def cheak(comp,user):
    if(comp == user):
        return 0    
    if(comp == 0 and user == 1):
        return -1
    if(comp == 1 and user == 2):
        return -1 
    if(comp == 2 and user == 0):
        return -1   

    return 1
comp = random.randint(0,2) 
user = int(input("0 for Snake, 1 for water and 2 for gun:\n"))       

score = cheak(comp,user)

print("you: ",user)
print("computer: ",comp)
if(score == 0):
    print("match is draw")
elif(score == -1):
    print("you lose")
else:
    print("you won")
