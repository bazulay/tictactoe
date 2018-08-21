import random

#this comment is for testing git 

board = [0, 0, 0, 0, 0, 0, 0, 0, 0]

user_id = 0
#added 
take_mode = int(input("select mode\n1.singleplayer\n2.dual player"))

def board_print(brd):
    format = ".XO"
    for row in range(3):
        print(' '.join(format[i] for i in brd[row*3:(row+1) * 3]))

def get_winner(brd):
    for i in range(3):
        row = set(brd[i*3:(i+1) * 3])
        col = set(brd[i::3])
        for result in (row, col):
            if len(result) == 1:
                value = result.pop()
                if value != 0:
                    return value
    slant1 = {brd[0], brd[4], brd[8]}
    slant2 = {brd[2], brd[4], brd[6]}
    for result in (slant1, slant2):
        if len(result) == 1:
            value = result.pop()
            if value != 0:
                return value


def computer_turn():
    comp_choice = random.randint(0, 8)
    while board[comp_choice] != 0:
        return computer_turn()
    return comp_choice


def play():
    global user_id
    global take_mode
    if take_mode == 2:
        board_print(board)
        if user_id % 2:
            user_input = int(input("Enter the square you wish to place: "))
            if user_input < 0 or user_input > 8 or board[user_input] != 0:
                print("Square doesn't exist.")
                return play()
            else:
                board[user_input] = 1
                user_id += 1
                if get_winner(board) == 1:
                    print("player 1 has won")
                else:
                    return play()
        else:
            take_turn = computer_turn()
            board[take_turn] = 2
            user_id += 1
            if get_winner(board) == 2:
                print("player 2 has won")
            else:
                return play()
    elif take_mode == 1:
        board_print(board)
        user_input = int(input("Enter the square you wish to place: "))
        if user_id % 2:
            if user_input < 0 or user_input > 8:
                print("Square doesn't exist.")
            else:
                board[user_input] = 1
                user_id += 1
                if get_winner(board) == 1:
                    print("player 1 has won")
                else:
                    return play()
        else:
            if user_input < 0 or user_input > 8:
                print("Square doesn't exist.")
            else:
                board[user_input] = 2
                user_id += 1
                if get_winner(board) == 2:
                    print("player 2 has won")
                else:
                    return play()
    else:
        print("mode not found")
        return play()

play()
