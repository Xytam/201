# File:    project1.py
# Author:  Jake Horvers
# Date:    11/20/2014
# Section: 7
# E-mail:  horvers1@umbc.edu 
# Description:
# Makes connect four


def main():
    #Initializes tiles and playing loop variables
    print("Welcome to Connect Four!")
    p1='X'
    p2='O'
    rows=0
    columns=0
    keepPlaying=True
    #keeps looping until they want to stop playing
    while(keepPlaying==True):
        #makes sure rows are read in properly
        rows=input('Please enter a number of rows: ')
        validRow=False
        while(not validRow):
            if(rows.isdigit()):
                rows=int(rows)
                if(rows<5):
                    rows=input('Please enter a valid choice: ')
                else:
                    validRow=True
            else:
                rows=input('Please enter a valid choice: ')
        
        #makes sure columns are read in properly
        columns=input('Please enter a number of columns: ')
        validCol=False
        while(not validCol):
            if(columns.isdigit()):
                columns=int(columns)
                if(columns<5):
                    columns=input('Please enter a valid choice: ')
                else:
                    validCol=True
            else:
                columns=input('Please enter a valid choice: ')
        
        #Makes it player 1s turn and generates the board
        turn='1'
        Board = generateBoard(rows,columns)
        #keeps playing until there is a winner (or draw)
        noWinner=True
        while noWinner==True:
            print('Players %s\'s turn. ' % turn)
            #decides player 1 or player 2
            if turn == '1':
                #prints the board, gets the move for player one and applies it to the board
                printboard(Board,columns,rows)
                move=getMove(Board,columns)
                move=int(move)
                makeMove(Board,p1,move,rows)
                #checks to see if the game is won/drawn
                if isDraw(Board,columns,rows):
                    winner = 'The game is a draw!'
                    noWinner=False

                if isWinner(Board, p1,rows,columns):
                    winner = 'Player 1 wins'
                    noWinner=False
                #changes turn
                turn = '2'
            else:
                #prints the board, gets the move for player two and applies it to the board
                printboard(Board,columns,rows)
                move=getMove(Board,columns)
                move=int(move)
                makeMove(Board,p2,move,rows)
                #checks to see if the game is won/drawn
                if isWinner(Board, p2,rows,columns):
                    winner = 'Player 2 wins!'
                    noWinner=False
                if isDraw(Board,columns,rows):
                    winner = 'The game is a draw!'
                    noWinner=False
                #changes turn
                turn = '1'
            #ensures the game is/isn't a draw
            if isDraw(Board,columns,rows):
                winner = 'The game is a draw!'
                noWinner=False
        #prints last board after the win,prints the winner, and asks to keep playing
        printboard(Board,columns,rows)
        print(winner)
        keepPlaying=playAgain()

#Prints the board
#Input: which board to print, the amount of rows and columns in the board
#Output:Graphical representation of the 2D array board
def printboard(board,columns,rows):
    #print the columns of the rows(my array is board[columns][rows]
    for j in range(rows):
        #prints each column and goes to the next line after
        for i in range(columns):
            print(board[i][j],end="")
        print()
    return board


#Generates the initial board to be used
#Input: The amount of rows and columns.
#Output: the 2D array board
def generateBoard(rows,columns):
    #generates an empty array
    board = []
    #fills the columns with an underscore for each row
    for x in range(columns):
        board.append(['_'] * rows)
    return board


#Makes the players move and inserts in into the board
#Input: The playing board, the player tile, the column they are moving in and the amount of rows in board
#Output: board with the new move in it
def makeMove(board, player, moveColumn,rows):
    #Checks from the bottom up in each column for the first empty space
    for y in range(rows-1, -1, -1):
        if board[moveColumn][y] == '_':
            board[moveColumn][y] = player
            return board

#Checks to see if the move the player entered is valid
#Input: the board the move is in,the move column, and the amount of columns in board
#Output: True or False based on the move
def isValidMove(board, move,columns):
    #if the move isn't a digit
    if not move.isdigit():
        return False
    #if it is,cast it and place it in the respective column(indexes are -1)
    move=int(move)-1
    #and it's not between the columns
    if move < 0 or move >= (columns):
        return False
    #and the row isn't full
    if board[move][0] != '_':
        return False
    return True


#Reads in the player's move
#Input:The board the move is in, the columns in the board
#Output: Statements regarding the move and returns the move if it is valid
def getMove(board,columns):
    #asks for move
    print('Please enter a move: ')
    valid=True

    #Accepts the move if it is Valid, if not, reprompts for a valid choice
    while valid:
        move=input()
        if isValidMove(board, move,columns):
            realMove=int(move)-1
            valid=False
            return realMove
        else:
            print("Please enter a valid choice: ")


#Checks to see if the game is a draw
#Input:the board to check and the amount of rows/columns in it
#Output:True or False 
def isDraw(board,columns,rows):
    #checks every row OF every column to see if there is an empty slot
    for x in range(columns):
        for y in range(rows):
            if board[x][y] == '_':
                return False
    return True

#Checks to see if a player won
#Input: The board to play on, the player's tile, and the amount of rows and columns
#Output: True or False if the player won
def isWinner(board, tile,rows,columns):

    # checks horizontal connect
    for y in range(rows):
        for x in range(columns - 3):
            if board[x][y] == tile and board[x+1][y] == tile and board[x+2][y] == tile and board[x+3][y] == tile:
                return True

    # checks vertical connect
    for x in range(columns):
        for y in range(rows - 3):
            if board[x][y] == tile and board[x][y+1] == tile and board[x][y+2] == tile and board[x][y+3] == tile:
                return True

    # checks / diagonal
    for x in range(columns - 3):
        for y in range(3, rows):
            if board[x][y] == tile and board[x+1][y-1] == tile and board[x+2][y-2] == tile and board[x+3][y-3] == tile:
                return True

    # checks \ diagonal
    for x in range(columns - 3):
        for y in range(rows - 3):
            if board[x][y] == tile and board[x+1][y+1] == tile and board[x+2][y+2] == tile and board[x+3][y+3] == tile:
                return True

    return False





def playAgain():
    a=0
    while(a==0):
        yesOrNo=str(input('Would you like to play again? (y/n): '))
        if(yesOrNo=='y' or yesOrNo=='n'):
            a=1
    if(yesOrNo=='y'):
        return True
    else:
        return False 

main()
