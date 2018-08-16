from enum import Enum
from random import randint
class gameState(Enum):
    win=1
    draw=2
    notfinished=3
class Game(object):
    def __init__(self,gamemode):        
        self.player1="X"
        self.player2="O"
        self.empty="."
        self.board=[self.empty]*9
        self.gamemode=gamemode  

    def board_print(self):        
        for i in range (3):
            currentrowstart=i*3            
            print(self.board[currentrowstart].value+self.board[currentrowstart+1].value+self.board[currentrowstart+2].value) 

    def play(self,place,player):     
        self.board[place]=player

    def start(self):
        self.board_print()
        exit_condition=gameState.notfinished
        turn=1    
        while exit_condition== gameState.notfinished:                                                             
            if turn%2==1:
                player=self.player1
            else:
                player=self.player2
                if self.gamemode=="s":
                    place=randint(0,8)
                    if self.is_place_taken(place):
                        continue
                    self.play(place,player)
            if (self.gamemode=="s"and player == self.player1)or self.gamemode=="m":
                print(player + "your turn!")           
                print("enter row")
                row=int(input())-1
                while not (row<=2 and row >=0):
                    print("row should be between 1 and 3, try again")
                    row=int(input())-1
                print("enter column")
                column=int(input())-1
                while not (column<=2 and column >=0):
                    print("column should be between 1 and 3, try again")
                    column=int(input())-1            
                if self.is_place_taken(row*3+column):
                    print("this spot is already taken")
                    continue
                self.play(row*3+column,player)
            turn = turn + 1 
            self.board_print()
            exit_condition=self.is_gameover(player)
            if exit_condition==gameState.win:
                print("Congratulations to "+ player.value +" who won the game")
            elif exit_condition== gameState.draw:
                print("This game ended in a draw, no one won")
    
    def is_place_taken(self,place):    
        if not self.board[place]==self.empty:
            return True
        return False

    def is_gameover(self,player):       
        if self.is_winner(player):
            return gameState.win
        elif self.is_board_full():
            return gameState.draw
        else:
            return gameState.notfinished

    def is_board_full(self):        
        for i in range (9):            
            if self.board[i]==self.empty:
                return False            
        return True         
        
    def is_winner(self,player):        
        return self.checkrows(player) or self.checkcolumns(player) or self.checkdiagonals(player)        

    def checkrows(self,player):        
        for i in range (3):            
            currentrowstart=i*3
            #check if one of the marks in the row is the one of the player before checking the whole row
            if self.board[currentrowstart]==player:
                if self.board[currentrowstart]==self.board[currentrowstart+1] and self.board[currentrowstart]== self.board[currentrowstart+2]:
                    return True                           
        return False   

    def checkcolumns(self,player):        
        for i in range (3):
            #check if one of the marks in the column is the one of the player before checking the whole column
            if self.board[i]==player:
                if self.board[i]==self.board[i+3] and self.board[i]== self.board[i+6]:
                    return True
        return False                    

    def checkdiagonals(self,player):                
            #check if the center is taken by the player(it is needed for both diagonals)
        if self.board[4]==player:
            if self.board[0]==self.board[4] and self.board[0]== self.board[8]:                
                return True                
            if self.board[2]==self.board[4] and self.board[2]== self.board[6]:                
                return True                    
        return False

if __name__ =="__main__":
    print("press s for single player or m for multiplayer")
    gamemode=input()
    while not (gamemode=="s"or gamemode=="m"):
        print("press s for single player or m for multiplayer")
        gamemode=input()
    gameinstance=Game(gamemode)
    gameinstance.start()    