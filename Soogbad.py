from enum import Enum
import random

class Gamemode(Enum):
    Singleplayer = 1
    Multiplayer = 2

class Game:
    def __init__(self, game_mode: Gamemode):
        self.option = ""
        self.game_mode, self.table = game_mode, [[".", ".", "."], [".", ".", "."], [".", ".", "."]]
        if game_mode == Gamemode.Multiplayer:
            self.print_table()
        player = "X"
        move = 1
        while self.winner() == ".":
            if game_mode == Gamemode.Multiplayer:
                position = self.input_position(player)
                self.play(player, position[0] - 1, position[1] - 1, True)
                if player == "X":
                    player = "O"
                else:
                    player = "X"
            else:
                if player == "X":
                    position = self.choose_position(move)
                    self.play(player, position[0], position[1], True)
                    player = "O"
                else:
                    position = self.input_position(player)
                    self.play(player, position[0] - 1, position[1] - 1, False)
                    player = "X"
            move += 1
        winner = self.winner()
        if winner == "":
            print("It's a Draw!")
        else:
            print(winner + " is the Winner!")
    def winner(self):
        for i in range(3):
            if self.table[i][0] == self.table[i][1] and self.table[i][1] == self.table[i][2]:
                return self.table[i][0]
            elif self.table[0][i] == self.table[1][i] and self.table[1][i] == self.table[2][i]:
                return self.table[0][i]
        if (self.table[0][0] == self.table[1][1] and self.table[1][1] == self.table[2][2]) or (self.table[0][2] == self.table[1][1] and self.table[1][1] == self.table[2][0]):
            return self.table[1][1]
        if self.table[0].__contains__(".") == False and self.table[1].__contains__(".") == False and self.table[2].__contains__(".") == False:
            return ""
        return "."
    def print_table(self):
        for row in self.table:
            for place in row:
                print(place, end=" ")
            print("")
    def play(self, player: chr, row: int, place: int, draw: bool):
        self.table[row][place] = player
        if draw:
            self.print_table()
    def choose_position(self, move: int):
        row = random.randint(-1, 2)
        place = random.randint(-1, 2)
        while self.table[row][place] != ".":
            row = random.randint(-1, 2)
            place = random.randint(-1, 2)
        return [row, place]
    def input_position(self, player: chr):
        if player == "":
            text = ""
        else:
            text = player + ", "
        while True:
            try:
                position = [int(input(text + "Enter the Row\n")), int(input(text + "Enter the Place\n"))]
                if position[0] >= 1 and position[0] <= 3 and position[1] >= 1 and position[1] <= 3:
                    if self.table[position[0] - 1][position[1] - 1] == ".":
                        return position
                    else:
                        print("Position is Taken")
                else:
                    print("Values Must be Between 1 and 3")
            except ValueError:
                print("Values Must be Between 1 and 3")


while True:
    mode_input = input("Type 's' for Singleplayer or 'm' for Multiplayer\n").lower()
    if mode_input == "s":
        game_mode = Gamemode.Singleplayer
        break
    elif mode_input == "m":
        game_mode = Gamemode.Multiplayer
        break
    print("Values Must be s or m")

while True:
    game = Game(game_mode)
