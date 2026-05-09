# tic tak game :
# 1. creat board

board = [" "," "," ",
         " "," "," ",
         " "," "," "]

current_player = "X"

def print_board():
    print()
    print(board[0], "/", board[1], "/", board[2])
    print(board[3], "/", board[4], "/", board[5])
    print(board[6], "/", board[7], "/", board[8])
    print()



    #win condition
wins = [
    [0,1,2],
    [3,4,5],
    [6,7,8],
    [0,3,6],
    [1,4,7],
    [2,5,8],
    [0,4,8],
    [2,4,6]
]

while True:
    print_board()

    position = input(f"player {current_player}, choose position(1-9):")
    
    #cheak number only
    if not position.isdigit():
        print("please enter number only")
        continue
    position = int(position) - 1
    #cheak range
    if position < 0 or position >8:
        print("choose between 1 to 9 only")
        continue

    #cheak empty position
    
    if board[position] != " ":
        print("position already taken,try again")
        continue

    board[position] = current_player

    winner = False
    for condition in wins:
        a,b,c = condition

        if board[a] == board[b] == board[c] != " ":
            print_board()
            print(f"player {current_player} wins!")

            winner = True
            break
    if winner:
        break

    #match drawn
    if " " not in board :
        print_board()
        print("match draw!")
        break
    #change player
    if current_player == "X":
        current_player = "O"

    else:
        current_player = "X"      
    


















