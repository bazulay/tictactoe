#Aviv Frenkel
board = [["." , "." , "."],
         ["." , "." , "."],
         ["." , "." , "."]];
players = {1: "x" , -1: "o"};
current_player = 1;
full = False;

def print_board():
    for line in board:
        for cell in line:
            print (cell + " " , end = "\t");
        print("\n");

def play(row , column , player):
    if (board[int(row) - 1][int(column) - 1] == "."):
        board[int(row) - 1][int(column) - 1] = player;
        return True;
    else:
        return False;

def is_winner(player):
    for i in range(3):
        win_row = True;
        win_column = True;
        for j in range(3):
            if (board[i][j] != player):
                win_row = False;
            if (board[j][i] != player):
                win_column = False;
        if(win_row or win_column):
            return True;
    first_diagonal = True;
    seconde_diagonal = True;
    for k in range(3):
        if (board[k][k] != player):
            first_diagonal = False;
        if (board[k][2-k] != player):
            seconde_diagonal = False;
        if (not first_diagonal and not seconde_diagonal):
            return False;
    if (first_diagonal or seconde_diagonal):
        return True;
    return False;

def get_input(player):
    print("player " + player);
    row = input("Enter row: ");
    column = input("Enter column: ")
    can_add = play(row, column, player);
    if (not can_add):
        print("Try Again!");
        get_input(player);
    else:
        print_board();

def check_full_board():
    for line in board:
        for cell in line:
            if (cell == "."):
                return False;
    return True;

while (not is_winner("x") and not is_winner("o") and not full):
    current = players[current_player];
    get_input(current);
    current_player *= -1;
    full = check_full_board();

if (full):
    print("No Winner - TEKO!!!!");
else:
    print("The Winner is " + current);