r = 'x'
bold = "\033[1m"
reset = "\033[0;0m"
check = 0
a = [[".", ".", "."], [".", ".", "."], [".", ".", "."]] #for print
b = [[], [1, 2, 3], [1, 2], [1, 2, 4], [1, 2, 3, 4], [], [1, 2], [], [], [1, 2, 3]] #what are the optins to win
#     0     1          2       3            4         5     6     7   8      9

#b = [[], [1, 2], [1, 2, 4], [1, 2], [1, 2, 3, 4], [1, 2], [1, 2, 4], [1, 2], [1, 2, 3]] #what are the optins to win


#print(" attempt :", b[4][1])
#if 1 in b[0]:
#    print("{} exists in {}".format(1, b[0]))

def check_width():

    if a[h-1] == ['X', 'X', 'X']:
        print(bold + "                                       ~~~~~~~~~~~~~~~Player  X  won the game!!!~~~~~~~~~~~~~~~" + reset)

    if a[h-1] == ['O', 'O', 'O']:
        print(bold + "                                       ~~~~~~~~~~~~~~~Player  O  won the game!!!~~~~~~~~~~~~~~~" + reset)

def check_height():

    if a[h-1][w-1] == 'X' and a[h-2][w-1] == 'X' and a[h-3][w-1] == 'X':
        print(bold + "                                       ~~~~~~~~~~~~~~~Player  X  won the game!!!~~~~~~~~~~~~~~~" + reset)

    if a[h-1][w-1] == 'O' and a[h-2][w-1] == 'O' and a[h-3][w-1] == 'O':
        print(bold + "                                       ~~~~~~~~~~~~~~~Player  O  won the game!!!~~~~~~~~~~~~~~~" + reset)

def check_right_diagonal():

    if a[0][0] == 'X' and a[1][1] == 'X' and a[2][2] == 'X':
        print(bold + "                                       ~~~~~~~~~~~~~~~Player  X  won the game!!!~~~~~~~~~~~~~~~" + reset)

    if a[0][0] == 'O' and a[1][1] == 'O' and a[2][2] == 'O':
        print(bold + "                                       ~~~~~~~~~~~~~~~Player  O  won the game!!!~~~~~~~~~~~~~~~" + reset)


def check_left_diagonal():
    if a[0][2] == 'X' and a[1][1] == 'X' and a[2][0] == 'X':
        print(bold + "                                       ~~~~~~~~~~~~~~~Player  X  won the game!!!~~~~~~~~~~~~~~~" + reset)
    if a[0][2] == 'O' and a[1][1] == 'O' and a[2][0] == 'O':
        print(bold + "                                       ~~~~~~~~~~~~~~~Player  O  won the game!!!~~~~~~~~~~~~~~~" + reset)



def is_winner(): # this function checks what are the new options through list b
    if 1 in b[check]:
        #print("Option {} exists in {}".format(1, b[check]))
        check_width()
    if 2 in b[check]:
        #print("Option {} exists in {}".format(2, b[check]))
        check_height()
    if 3 in b[check]:
        #print("Option {} exists in {}".format(3, b[check]))
        check_right_diagonal()
    if 4 in b[check]:
        #print("Option {} exists in {}".format(4, b[check]))
        check_left_diagonal()


#o1 = a[0][0]
def print_board(): # this function prints the board when the player choose his new place

    print("")
    print("    Turn of: ", r)
    print("   --------------")
    print("")
    print("    1  |  2  |  3")
    print(" -"*9)
    print("1| ", end=" ")
    print(a[0][0], " | ",a[0][1], " | ",a[0][2], " ")
    print("   ----+-----+----")
    print("2| ", end=" ")
    print(a[1][0], " | ",a[1][1], " | ",a[1][2], " ")
    print("   ----+-----+----")
    print("3| ", end=" ")
    print(a[2][0], " | ",a[2][1], " | ",a[2][2], " ")
    print("")
    is_winner()



print_board()

w = int(input("Please write a number for width..."))
h = int(input("Please write a number for height..."))
#check = (w*h) - 1
check = w*h

while True: # this while check whose turn and send a message to function print_board where and what she need to print
    try:
        if a[h-1][w-1] == 'X' or a[h-1][w-1] == 'O':
            print("")
            print("This place is taken. Try another place")
            print("")
        elif r == 'x':
            a[h-1][w-1] = 'X'
            r = 'o'
        elif r == 'o':
            a[h-1][w-1] = 'O'
            r = 'x'

        print_board()

        w = int(input("Please write a number for width..."))
        h = int(input("Please write a number for height..."))
        #check = (w*h) - 1
        check = w*h
        """print("width = ", w)
        print("height = ", h)
        print("check = ", check)"""

    except IndexError as e:
        print("")
        print("Error! {}. You can write only the numbers 1, 2, 3 ! Please try again..".format(e))
        print("")
        #print("check: ", check, "Width:", w, "Height:", h, "Round: ", r)
        w = int(input("Please write a number for width..."))
        h = int(input("Please write a number for height..."))
        #check = (w*h) - 1
        check = w*h
